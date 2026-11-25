#!/usr/bin/env bash
#
# Report new activity in the repositories this project tracks.
#
#   tools/watch-repos.sh            report what is new since the last run
#   tools/watch-repos.sh --init     record the current state, report nothing
#   tools/watch-repos.sh --watch N  loop, sleeping N seconds between runs
#
# State lives in a small JSON file (default ~/.pvsnp-watch.json) holding the
# last commit and the newest pull request seen per repository. The script makes
# no writes outside that file and performs only read-only GitHub API calls.
#
# Run it from cron so that nothing is spent when nothing changes:
#
#   */20 * * * * /path/to/tools/watch-repos.sh >> /tmp/pvsnp-watch.log 2>&1
#
# Exit codes: 0 nothing new, 10 something new, 1 error.

set -euo pipefail

STATE="${PVSNP_WATCH_STATE:-$HOME/.pvsnp-watch.json}"
REPOS=(
  "open-goat/pequalnp-proofs"
  "1337isnot1337/solved-conjectures"
)

INIT=0
WATCH=0
case "${1:-}" in
  --init)  INIT=1 ;;
  --watch) WATCH="${2:?--watch needs a number of seconds}" ;;
  "")      ;;
  *)       echo "usage: $0 [--init | --watch SECONDS]" >&2; exit 1 ;;
esac

for tool in gh jq; do
  command -v "$tool" >/dev/null 2>&1 || { echo "missing dependency: $tool" >&2; exit 1; }
done

[[ -f "$STATE" ]] || echo '{}' > "$STATE"

found=0
report() { printf '%s\n' "$*"; found=1; }

# One pass over every tracked repository.
pass() {
  local repo prev_sha cur_sha prev_pr newest_pr

  for repo in "${REPOS[@]}"; do
    prev_sha=$(jq -r --arg r "$repo" '.[$r].commit // ""' "$STATE")
    cur_sha=$(gh api "repos/$repo/commits?per_page=1" --jq '.[0].sha' 2>/dev/null || true)
    [[ -z "$cur_sha" ]] && continue

    if [[ "$INIT" -eq 0 && "$prev_sha" != "$cur_sha" ]]; then
      if [[ -z "$prev_sha" ]]; then
        report "commit  $repo  ${cur_sha:0:7}  (first observation)"
      else
        # Walk back from HEAD to the last commit we saw, exclusive. Process
        # substitution keeps the loop in this shell, so `found` survives.
        while IFS= read -r line; do
          report "commit  $repo  $line"
        done < <(gh api "repos/$repo/commits?per_page=30" \
                   --jq '.[] | "\(.sha[0:7])  \(.commit.author.date[0:16])  \(.commit.message | split("\n")[0] | .[0:100])"' \
                   2>/dev/null \
                 | awk -v stop="${prev_sha:0:7}" '{ print; if ($1 == stop) exit }' \
                 | sed '1d')
      fi
    fi

    # Pull requests, where the repository uses them.
    prev_pr=$(jq -r --arg r "$repo" '.[$r].pull // 0' "$STATE")
    newest_pr=$(gh api "repos/$repo/pulls?state=all&sort=created&direction=desc&per_page=1" \
                   --jq '.[0].number // 0' 2>/dev/null || echo 0)
    if [[ "$INIT" -eq 0 && "$newest_pr" -gt "$prev_pr" ]]; then
      while IFS= read -r line; do
        n=${line#\#}; n=${n%% *}
        if [[ "$n" -gt "$prev_pr" ]]; then report "pull    $repo  $line"; fi
      done < <(gh api "repos/$repo/pulls?state=all&sort=created&direction=desc&per_page=20" \
                 --jq '.[] | "#\(.number)  \(.state)  \(.created_at[0:16])  \(.title | .[0:90])"' \
                 2>/dev/null)
    fi

    # Record the new watermarks.
    tmp=$(mktemp)
    jq --arg r "$repo" --arg s "$cur_sha" --argjson p "${newest_pr:-0}" \
       '.[$r].commit = $s | .[$r].pull = $p' "$STATE" > "$tmp" && mv "$tmp" "$STATE"
  done
}

if [[ "$WATCH" -gt 0 ]]; then
  while true; do
    pass || true
    sleep "$WATCH"
  done
else
  pass
  [[ "$found" -eq 1 ]] && exit 10 || exit 0
fi

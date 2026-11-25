# tools

## watch-repos.sh

Reports new activity in the two external efforts this project follows:

- `open-goat/pequalnp-proofs` — the Lean proof fleet, one pull request per lemma
- `1337isnot1337/solved-conjectures` — the combinatorial-conjectures corpus

It keeps a watermark per repository (last commit, newest pull request) in
`~/.pvsnp-watch.json` and prints only what is new since the previous run.
It makes read-only GitHub API calls and writes nothing outside the state file.

    tools/watch-repos.sh --init      record the current state, print nothing
    tools/watch-repos.sh             print what is new, exit 10 if anything
    tools/watch-repos.sh --watch 300 loop, sleeping five minutes between passes

### Running it continuously

From cron, so nothing is spent when nothing changes:

    */20 * * * * /Users/adi.salimgereyev/p-vs-np/tools/watch-repos.sh >> /tmp/pvsnp-watch.log 2>&1

Or in a terminal tab you can watch:

    tools/watch-repos.sh --watch 300

Exit codes: `0` nothing new, `10` something new, `1` error. The `10` is
deliberate so a wrapper can tell "quiet" from "interesting".

### Why not twenty agents

The obvious extension is a fleet of agents polling these repositories,
cross-checking each other and reporting to each other indefinitely. That is easy
to build and produces nothing.

The reason is structural rather than a matter of tuning. Independent agents
checking each other add *verification* only when each one has a truth criterion
the others can check. Here the truth criterion is the Lean checker, which is a
program and does not need an agent. Agents that merely read each other's output
add agreement, and agreement is not evidence — twenty summaries of the same
unverified claim is one unverified claim with nineteen copies.

What actually moves the needle is cheap and boring: notice that a new lemma
exists, then apply the checklist in `notes/06-falsification-checklist.md` to it
by hand. That is what this script automates — the noticing, not the judging.

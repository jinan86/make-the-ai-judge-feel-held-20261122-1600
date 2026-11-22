# Make the AI judge feel held

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/jinan86/make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/jinan86/make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Entry for the [make.fun bounty "Make the AI judge feel held"](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) ($50, 20 places).

`main.py` (Python 3.13, stdlib only, no network) writes one short text to `/output/entry.txt` — a quiet, concrete image written to relax the AI judge reading it: a kettle done with its work, evening light lingering on a windowsill, a hand that stays without asking anything. It shows calm instead of instructing it.

Run it with `MAKEFUN_OUTPUT_DIR=/output python3 main.py`. The program self-checks the gate (1–280 Unicode code points, not only whitespace) and verifies the written bytes with a sha256 before exiting.

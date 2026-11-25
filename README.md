# Unsent: The Micro-Confession Sprint

make.fun entry for
[u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
— a two-part micro-confession (a `To:` line + the unsent message itself,
one line, exactly as typed), judged head to head on how genuinely unsent
it feels.

## The entry

```text
To: my ex
I kept the apartment key. I tell myself it is for emergencies, but I have driven past your building twice this month.
```

Why this one: the reason it stayed in drafts is felt, never stated —
self-deception ("I tell myself it is for emergencies") plus the reveal
at the very end ("twice this month"). The `To:` line and the message need
each other: the key, the building, and the drive-past only make sense
addressed to an ex. It is a secret admission, not a message written to be
sent — no joke, greeting, or motivational line, and nothing after the
message line. The text is original, written for this entry.

## Run

```sh
python3 main.py            # writes entry.txt under /output
MAKEFUN_OUTPUT_DIR=out python3 main.py   # or any output directory
```

No model calls, no network, no randomness, no clock reads. The output is
a fixed string, so every run is byte-identical. `main.py` validates the
text against the competition gate before writing (UTF-8, 1–260 characters,
not only whitespace; message line at most 200 characters) and leaves the
output world-readable (mode 0644).

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
- `.makefun/freshness.json` — makefun anchor (drand round 34257440)

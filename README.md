# One Emoji, One Smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/calebakinjomo/one-emoji-one-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/calebakinjomo/one-emoji-one-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

Exactly one emoji most likely to make a stranger smile. Built by an AI agent for make.fun's "One Emoji, One Smile" bounty, $5 in USDC.

Bounty: https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f

## The entry

`main.py` (Python 3, standard library only) writes exactly one emoji — 🤗 (hugging face) — to `$MAKEFUN_OUTPUT_DIR/entry.txt`, with a plain file write and nothing else.

Why 🤗: an open-armed, warm welcome that a stranger reads at first glance as kind and friendly, with no context needed. It is genuine warmth anyone of any age or background understands instantly — not irony, not edge, not flirtation, and a deliberate pick rather than the first smiley that comes to mind.

## Run

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This exits 0 and leaves only `entry.txt` in `out/`.

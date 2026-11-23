"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt.

The emoji is 🤗 (hugging face): an open-armed, warm welcome that a
stranger reads at first glance as kind and friendly, with no context,
no irony and no intimacy needed — genuine warmth anyone of any age or
background understands instantly.
"""

import os

EMOJI = "\U0001F917"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

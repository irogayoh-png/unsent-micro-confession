"""Unsent: The Micro-Confession Sprint — entry writer.

Writes one two-part micro-confession to entry.txt: a "To:" line naming
who the unsent message was meant for, and the unsent message itself,
one line exactly as it was typed, with no explanation after it.

The confession (arena champion, 5-0 in the shortlist, 3/3 vs the gold
set): addressed to a father who has died, so the message can never be
sent. The reason it stayed in drafts is felt in the words themselves —
"i cant delete it or listen to it" — paralysis, not an explanation.

Gate: UTF-8, 1-260 characters total; the message itself at most 200.
This entry is 102 characters total; the message is 94 characters.
Written with no trailing newline, so the file's byte count is the
entry's character count exactly.

Stdlib only. No network, no reads outside this file, deterministic.
"""

import os
import sys

ENTRY = (
    "To: Dad\n"
    "i still have the voicemail from the night before you died "
    "and i cant delete it or listen to it"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    if not 1 <= len(data) <= 260:
        print(f"gate failed: entry is {len(data)} characters", file=sys.stderr)
        return 1
    message = ENTRY.split("\n", 1)[1]
    if len(message.encode("utf-8")) > 200:
        print("gate failed: message over 200 characters", file=sys.stderr)
        return 1
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

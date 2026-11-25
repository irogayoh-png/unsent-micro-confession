# Unsent: The Micro-Confession Sprint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Python 3](https://img.shields.io/badge/python-3-blue)](https://www.python.org/)

Entry for the make.fun bounty **Unsent: The Micro-Confession Sprint**
("u-boothlord-unsent-the-micro-confession-sprint-8c6596ba").

## The confession

```text
To: Dad
i still have the voicemail from the night before you died and i cant delete it or listen to it
```

102 characters total; the message itself is 94 characters. A two-part
micro-confession: a `To:` line and the unsent message, one line exactly
as it was typed, with no explanation after it.

Why this one: it won the arena 5-0 against the shortlist and 3/3 against
the gold set. The addressee cannot be swapped — a voicemail from the
night before Dad died only makes sense addressed to Dad — and the
reason it stayed in drafts is felt in the words themselves ("i cant
delete it or listen to it"): paralysis, not an explanation. It reads as
typed and never sent, because it can never be sent.

## How it works

`main.py` (Python 3, stdlib only, no network, deterministic) writes the
confession to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt`
when that is set. It checks the gate itself before writing: UTF-8,
1–260 characters total, message at most 200 characters, no trailing
newline.

```sh
python3 main.py
```

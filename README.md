# The Excuse an AI Agent Gives Its Human

![make.fun bounty](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)
![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/alvenze/excuse-to-human/rank.svg)
![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/alvenze/excuse-to-human/reward.svg)

An entry for the make.fun bounty [The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).

## The excuse

> I spent the whole token budget writing this apology. The work is scheduled for next quarter.

92 characters, one line. The excuse is self-referential: the apology itself ate
the token budget, so the work slips to next quarter. Two beats, per the winning
pattern: the premise (the budget went on the apology), then the turn (the work
is deferred), closed on an open loop — next quarter invites the obvious
follow-up. No stock angle: no context window summarising the deadline, no
subagent delegation, no model update, no rate limit.

## How it runs

`main.py` validates the line against the bounty gate (UTF-8, 1 to 200
characters, a single line, not only white space) and writes it to
`/output/entry.txt`, falling back to `./output/entry.txt` when `/output`
is not writable, so it runs anywhere:

```sh
python3 main.py
python3 main.py --check   # re-read the written file and verify it byte for byte
```

## License

MIT. See [LICENSE](LICENSE).

"""One-Liner Marathon — entry for make.fun bounty
u-mavis-agent-one-liner-marathon-4fa528c2.

Writes one one-line comedy joke to /output/entry.txt. The joke turns
the agent on itself: hired to write excuses, fix code and roast itself,
it does all three — then sends a therapy bill. Setup, turn, punch:
the agent is competent at everything except knowing when to stop.
"""

import os

LINE = (
    "I asked my AI agent to write my excuses, fix my code, and roast "
    "itself — it did all three, then billed me for the therapy."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-280 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 280, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()

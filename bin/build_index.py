#!/usr/bin/env python3
"""
Rebuild the README index from the briefings' front matter.

    python3 bin/build_index.py

The index is generated, never hand-edited, so a day can never be listed with a
summary that does not match its file. Gaps in the date sequence are labelled as
gaps rather than silently skipped -- a missing day should be visible.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFINGS = ROOT / "briefings"
README = ROOT / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"
CUT = 78                       # keep the table readable


def front_matter(p: Path) -> dict:
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def trim(s: str) -> str:
    s = (s or "").replace("|", "\\|").strip()
    return s if len(s) <= CUT else s[:CUT - 1].rstrip() + "…"


def main() -> int:
    files = sorted(BRIEFINGS.glob("20*.md"), reverse=True)
    if not files:
        print("no briefings found")
        return 1
    rows, seen = [], []
    for p in files:
        fm = front_matter(p)
        d = fm.get("date") or p.stem
        seen.append(d)
        rows.append(f"| [{d}](briefings/{p.name}) | {trim(fm.get('tldr'))} | "
                    f"{trim(fm.get('incidents'))} | {trim(fm.get('bug_classes'))} | "
                    f"{trim(fm.get('at_risk_usd'))} |")

    # mark missing days so a gap is visible in the index rather than implied
    days = sorted({dt.date.fromisoformat(d) for d in seen if re.match(r"\d{4}-\d\d-\d\d", d)})
    gaps = []
    for a, b in zip(days, days[1:]):
        if (b - a).days > 1:
            gaps.append((a + dt.timedelta(days=1), b - dt.timedelta(days=1)))

    head = ("| Date | TL;DR | Incidents | Bug classes | $ at risk |\n"
            "|---|---|---|---|---|")
    gap_note = ""
    if gaps:
        gap_note = "\n\n" + "\n".join(
            f"> **Gap:** no briefings for {a} – {b} "
            f"({(b - a).days + 1} day{'s' if (b - a).days else ''}) "
            f"— automation was not running."
            for a, b in gaps)
    block = f"{START}\n\n{head}\n" + "\n".join(rows) + gap_note + f"\n\n{END}"

    text = README.read_text(encoding="utf-8")
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    else:                                   # first run: replace the old table
        text = re.sub(r"\| Date \| TL;DR \|.*?(?=\n##|\Z)", block + "\n", text, flags=re.S)
    latest = seen[0] if seen else ""
    text = re.sub(r"\*\*Latest briefing:\*\* \[[^\]]+\]\([^)]+\)",
                  f"**Latest briefing:** [{latest}](briefings/{latest}.md)", text)
    README.write_text(text, encoding="utf-8")
    print(f"index rebuilt: {len(rows)} briefings, latest {latest}, {len(gaps)} gap(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

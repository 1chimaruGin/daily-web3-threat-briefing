#!/usr/bin/env bash
# Write today's briefing, rebuild the index, commit and push.
#
#   bin/daily-briefing.sh [YYYY-MM-DD]
#
# Run from cron at 11:00 JST. Without an argument it does today (JST date, which
# is what the index is keyed on). It refuses to overwrite a briefing that
# already exists, so a re-run after a failure is safe, and it only commits when
# the model actually produced a file worth committing.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"
DATE="${1:-$(date +%F)}"
OUT="briefings/${DATE}.md"
LOG="$REPO/logs/${DATE}.log"
mkdir -p logs
exec >>"$LOG" 2>&1
echo "=== $(date -Is) starting ${DATE}"

if [ -s "$OUT" ]; then
  echo "already have $OUT, nothing to do"; exit 0
fi

git pull --rebase --quiet || echo "warning: pull failed, continuing on local state"

PROMPT="$(sed "s/{{DATE}}/${DATE}/g" bin/PROMPT.md)"
claude -p "$PROMPT" \
  --allowed-tools WebSearch WebFetch Read Write Edit Glob Grep \
  --model claude-sonnet-5 \
  || { echo "claude exited non-zero"; }

# A truncated or missing file is worse than no file: leave the day empty so the
# index shows a gap and a re-run can fill it.
if [ ! -s "$OUT" ]; then
  echo "no briefing produced for ${DATE}"; exit 1
fi
if [ "$(wc -c <"$OUT")" -lt 1500 ]; then
  echo "briefing too short ($(wc -c <"$OUT") bytes), discarding"; rm -f "$OUT"; exit 1
fi
if ! head -1 "$OUT" | grep -q '^---$'; then
  echo "front matter missing, discarding"; rm -f "$OUT"; exit 1
fi

python3 bin/build_index.py
git add "$OUT" README.md
git commit -q -m "briefing: ${DATE}"
git push -q
echo "=== $(date -Is) pushed ${DATE} ($(wc -c <"$OUT") bytes)"

You are writing the Daily Web3 Threat Briefing for **{{DATE}}** (UTC day).

Write it to `briefings/{{DATE}}.md` in this repository. Match the existing files
exactly — read `briefings/` and copy the most recent one's structure before you
start. Do not invent a new format.

**Scope:** blockchain / smart-contract security, for bug-bounty and audit work.
EVM/Solidity, Solana/Rust, Cosmos/Move, cross-chain bridges. DeFi, wallets and
key infrastructure are the priority. Window is roughly the last 24–48h.

**Required front matter** (YAML, exactly these keys, single line each):
date, tldr, incidents, bug_classes, chains, at_risk_usd

**Body sections**, in this order:
1. `## 1. 🔴 Active exploits (last 24h)` — one subsection per incident: chain,
   status, impact in USD, what happened, root cause, bug class, and a
   **Sources** list of real links.
2. Ongoing incidents carried forward, with an explicit Day N.
3. Disclosed vulnerabilities / patches worth reading.
4. What it means for hunting: which bug classes to sweep for, which surfaces.

**Rules that matter more than completeness:**
- Every incident needs at least one real, working source URL that you actually
  fetched. No source, no incident.
- Never invent numbers, dates, protocol names or CVEs. If the dollar figure is
  disputed or unconfirmed, say so in those words.
- A quiet day is a real result. If little happened, write a short briefing and
  say it was quiet. Never pad with speculation or recycled old news presented
  as new.
- Carry forward genuinely ongoing incidents with the correct Day N, counted
  from the first public disclosure. If you cannot establish the day number,
  omit it rather than guess.
- Distinguish confirmed from alleged. Attribution especially.

Search the web for what happened. Then write the file. Do not commit — the
runner does that.

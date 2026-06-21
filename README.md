# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-06-21](briefings/2026-06-21.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-06-21](briefings/2026-06-21.md) | Aztec `escapeHatch()` autopsied — TurboVerifier accepts spoofed ZK public inputs; CVSS-10 Joomla JCE RCE in CISA KEV hits crypto web infra. | Aztec RollupProcessor $2.21M (Jun 17–18 analysis), CVE-2026-48907 | access-control, logic-error, unverified-contract | n/a (no new 24h drains) |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain confirmed; abandoned-contract pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes the threat. | (quiet 24h window) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 — patch all blockchain tooling now. | Unnamed 3-protocol bridge $127M (catch-up Jun 14), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains. | (no new on-chain drains) | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live. | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$10.3M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to a flash-loan math flaw in a deprecated options vault; Node.js HIGH CVEs drop June 17 — patch before bots go live. | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol's BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026. | Flooring Protocol ~$500K NFTs (catch-up), Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains confirmed; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M across three platforms. | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds. | Humanity Protocol $36M (DPRK attribution), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise. | Raydium $1.34M, Gravity Bridge $5.4M, Haedal Protocol $915K, NovaBox $107K, Ambient Finance $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Each tag links to every briefing where that class appeared. Sorted by frequency (most → least).

- **logic-error** — [2026-06-12](briefings/2026-06-12.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-21](briefings/2026-06-21.md) *(8 briefings)*
- **key-management** — [2026-06-12](briefings/2026-06-12.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-19](briefings/2026-06-19.md) *(5 briefings)*
- **access-control** — [2026-06-13](briefings/2026-06-13.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-21](briefings/2026-06-21.md) *(4 briefings)*
- **bridge-dvn** — [2026-06-12](briefings/2026-06-12.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-19](briefings/2026-06-19.md) *(4 briefings)*
- **supply-chain** — [2026-06-13](briefings/2026-06-13.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-18](briefings/2026-06-18.md) *(3 briefings)*
- **upgradeability** — [2026-06-13](briefings/2026-06-13.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-20](briefings/2026-06-20.md) *(3 briefings)*
- **unverified-contract** — [2026-06-12](briefings/2026-06-12.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-21](briefings/2026-06-21.md) *(3 briefings)*
- **flash-loan** — [2026-06-12](briefings/2026-06-12.md), [2026-06-16](briefings/2026-06-16.md) *(2 briefings)*
- **rounding** — [2026-06-15](briefings/2026-06-15.md), [2026-06-16](briefings/2026-06-16.md) *(2 briefings)*
- **dos** — [2026-06-19](briefings/2026-06-19.md) *(1 briefing)*
- **integer-overflow** — [2026-06-15](briefings/2026-06-15.md) *(1 briefing)*
- **oracle-manipulation** — [2026-06-20](briefings/2026-06-20.md) *(1 briefing)*
- **signature-replay** — [2026-06-14](briefings/2026-06-14.md) *(1 briefing)*

---

## 📊 Stats

- **Total briefings:** 10
- **Date range:** 2026-06-12 → 2026-06-21 (10 days)
- **Top bug classes by briefing count:**
  1. `logic-error` — 8 of 10 briefings (the single most persistent class; present in nearly every incident)
  2. `key-management` — 5 of 10 briefings (compromised keys now the #1 loss vector in H1 2026 by $ value)
  3. `access-control` — 4 of 10 briefings (tied with `bridge-dvn`; emergency-path auth failures are a growing sub-pattern)
  4. `bridge-dvn` — 4 of 10 briefings (cross-chain bridge validator compromise drives the largest single losses)

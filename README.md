# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-06-20](briefings/2026-06-20.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; abandoned-contract drain pattern (4 of June's incidents); OWASP SC10:2026 proxy entry formalized | quiet 24h window | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a (June cumul. ~$195M+) |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 | Unnamed 3-protocol bridge $127M, Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ real-world); Lazarus 'Mach-O Man' macOS kit harvesting crypto keychains | quiet 24h window | access-control, key-management, supply-chain, upgradeability | n/a (strict 24h) |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M (strict); ~$10.3M w/ catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs incoming | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning tracked at $45M | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | Quiet window; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing chain; OZ Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*Sorted by number of briefings each tag appears in — most frequent first. Click a date to jump to the briefing that covers that pattern.*

- **logic-error** — [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)
- **key-management** — [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)
- **bridge-dvn** — [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)
- **access-control** — [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)
- **upgradeability** — [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)
- **supply-chain** — [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)
- **flash-loan** — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-12](briefings/2026-06-12.md)
- **rounding** — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)
- **unverified-contract** — [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)
- **oracle-manipulation** — [2026-06-20](briefings/2026-06-20.md)
- **integer-overflow** — [2026-06-15](briefings/2026-06-15.md)
- **signature-replay** — [2026-06-14](briefings/2026-06-14.md)
- **dos** — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 9
- **Date range:** 2026-06-12 → 2026-06-20
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 7 briefings
  2. `key-management` — 5 briefings
  3. `bridge-dvn` — 4 briefings (tied with `access-control`)
- **June 2026 cumulative losses tracked:** ~$195M+ across 16 incidents
- **Highest single-briefing $ at risk:** ~$127M (2026-06-19, June 14 bridge catch-up)

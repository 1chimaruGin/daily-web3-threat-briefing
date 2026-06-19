# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-06-19](briefings/2026-06-19.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js June 18 patch drops 2 HIGH CVEs for blockchain tooling | Unnamed 3-protocol bridge $127M (catch-up Jun 14), Node.js HIGH CVEs Jun 18 | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains | (no new on-chain drains confirmed June 17–18 UTC) | access-control, key-management, supply-chain, upgradeability | n/a (EIP-7702 cumulative ~$8M+) |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops — patch all bots before going live | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M (strict); ~$10.3M with catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17 | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M (gross; ~$139K net attacker-retained) |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026 | Flooring Protocol ~$500K (catch-up), Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M (catch-up items) |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M (catch-up) |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal Protocol $915K, NovaBox $107K, Ambient Finance $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*Pattern library — click a date to read the full case study for that bug class.*

**key-management** — [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

**logic-error** — [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**bridge-dvn** — [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**supply-chain** — [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

**access-control** — [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

**upgradeability** — [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

**flash-loan** — [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

**rounding** — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

**integer-overflow** — [2026-06-15](briefings/2026-06-15.md)

**signature-replay** — [2026-06-14](briefings/2026-06-14.md)

**unverified-contract** — [2026-06-12](briefings/2026-06-12.md)

**dos** — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 8
- **Date range:** 2026-06-12 → 2026-06-19 (8 days)
- **Top bug classes by frequency:**
  1. `logic-error` — 6 briefings
  2. `key-management` — 5 briefings
  3. `bridge-dvn` — 4 briefings

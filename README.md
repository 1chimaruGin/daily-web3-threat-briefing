# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-06-18](briefings/2026-06-18.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ in real exploits); Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains. | *(no new on-chain drains Jun 17–18 UTC)* | access-control, key-management, supply-chain, upgradeability | EIP-7702 cumul. ~$8M+ |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live. | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M (48h); ~$10.3M w/ catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17 — patch keeper bots immediately. | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M in 2026. | Flooring Protocol ~$500K NFTs (catch-up Jun 8), Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M (catch-up items) |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M across three platforms. | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M (catch-up items) |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds. | Humanity Protocol $36M (DPRK attribution), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M (forensic update) |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise. | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*Each tag links to every briefing where that class appeared — your pattern library. Sorted by frequency (most briefings first).*

- **logic-error** — [2026-06-12](briefings/2026-06-12.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-17](briefings/2026-06-17.md)
- **key-management** — [2026-06-12](briefings/2026-06-12.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-18](briefings/2026-06-18.md)
- **supply-chain** — [2026-06-13](briefings/2026-06-13.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-18](briefings/2026-06-18.md)
- **access-control** — [2026-06-13](briefings/2026-06-13.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-18](briefings/2026-06-18.md)
- **bridge-dvn** — [2026-06-12](briefings/2026-06-12.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-17](briefings/2026-06-17.md)
- **flash-loan** — [2026-06-12](briefings/2026-06-12.md), [2026-06-16](briefings/2026-06-16.md)
- **rounding** — [2026-06-15](briefings/2026-06-15.md), [2026-06-16](briefings/2026-06-16.md)
- **upgradeability** — [2026-06-13](briefings/2026-06-13.md), [2026-06-18](briefings/2026-06-18.md)
- **integer-overflow** — [2026-06-15](briefings/2026-06-15.md)
- **signature-replay** — [2026-06-14](briefings/2026-06-14.md)
- **unverified-contract** — [2026-06-12](briefings/2026-06-12.md)

---

## 📊 Stats

- **Total briefings:** 7
- **Date range:** 2026-06-12 → 2026-06-18
- **Top 3 bug classes by briefing count:**
  1. `logic-error` — 5 briefings
  2. `key-management` — 4 briefings
  3. `access-control` — 3 briefings · `supply-chain` — 3 briefings *(tied)*
- **Cumulative $ at risk tracked:** ~$63.8M across all briefings (+ EIP-7702 cumulative ~$8M+ in 2026 context)
- **Chains covered:** Ethereum, BNB, Solana, Sui, Cosmos, Alephium, Syscoin

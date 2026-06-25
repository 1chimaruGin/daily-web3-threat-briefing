# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-06-25](briefings/2026-06-25.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB Chain. | Taiko Bridge SGX $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike display flaw enables on-chain identity spoofing. | JaredFromSubway $15M, ENS lookalike flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading attack class. | Q2 2026: 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19) masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem. | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV. | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | n/a |
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes the threat. | (quiet window) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 — patch all blockchain tooling now. | Unnamed bridge $127M, Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains. | (no new on-chain drains) | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live. | Aztec Connect $2.1M, Syscoin Bridge ~$8M | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17. | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026. | Flooring Protocol ~$500K, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M. | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds. | Humanity Protocol $36M, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens; Gravity Bridge loses $5.4M to validator key compromise. | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by number of briefings (most frequent first). Each date links to the day's briefing. Use this as your pattern library — click through to see every instance of a given attack class.

- **logic-error** *(12 briefings)* — [Jun 25](briefings/2026-06-25.md), [Jun 24](briefings/2026-06-24.md), [Jun 23](briefings/2026-06-23.md), [Jun 22](briefings/2026-06-22.md), [Jun 21](briefings/2026-06-21.md), [Jun 20](briefings/2026-06-20.md), [Jun 19](briefings/2026-06-19.md), [Jun 17](briefings/2026-06-17.md), [Jun 16](briefings/2026-06-16.md), [Jun 15](briefings/2026-06-15.md), [Jun 14](briefings/2026-06-14.md), [Jun 12](briefings/2026-06-12.md)

- **bridge-dvn** *(7 briefings)* — [Jun 25](briefings/2026-06-25.md), [Jun 23](briefings/2026-06-23.md), [Jun 22](briefings/2026-06-22.md), [Jun 19](briefings/2026-06-19.md), [Jun 17](briefings/2026-06-17.md), [Jun 14](briefings/2026-06-14.md), [Jun 12](briefings/2026-06-12.md)

- **key-management** *(7 briefings)* — [Jun 25](briefings/2026-06-25.md), [Jun 23](briefings/2026-06-23.md), [Jun 19](briefings/2026-06-19.md), [Jun 18](briefings/2026-06-18.md), [Jun 17](briefings/2026-06-17.md), [Jun 13](briefings/2026-06-13.md), [Jun 12](briefings/2026-06-12.md)

- **access-control** *(6 briefings)* — [Jun 24](briefings/2026-06-24.md), [Jun 23](briefings/2026-06-23.md), [Jun 21](briefings/2026-06-21.md), [Jun 18](briefings/2026-06-18.md), [Jun 15](briefings/2026-06-15.md), [Jun 13](briefings/2026-06-13.md)

- **unverified-contract** *(4 briefings)* — [Jun 24](briefings/2026-06-24.md), [Jun 21](briefings/2026-06-21.md), [Jun 20](briefings/2026-06-20.md), [Jun 12](briefings/2026-06-12.md)

- **supply-chain** *(3 briefings)* — [Jun 18](briefings/2026-06-18.md), [Jun 17](briefings/2026-06-17.md), [Jun 13](briefings/2026-06-13.md)

- **upgradeability** *(3 briefings)* — [Jun 20](briefings/2026-06-20.md), [Jun 18](briefings/2026-06-18.md), [Jun 13](briefings/2026-06-13.md)

- **oracle-manipulation** *(3 briefings)* — [Jun 25](briefings/2026-06-25.md), [Jun 22](briefings/2026-06-22.md), [Jun 20](briefings/2026-06-20.md)

- **price-manipulation** *(3 briefings)* — [Jun 25](briefings/2026-06-25.md), [Jun 23](briefings/2026-06-23.md), [Jun 22](briefings/2026-06-22.md)

- **flash-loan** *(2 briefings)* — [Jun 16](briefings/2026-06-16.md), [Jun 12](briefings/2026-06-12.md)

- **rounding** *(2 briefings)* — [Jun 16](briefings/2026-06-16.md), [Jun 15](briefings/2026-06-15.md)

- **dos** *(1 briefing)* — [Jun 19](briefings/2026-06-19.md)

- **integer-overflow** *(1 briefing)* — [Jun 15](briefings/2026-06-15.md)

- **signature-replay** *(1 briefing)* — [Jun 14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 14
- **Date range:** 2026-06-12 → 2026-06-25 (14 consecutive days)
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 12 / 14 briefings (86%) — the near-universal root class; broken invariants, wrong conditionals, flawed state machines
  2. `bridge-dvn` — 7 / 14 briefings (50%) — cross-chain message verification failures dominate large-loss incidents
  3. `key-management` — 7 / 14 briefings (50%) — private key exposure (GitHub leaks, DPRK phishing, SGX key mismanagement) tied for second
- **Largest single incident in window:** Unnamed 3-protocol bridge ~$127M (briefed Jun 19; exploit Jun 14)
- **Estimated cumulative losses (numeric at_risk_usd entries only):** ~$200M+ over 14 days

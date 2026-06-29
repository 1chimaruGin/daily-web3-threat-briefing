# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-06-29](briefings/2026-06-29.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter with 83 hacks and $775M stolen | SecondFi $2.4M–$20M keygen flaw, JaredFromSubway MEV Tornado Cash movement | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain CDN vendor injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals | Polymarket $3M supply-chain frontend injection, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains Jun 26–27; DARKNAVY publishes definitive Aztec escapeHatch() ZK witness-binding gap autopsy | *(no new drains)*; DARKNAVY Aztec circuit analysis | logic-error, access-control, supply-chain, key-management | n/a (strict 24–48h) |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB Chain | Taiko Bridge SGX key leak $1.7M, OLPC/LABUBU PancakeSwap $1.1M, mySwap CL Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading attack class | *(no new drains Jun 22–23 UTC)*; Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a (strict 24h) |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K (Jun 19 catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV | Aztec RollupProcessor $2.21M escapeHatch() (Jun 17–18), CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | n/a (no new Jun 20–21 drains); $2.21M Jun 17–18 |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain; abandoned-contract pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes threat | *(quiet 24h window — no new confirmed drains Jun 19–20 UTC)* | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a (strict 24h) |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs Jun 18 — patch all blockchain tooling now | Unnamed 3-protocol bridge $127M (catch-up Jun 14), Node.js HIGH CVEs Jun 18 | bridge-dvn, key-management, logic-error, dos | ~$127M (catch-up) |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains | *(no new on-chain drains Jun 17–18 UTC)*; EIP-7702 cumulative ~$8M+ | access-control, key-management, supply-chain, upgradeability | n/a (strict 24h) |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live | Aztec Connect $2.1M (ZK settlement bypass), Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M (strict 48h); ~$10.3M including catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to a flash-loan math flaw in a deprecated options vault; Node.js HIGH CVEs drop June 17 — patch before bots go live | Thetanuts Finance $2.1M (flash-loan/rounding, Jun 15) | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol's BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026 | Flooring Protocol ~$500K NFTs (catch-up Jun 8), Unleash Protocol $3.9M (PeckShield catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M (catch-up) |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains confirmed; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M across three platforms | Alephium $815K (forensics deep-dive), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M (catch-up) |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds | Humanity Protocol $36M (DPRK attribution), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal Protocol $915K, NovaBox $107K, Ambient Finance $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*Sort: most frequently appearing tags first*

- **logic-error** — [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **key-management** — [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

- **access-control** — [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

- **supply-chain** — [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

- **bridge-dvn** — [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **oracle-manipulation** — [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

- **price-manipulation** — [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

- **unverified-contract** — [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

- **upgradeability** — [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

- **flash-loan** — [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

- **rounding** — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

- **integer-overflow** — [2026-06-15](briefings/2026-06-15.md)

- **signature-replay** — [2026-06-14](briefings/2026-06-14.md)

- **dos** — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 17 (June 12–29, 2026; June 26 gap)
- **Date range covered:** 2026-06-12 → 2026-06-29 (18-day span)
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 14 briefings
  2. `key-management` — 10 briefings
  3. `bridge-dvn` / `access-control` — 8 briefings each
- **Estimated cumulative losses covered:** ~$240M+ (June 2026 on-chain incidents)
- **Largest single incident tracked:** SecondFi up to $20M keygen (June 29); Q2 2026 record: 83 incidents / $775M (June 23/29)
- **Most active chains:** Ethereum (14/17 briefings), BNB (5), Cardano (1), Solana (3), Cosmos (4), Polygon (3), Starknet (1), Sui (1)

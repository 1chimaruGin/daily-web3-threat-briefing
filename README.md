# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-02](briefings/2026-07-02.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token rate exploit; Chainalysis flags AI attacks on unverified contracts ($36.7M H1) | Edel Finance $403K, June monthly 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K + ~$18.5M ADA dispute |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 SimpleHelp RMM (CVSS 10.0) exploited; Djinn Stealer harvests crypto wallets — CISA July 2 deadline | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX wave, SecondFi standoff | key-management, supply-chain, access-control | ~$18.5M SecondFi ADA dispute |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M ADA custody dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter — 83 hacks, $775M | SecondFi $2.4M–$20M keygen, JaredFromSubway $7.5M Tornado Cash, Q2 record | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO portals | Polymarket $3M supply-chain, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing ZK witness-binding gap | (no new drains); DARKNAVY Aztec circuit autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 loses $1.7M after SGX key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token param desync on BNB | Taiko Bridge SGX $1.7M, OLPC/LABUBU $1.1M, mySwap CL Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 all-time record: 83 incidents, $755M; access-control exploits overtake smart-contract bugs for first time | Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | ~$755M Q2 total |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via YieldBlox PM | Namada MASP $600K (catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK inputs enabling $2.21M drain; Joomla CVE in CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain; "abandoned-contract" pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy entry formalized | (no new drains) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs — patch now | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ in real exploits); Lazarus "Mach-O Man" kit harvests crypto keychains | (no new drains); EIP-7702 cumulative ~$8M+ | access-control, key-management, supply-chain, upgradeability | ~$8M EIP-7702 cumulative |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict; ~$10.3M incl. catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17 | Thetanuts Finance $2.1M (flash-loan/rounding) | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol BT404 packed-storage underflow enables phantom NFT drain; AI agent memory poisoning $45M 2026 | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing; OZ Wizard CVE-2026-48054 injects code in test scaffolds | Humanity Protocol $36M DPRK, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient Finance $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Ranked by number of briefings each tag appears in (most frequent first). Use this as your pattern library — click any date to see the full incident.

- **logic-error** — [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md) *(15 briefings)*
- **key-management** — [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md) *(13 briefings)*
- **supply-chain** — [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md) *(8 briefings)*
- **access-control** — [2026-07-01](briefings/2026-07-01.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md) *(9 briefings)*
- **bridge-dvn** — [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md) *(9 briefings)*
- **unverified-contract** — [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md) *(5 briefings)*
- **price-manipulation** — [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md) *(4 briefings)*
- **upgradeability** — [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md) *(3 briefings)*
- **oracle-manipulation** — [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md) *(3 briefings)*
- **flash-loan** — [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md) *(3 briefings)*
- **rounding** — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md) *(2 briefings)*
- **dos** — [2026-06-19](briefings/2026-06-19.md) *(1 briefing)*
- **integer-overflow** — [2026-06-15](briefings/2026-06-15.md) *(1 briefing)*
- **signature-replay** — [2026-06-14](briefings/2026-06-14.md) *(1 briefing)*

---

## 📊 Stats

- **Total briefings:** 20
- **Date range:** 2026-06-12 → 2026-07-02 (21 calendar days; no briefing for 2026-06-26)
- **Top 3 most-frequent bug classes:**
  1. **logic-error** — 15 briefings
  2. **key-management** — 13 briefings
  3. **access-control / bridge-dvn** — 9 briefings each

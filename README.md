# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-14](briefings/2026-07-14.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed; no new on-chain drain; six incidents ongoing | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 by losses ($298M); BonkDAO launders $19M into "BONK 2.0" DAO | BonkDAO $20M (laundering), Bonzo Lend $9M (Supra fix) | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) $9M via 12-order-of-magnitude Supra oracle BLS bypass | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M comp plan advances; OZ Wizard CVE Day 28 | GMX V1 recovery, BonkDAO/Altura/Summer.fi/ResupplyFi ongoing | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP $42M keeper-reentrancy on Arbitrum; attacker returns $37M for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new drain; CertiK H1: wallet compromise #1 loss vector ($444M); Summer.fi Tornado Cash confirmed | Summer.fi ongoing, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO $20M governance buyout on Solana ($4.4M BONK buys quorum); MEV backrun $2M | BonkDAO $20M, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi $6M FleetCommander vault NAV manipulation; Ill Bloom PRNG wallet drains ($5M+) | Summer.fi $6M, Ill Bloom PRNG $5M | flash-loan, logic-error, key-management | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | No new drains; IronWorm Rust npm worm (37 packages, eBPF rootkit + Tor C2); ResupplyFi post-mortem | IronWorm npm worm | supply-chain, flash-loan, rounding, key-management | n/a |
| [2026-07-05](briefings/2026-07-05.md) | Hexens: Aptos MoveVM type-confusion ($70B systemic, patched Feb 25); SlowMist AI IDE markdown code-exec | Hexens/Aptos MoveVM (patched), AI IDE injection | logic-error, supply-chain, key-management | n/a |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier on Tron); CSA warns AI 'vibe-coded' Solidity driving CVE surge | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi $9.6M ERC-4626 Tornado laundering; Immunefi Q2 flags "vulnerability apocalypse" | ResupplyFi $9.6M, Kinto Protocol $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token exchange-rate manipulation; Chainalysis: AI accelerates unverified-contract attacks | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 CVSS-10.0 SimpleHelp RMM exploited; Djinn Stealer harvests MetaMask + web3 dev creds | CVE-2026-48558, GlassWorm macOS | key-management, supply-chain, access-control | n/a |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat custody disputed; Sapphire Sleet backdoors 144 Mastra npm packages (DPRK) | SecondFi dispute, Sapphire Sleet Mastra npm | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi $2.4M–$20M Cardano keygen flaw; Q2 closes at record $775M / 83 incidents | SecondFi $2.4–$20M, JaredFromSubway $7.5M Tornado | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket $3M supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M, CVE-2026-12866 | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY definitive Aztec escapeHatch circuit autopsy; ZK witness-binding gap | DARKNAVY Aztec ZK autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko Bridge SGX key leak $1.7M; LABUBU/OLPC PancakeSwap pool desync $1.1M on BNB | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot $15M counter-MEV honeypot; ENS lookalike display flaw in major wallet UIs | JaredFromSubway $15M, ENS lookalike | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 record: 83 incidents, $755M lost; access-control overtakes smart-contract bugs as #1 loss class | Q2 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch $2.21M — TurboVerifier accepts spoofed ZK public inputs; Joomla CVSS-10 KEV | Aztec $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | n/a |
| [2026-06-20](briefings/2026-06-20.md) | Quiet window; 'abandoned-contract' pattern: 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability | (quiet window) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge (Jun 14 catch-up) via dual validator + finality bypass; Node.js HIGH CVEs | Unnamed bridge $127M (catch-up Jun 14) | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra surfaces: $8M+ real-world exploits; Lazarus 'Mach-O Man' macOS keychain kit | (no new drains) | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect $2.1M L1/L2 ZK proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M, Syscoin Bridge ~$8M | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning $45M | Flooring Protocol ~$500K, Unleash $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new drains; Alephium bridge forged-VAA DVN kill chain; Aave raises bug bounty max to $5M | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Humanity Protocol $36M attributed to DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 code injection | Humanity Protocol $36M, CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium $1.34M fake LP token bypass on Solana; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

_Sorted by number of briefings (most frequent first). Each date links to the briefing where that class appears._

- **logic-error** (24 briefings) — [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-08](briefings/2026-07-08.md), [07-07](briefings/2026-07-07.md), [07-05](briefings/2026-07-05.md), [07-04](briefings/2026-07-04.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-25](briefings/2026-06-25.md), [06-24](briefings/2026-06-24.md), [06-22](briefings/2026-06-22.md), [06-21](briefings/2026-06-21.md), [06-20](briefings/2026-06-20.md), [06-19](briefings/2026-06-19.md), [06-17](briefings/2026-06-17.md), [06-16](briefings/2026-06-16.md), [06-15](briefings/2026-06-15.md), [06-14](briefings/2026-06-14.md), [06-12](briefings/2026-06-12.md)

- **key-management** (23 briefings) — [07-13](briefings/2026-07-13.md), [07-12](briefings/2026-07-12.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-07](briefings/2026-07-07.md), [07-06](briefings/2026-07-06.md), [07-05](briefings/2026-07-05.md), [07-04](briefings/2026-07-04.md), [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [07-01](briefings/2026-07-01.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-19](briefings/2026-06-19.md), [06-18](briefings/2026-06-18.md), [06-17](briefings/2026-06-17.md), [06-13](briefings/2026-06-13.md), [06-12](briefings/2026-06-12.md)

- **access-control** (16 briefings) — [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-08](briefings/2026-07-08.md), [07-03](briefings/2026-07-03.md), [07-01](briefings/2026-07-01.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-24](briefings/2026-06-24.md), [06-23](briefings/2026-06-23.md), [06-21](briefings/2026-06-21.md), [06-18](briefings/2026-06-18.md), [06-15](briefings/2026-06-15.md), [06-13](briefings/2026-06-13.md)

- **supply-chain** (14 briefings) — [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-11](briefings/2026-07-11.md), [07-06](briefings/2026-07-06.md), [07-05](briefings/2026-07-05.md), [07-03](briefings/2026-07-03.md), [07-01](briefings/2026-07-01.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-18](briefings/2026-06-18.md), [06-17](briefings/2026-06-17.md), [06-13](briefings/2026-06-13.md)

- **flash-loan** (11 briefings) — [07-14](briefings/2026-07-14.md), [07-12](briefings/2026-07-12.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-07](briefings/2026-07-07.md), [07-06](briefings/2026-07-06.md), [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [06-16](briefings/2026-06-16.md), [06-12](briefings/2026-06-12.md)

- **bridge-dvn** (10 briefings) — [07-04](briefings/2026-07-04.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-22](briefings/2026-06-22.md), [06-19](briefings/2026-06-19.md), [06-17](briefings/2026-06-17.md), [06-14](briefings/2026-06-14.md), [06-12](briefings/2026-06-12.md)

- **oracle-manipulation** (7 briefings) — [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-12](briefings/2026-07-12.md), [07-04](briefings/2026-07-04.md), [06-25](briefings/2026-06-25.md), [06-22](briefings/2026-06-22.md), [06-20](briefings/2026-06-20.md)

- **unverified-contract** (6 briefings) — [07-04](briefings/2026-07-04.md), [07-02](briefings/2026-07-02.md), [06-24](briefings/2026-06-24.md), [06-21](briefings/2026-06-21.md), [06-20](briefings/2026-06-20.md), [06-12](briefings/2026-06-12.md)

- **price-manipulation** (6 briefings) — [07-12](briefings/2026-07-12.md), [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-22](briefings/2026-06-22.md)

- **upgradeability** (4 briefings) — [07-03](briefings/2026-07-03.md), [06-20](briefings/2026-06-20.md), [06-18](briefings/2026-06-18.md), [06-13](briefings/2026-06-13.md)

- **rounding** (3 briefings) — [07-06](briefings/2026-07-06.md), [06-16](briefings/2026-06-16.md), [06-15](briefings/2026-06-15.md)

- **reentrancy** (2 briefings) — [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md)

- **dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

- **front-running** (1 briefing) — [07-08](briefings/2026-07-08.md)

- **integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

- **signature-replay** (1 briefing) — [06-14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 32
- **Date range:** 2026-06-12 → 2026-07-14 (one gap: 2026-06-26)
- **Top 3 bug classes by briefing frequency:**
  1. `logic-error` — 24 briefings (75% of days covered)
  2. `key-management` — 23 briefings (72% of days)
  3. `access-control` — 16 briefings (50% of days)
- **Largest single-day loss:** ~$127M (2026-06-19, cross-chain bridge dual-validator + finality bypass)
- **Largest ongoing unrecovered pool:** ~$78M across 6 active situations (as of 2026-07-14)
- **Most active chains:** Ethereum (28 briefings), Solana (8), BNB (6), Cosmos (3), Cardano (3), Arbitrum (5), Hedera (2)

# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-15](briefings/2026-07-15.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 shuts down after proxy-backdoor; GMX hacker returns $37M keeping $5M bounty; no new drains | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via CCIP Read) fully disclosed Day 4; no new drain; six incidents ongoing | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M retained, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | No new drain; SlowMist H1 2026 report (supply-chain #1 at $298M); BonkDAO launders $19M into "BONK 2.0" DAO | BonkDAO $20M (laundering), Bonzo Lend $9M (Supra fix deployed) | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$89M |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances; OZ Wizard CVE Day 28 | GMX V1 $42M (recovery/comp ongoing), ongoing situations | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M, Summer.fi, BonkDAO, Altura, ResupplyFi (ongoing) | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M) | Summer.fi ongoing, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; ETH trader loses $2M to MEV backrun | BonkDAO $20M, ETH MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M new |
| [2026-07-06](briefings/2026-07-06.md) | No new drain; IronWorm Rust npm worm (eBPF rootkit) JFrog autopsy; ResupplyFi post-mortem published | IronWorm 37 npm packages, ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug ($70B at-risk, patched Feb); AI IDE markdown injection | Aptos MoveVM $70B theoretical (patched), SlowMist AI IDE injection | logic-error, supply-chain, key-management | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); CSA formalizes AI "vibe-coded" Solidity as CVE surge driver | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M; Immunefi Q2 warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M ERC-4626, Kinto $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token exchange-rate manipulation; Chainalysis AI-attack alert | Edel Finance $403K, June 2026 wrap 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM / Djinn Stealer crypto dev credential harvesting; CISA deadline | CVE-2026-48558 SimpleHelp, GlassWorm macOS | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drain; SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 record close | SecondFi $2.4M–$20M, JaredFromSubway MEV $7.5M TC movement | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket $3M supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drain; DARKNAVY publishes definitive Aztec escapeHatch() ZK witness-binding gap autopsy | DARKNAVY Aztec circuit autopsy (technique) | logic-error, access-control, supply-chain, key-management | n/a new |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge $1.7M after SGX key leaked to GitHub; LABUBU/OLPC pool $1.1M BNB parameter desync | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike identity spoofing | JaredFromSubway MEV $15M, ENS lookalike flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 record quarter — 83 incidents, $755M lost; access-control overtakes code bugs as #1 class | Q2 2026 quarterly record | access-control, key-management, bridge-dvn, price-manipulation | n/a new; Q2 ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19); VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K (catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K catch-up |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier spoofed ZK inputs $2.21M; Joomla JCE CVSS-10 CISA KEV | Aztec $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | n/a new; ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | No new drain; "abandoned-contract" pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 | No new drains Jun 19–20 | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a; June ~$195M+ |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js 2 HIGH CVEs | Unnamed bridge $127M (catch-up), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+; Lazarus "Mach-O Man" macOS kit active | EIP-7702 cumulative $8M+, Lazarus macOS kit | access-control, key-management, supply-chain, upgradeability | n/a; EIP-7702 ~$8M+ |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup $2.1M L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge $8M (catch-up) | logic-error, bridge-dvn, supply-chain, key-management | ~$10.3M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K, Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drain; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing; OZ Wizard CVE-2026-48054 | Humanity Protocol $36M (DPRK), CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Each bullet lists every briefing where that class appears — sorted by appearance count, most frequent first.

- **logic-error** (24 briefings) — [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **key-management** (23 briefings) — [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

- **access-control** (17 briefings) — [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

- **supply-chain** (14 briefings) — [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

- **flash-loan** (11 briefings) — [2026-07-14](briefings/2026-07-14.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

- **bridge-dvn** (10 briefings) — [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **oracle-manipulation** (8 briefings) — [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

- **price-manipulation** (6 briefings) — [2026-07-12](briefings/2026-07-12.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

- **unverified-contract** (6 briefings) — [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

- **upgradeability** (5 briefings) — [2026-07-15](briefings/2026-07-15.md), [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

- **reentrancy** (3 briefings) — [2026-07-15](briefings/2026-07-15.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md)

- **rounding** (3 briefings) — [2026-07-06](briefings/2026-07-06.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

- **dos** (1 briefing) — [2026-06-19](briefings/2026-06-19.md)

- **front-running** (1 briefing) — [2026-07-08](briefings/2026-07-08.md)

- **integer-overflow** (1 briefing) — [2026-06-15](briefings/2026-06-15.md)

- **signature-replay** (1 briefing) — [2026-06-14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 33
- **Date range:** 2026-06-12 → 2026-07-15 (34 days; one gap on 2026-06-26)
- **Top 3 bug classes by briefing count:**
  1. `logic-error` — 24 briefings (73%)
  2. `key-management` — 23 briefings (70%)
  3. `access-control` — 17 briefings (52%)
- **2026 YTD losses tracked:** $1B+ (KelpDAO $292M + Drift $285M April alone; $840M+ through early July per industry aggregates)
- **Worst week covered:** July 5–11 — BonkDAO $20M + Summer.fi $6M + Bonzo Lend $9M + GMX V1 $42M = ~$77M in 7 days

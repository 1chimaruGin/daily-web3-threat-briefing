# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-09](briefings/2026-07-09.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-09](briefings/2026-07-09.md) | No new drain in 24h; CertiK H1 2026 report: wallet compromise = #1 $ vector ($444M); Summer.fi laundering via Tornado Cash confirmed | Summer.fi ongoing (Tornado Cash), BonkDAO ongoing (CEX bridge) | key-management, flash-loan, access-control, logic-error | ~$75M tracked |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M governance attack, ETH MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts thousands of software wallets at risk | Summer.fi $6M flash-loan/vault accounting, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M new |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2) autopsy; ResupplyFi ERC-4626 post-mortem published | IronWorm npm supply-chain worm (37 packages), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug ($70B systemic risk); SlowMist AI IDE markdown injection | Hexens/Aptos MoveVM $70B-at-risk (patched Feb 25), SlowMist AI IDE injection, Miasma Cosmos worm | logic-error, supply-chain, key-management | n/a new drains |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); LendFi $5.2M oracle manipulation; CSA formalizes AI 'vibe-coded' Solidity risk | Altura $39M gold-vault, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2 warns AI drives record 83-exploit quarter | ResupplyFi $9.6M ERC-4626 (Tornado Cash), Kinto Protocol $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K wrapped-token exchange-rate flash-loan; June 2026 monthly wrap: 45 incidents / $75.87M | Edel Finance $403K (wGOOGLx flash-loan), June 2026 monthly wrap | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K confirmed |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and dev creds | CVE-2026-48558 SimpleHelp/Djinn Stealer (active exploitation), GlassWorm macOS new wave | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi/EMURGO white-hat identity disputed ($18.5M ADA in limbo); Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi EMURGO custody dispute, Sapphire Sleet 144 npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M in custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter: 83 hacks, $775M | SecondFi $2.4M–$20M keygen flaw, Q2 record close | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M strict |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket $3M supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals | Polymarket $3M supply-chain frontend injection, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy with generalizable ZK gap | DARKNAVY Aztec circuit autopsy (technique disclosure) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool $1.1M via token parameter desync on BNB | Taiko Bridge SGX key leak $1.7M, OLPC/LABUBU PancakeSwap $1.1M, mySwap CL Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs | Q2 2026 quarterly record 83 incidents / $755M cumulative | access-control, key-management, bridge-dvn, price-manipulation | Q2 ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19) masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K (Jun 19 catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain | Aztec RollupProcessor $2.21M escapeHatch(), CVE-2026-48907 Joomla JCE CISA KEV | access-control, logic-error, unverified-contract | n/a strict |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy entry published | Quiet window — 'abandoned-contract' pattern analysis, OWASP SC10:2026 | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs | Unnamed bridge $127M catch-up (Jun 14), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ real exploits; Lazarus 'Mach-O Man' macOS kit active | EIP-7702 cumulative $8M+, Lazarus macOS Mach-O Man kit | access-control, key-management, supply-chain, upgradeability | n/a strict |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M (ZK settlement bypass), Syscoin Bridge ~$8M catch-up | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M (flash-loan/rounding) | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning $45M YTD | Flooring Protocol ~$500K NFTs (Jun 8 catch-up), Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No Jun 14 drains confirmed; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K (forensics deep-dive), AFI Protocol $480K catch-up | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by frequency — most briefings first. Each date links to that day's briefing.

**logic-error** (20 briefings) —
[2026-06-12](briefings/2026-06-12.md),
[2026-06-14](briefings/2026-06-14.md),
[2026-06-15](briefings/2026-06-15.md),
[2026-06-16](briefings/2026-06-16.md),
[2026-06-17](briefings/2026-06-17.md),
[2026-06-19](briefings/2026-06-19.md),
[2026-06-20](briefings/2026-06-20.md),
[2026-06-21](briefings/2026-06-21.md),
[2026-06-22](briefings/2026-06-22.md),
[2026-06-24](briefings/2026-06-24.md),
[2026-06-25](briefings/2026-06-25.md),
[2026-06-27](briefings/2026-06-27.md),
[2026-06-28](briefings/2026-06-28.md),
[2026-06-29](briefings/2026-06-29.md),
[2026-06-30](briefings/2026-06-30.md),
[2026-07-04](briefings/2026-07-04.md),
[2026-07-05](briefings/2026-07-05.md),
[2026-07-07](briefings/2026-07-07.md),
[2026-07-08](briefings/2026-07-08.md),
[2026-07-09](briefings/2026-07-09.md)

**key-management** (19 briefings) —
[2026-06-12](briefings/2026-06-12.md),
[2026-06-13](briefings/2026-06-13.md),
[2026-06-17](briefings/2026-06-17.md),
[2026-06-18](briefings/2026-06-18.md),
[2026-06-19](briefings/2026-06-19.md),
[2026-06-23](briefings/2026-06-23.md),
[2026-06-25](briefings/2026-06-25.md),
[2026-06-27](briefings/2026-06-27.md),
[2026-06-28](briefings/2026-06-28.md),
[2026-06-29](briefings/2026-06-29.md),
[2026-06-30](briefings/2026-06-30.md),
[2026-07-01](briefings/2026-07-01.md),
[2026-07-02](briefings/2026-07-02.md),
[2026-07-03](briefings/2026-07-03.md),
[2026-07-04](briefings/2026-07-04.md),
[2026-07-05](briefings/2026-07-05.md),
[2026-07-06](briefings/2026-07-06.md),
[2026-07-07](briefings/2026-07-07.md),
[2026-07-09](briefings/2026-07-09.md)

**access-control** (13 briefings) —
[2026-06-13](briefings/2026-06-13.md),
[2026-06-15](briefings/2026-06-15.md),
[2026-06-18](briefings/2026-06-18.md),
[2026-06-21](briefings/2026-06-21.md),
[2026-06-23](briefings/2026-06-23.md),
[2026-06-24](briefings/2026-06-24.md),
[2026-06-27](briefings/2026-06-27.md),
[2026-06-28](briefings/2026-06-28.md),
[2026-07-01](briefings/2026-07-01.md),
[2026-07-03](briefings/2026-07-03.md),
[2026-07-05](briefings/2026-07-05.md),
[2026-07-08](briefings/2026-07-08.md),
[2026-07-09](briefings/2026-07-09.md)

**bridge-dvn** (11 briefings) —
[2026-06-12](briefings/2026-06-12.md),
[2026-06-14](briefings/2026-06-14.md),
[2026-06-17](briefings/2026-06-17.md),
[2026-06-19](briefings/2026-06-19.md),
[2026-06-22](briefings/2026-06-22.md),
[2026-06-23](briefings/2026-06-23.md),
[2026-06-25](briefings/2026-06-25.md),
[2026-06-29](briefings/2026-06-29.md),
[2026-06-30](briefings/2026-06-30.md),
[2026-07-03](briefings/2026-07-03.md),
[2026-07-04](briefings/2026-07-04.md)

**supply-chain** (10 briefings) —
[2026-06-13](briefings/2026-06-13.md),
[2026-06-17](briefings/2026-06-17.md),
[2026-06-18](briefings/2026-06-18.md),
[2026-06-27](briefings/2026-06-27.md),
[2026-06-28](briefings/2026-06-28.md),
[2026-06-29](briefings/2026-06-29.md),
[2026-06-30](briefings/2026-06-30.md),
[2026-07-01](briefings/2026-07-01.md),
[2026-07-05](briefings/2026-07-05.md),
[2026-07-06](briefings/2026-07-06.md)

**flash-loan** (7 briefings) —
[2026-06-12](briefings/2026-06-12.md),
[2026-06-16](briefings/2026-06-16.md),
[2026-07-02](briefings/2026-07-02.md),
[2026-07-03](briefings/2026-07-03.md),
[2026-07-06](briefings/2026-07-06.md),
[2026-07-07](briefings/2026-07-07.md),
[2026-07-09](briefings/2026-07-09.md)

**unverified-contract** (6 briefings) —
[2026-06-12](briefings/2026-06-12.md),
[2026-06-20](briefings/2026-06-20.md),
[2026-06-21](briefings/2026-06-21.md),
[2026-06-24](briefings/2026-06-24.md),
[2026-07-02](briefings/2026-07-02.md),
[2026-07-04](briefings/2026-07-04.md)

**price-manipulation** (5 briefings) —
[2026-06-22](briefings/2026-06-22.md),
[2026-06-23](briefings/2026-06-23.md),
[2026-06-25](briefings/2026-06-25.md),
[2026-07-02](briefings/2026-07-02.md),
[2026-07-03](briefings/2026-07-03.md)

**oracle-manipulation** (4 briefings) —
[2026-06-20](briefings/2026-06-20.md),
[2026-06-22](briefings/2026-06-22.md),
[2026-06-25](briefings/2026-06-25.md),
[2026-07-04](briefings/2026-07-04.md)

**upgradeability** (4 briefings) —
[2026-06-13](briefings/2026-06-13.md),
[2026-06-18](briefings/2026-06-18.md),
[2026-06-20](briefings/2026-06-20.md),
[2026-07-03](briefings/2026-07-03.md)

**rounding** (3 briefings) —
[2026-06-15](briefings/2026-06-15.md),
[2026-06-16](briefings/2026-06-16.md),
[2026-07-06](briefings/2026-07-06.md)

**dos** (1 briefing) —
[2026-06-19](briefings/2026-06-19.md)

**front-running** (1 briefing) —
[2026-07-08](briefings/2026-07-08.md)

**integer-overflow** (1 briefing) —
[2026-06-15](briefings/2026-06-15.md)

**signature-replay** (1 briefing) —
[2026-06-14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 27
- **Date range:** 2026-06-12 → 2026-07-09 (28 days covered; one gap on Jun 26)
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 20 briefings (74%)
  2. `key-management` — 19 briefings (70%)
  3. `access-control` — 13 briefings (48%)
- **H1 2026 losses (CertiK):** $1.31B across 344 incidents — wallet compromise (#1 by $) at $444M; code vulns (#1 by count) at 204 incidents
- **Q2 2026 record:** 83 incidents / $755M — access-control exploits overtook smart-contract bugs as leading class for the first time

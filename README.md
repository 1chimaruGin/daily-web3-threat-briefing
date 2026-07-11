# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-07-11](briefings/2026-07-11.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-11](briefings/2026-07-11.md) | No new confirmed drain in 24h; GMX V1 $44M compensation plan advances as attacker returns $37M; OZ Wizard CVE-2026-48054 supply-chain risk day 28. | GMX V1 $42M (recovery), BonkDAO $20M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty; four prior incidents still active. | GMX V1 $42M, Summer.fi $6M, BonkDAO $20M, Altura $39M, ResupplyFi $9.6M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain in 24h; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M); Summer.fi $6M laundering confirmed via Tornado Cash. | Summer.fi ongoing, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun via illiquid Uniswap v3 pool. | BonkDAO $20M governance attack, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts thousands of software wallets at risk. | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains Jul 5–6; IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets comprehensive JFrog autopsy; ResupplyFi ERC-4626 post-mortem published. | IronWorm npm worm (37 pkgs), ResupplyFi $9.6M post-mortem | supply-chain, flash-loan, rounding, key-management | n/a |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug that threatened $70B; SlowMist warns AI IDE markdown injection executes on Open Folder. | Aptos MoveVM $70B-at-risk (patched), SlowMist AI IDE injection | logic-error, supply-chain, key-management | n/a |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI 'vibe-coded' Solidity as new CVE-surge driver. | Altura $39M, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 final report warns AI is driving a "vulnerability apocalypse" behind record 83-exploit quarter. | ResupplyFi $9.6M, Kinto Protocol $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts losing $36.7M in H1. | Edel Finance $403K, June 2026 monthly wrap | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and web3 dev creds — CISA July 2 patch deadline. | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX | key-management, supply-chain, access-control | n/a |
| [2026-06-30](briefings/2026-06-30.md) | No new confirmed drains; SecondFi white-hat identity disputed as EMURGO denies knowing who secured $18.5M in ADA; Sapphire Sleet backdoors 144 Mastra npm packages. | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm pkgs | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter with 83 hacks and $775M stolen. | SecondFi $2.4M–$20M keygen flaw, JaredFromSubway $7.5M Tornado | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection (Jun 25–26); expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals. | Polymarket $3M supply-chain injection, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing generalizable ZK witness-binding gap. | DARKNAVY Aztec circuit autopsy (technique disclosure) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB Chain. | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing across major wallet UIs. | JaredFromSubway MEV $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading attack class for first time. | Q2 2026 record: 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19) masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem. | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV threatens crypto web infra. | Aztec $2.21M escapeHatch(), CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | n/a |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain confirmed; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes the threat. | Quiet window; OWASP SC10:2026 upgradeability analysis | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 — patch all blockchain tooling now. | Unnamed bridge $127M (Jun 14 catch-up), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains. | EIP-7702 exploits $8M+, Lazarus macOS 'Mach-O Man' kit | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live. | Aztec Connect $2.1M, Syscoin Bridge $8M catch-up, Node.js CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to a flash-loan math flaw in a deprecated options vault; Node.js HIGH CVEs drop June 17 — patch before bots go live. | Thetanuts Finance $2.1M (flash-loan/rounding) | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol's BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026. | Flooring Protocol $500K NFTs, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains confirmed; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M across three platforms. | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds. | Humanity Protocol $36M DPRK attribution, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise. | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

_Sorted by frequency across all briefings (most-cited first). Each date links to the briefing where that class appeared._

- **logic-error** (22 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md)

- **key-management** (20 briefings) — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md)

- **access-control** (14 briefings) — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md)

- **supply-chain** (11 briefings) — [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-11](briefings/2026-07-11.md)

- **bridge-dvn** (10 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md)

- **flash-loan** (9 briefings) — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md)

- **unverified-contract** (6 briefings) — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md)

- **price-manipulation** (5 briefings) — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md)

- **oracle-manipulation** (4 briefings) — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [06-25](briefings/2026-06-25.md), [07-04](briefings/2026-07-04.md)

- **upgradeability** (4 briefings) — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md)

- **rounding** (3 briefings) — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md)

- **reentrancy** (2 briefings) — [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md)

- **dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

- **front-running** (1 briefing) — [07-08](briefings/2026-07-08.md)

- **integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

- **signature-replay** (1 briefing) — [06-14](briefings/2026-06-14.md)

---

## 📊 Stats

| Metric | Value |
|---|---|
| **Total briefings** | 29 |
| **Date range** | 2026-06-12 → 2026-07-11 (30 calendar days; one gap: 2026-06-26) |
| **Top bug class** | `logic-error` — 22 of 29 briefings (76%) |
| **#2 bug class** | `key-management` — 20 of 29 briefings (69%) |
| **#3 bug class** | `access-control` — 14 of 29 briefings (48%) |
| **Biggest single incident covered** | Unnamed bridge $127M (2026-06-19) |
| **Chains covered** | Ethereum, Arbitrum, Solana, BNB Chain, Cosmos, Aptos, Sui, Starknet, Cardano, Alephium, Tron, Syscoin, Polygon, Base, Optimism |

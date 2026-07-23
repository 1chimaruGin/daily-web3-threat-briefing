# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-23](briefings/2026-07-23.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% on BNB Chain after BTCB Median Oracle manipulation minted 4.5M unbacked tokens; July oracle-attack wave now spans four protocols | 42DAO BLC $915K | `oracle-manipulation` `price-manipulation` `key-management` `bridge-dvn` | ~$915K new; ~$159M July MTD |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw — single valid sig amplified 65,000× | Wanchain Bridge ~$10–13M NIGHT | `signature-replay` `bridge-dvn` `key-management` | ~$10–13M new; ~$158M July MTD |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core $1.65M Solana flash-loan pool-ratio attack — same exploit 2023 partial fix never ported to Solana; Summer.fi announces shutdown | Allbridge Core $1.65M, Summer.fi full shutdown | `flash-loan` `price-manipulation` `logic-error` | ~$1.65M new; ~$148M July MTD |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 wallet-extension PoC code goes live (35M users); CoinDCX post-mortem confirms 6-day dwell + employee arrest | CoinDCX $44M post-mortem, PETS 2026 wallet-extension PoC, Across Solana technical disclosure | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing hardware wallet apps with fakes; PETS 2026 browser-extension paper drops for 35M users | macOS wallet-replacement infostealer, PETS 2026 extension disclosures, Ill Bloom ongoing | `key-management` `supply-chain` `logic-error` | ~$5M+ Ill Bloom sweeps; $147M July MTD |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana relayer attacked July 17 | CoinDCX $44M, Across Protocol Solana, DeFiTuna $580K, BigONE $27M | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed perp neo-brokerage) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | `access-control` `logic-error` `oracle-manipulation` `key-management` `flash-loan` | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key — third oracle attack in five days | Ostium $18–22M | `key-management` `oracle-manipulation` `price-manipulation` `access-control` `upgradeability` | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 $37M recovered | `upgradeability` `reentrancy` `access-control` `oracle-manipulation` `supply-chain` | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 web3.py SSRF via EIP-3668 CCIP Read fully disclosed; no new drain; six incidents ongoing (~$78M) | CVE-2026-40072 web3.py SSRF | `oracle-manipulation` `access-control` `logic-error` `supply-chain` `flash-loan` | ~$78M ongoing |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026 report: 182 incidents, supply-chain #1 loss class ($298M); BonkDAO attacker launders $19M into "BONK 2.0" DAO | BonkDAO laundering, Bonzo Lend $9M fix deployed | `oracle-manipulation` `access-control` `logic-error` `key-management` `supply-chain` | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation; Ill Bloom PRNG keeps draining wallets | Bonzo Lend $9M, Ill Bloom $5M+ ongoing | `oracle-manipulation` `price-manipulation` `key-management` `flash-loan` | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances as attacker returns $37M; OZ Wizard CVE-2026-48054 day 28 | GMX V1 recovery/comp ongoing | `reentrancy` `flash-loan` `access-control` `logic-error` `supply-chain` | ~$75M unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M (Arbitrum) | `reentrancy` `flash-loan` `access-control` `logic-error` `key-management` | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M); Summer.fi laundering confirmed via Tornado Cash | Summer.fi Tornado Cash laundering, BonkDAO to exchanges | `key-management` `flash-loan` `access-control` `logic-error` | ~$75M ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M, MEV backrun $2M | `access-control` `logic-error` `front-running` | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG flaw disclosed ($5M cumulative wallet drains) | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | `flash-loan` `logic-error` `key-management` | ~$11M new |
| [2026-07-06](briefings/2026-07-06.md) | No new drain; IronWorm Rust npm worm (eBPF rootkit + Tor C2, 37 packages) fully autopsied; ResupplyFi post-mortem published | IronWorm npm worm 37 packages, ResupplyFi $9.6M post-mortem | `supply-chain` `flash-loan` `rounding` `key-management` | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion threatening $70B; SlowMist warns AI IDE markdown injection executes on Open Folder | Aptos MoveVM $70B-at-risk (patched), SlowMist AI IDE injection, Miasma Cosmos worm | `logic-error` `supply-chain` `key-management` | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault locked (COO-tied DVN verifier); CSA formalizes AI 'vibe-coded' Solidity as new CVE-surge driver | Altura $39M gold-vault, LendFi $5.2M oracle | `key-management` `bridge-dvn` `oracle-manipulation` `logic-error` `unverified-contract` | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi $9.6M ERC-4626 laundering active; Kinto $1.55M proxy-backdoor; Immunefi Q2 warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M ERC-4626, Kinto $1.55M proxy | `flash-loan` `price-manipulation` `upgradeability` `access-control` `key-management` | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token exchange-rate manipulation; June 2026 wrap: 45 incidents, $75.87M lost | Edel Finance $403K, June 2026 monthly wrap | `flash-loan` `price-manipulation` `unverified-contract` `key-management` | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild by Djinn Stealer — CISA KEV July 2 patch deadline | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX | `key-management` `supply-chain` `access-control` | n/a new |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi ADA custody dispute; Sapphire Sleet backdoors 144 Mastra npm packages targeting crypto teams | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm packages | `key-management` `supply-chain` `logic-error` `bridge-dvn` | ~$18.5M in custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter: 83 hacks, $775M | SecondFi $2.4M–$20M keygen flaw, Q2 record close | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$22.5M new; Q2 $775M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket $3M supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 threatens DAO governance portals | Polymarket $3M injection, CVE-2026-12866 expr-eval | `supply-chain` `key-management` `logic-error` `access-control` | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drain; DARKNAVY publishes definitive Aztec escapeHatch() ZK circuit autopsy revealing generalizable witness-binding gap | (no new drain); DARKNAVY Aztec ZK autopsy | `logic-error` `access-control` `supply-chain` `key-management` | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; OLPC/LABUBU PancakeSwap pool $1.1M token-param desync | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap Starknet $305K | `key-management` `bridge-dvn` `price-manipulation` `oracle-manipulation` `logic-error` | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike flaw | `logic-error` `unverified-contract` `access-control` | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record: 83 incidents, $755M lost; access-control overtakes smart-contract bugs as leading class | (no new drain); Q2 2026 record | `access-control` `key-management` `bridge-dvn` `price-manipulation` | Q2 ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K (catch-up) | `logic-error` `bridge-dvn` `oracle-manipulation` `price-manipulation` | ~$600K catch-up |
| [2026-06-21](briefings/2026-06-21.md) | Aztec $2.21M escapeHatch() TurboVerifier spoofed ZK public inputs autopsied; CVE-2026-48907 Joomla CVSS-10 CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla | `access-control` `logic-error` `unverified-contract` | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | Quiet window; abandoned-contract pattern in 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry | (no new drain) | `unverified-contract` `logic-error` `upgradeability` `oracle-manipulation` | n/a; June ~$195M+ |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 (catch-up) via dual validator+finality bypass; Node.js drops 2 HIGH CVEs Jun 18 | Unnamed bridge $127M (Jun 14 catch-up), Node.js HIGH CVEs | `bridge-dvn` `key-management` `logic-error` `dos` | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit harvesting keychains | (no new drain); EIP-7702 $8M+ cumulative | `access-control` `key-management` `supply-chain` `upgradeability` | n/a new; ~$8M EIP-7702 cumulative |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect $2.1M ZK L1/L2 proof-boundary bypass; Node.js HIGH CVE drops; Syscoin Bridge $8M SPV forgery (catch-up) | Aztec Connect $2.1M, Syscoin Bridge $8M (catch-up), Node.js HIGH CVE | `logic-error` `bridge-dvn` `supply-chain` `key-management` | ~$2.1M strict; ~$10.3M incl catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault (mostly whitehatted); Node.js HIGH CVEs inbound | Thetanuts Finance $2.1M | `flash-loan` `rounding` `logic-error` | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agents claim $45M cumulative 2026 | Flooring Protocol ~$500K, Unleash Protocol $3.9M (catch-up) | `integer-overflow` `rounding` `logic-error` `access-control` | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new drain; Alephium bridge forged-VAA DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | `bridge-dvn` `signature-replay` `logic-error` | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M (DPRK attributed), CVE-2026-48054 OZ Wizard | `key-management` `upgradeability` `access-control` `supply-chain` | ~$36M attributed |
| [2026-06-12](briefings/2026-06-12.md) | Raydium $1.34M fake LP tokens on legacy Solana pools; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | `flash-loan` `logic-error` `key-management` `bridge-dvn` `unverified-contract` | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by frequency (number of briefings). Each date links to the briefing where that class appears.

- **logic-error** (29 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-21](briefings/2026-07-21.md)

- **key-management** (29 briefings) — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-22](briefings/2026-07-22.md), [07-23](briefings/2026-07-23.md)

- **access-control** (19 briefings) — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md)

- **supply-chain** (17 briefings) — [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md)

- **flash-loan** (13 briefings) — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-21](briefings/2026-07-21.md)

- **bridge-dvn** (14 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-18](briefings/2026-07-18.md), [07-20](briefings/2026-07-20.md), [07-22](briefings/2026-07-22.md), [07-23](briefings/2026-07-23.md)

- **oracle-manipulation** (11 briefings) — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [06-25](briefings/2026-06-25.md), [07-04](briefings/2026-07-04.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-23](briefings/2026-07-23.md)

- **price-manipulation** (9 briefings) — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-12](briefings/2026-07-12.md), [07-16](briefings/2026-07-16.md), [07-21](briefings/2026-07-21.md), [07-23](briefings/2026-07-23.md)

- **upgradeability** (6 briefings) — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md)

- **unverified-contract** (6 briefings) — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md)

- **reentrancy** (3 briefings) — [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-15](briefings/2026-07-15.md)

- **rounding** (3 briefings) — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md)

- **signature-replay** (2 briefings) — [06-14](briefings/2026-06-14.md), [07-22](briefings/2026-07-22.md)

- **dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

- **front-running** (1 briefing) — [07-08](briefings/2026-07-08.md)

- **integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

---

## 📊 Stats

- **Total briefings:** 41 (no briefing for 2026-06-26)
- **Date range:** 2026-06-12 → 2026-07-23 (42 days covered)
- **Top 3 most frequent bug classes:**
  1. `logic-error` — 29 briefings (tied)
  1. `key-management` — 29 briefings (tied)
  3. `access-control` — 19 briefings
- **July 2026 MTD losses:** ~$159M across 17+ incidents (PeckShield / SlowMist tracking)
- **Q2 2026 total (closed):** ~$755–775M across 83 incidents — all-time quarterly record

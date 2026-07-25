# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-25](briefings/2026-07-25.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration and flawed exchange count-check; Injective npm advisory still active | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K new; ~$196M July MTD |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade Arbitrum bridge drained $24.15M after validator signing keys compromised; three simultaneous bridge exploits total $35.55M | AFX Trade $24.15M, Verus ETH Bridge ~$7.4M, B² Network ~$4M | key-management, bridge-dvn | ~$35.55M new; ~$195M July MTD |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% on BNB Chain after BTCB Median Oracle manipulation minted unbacked tokens | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K new; ~$159M July MTD |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw amplifying a single valid sig 65,000× | Wanchain Bridge $10–13M NIGHT | signature-replay, bridge-dvn, key-management | ~$10–13M new; ~$158M July MTD |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 partial fix | Allbridge Core $1.65M | flash-loan, price-manipulation, logic-error | ~$1.65M new; ~$148M July MTD |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 opens with 35M-user wallet-extension PoC; CoinDCX post-mortem confirms 6-day dwell and employee arrest | CoinDCX $44M post-mortem, PETS 2026 PoC | key-management, supply-chain, bridge-dvn, logic-error | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 wallet-extension paper for 35M users | macOS wallet-replacement infostealer, PETS 2026 disclosures | key-management, supply-chain, logic-error | ~$5M+ active; $147M July MTD |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked same day | CoinDCX $44M, Across Protocol Solana, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade drained $1.34M on Arbitrum — third Arbitrum perp hack in one week; Ostium still halted | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum; third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M tracked |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery ($37M returned) | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M tracked |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed; six ongoing incidents (~$78M unrecovered) | Ongoing: BonkDAO, Bonzo Lend, GMX V1, Altura, Summer.fi, ResupplyFi | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 at $298M; BonkDAO attacker launders $19M into BONK 2.0 | BonkDAO laundering, Bonzo Lend fix deployed | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation | Bonzo Lend $9M, Ill Bloom $5M+ ongoing | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new |
| [2026-07-11](briefings/2026-07-11.md) | No new confirmed drain; GMX V1 $44M compensation plan advances; OZ Wizard CVE day 28 | GMX V1 recovery, ongoing: BonkDAO, Altura, Summer.fi, ResupplyFi | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M tracked |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise #1 loss vector at $444M; Summer.fi laundering confirmed | Summer.fi, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance token buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG flaw puts thousands of wallets at risk | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M new |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets JFrog autopsy across 37 packages | IronWorm npm worm (37 packages), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new drains |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion threatening $70B; SlowMist warns AI IDE markdown injection RCE | Hexens/Aptos MoveVM $70B at risk (patched), AI IDE markdown injection | logic-error, supply-chain, key-management | n/a new drains; $70B theoretical (patched) |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug — COO-tied DVN verifier locked depositors; CSA formalizes AI Solidity as new CVE-surge driver | Altura $39M, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi launders $6.5M through Tornado Cash; Kinto $1.55M proxy-backdoor exploit confirmed | ResupplyFi $9.6M, Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance loses $403K to flash-loan wrapped-token exchange-rate manipulation | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 SimpleHelp RMM CVSS-10 exploited in-the-wild; Djinn Stealer harvesting crypto wallets — CISA deadline | CVE-2026-48558, GlassWorm macOS wave | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat dispute; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M disputed custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes at 83 hacks / $775M | SecondFi $2.4M–$20M keygen | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M to supply-chain frontend injection; CVE-2026-12866 expr-eval CVSS-9.8 RCE | Polymarket $3M, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed drains; DARKNAVY publishes definitive Aztec escapeHatch() autopsy revealing ZK witness-binding gap | Aztec circuit autopsy (technique disclosure) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko Bridge loses $1.7M to SGX signing key leaked to GitHub; LABUBU/OLPC $1.1M via token param desync on BNB | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike enables on-chain identity spoofing | JaredFromSubway MEV $15M, ENS lookalike flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control overtakes smart-contract bugs as #1 | Q2 2026 record: 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a (quarterly record briefing) |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK inputs enabling $2.21M drain; Joomla CVSS-10 KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla KEV | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; abandoned-contract pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy entry | (no new drains) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge exploited Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M (catch-up) |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ real-world exploits; Lazarus 'Mach-O Man' macOS active | (no new on-chain drains) | access-control, key-management, supply-chain, upgradeability | n/a; EIP-7702 cumulative ~$8M+ |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up) | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M (strict window) |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs incoming | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K, Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M (catch-up) |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M (catch-up) |
| [2026-06-13](briefings/2026-06-13.md) | Humanity Protocol $36M breach attributed to DPRK phishing; OZ Wizard CVE-2026-48054 injects into test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by number of briefings containing each tag (most frequent first). Click a date to jump to that day's analysis.

**logic-error** (30 briefings) — [2026-06-12](briefings/2026-06-12.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-30](briefings/2026-06-30.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-25](briefings/2026-07-25.md)

**key-management** (30 briefings) — [2026-06-12](briefings/2026-06-12.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-30](briefings/2026-06-30.md), [2026-07-01](briefings/2026-07-01.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-24](briefings/2026-07-24.md)

**access-control** (19 briefings) — [2026-06-13](briefings/2026-06-13.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-28](briefings/2026-06-28.md), [2026-07-01](briefings/2026-07-01.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-17](briefings/2026-07-17.md)

**supply-chain** (18 briefings) — [2026-06-13](briefings/2026-06-13.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-30](briefings/2026-06-30.md), [2026-07-01](briefings/2026-07-01.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-25](briefings/2026-07-25.md)

**bridge-dvn** (15 briefings) — [2026-06-12](briefings/2026-06-12.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-30](briefings/2026-06-30.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-24](briefings/2026-07-24.md)

**flash-loan** (13 briefings) — [2026-06-12](briefings/2026-06-12.md), [2026-06-16](briefings/2026-06-16.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-21](briefings/2026-07-21.md)

**oracle-manipulation** (11 briefings) — [2026-06-20](briefings/2026-06-20.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-25](briefings/2026-06-25.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-23](briefings/2026-07-23.md)

**price-manipulation** (10 briefings) — [2026-06-22](briefings/2026-06-22.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-25](briefings/2026-06-25.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-25](briefings/2026-07-25.md)

**unverified-contract** (6 briefings) — [2026-06-12](briefings/2026-06-12.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-24](briefings/2026-06-24.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-04](briefings/2026-07-04.md)

**upgradeability** (6 briefings) — [2026-06-13](briefings/2026-06-13.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-20](briefings/2026-06-20.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-16](briefings/2026-07-16.md)

**reentrancy** (3 briefings) — [2026-07-10](briefings/2026-07-10.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-15](briefings/2026-07-15.md)

**rounding** (3 briefings) — [2026-06-15](briefings/2026-06-15.md), [2026-06-16](briefings/2026-06-16.md), [2026-07-06](briefings/2026-07-06.md)

**signature-replay** (2 briefings) — [2026-06-14](briefings/2026-06-14.md), [2026-07-22](briefings/2026-07-22.md)

**integer-overflow** (1 briefing) — [2026-06-15](briefings/2026-06-15.md)

**dos** (1 briefing) — [2026-06-19](briefings/2026-06-19.md)

**front-running** (1 briefing) — [2026-07-08](briefings/2026-07-08.md)

---

## 📊 Stats

- **Total briefings:** 44
- **Date range:** 2026-06-12 → 2026-07-25 (44 days; one gap on 2026-06-26)
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 30 briefings (68%)
  2. `key-management` — 30 briefings (68%)
  3. `access-control` — 19 briefings (43%)
- **Emerging trend:** `supply-chain` appears in 18 briefings (41%), accelerating through July — npm worms, macOS infostealers, and OIDC pipeline compromise all contributing.
- **July 2026 MTD losses:** ~$196M across tracked incidents as of 2026-07-25.
- **Largest single-day cluster tracked:** 2026-07-24 — three simultaneous bridge exploits totaling $35.55M in under 7 hours (AFX Trade $24.15M, Verus ETH Bridge $7.54M, B² Network $3.86M).

# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-08-13](briefings/2026-08-13.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-08-13](briefings/2026-08-13.md) | Ravencoin active 3-day reorg after KAWPOW PoW bypass; Coreum XRPL bridge loses 200K XRP via relay forgery | Ravencoin KAWPOW, Coreum XRPL Bridge $200K, Coldcard $130M (D14), BTCPay (D6) | logic-error, bridge-dvn, key-management, access-control, supply-chain | ~$130M+ |
| [2026-08-12](briefings/2026-08-12.md) | Coldcard Day 13 (~$130M+); ecosystem audit finds 4,962 vulns in 390 projects; BTCPay macaroons still live D5 | Coldcard $130M (D13), BTCPay (D5), Wanchain $10-13M (D22), Coinsbuy $7.9M (D4), ChainDrop (D8) | key-management, access-control, supply-chain, signature-replay | ~$130M+ |
| [2026-08-11](briefings/2026-08-11.md) | Coinsbuy CEX loses $7.9M via hot-wallet compromise; Coldcard Day 12 ~$130M+; Wanchain post-mortem published | Coinsbuy $7.9M, Coldcard $130M (D12), BTCPay (D3), Wanchain $10-13M (D21) | key-management, access-control, supply-chain, signature-replay | ~$130M+ |
| [2026-08-10](briefings/2026-08-10.md) | Coldcard Day 11 (~$130M+, no arrests); ChainDrop npm worm D6 self-propagating, 1.3B+ monthly downloads at risk | Coldcard $130M (D11), BTCPay (D2), ChainDrop 400–868+ packages, Wanchain (D20) | key-management, access-control, supply-chain, signature-replay | ~$130M+ |
| [2026-08-09](briefings/2026-08-09.md) | Coldcard Day 10 (~$130M+); BTCPay Server critical LND macaroon auth-bypass actively draining Lightning nodes | Coldcard $130M (D10), BTCPay Lightning drains | key-management, access-control, supply-chain, signature-replay | ~$130M+ |
| [2026-08-08](briefings/2026-08-08.md) | Coldcard Day 9 ~$130M ongoing; pre-emptive hunt window for abi.encodePacked bridge signature-replay patterns | Coldcard $130M (D9), Wanchain $10-13M (D18) | key-management, signature-replay, oracle-manipulation, supply-chain | ~$140M |
| [2026-08-07](briefings/2026-08-07.md) | Shai-Hulud evolves into CHAINDROP second wave — 1,280+ npm packages, 2B monthly downloads; Coldcard Day 8 | CHAINDROP npm worm 1,280+ pkgs, Coldcard $130M (D8) | supply-chain, key-management, signature-replay | ~$130M |
| [2026-08-06](briefings/2026-08-06.md) | Shai-Hulud npm worm plants Ethereum-C2 backdoor in 400+ packages; Coldcard phishing surge Day 7 | Shai-Hulud npm 400+ pkgs, Coldcard $130M (D7), Wanchain deadline expired | supply-chain, key-management, signature-replay, access-control | ~$130M |
| [2026-08-05](briefings/2026-08-05.md) | Coldcard fragments into 15-attacker free-for-all ~$130M; XRPL manifest-flood DoS patched in xrpld 3.2.1 | Coldcard $130M (15 attackers), XRPL DoS hotfix | key-management, dos, signature-replay | ~$130M |
| [2026-08-04](briefings/2026-08-04.md) | Coldcard Wave 4 escalates to ~$116M across 5,200+ addresses; Adform CDN JS poisoning swaps wallet addresses | Coldcard $116M (W4), Adform CDN supply-chain | key-management, supply-chain, signature-replay, bridge-dvn | ~$116M |
| [2026-08-03](briefings/2026-08-03.md) | Coldcard enters laundering phase ($89M); AFX Trade executes $24M distribution; BlueNoroff ClickFix hits 100+ targets | Coldcard $89M (W3 launder), AFX Trade $24M comp, BlueNoroff ClickFix | key-management, bridge-dvn, supply-chain, signature-replay | ~$89M |
| [2026-08-02](briefings/2026-08-02.md) | Coldcard escalates to $89M / 4,585 addresses in three waves; Wave 3 uses P2WSH to evade clustering | Coldcard $89M (W3), AFX Trade, Wanchain deadline T-4 | key-management, bridge-dvn, signature-replay | ~$89M |
| [2026-08-01](briefings/2026-08-01.md) | Coldcard firmware entropy flaw drains $38M BTC from ~500 wallets; AFX Trade sets Aug 3 compensation plan | Coldcard $38M BTC, AFX Trade recovery | key-management, bridge-dvn, signature-replay | ~$38M |
| [2026-07-31](briefings/2026-07-31.md) | Wanchain sets Aug 6 white-hat deadline on $10M NIGHT; Drift exploiter moves $44.4M to Tornado Cash | Wanchain $10M deadline, Drift $44.4M Tornado Cash | signature-replay, key-management, supply-chain | ~$0 new |
| [2026-07-30](briefings/2026-07-30.md) | Unidentified BNB Chain DAO drained $8.2M via anyone-callable vault; Garden Finance HTLC hit across 4 chains | Crypto DAO BNB $8.2M, Garden Finance HTLC $450K | access-control, logic-error, bridge-dvn, flash-loan | ~$9.4M |
| [2026-07-29](briefings/2026-07-29.md) | Blockaid confirms record $1.1B H1 2026 losses (DPRK drove $577M); GMX reentrancy post-mortems published | Blockaid H1 report, GMX $42M recovered, BarnBridge $776K | reentrancy, logic-error, access-control, key-management | ~$0 new |
| [2026-07-28](briefings/2026-07-28.md) | WEMIX loses $6.25M to owner-key compromise enabling unauthorized stablecoin minting | WEMIX $6.25M, Triple-A $12M (ongoing) | access-control, key-management, oracle-manipulation | ~$6.25M |
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M; CertiK reports physical wrench attacks claimed $124M in H1 at record pace | Triple-A $12M revised | key-management, unverified-contract, access-control | ~$12M |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A crypto gateway loses $9.7M as hot wallets across 6 chains drained simultaneously | Triple-A $9.7M | key-management, access-control | ~$9.7M |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration and flawed exchange count-check | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade Arbitrum bridge drained $24.15M after validator signing keys compromised; 3 simultaneous July 23 hacks | AFX Trade $24.15M, Verus ETH bridge $7.4M, B² Network $4M | key-management, bridge-dvn | ~$35.55M |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% via BTCB Median Oracle manipulation; July oracle-attack wave spans 4 protocols | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw — single signature amplified 65,000× | Wanchain Bridge $10-13M NIGHT | signature-replay, bridge-dvn, key-management | ~$10-13M |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 fix | Allbridge Core $1.65M, Summer.fi shutdown | flash-loan, price-manipulation, logic-error | ~$1.65M |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 opens with 35M-user wallet-extension PoC live; CoinDCX post-mortem confirms 6-day dwell, arrest | CoinDCX $44M post-mortem, PETS 2026 PoC, Across Protocol disclosure | key-management, supply-chain, bridge-dvn, logic-error | ~$147M MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 paper drops for 35M users | macOS wallet-replacement infostealer, PETS 2026 wallet-extension (35M users) | key-management, supply-chain, logic-error | ~$5M+ |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol Solana relayer, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key — third oracle attack in five days | Ostium $18–22M, Kinto shutdown, Altura $39M locked | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 $37M returned | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via CCIP Read) fully disclosed; six incidents ongoing (~$78M unrecovered) | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M retained, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 by losses at $298M; BonkDAO attacker launders into BONK 2.0 | BonkDAO $20M laundering, Bonzo Lend $9M fix | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation | Bonzo Lend $9M, Ill Bloom $5M+ ongoing | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation advances as attacker returns $37M; OZ Wizard CVE D28 | GMX V1 recovery, BonkDAO $20M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned for $5M bounty | GMX V1 $42M, Summer.fi, BonkDAO, Altura, ResupplyFi | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector at $444M | Summer.fi laundering, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M governance, Ethereum MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG puts thousands of wallets at risk | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets JFrog autopsy; ResupplyFi ERC-4626 post-mortem public | IronWorm npm 37 packages, ResupplyFi $9.6M post-mortem | supply-chain, flash-loan, rounding, key-management | ~$0 new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion ($70B at risk); SlowMist AI IDE markdown injection | Aptos MoveVM $70B theoretical (patched), SlowMist AI IDE injection | logic-error, supply-chain, key-management | ~$0 new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug via COO-tied DVN verifier; CSA formalizes AI vibe-coded Solidity as CVE driver | Altura $39M, LendFi $5.2M oracle | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M; Immunefi Q2 warns AI driving vulnerability apocalypse behind record quarter | ResupplyFi $9.6M ERC-4626, Kinto $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance loses $403K to flash-loan wrapped-token exchange-rate manipulation | Edel Finance $403K, June 2026 wrap 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets | CVE-2026-48558 SimpleHelp, GlassWorm macOS, SecondFi custody standoff | key-management, supply-chain, access-control | ~$0 new |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi $18.5M custody dispute, Sapphire Sleet 144 npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 closes at record 83 hacks $775M | SecondFi $2.4M–$20M keygen, JaredFromSubway MEV, Q2 record | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M supply-chain, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy (generalizable ZK witness-binding gap) | DARKNAVY Aztec circuit autopsy | logic-error, access-control, supply-chain, key-management | ~$0 new |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M on BNB | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 all-time quarterly record — 83 incidents $755M lost; access-control overtakes smart-contract bugs | Q2 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | ~$0 new |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier spoofed ZK public inputs $2.21M; Joomla JCE CVSS-10 in KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | ~$0 new |
| [2026-06-20](briefings/2026-06-20.md) | Quiet window; abandoned-contract pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 formalizes threat | (no new drains) | unverified-contract, logic-error, upgradeability, oracle-manipulation | ~$0 new |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs | Unnamed 3-protocol bridge $127M, Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ real-world exploits; Lazarus Mach-O Man macOS kit active | (no new confirmed drains) | access-control, key-management, supply-chain, upgradeability | ~$0 new |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge ~$8M catch-up, Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M catch-up | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K, AFI Protocol $480K catch-up | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing chain; OZ Wizard CVE-2026-48054 | Humanity Protocol $36M DPRK, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by number of briefings where the class appears (most frequent first). Dates link to the relevant briefing.

**key-management** (48 briefings) —
[2026-08-13](briefings/2026-08-13.md), [2026-08-12](briefings/2026-08-12.md), [2026-08-11](briefings/2026-08-11.md), [2026-08-10](briefings/2026-08-10.md), [2026-08-09](briefings/2026-08-09.md), [2026-08-08](briefings/2026-08-08.md), [2026-08-07](briefings/2026-08-07.md), [2026-08-06](briefings/2026-08-06.md), [2026-08-05](briefings/2026-08-05.md), [2026-08-04](briefings/2026-08-04.md), [2026-08-03](briefings/2026-08-03.md), [2026-08-02](briefings/2026-08-02.md), [2026-08-01](briefings/2026-08-01.md), [2026-07-31](briefings/2026-07-31.md), [2026-07-29](briefings/2026-07-29.md), [2026-07-28](briefings/2026-07-28.md), [2026-07-27](briefings/2026-07-27.md), [2026-07-26](briefings/2026-07-26.md), [2026-07-24](briefings/2026-07-24.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

**logic-error** (33 briefings) —
[2026-08-13](briefings/2026-08-13.md), [2026-07-30](briefings/2026-07-30.md), [2026-07-29](briefings/2026-07-29.md), [2026-07-25](briefings/2026-07-25.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**access-control** (30 briefings) —
[2026-08-13](briefings/2026-08-13.md), [2026-08-12](briefings/2026-08-12.md), [2026-08-11](briefings/2026-08-11.md), [2026-08-10](briefings/2026-08-10.md), [2026-08-09](briefings/2026-08-09.md), [2026-08-06](briefings/2026-08-06.md), [2026-07-30](briefings/2026-07-30.md), [2026-07-29](briefings/2026-07-29.md), [2026-07-28](briefings/2026-07-28.md), [2026-07-27](briefings/2026-07-27.md), [2026-07-26](briefings/2026-07-26.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md), [2026-07-17](briefings/2026-07-17.md)

**supply-chain** (29 briefings) —
[2026-08-13](briefings/2026-08-13.md), [2026-08-12](briefings/2026-08-12.md), [2026-08-11](briefings/2026-08-11.md), [2026-08-10](briefings/2026-08-10.md), [2026-08-09](briefings/2026-08-09.md), [2026-08-08](briefings/2026-08-08.md), [2026-08-07](briefings/2026-08-07.md), [2026-08-06](briefings/2026-08-06.md), [2026-08-04](briefings/2026-08-04.md), [2026-08-03](briefings/2026-08-03.md), [2026-07-31](briefings/2026-07-31.md), [2026-07-25](briefings/2026-07-25.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

**bridge-dvn** (21 briefings) —
[2026-08-13](briefings/2026-08-13.md), [2026-08-04](briefings/2026-08-04.md), [2026-08-03](briefings/2026-08-03.md), [2026-08-02](briefings/2026-08-02.md), [2026-08-01](briefings/2026-08-01.md), [2026-07-30](briefings/2026-07-30.md), [2026-07-24](briefings/2026-07-24.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**signature-replay** (15 briefings) —
[2026-08-12](briefings/2026-08-12.md), [2026-08-11](briefings/2026-08-11.md), [2026-08-10](briefings/2026-08-10.md), [2026-08-09](briefings/2026-08-09.md), [2026-08-08](briefings/2026-08-08.md), [2026-08-07](briefings/2026-08-07.md), [2026-08-06](briefings/2026-08-06.md), [2026-08-05](briefings/2026-08-05.md), [2026-08-04](briefings/2026-08-04.md), [2026-08-03](briefings/2026-08-03.md), [2026-08-02](briefings/2026-08-02.md), [2026-08-01](briefings/2026-08-01.md), [2026-07-31](briefings/2026-07-31.md), [2026-07-22](briefings/2026-07-22.md), [2026-06-14](briefings/2026-06-14.md)

**flash-loan** (14 briefings) —
[2026-07-30](briefings/2026-07-30.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

**oracle-manipulation** (13 briefings) —
[2026-08-08](briefings/2026-08-08.md), [2026-07-28](briefings/2026-07-28.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

**price-manipulation** (10 briefings) —
[2026-07-25](briefings/2026-07-25.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

**unverified-contract** (7 briefings) —
[2026-07-27](briefings/2026-07-27.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

**upgradeability** (6 briefings) —
[2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

**reentrancy** (4 briefings) —
[2026-07-29](briefings/2026-07-29.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md)

**rounding** (3 briefings) —
[2026-07-06](briefings/2026-07-06.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

**dos** (2 briefings) —
[2026-08-05](briefings/2026-08-05.md), [2026-06-19](briefings/2026-06-19.md)

**integer-overflow** (1 briefing) —
[2026-06-15](briefings/2026-06-15.md)

**front-running** (1 briefing) —
[2026-07-08](briefings/2026-07-08.md)

---

## 📊 Stats

- **Total briefings:** 62
- **Date range:** June 12, 2026 — August 13, 2026
- **Top 3 bug classes:**
  1. `key-management` — 48 briefings (77% of all days)
  2. `logic-error` — 33 briefings (53% of all days)
  3. `access-control` — 30 briefings (48% of all days)
- **Notable:** `supply-chain` surged in August (10 of 13 Aug briefings) driven by the CHAINDROP/Shai-Hulud npm worm campaign. `signature-replay` appeared in 12 consecutive August briefings (Aug 1–12) due to the Coldcard hack's laundering patterns and Wanchain bridge exploitation.

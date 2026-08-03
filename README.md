# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.  
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.  
**Latest briefing:** [2026-08-03](briefings/2026-08-03.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-08-03](briefings/2026-08-03.md) | Coldcard attacker enters Wave 3 laundering phase; AFX Trade executes $24M victim distribution; BlueNoroff ClickFix hits 100+ crypto targets | Coldcard $89M (Day 4), AFX Trade $24M compensation, BlueNoroff ClickFix | key-management, bridge-dvn, supply-chain, signature-replay | ~$89M cumulative |
| [2026-08-02](briefings/2026-08-02.md) | Coldcard escalates to $89M / 4,585 addresses in three waves; Wave 3 switches to P2WSH to evade chain-analytics | Coldcard $89M (Wave 3), AFX Trade, Wanchain deadline | key-management, bridge-dvn, signature-replay | ~$89M |
| [2026-08-01](briefings/2026-08-01.md) | Coldcard firmware entropy flaw drains $38M BTC from ~500 wallets; AFX sets Aug 3 compensation plan | Coldcard $38M BTC entropy flaw, AFX Trade recovery | key-management, bridge-dvn, signature-replay | ~$38M confirmed |
| [2026-07-31](briefings/2026-07-31.md) | Wanchain sets Aug 6 white-hat deadline on $10M NIGHT; Drift exploiter moves $44.4M to Tornado Cash; CVE-2026-40072 web3.py SSRF | Wanchain deadline, Drift $44.4M laundering | signature-replay, key-management, supply-chain | ~$222M July MTD |
| [2026-07-30](briefings/2026-07-30.md) | BNB Chain DAO drained $8.2M via anyone-callable vault; Garden Finance HTLC hit across 4 chains for $450K | BNB DAO $8.2M, Garden Finance $450K | access-control, logic-error, bridge-dvn, flash-loan | ~$9.4M new |
| [2026-07-29](briefings/2026-07-29.md) | Blockaid confirms $1.1B H1 2026 losses (DPRK drove $577M); GMX cross-contract reentrancy post-mortems published | Blockaid H1 report, GMX recovery, BarnBridge $776K | reentrancy, logic-error, access-control, key-management | ~$214M July MTD |
| [2026-07-28](briefings/2026-07-28.md) | WEMIX loses $6.25M to owner-key compromise enabling unauthorized stablecoin minting | WEMIX $6.25M, Triple-A ongoing | access-control, key-management, oracle-manipulation | ~$6.25M new |
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M; CertiK reports physical wrench attacks claimed $124M in H1 2026 | Triple-A $12M revised | key-management, unverified-contract, access-control | ~$12M |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A crypto payment gateway loses $9.7M as hot wallets drained across 6 chains simultaneously | Triple-A $9.7M | key-management, access-control | ~$9.7M new |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration; Injective Labs npm supply chain advisory | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade Arbitrum bridge drained $24.15M after validator keys compromised; three simultaneous exploits total $35.55M | AFX Trade $24.15M, Verus ETH bridge $7.4M, B² $4M | key-management, bridge-dvn | ~$35.55M new |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% on BNB after BTCB Median Oracle manipulation | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K new |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw amplifying a valid sig 65,000× | Wanchain $10–13M NIGHT | signature-replay, bridge-dvn, key-management | ~$10–13M new |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 partial fix | Allbridge Core $1.65M, Summer.fi shutdown | flash-loan, price-manipulation, logic-error | ~$1.65M new |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 wallet-extension PoC code goes live for 35M users; CoinDCX post-mortem confirms 6-day dwell time | CoinDCX post-mortem, PETS 2026 PoC, Across Protocol | key-management, supply-chain, bridge-dvn, logic-error | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 paper drops for 35M users | macOS wallet replacement, PETS 2026, Ill Bloom $5M+ | key-management, supply-chain, logic-error | ~$5M+ active |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed perp) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key — third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M tracked |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns $37M | Kinto shutdown, GMX V1 recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M tracked |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via CCIP Read) fully disclosed Day 4; six incidents ongoing | CVE-2026-40072, ongoing incidents | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M tracked |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026 report: 182 incidents, supply-chain #1 by losses at $298M; BonkDAO launders $19M | BonkDAO laundering, Bonzo Lend recovery | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new |
| [2026-07-11](briefings/2026-07-11.md) | GMX V1 $44M compensation plan advances as attacker returns $37M; OZ Wizard CVE day 28 | GMX V1 recovery, ongoing incidents | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M tracked |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026: wallet compromise #1 loss vector at $444M; Summer.fi laundering confirmed | Summer.fi laundering, BonkDAO to exchanges | key-management, flash-loan, access-control, logic-error | ~$75M tracked |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; ETH trader loses $2M to MEV backrun | BonkDAO $20M, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts wallets at risk | Summer.fi $6M, Ill Bloom $5M | flash-loan, logic-error, key-management | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | No new drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets JFrog autopsy | IronWorm npm (37 pkgs), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion threatening $70B; SlowMist warns AI IDE markdown injection | Aptos MoveVM (patched), SlowMist AI IDE, Miasma worm | logic-error, supply-chain, key-management | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); CSA formalizes AI vibe-coded Solidity as CVE-surge driver | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2 warns AI is driving vulnerability apocalypse | ResupplyFi $9.6M (TC), Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation | Edel Finance $403K, June wrap $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited; Djinn Stealer harvests crypto wallets | CVE-2026-48558 SimpleHelp, GlassWorm macOS | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi custody dispute, Sapphire Sleet (144 pkgs) | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M in dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 closes as record quarter | SecondFi $2.4M–$20M, JaredFromSubway $7.5M | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M to supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M supply-chain, CVE-2026-12866 | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing ZK witness-binding gap | DARKNAVY Aztec autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M | Taiko $1.7M, OLPC/LABUBU $1.1M, mySwap $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables identity spoofing | JaredFromSubway MEV $15M, ENS lookalike | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 all-time quarterly record — 83 incidents, $755M lost; access-control overtakes smart-contract bugs | Q2 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a (quarterly) |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs; Joomla CVSS-10 in CISA KEV | Aztec $2.21M, CVE-2026-48907 | access-control, logic-error, unverified-contract | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | No new drain; abandoned-contract pattern in 4 of June's 16 incidents; OWASP SC10:2026 proxy entry | Quiet window | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js 2 HIGH CVEs | Bridge $127M catch-up, Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ exploits); Lazarus Mach-O Man macOS kit | (no new on-chain drains) | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE | Aztec Connect $2.1M, Syscoin Bridge $8M catch-up | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring ~$500K, Unleash $3.9M catch-up | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises bounty to $5M | Alephium $815K, AFI $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing; OZ Wizard CVE-2026-48054 disclosed | Humanity Protocol $36M (DPRK), CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by frequency — most-referenced bug classes appear first. Each date links to the briefing where that class appears.

**key-management** (39 briefings) — [06-12](briefings/2026-06-12.md) [06-13](briefings/2026-06-13.md) [06-17](briefings/2026-06-17.md) [06-18](briefings/2026-06-18.md) [06-19](briefings/2026-06-19.md) [06-23](briefings/2026-06-23.md) [06-25](briefings/2026-06-25.md) [06-27](briefings/2026-06-27.md) [06-28](briefings/2026-06-28.md) [06-29](briefings/2026-06-29.md) [06-30](briefings/2026-06-30.md) [07-01](briefings/2026-07-01.md) [07-02](briefings/2026-07-02.md) [07-03](briefings/2026-07-03.md) [07-04](briefings/2026-07-04.md) [07-05](briefings/2026-07-05.md) [07-06](briefings/2026-07-06.md) [07-07](briefings/2026-07-07.md) [07-09](briefings/2026-07-09.md) [07-10](briefings/2026-07-10.md) [07-12](briefings/2026-07-12.md) [07-13](briefings/2026-07-13.md) [07-14](briefings/2026-07-14.md) [07-16](briefings/2026-07-16.md) [07-17](briefings/2026-07-17.md) [07-18](briefings/2026-07-18.md) [07-19](briefings/2026-07-19.md) [07-20](briefings/2026-07-20.md) [07-22](briefings/2026-07-22.md) [07-23](briefings/2026-07-23.md) [07-24](briefings/2026-07-24.md) [07-26](briefings/2026-07-26.md) [07-27](briefings/2026-07-27.md) [07-28](briefings/2026-07-28.md) [07-29](briefings/2026-07-29.md) [07-31](briefings/2026-07-31.md) [08-01](briefings/2026-08-01.md) [08-02](briefings/2026-08-02.md) [08-03](briefings/2026-08-03.md)

**logic-error** (32 briefings) — [06-12](briefings/2026-06-12.md) [06-14](briefings/2026-06-14.md) [06-15](briefings/2026-06-15.md) [06-16](briefings/2026-06-16.md) [06-17](briefings/2026-06-17.md) [06-19](briefings/2026-06-19.md) [06-20](briefings/2026-06-20.md) [06-21](briefings/2026-06-21.md) [06-22](briefings/2026-06-22.md) [06-24](briefings/2026-06-24.md) [06-25](briefings/2026-06-25.md) [06-27](briefings/2026-06-27.md) [06-28](briefings/2026-06-28.md) [06-29](briefings/2026-06-29.md) [06-30](briefings/2026-06-30.md) [07-04](briefings/2026-07-04.md) [07-05](briefings/2026-07-05.md) [07-07](briefings/2026-07-07.md) [07-08](briefings/2026-07-08.md) [07-09](briefings/2026-07-09.md) [07-10](briefings/2026-07-10.md) [07-11](briefings/2026-07-11.md) [07-13](briefings/2026-07-13.md) [07-14](briefings/2026-07-14.md) [07-17](briefings/2026-07-17.md) [07-18](briefings/2026-07-18.md) [07-19](briefings/2026-07-19.md) [07-20](briefings/2026-07-20.md) [07-21](briefings/2026-07-21.md) [07-25](briefings/2026-07-25.md) [07-29](briefings/2026-07-29.md) [07-30](briefings/2026-07-30.md)

**access-control** (24 briefings) — [06-13](briefings/2026-06-13.md) [06-15](briefings/2026-06-15.md) [06-18](briefings/2026-06-18.md) [06-21](briefings/2026-06-21.md) [06-23](briefings/2026-06-23.md) [06-24](briefings/2026-06-24.md) [06-27](briefings/2026-06-27.md) [06-28](briefings/2026-06-28.md) [07-01](briefings/2026-07-01.md) [07-03](briefings/2026-07-03.md) [07-08](briefings/2026-07-08.md) [07-09](briefings/2026-07-09.md) [07-10](briefings/2026-07-10.md) [07-11](briefings/2026-07-11.md) [07-13](briefings/2026-07-13.md) [07-14](briefings/2026-07-14.md) [07-15](briefings/2026-07-15.md) [07-16](briefings/2026-07-16.md) [07-17](briefings/2026-07-17.md) [07-26](briefings/2026-07-26.md) [07-27](briefings/2026-07-27.md) [07-28](briefings/2026-07-28.md) [07-29](briefings/2026-07-29.md) [07-30](briefings/2026-07-30.md)

**supply-chain** (20 briefings) — [06-13](briefings/2026-06-13.md) [06-17](briefings/2026-06-17.md) [06-18](briefings/2026-06-18.md) [06-27](briefings/2026-06-27.md) [06-28](briefings/2026-06-28.md) [06-29](briefings/2026-06-29.md) [06-30](briefings/2026-06-30.md) [07-01](briefings/2026-07-01.md) [07-05](briefings/2026-07-05.md) [07-06](briefings/2026-07-06.md) [07-11](briefings/2026-07-11.md) [07-13](briefings/2026-07-13.md) [07-14](briefings/2026-07-14.md) [07-15](briefings/2026-07-15.md) [07-18](briefings/2026-07-18.md) [07-19](briefings/2026-07-19.md) [07-20](briefings/2026-07-20.md) [07-25](briefings/2026-07-25.md) [07-31](briefings/2026-07-31.md) [08-03](briefings/2026-08-03.md)

**bridge-dvn** (19 briefings) — [06-12](briefings/2026-06-12.md) [06-14](briefings/2026-06-14.md) [06-17](briefings/2026-06-17.md) [06-19](briefings/2026-06-19.md) [06-22](briefings/2026-06-22.md) [06-23](briefings/2026-06-23.md) [06-25](briefings/2026-06-25.md) [06-29](briefings/2026-06-29.md) [06-30](briefings/2026-06-30.md) [07-04](briefings/2026-07-04.md) [07-18](briefings/2026-07-18.md) [07-20](briefings/2026-07-20.md) [07-22](briefings/2026-07-22.md) [07-23](briefings/2026-07-23.md) [07-24](briefings/2026-07-24.md) [07-30](briefings/2026-07-30.md) [08-01](briefings/2026-08-01.md) [08-02](briefings/2026-08-02.md) [08-03](briefings/2026-08-03.md)

**flash-loan** (14 briefings) — [06-12](briefings/2026-06-12.md) [06-16](briefings/2026-06-16.md) [07-02](briefings/2026-07-02.md) [07-03](briefings/2026-07-03.md) [07-06](briefings/2026-07-06.md) [07-07](briefings/2026-07-07.md) [07-09](briefings/2026-07-09.md) [07-10](briefings/2026-07-10.md) [07-11](briefings/2026-07-11.md) [07-12](briefings/2026-07-12.md) [07-14](briefings/2026-07-14.md) [07-17](briefings/2026-07-17.md) [07-21](briefings/2026-07-21.md) [07-30](briefings/2026-07-30.md)

**oracle-manipulation** (12 briefings) — [06-20](briefings/2026-06-20.md) [06-22](briefings/2026-06-22.md) [06-25](briefings/2026-06-25.md) [07-04](briefings/2026-07-04.md) [07-12](briefings/2026-07-12.md) [07-13](briefings/2026-07-13.md) [07-14](briefings/2026-07-14.md) [07-15](briefings/2026-07-15.md) [07-16](briefings/2026-07-16.md) [07-17](briefings/2026-07-17.md) [07-23](briefings/2026-07-23.md) [07-28](briefings/2026-07-28.md)

**price-manipulation** (10 briefings) — [06-22](briefings/2026-06-22.md) [06-23](briefings/2026-06-23.md) [06-25](briefings/2026-06-25.md) [07-02](briefings/2026-07-02.md) [07-03](briefings/2026-07-03.md) [07-12](briefings/2026-07-12.md) [07-16](briefings/2026-07-16.md) [07-21](briefings/2026-07-21.md) [07-23](briefings/2026-07-23.md) [07-25](briefings/2026-07-25.md)

**unverified-contract** (7 briefings) — [06-12](briefings/2026-06-12.md) [06-20](briefings/2026-06-20.md) [06-21](briefings/2026-06-21.md) [06-24](briefings/2026-06-24.md) [07-02](briefings/2026-07-02.md) [07-04](briefings/2026-07-04.md) [07-27](briefings/2026-07-27.md)

**signature-replay** (6 briefings) — [06-14](briefings/2026-06-14.md) [07-22](briefings/2026-07-22.md) [07-31](briefings/2026-07-31.md) [08-01](briefings/2026-08-01.md) [08-02](briefings/2026-08-02.md) [08-03](briefings/2026-08-03.md)

**upgradeability** (6 briefings) — [06-13](briefings/2026-06-13.md) [06-18](briefings/2026-06-18.md) [06-20](briefings/2026-06-20.md) [07-03](briefings/2026-07-03.md) [07-15](briefings/2026-07-15.md) [07-16](briefings/2026-07-16.md)

**reentrancy** (4 briefings) — [07-10](briefings/2026-07-10.md) [07-11](briefings/2026-07-11.md) [07-15](briefings/2026-07-15.md) [07-29](briefings/2026-07-29.md)

**rounding** (3 briefings) — [06-15](briefings/2026-06-15.md) [06-16](briefings/2026-06-16.md) [07-06](briefings/2026-07-06.md)

**integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

**dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

**front-running** (1 briefing) — [07-08](briefings/2026-07-08.md)

---

## 📊 Stats

- **Total briefings:** 52
- **Date range:** 2026-06-12 → 2026-08-03 (53 calendar days; one planned gap on 2026-06-26)
- **Top 3 bug classes by frequency:**
  1. **key-management** — 39/52 briefings (75%) — persistent #1 across the entire archive; wallets, signing keys, DPRK social engineering, hardware entropy flaws
  2. **logic-error** — 32/52 briefings (62%) — covers arithmetic mistakes, CEI violations, deprecated code paths, bad math in AMM/vault accounting
  3. **access-control** — 24/52 briefings (46%) — missing role checks, unchecked callers, governance token buyouts, proxy admin exposure
- **Highest single-day estimated losses (tracked window):** ~$127M — [2026-06-19](briefings/2026-06-19.md) ($127M cross-chain bridge catch-up); $107M tracked across multiple ongoing incidents on [2026-07-10](briefings/2026-07-10.md)
- **Largest single active incident:** Coldcard PRNG firmware flaw — ~$89M cumulative across 4,585 Bitcoin addresses as of 2026-08-03
- **July 2026 total losses (MTD at month close):** ~$222M across 30+ incidents

# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-07-28](briefings/2026-07-28.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-07-28](briefings/2026-07-28.md) | WEMIX loses $6.25M to owner-key compromise enabling unauthorized stablecoin minting | WEMIX $6.25M, Triple-A $12M (ongoing) | access-control, key-management, oracle-manipulation | ~$6.25M new; ~$214M July MTD |
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M as firm issues first official statement; CertiK wrench attacks $124M H1 | Triple-A $12M (updated from $9.7M) | key-management, unverified-contract, access-control | ~$12M new; ~$208M July MTD |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A crypto payment gateway loses $9.7M as hot wallets across 6 chains drained simultaneously | Triple-A $9.7M | key-management, access-control | ~$9.7M new; ~$206M July MTD |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration and flawed exchange count-check | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K new; ~$196M July MTD |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade's Arbitrum bridge drained $24.15M after validator signing keys compromised; three simultaneous bridge exploits $35.55M | AFX Trade $24.15M, Verus ETH bridge ~$7.4M, B² Network ~$4M | key-management, bridge-dvn | ~$35.55M new; ~$195M July MTD |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO's BLC stablecoin depegged 99% on BNB Chain after BTCB Median Oracle manipulation | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K new; ~$159M July MTD |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw amplifying a single valid signature 65,000× | Wanchain Bridge $10–13M | signature-replay, bridge-dvn, key-management | ~$10–13M new; ~$158M July MTD |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 partial fix | Allbridge Core $1.65M, Summer.fi shutdown announced | flash-loan, price-manipulation, logic-error | ~$1.65M new; ~$148M July MTD |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 opens with 35M-user wallet-extension PoC code live; CoinDCX post-mortem confirms 6-day dwell time | CoinDCX $44M post-mortem (employee arrest), Across Protocol Solana PoC | key-management, supply-chain, bridge-dvn, logic-error | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 wallet-extension paper | macOS wallet-replacement infostealer, PETS 2026 disclosures | key-management, supply-chain, logic-error | ~$5M+ (Ill Bloom active); $147M July MTD |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol Solana, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum — third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M cumulative tracked |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery ($37M returned) | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M tracked |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed Day 4; six incidents ongoing | CVE-2026-40072, six ongoing situations | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M tracked |
| [2026-07-13](briefings/2026-07-13.md) | No new major drain; SlowMist H1 2026 drops (182 incidents, supply-chain #1 by losses at $298M) | BonkDAO laundering (ongoing), Bonzo fix deployed | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M tracked |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation; Ill Bloom PRNG ongoing | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new confirmed drain; GMX V1 $44M compensation plan advances as attacker returns $37M | GMX V1 recovery, six ongoing situations | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M tracked |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M) | Summer.fi laundering confirmed, BonkDAO to exchanges | key-management, flash-loan, access-control, logic-error | ~$75M tracked |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to MEV backrun | BonkDAO $20M, Ethereum MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG puts thousands of wallets at risk | Summer.fi $6M, Ill Bloom $5M cumulative | flash-loan, logic-error, key-management | ~$11M new/disclosed |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2) autopsy; ResupplyFi post-mortem | IronWorm npm worm (37 packages), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new; ~$49M ongoing |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug that threatened $70B; AI IDE markdown injection | Hexens/Aptos MoveVM $70B systemic (patched), AI IDE injection, Miasma worm Cosmos | logic-error, supply-chain, key-management | n/a new; $70B Aptos theoretical (patched) |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); CSA formalizes 'vibe-coded' Solidity as CVE-surge driver | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 final warns "vulnerability apocalypse" | ResupplyFi $9.6M, Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI attacks on unverified contracts ($36.7M H1) | Edel Finance $403K, June 2026 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K confirmed |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild by Djinn Stealer harvesting crypto wallets | CVE-2026-48558 SimpleHelp RMM, Djinn Stealer, GlassWorm macOS | key-management, supply-chain, access-control | n/a new; ~$18.5M SecondFi ongoing |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi/EMURGO white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO dispute (ongoing), Sapphire Sleet Mastra 144 packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M ADA custody dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes at record 83 hacks / $775M | SecondFi $2.4M–$20M, JaredFromSubway MEV Tornado Cash, Q2 record | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new; Q2 aggregate $775M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO portals | Polymarket $3M supply-chain, CVE-2026-12866 | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy | DARKNAVY Aztec circuit autopsy (technique disclosure) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M | Taiko Bridge SGX key $1.7M, OLPC/LABUBU $1.1M, mySwap Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control overtakes smart-contract bugs as #1 class | Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a new; Q2 cumulative ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19) masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K catch-up |
| [2026-06-21](briefings/2026-06-21.md) | Aztec Connect's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain | Aztec RollupProcessor $2.21M escapeHatch() | access-control, logic-error, unverified-contract | n/a new (technical analysis) |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy entry | Quiet 24h window | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a; June cumulative ~$195M+ |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass | 3-protocol bridge $127M (catch-up Jun 14) | bridge-dvn, key-management, logic-error, dos | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit | EIP-7702 real-world exploits ~$8M, Lazarus macOS | access-control, key-management, supply-chain, upgradeability | n/a new; EIP-7702 cumulative ~$8M+ |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge ~$8M, Node.js CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict window |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to a flash-loan math flaw in a deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K forensics, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OZ Wizard CVE-2026-48054 | Humanity Protocol $36M (DPRK), CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by frequency (most briefings first). Click a date to jump to that briefing.

- **key-management** (33 briefings) — [2026-07-28](briefings/2026-07-28.md), [2026-07-27](briefings/2026-07-27.md), [2026-07-26](briefings/2026-07-26.md), [2026-07-24](briefings/2026-07-24.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

- **logic-error** (30 briefings) — [2026-07-25](briefings/2026-07-25.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **access-control** (22 briefings) — [2026-07-28](briefings/2026-07-28.md), [2026-07-27](briefings/2026-07-27.md), [2026-07-26](briefings/2026-07-26.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

- **supply-chain** (18 briefings) — [2026-07-25](briefings/2026-07-25.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

- **bridge-dvn** (15 briefings) — [2026-07-24](briefings/2026-07-24.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **flash-loan** (13 briefings) — [2026-07-21](briefings/2026-07-21.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

- **oracle-manipulation** (12 briefings) — [2026-07-28](briefings/2026-07-28.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

- **price-manipulation** (10 briefings) — [2026-07-25](briefings/2026-07-25.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

- **unverified-contract** (7 briefings) — [2026-07-27](briefings/2026-07-27.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

- **upgradeability** (6 briefings) — [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

- **rounding** (3 briefings) — [2026-07-06](briefings/2026-07-06.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

- **reentrancy** (3 briefings) — [2026-07-15](briefings/2026-07-15.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md)

- **signature-replay** (2 briefings) — [2026-07-22](briefings/2026-07-22.md), [2026-06-14](briefings/2026-06-14.md)

- **integer-overflow** (1 briefing) — [2026-06-15](briefings/2026-06-15.md)

- **front-running** (1 briefing) — [2026-07-08](briefings/2026-07-08.md)

- **dos** (1 briefing) — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 46
- **Date range:** 2026-06-12 → 2026-07-28 (47 days; 1 gap on 2026-06-26)
- **Top 3 bug classes by frequency:** `key-management` (33 briefings) · `logic-error` (30) · `access-control` (22)
- **July 2026 MTD losses:** ~$214M across 20+ incidents
- **Q2 2026 total losses:** ~$755M across 83 incidents (all-time quarterly record)

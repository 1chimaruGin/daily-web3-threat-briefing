# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.  
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.  
**Latest briefing:** [2026-08-02](briefings/2026-08-02.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-08-02](briefings/2026-08-02.md) | Coldcard firmware attack escalates to $89M / 4,585 addresses; Wave 3 switches to P2WSH to evade chain analytics | Coldcard $89M Wave 3, AFX Trade Aug 3, Wanchain Aug 6 T-4 | key-management, bridge-dvn, signature-replay | ~$89M |
| [2026-08-01](briefings/2026-08-01.md) | Coldcard firmware entropy flaw drains $38M BTC from ~500 wallets; AFX Trade sets Aug 3 compensation plan | Coldcard $38M, AFX Trade Aug 3, Wanchain Aug 6 | key-management, bridge-dvn, signature-replay | ~$38M confirmed |
| [2026-07-31](briefings/2026-07-31.md) | Wanchain sets Aug 6 white-hat deadline on $10M NIGHT; Drift exploiter moves $44.4M to Tornado Cash; CVE-2026-40072 web3.py SSRF | Wanchain $10M deadline, Drift laundering, CVE-2026-40072 | signature-replay, key-management, supply-chain | ~$0 new |
| [2026-07-30](briefings/2026-07-30.md) | Unidentified BNB Chain DAO drained $8.2M via anyone-callable vault; Garden Finance HTLC $450K across 4 chains | BNB DAO $8.2M, Garden Finance HTLC $450K, BarnBridge $776K | access-control, logic-error, bridge-dvn, flash-loan | ~$9.4M |
| [2026-07-29](briefings/2026-07-29.md) | Blockaid confirms record $1.1B H1 2026 losses (DPRK drove $577M); GMX reentrancy post-mortems published | Blockaid H1 report, GMX post-mortem, BarnBridge $776K | reentrancy, logic-error, access-control, key-management | ~$0 new |
| [2026-07-28](briefings/2026-07-28.md) | WEMIX loses $6.25M to owner-key compromise enabling unauthorized stablecoin minting | WEMIX $6.25M, Triple-A $12M ongoing | access-control, key-management, oracle-manipulation | ~$6.25M |
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M; CertiK reports physical wrench attacks claimed $124M in H1 2026 at record pace | Triple-A $12M revised, CertiK wrench attacks $124M | key-management, unverified-contract, access-control | ~$12M |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A crypto payment gateway loses $9.7M as hot wallets across 6 chains drained simultaneously | Triple-A $9.7M, Chainalysis Drift $285M post-mortem | key-management, access-control | ~$9.7M |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration; Injective Labs npm supply chain advisory | Lien Finance $542K, Injective npm advisory | logic-error, price-manipulation, supply-chain | ~$542K |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade $24.15M bridge validator keys compromised; three bridge/exchange exploits totaling $35.55M in one day | AFX Trade $24.15M, Verus ETH bridge $7.4M, B² Network $4M | key-management, bridge-dvn | ~$35.55M |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% on BNB Chain after BTCB Median Oracle manipulation | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw amplifying one valid sig 65,000× | Wanchain Bridge $10–13M NIGHT | signature-replay, bridge-dvn, key-management | ~$10–13M |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 partial fix | Allbridge Core $1.65M, Summer.fi shutdown | flash-loan, price-manipulation, logic-error | ~$1.65M |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 opens with 35M-user wallet-extension PoC code live; CoinDCX post-mortem confirms 6-day dwell time | CoinDCX post-mortem, PETS 2026 PoC, Across Protocol disclosure | key-management, supply-chain, bridge-dvn, logic-error | n/a |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 wallet-extension paper drops | macOS wallet-replacement infostealer, PETS 2026 disclosures, Ill Bloom ongoing | key-management, supply-chain, logic-error | ~$5M+ |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol Solana, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum — third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M tracked |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed Day 4; six incidents ongoing | Multiple ongoing (BonkDAO, Bonzo, GMX, Altura, Summer.fi, ResupplyFi) | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026 report: 182 incidents, supply-chain #1 by losses at $298M; BonkDAO launders $19M | BonkDAO laundering, Bonzo Lend fix | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation; Ill Bloom PRNG ongoing | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M |
| [2026-07-11](briefings/2026-07-11.md) | GMX V1 $44M compensation plan advances; OZ Wizard CVE-2026-48054 supply-chain risk Day 28 | GMX V1 recovery, BonkDAO, Altura, Summer.fi, ResupplyFi ongoing | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | CertiK H1 2026: wallet compromise is #1 loss vector at $444M; Summer.fi $6M laundering via Tornado Cash | Summer.fi laundering, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG drains $5M from software wallets | Summer.fi $6M, Ill Bloom PRNG $5M | flash-loan, logic-error, key-management | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets JFrog autopsy; ResupplyFi ERC-4626 post-mortem public | IronWorm npm worm (37 packages), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion ($70B at risk); SlowMist warns AI IDE markdown injection | Hexens/Aptos MoveVM disclosure, SlowMist AI IDE, Miasma Cosmos worm | logic-error, supply-chain, key-management | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); CSA formalizes AI vibe-coded Solidity as CVE-surge driver | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M, Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI attacks | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 SimpleHelp RMM exploited in-the-wild (Djinn Stealer harvests crypto creds) | CVE-2026-48558 SimpleHelp, Djinn Stealer, GlassWorm macOS | key-management, supply-chain, access-control | n/a new |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes at record $775M | SecondFi $2.4M–$20M, JaredFromSubway laundering | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; CVE-2026-12866 expr-eval CVSS-9.8 RCE | Polymarket $3M, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes definitive Aztec escapeHatch() ZK witness-binding gap autopsy | DARKNAVY Aztec ZK circuit autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool $1.1M BNB | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike enables identity spoofing | JaredFromSubway MEV $15M, ENS lookalike flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record: 83 incidents, $755M; access-control overtakes smart-contract bugs | Q2 2026 quarterly record | access-control, key-management, bridge-dvn, price-manipulation | n/a |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() TurboVerifier accepts spoofed ZK public inputs ($2.21M); Joomla JCE CVSS-10 in CISA KEV | Aztec $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | No new drains; abandoned-contract pattern in 4 of June's 16 incidents; OWASP SC10:2026 proxy entry formalized | (no new confirmed drains) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js HIGH CVEs | Unnamed bridge $127M, Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ real exploits; Lazarus macOS kit active | (no new drains) | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge $8M, Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow; AI agent memory poisoning $45M in 2026 | Flooring Protocol ~$500K, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Humanity Protocol $36M breach attributed to DPRK phishing chain; OZ Wizard CVE-2026-48054 drops | Humanity Protocol $36M, CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

**key-management** — [2026-08-02](briefings/2026-08-02.md), [2026-08-01](briefings/2026-08-01.md), [2026-07-31](briefings/2026-07-31.md), [2026-07-29](briefings/2026-07-29.md), [2026-07-28](briefings/2026-07-28.md), [2026-07-27](briefings/2026-07-27.md), [2026-07-26](briefings/2026-07-26.md), [2026-07-24](briefings/2026-07-24.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

**logic-error** — [2026-07-30](briefings/2026-07-30.md), [2026-07-29](briefings/2026-07-29.md), [2026-07-25](briefings/2026-07-25.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**access-control** — [2026-07-30](briefings/2026-07-30.md), [2026-07-29](briefings/2026-07-29.md), [2026-07-28](briefings/2026-07-28.md), [2026-07-27](briefings/2026-07-27.md), [2026-07-26](briefings/2026-07-26.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

**supply-chain** — [2026-07-31](briefings/2026-07-31.md), [2026-07-25](briefings/2026-07-25.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-19](briefings/2026-07-19.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

**bridge-dvn** — [2026-08-02](briefings/2026-08-02.md), [2026-08-01](briefings/2026-08-01.md), [2026-07-30](briefings/2026-07-30.md), [2026-07-24](briefings/2026-07-24.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-22](briefings/2026-07-22.md), [2026-07-20](briefings/2026-07-20.md), [2026-07-18](briefings/2026-07-18.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**oracle-manipulation** — [2026-07-28](briefings/2026-07-28.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

**flash-loan** — [2026-07-30](briefings/2026-07-30.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-17](briefings/2026-07-17.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

**price-manipulation** — [2026-07-25](briefings/2026-07-25.md), [2026-07-23](briefings/2026-07-23.md), [2026-07-21](briefings/2026-07-21.md), [2026-07-16](briefings/2026-07-16.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

**signature-replay** — [2026-08-02](briefings/2026-08-02.md), [2026-08-01](briefings/2026-08-01.md), [2026-07-31](briefings/2026-07-31.md), [2026-07-22](briefings/2026-07-22.md), [2026-06-14](briefings/2026-06-14.md)

**upgradeability** — [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

**unverified-contract** — [2026-07-27](briefings/2026-07-27.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

**reentrancy** — [2026-07-29](briefings/2026-07-29.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md)

**rounding** — [2026-07-06](briefings/2026-07-06.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

**front-running** — [2026-07-08](briefings/2026-07-08.md)

**dos** — [2026-06-19](briefings/2026-06-19.md)

**integer-overflow** — [2026-06-15](briefings/2026-06-15.md)

---

## 📊 Stats

- **Total briefings:** 51 (2026-06-12 through 2026-08-02; 2026-06-26 skipped)
- **Date range:** 2026-06-12 → 2026-08-02 (52 calendar days)
- **Top 3 most-frequent bug classes:**
  1. **key-management** — 38 briefings
  2. **logic-error** — 31 briefings
  3. **access-control** — 23 briefings

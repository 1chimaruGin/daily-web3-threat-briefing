# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.  
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.  
**Latest briefing:** [2026-07-31](briefings/2026-07-31.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-07-31](briefings/2026-07-31.md) | Wanchain sets Aug 6 white-hat deadline; Drift exploiter moves $44.4M to Tornado Cash; CVE-2026-40072 web3.py SSRF | Wanchain recovery deadline, Drift $44.4M Tornado Cash | signature-replay, key-management, supply-chain | ~$0 new; ~$222M July MTD |
| [2026-07-30](briefings/2026-07-30.md) | BNB Chain DAO drained $8.2M via anyone-callable vault; Garden Finance HTLC hit across 4 chains for $450K | Crypto DAO BNB $8.2M, Garden Finance HTLC $450K, BarnBridge $776K | access-control, logic-error, bridge-dvn, flash-loan | ~$9.4M new; ~$222M July MTD |
| [2026-07-29](briefings/2026-07-29.md) | Blockaid confirms record $1.1B H1 losses (DPRK drove $577M); GMX post-mortems published; Node.js HIGH patches | Blockaid H1 report, GMX recovery, BarnBridge $776K | reentrancy, logic-error, access-control, key-management | ~$0 new; ~$214M July MTD |
| [2026-07-28](briefings/2026-07-28.md) | WEMIX loses $6.25M to owner-key compromise enabling stablecoin minting; Triple-A ongoing | WEMIX $6.25M, Triple-A $12M ongoing | access-control, key-management, oracle-manipulation | ~$6.25M new; ~$214M July MTD |
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M; CertiK reports $124M in H1 2026 physical wrench attacks | Triple-A $12M (updated) | key-management, unverified-contract, access-control | ~$12M; ~$208M July MTD |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A crypto gateway loses $9.7M across 6 chains simultaneously; Chainalysis Drift $285M post-mortem | Triple-A $9.7M | key-management, access-control | ~$9.7M new; ~$206M July MTD |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration + flawed count-check; Injective npm advisory | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K new; ~$196M July MTD |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade Arbitrum bridge drained $24.15M after validator keys compromised; 3 bridge exploits on July 23 total $35.55M | AFX Trade $24.15M, Verus ETH bridge ~$7.4M, B² Network ~$4M | key-management, bridge-dvn | ~$35.55M new; ~$195M July MTD |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% on BNB Chain after BTCB Median Oracle manipulation | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K new; ~$159M July MTD |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw amplifying one valid signature 65,000× | Wanchain Bridge $10–13M NIGHT | signature-replay, bridge-dvn, key-management | ~$10–13M new; ~$158M July MTD |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 partial fix | Allbridge Core $1.65M | flash-loan, price-manipulation, logic-error | ~$1.65M new; ~$148M July MTD |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 wallet-extension PoC live (35M users); CoinDCX post-mortem confirms 6-day dwell + employee arrest | CoinDCX $44M post-mortem, PETS 2026 PoC | key-management, supply-chain, bridge-dvn, logic-error | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 wallet-extension paper drops | macOS wallet-replacement infostealer, PETS 2026 (35M users), Ill Bloom $5M+ | key-management, supply-chain, logic-error | ~$5M+ Ill Bloom sweeps; $147M July MTD |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol Solana, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key — third oracle attack in five days | Ostium $18–22M, Kinto shutdown, Altura $39M locked | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 web3.py SSRF via EIP-3668 CCIP Read disclosed Day 4; no new drain | 6 incidents ongoing (~$78M) | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | No new drain; SlowMist H1 2026 report (182 incidents, supply-chain #1 at $298M); BonkDAO launders $19M into BONK 2.0 | BonkDAO laundering, Bonzo Lend $9M recovery | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation; Ill Bloom still draining | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances; OZ Wizard CVE Day 28 unpatched | GMX V1 recovery ongoing | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M); Summer.fi laundering confirmed | Summer.fi Tornado Cash, BonkDAO ongoing | key-management, flash-loan, access-control, logic-error | ~$75M tracked ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to MEV backrun | BonkDAO $20M, Ethereum MEV $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG drains thousands of software wallets | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M new |
| [2026-07-06](briefings/2026-07-06.md) | No new drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets JFrog autopsy; ResupplyFi ERC-4626 post-mortem | IronWorm npm (37 packages), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug (~$70B systemic); SlowMist AI IDE markdown injection | Hexens/Aptos MoveVM $70B-at-risk (patched), AI IDE markdown injection | logic-error, supply-chain, key-management | n/a new drains |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI 'vibe-coded' Solidity as CVE driver | Altura $39M, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2 report warns AI is driving "vulnerability apocalypse" | ResupplyFi $9.6M, Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets — CISA July 2 deadline | CVE-2026-48558 SimpleHelp RMM (Djinn Stealer) | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat custody disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M in custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes at 83 hacks / $775M | SecondFi $2.4M–$20M, Q2 record close | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new; Q2 $775M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO portals | Polymarket $3M, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY Aztec circuit autopsy reveals generalizable ZK witness-binding gap | DARKNAVY Aztec autopsy (technique) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables identity spoofing | JaredFromSubway MEV $15M, ENS lookalike flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M; access-control overtakes smart-contract bugs as #1 | Q2 2026 record (83 incidents / $755M) | access-control, key-management, bridge-dvn, price-manipulation | n/a new; Q2 $755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs; CVSS-10 Joomla JCE RCE in CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | Quiet window; 'abandoned-contract' pattern in 4 of June's incidents; OWASP SC10:2026 proxy-upgradeability formalized | (quiet) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained via dual validator+finality bypass (catch-up Jun 14); Node.js HIGH CVEs drop | Unnamed bridge $127M (catch-up) | bridge-dvn, key-management, logic-error, dos | ~$127M (catch-up) |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ real-world); Lazarus 'Mach-O Man' macOS kit active | (technique disclosures) | access-control, key-management, supply-chain, upgradeability | n/a new |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K, Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium forged-VAA bridge kill chain detailed; Aave raises max bounty to $5M | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M on DPRK phishing; OpenZeppelin Wizard CVE-2026-48054 code injection disclosed | Humanity Protocol $36M, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*(Most frequent → least; each date links to that day's briefing)*

**key-management** — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-22](briefings/2026-07-22.md), [07-23](briefings/2026-07-23.md), [07-24](briefings/2026-07-24.md), [07-26](briefings/2026-07-26.md), [07-27](briefings/2026-07-27.md), [07-28](briefings/2026-07-28.md), [07-29](briefings/2026-07-29.md), [07-31](briefings/2026-07-31.md)

**logic-error** — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-21](briefings/2026-07-21.md), [07-25](briefings/2026-07-25.md), [07-29](briefings/2026-07-29.md), [07-30](briefings/2026-07-30.md)

**access-control** — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-26](briefings/2026-07-26.md), [07-27](briefings/2026-07-27.md), [07-28](briefings/2026-07-28.md), [07-29](briefings/2026-07-29.md), [07-30](briefings/2026-07-30.md)

**supply-chain** — [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-25](briefings/2026-07-25.md), [07-31](briefings/2026-07-31.md)

**bridge-dvn** — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-18](briefings/2026-07-18.md), [07-20](briefings/2026-07-20.md), [07-22](briefings/2026-07-22.md), [07-23](briefings/2026-07-23.md), [07-24](briefings/2026-07-24.md), [07-30](briefings/2026-07-30.md)

**flash-loan** — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-21](briefings/2026-07-21.md), [07-30](briefings/2026-07-30.md)

**oracle-manipulation** — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [06-25](briefings/2026-06-25.md), [07-04](briefings/2026-07-04.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-23](briefings/2026-07-23.md), [07-28](briefings/2026-07-28.md)

**price-manipulation** — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-12](briefings/2026-07-12.md), [07-16](briefings/2026-07-16.md), [07-21](briefings/2026-07-21.md), [07-23](briefings/2026-07-23.md), [07-25](briefings/2026-07-25.md)

**unverified-contract** — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md), [07-27](briefings/2026-07-27.md)

**upgradeability** — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md)

**reentrancy** — [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-15](briefings/2026-07-15.md), [07-29](briefings/2026-07-29.md)

**signature-replay** — [06-14](briefings/2026-06-14.md), [07-22](briefings/2026-07-22.md), [07-31](briefings/2026-07-31.md)

**rounding** — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md)

**dos** — [06-19](briefings/2026-06-19.md)

**front-running** — [07-08](briefings/2026-07-08.md)

**integer-overflow** — [06-15](briefings/2026-06-15.md)

---

## 📊 Stats

- **Total briefings:** 49
- **Date range:** 2026-06-12 → 2026-07-31 (50 days; one gap: 2026-06-26)
- **Top 3 bug classes by frequency:**
  1. `key-management` — 35 briefings
  2. `logic-error` — 32 briefings
  3. `access-control` — 24 briefings
- **July 2026 MTD losses:** ~$222M across 30+ confirmed incidents
- **H1 2026 total losses:** $1.1B+ across 212 incidents (Blockaid; record high)

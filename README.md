# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-30](briefings/2026-07-30.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-07-30](briefings/2026-07-30.md) | BNB Chain DAO drained $8.2M via anyone-callable vault; Garden Finance HTLC hit across 4 chains $450K | Crypto DAO BNB $8.2M, Garden Finance HTLC $450K, BarnBridge $776K | access-control, logic-error, bridge-dvn, flash-loan | ~$9.4M new |
| [2026-07-29](briefings/2026-07-29.md) | Blockaid confirms record $1.1B H1 losses (DPRK $577M); GMX reentrancy post-mortems; Node.js HIGH patches | Blockaid H1 report, GMX $42M recovered, BarnBridge $776K | reentrancy, logic-error, access-control, key-management | ~$214M July MTD |
| [2026-07-28](briefings/2026-07-28.md) | WEMIX loses $6.25M to owner-key compromise enabling unauthorized stablecoin minting | WEMIX $6.25M, Triple-A $12M ongoing | access-control, key-management, oracle-manipulation | ~$6.25M new |
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M; CertiK flags $124M in H1 physical 'wrench attacks' | Triple-A $12M revised | key-management, unverified-contract, access-control | ~$12M new |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A payment gateway loses $9.7M across 6 chains simultaneously; Chainalysis Drift $285M post-mortem | Triple-A $9.7M | key-management, access-control | ~$9.7M new |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance drained $542K via permissionless bond registration + flawed exchange count-check | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K new |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade's bridge drained $24.15M after validator keys compromised; three simultaneous exploits $35.55M | AFX Trade $24.15M, Verus ETH bridge ~$7.4M, B² Network ~$4M | key-management, bridge-dvn | ~$35.55M new |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% on BNB Chain via BTCB Median Oracle manipulation | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K new |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature encoding flaw (65,000× amplification) | Wanchain Bridge $10–13M | signature-replay, bridge-dvn, key-management | ~$10–13M new |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack — same exploit missed by 2023 fix | Allbridge Core $1.65M, Summer.fi shutdown | flash-loan, price-manipulation, logic-error | ~$1.65M new |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026: 35M-user wallet-extension PoC live; CoinDCX post-mortem: 6-day dwell, employee arrested | CoinDCX $44M post-mortem, PETS 2026 PoC, Across Solana event-spoofing | key-management, supply-chain, bridge-dvn, logic-error | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 paper: 35M users at risk | macOS wallet-replacement infostealer, PETS 2026 disclosures | key-management, supply-chain, logic-error | ~$5M+ active |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol Solana relayer, DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed perp) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key — third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M tracked |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor; GMX V1 hacker returns $37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed Day 4; six incidents ongoing | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 by losses ($298M); BonkDAO launders $19M into BONK 2.0 | BonkDAO laundering, Bonzo Lend Supra fix | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-orders-of-magnitude oracle price manipulation + zeroed signature | Bonzo Lend $9M, Ill Bloom $5M+ ongoing | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances; OZ Wizard CVE-2026-48054 risk day 28 | GMX V1 recovery, BonkDAO, Altura, Summer.fi, ResupplyFi | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 flags wallet compromise as #1 loss vector ($444M); Summer.fi laundering | Summer.fi laundering, BonkDAO funds to exchanges | key-management, flash-loan, access-control, logic-error | ~$75M tracked |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; MEV backrun $2M via illiquid Uniswap v3 pool | BonkDAO $20M governance, Ethereum MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG puts wallets at risk | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | flash-loan, logic-error, key-management | ~$11M new |
| [2026-07-06](briefings/2026-07-06.md) | No new drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2) JFrog autopsy; ResupplyFi post-mortem | IronWorm npm worm (37 pkg), ResupplyFi $9.6M ERC-4626 post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion ($70B at-risk); SlowMist AI IDE markdown injection | Hexens/Aptos MoveVM $70B theoretical, SlowMist AI IDE injection | logic-error, supply-chain, key-management | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); CSA formalizes AI 'vibe-coded' Solidity CVE driver | Altura $39M, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2 warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M ERC-4626, Kinto Protocol $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K via flash-loan wrapped-token exchange-rate manipulation; Chainalysis AI-contract warning | Edel Finance $403K, June 2026 wrap: 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited; Djinn Stealer harvests crypto wallets | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX, SecondFi ongoing | key-management, supply-chain, access-control | n/a new |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 closes at 83 hacks / $775M | SecondFi $2.4M–$20M keygen, JaredFromSubway MEV $7.5M, Q2 record | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M to supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M supply-chain, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | DARKNAVY publishes definitive Aztec escapeHatch() autopsy — generalizable ZK witness-binding gap | DARKNAVY Aztec circuit autopsy (technique) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC $1.1M on BNB Chain | Taiko Bridge SGX $1.7M, OLPC/LABUBU $1.1M, mySwap Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw found in wallet UIs | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 all-time quarterly record: 83 incidents, $755M lost; access-control surpasses smart-contract bugs | Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack detailed | Namada MASP $600K catch-up | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier spoofed ZK inputs drain $2.21M; CVSS-10 Joomla CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | No new drain; 'abandoned-contract' pattern in 4 of June's 16 incidents; OWASP SC10:2026 published | (quiet window) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js 2 HIGH CVEs Jun 18 | Unnamed 3-protocol bridge $127M catch-up, Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ real exploits); Lazarus macOS kit harvesting keys | (no new on-chain drains) | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE released today | Aztec Connect $2.1M, Syscoin Bridge ~$8M catch-up, Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M flash-loan/rounding | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent $45M cumulative | Flooring Protocol ~$500K, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K forensics, AFI Protocol $480K catch-up | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK; OpenZeppelin Wizard CVE-2026-48054 disclosed | Humanity Protocol $36M DPRK, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by frequency (number of briefings containing each tag):

- **key-management** *(36 briefings)* — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-22](briefings/2026-07-22.md), [07-23](briefings/2026-07-23.md), [07-24](briefings/2026-07-24.md), [07-26](briefings/2026-07-26.md), [07-27](briefings/2026-07-27.md), [07-28](briefings/2026-07-28.md), [07-29](briefings/2026-07-29.md)

- **logic-error** *(35 briefings)* — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-21](briefings/2026-07-21.md), [07-23](briefings/2026-07-23.md), [07-25](briefings/2026-07-25.md), [07-29](briefings/2026-07-29.md), [07-30](briefings/2026-07-30.md)

- **access-control** *(24 briefings)* — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-26](briefings/2026-07-26.md), [07-27](briefings/2026-07-27.md), [07-28](briefings/2026-07-28.md), [07-29](briefings/2026-07-29.md), [07-30](briefings/2026-07-30.md)

- **supply-chain** *(19 briefings)* — [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md), [07-25](briefings/2026-07-25.md)

- **bridge-dvn** *(16 briefings)* — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-18](briefings/2026-07-18.md), [07-20](briefings/2026-07-20.md), [07-22](briefings/2026-07-22.md), [07-23](briefings/2026-07-23.md), [07-24](briefings/2026-07-24.md), [07-30](briefings/2026-07-30.md)

- **flash-loan** *(14 briefings)* — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-21](briefings/2026-07-21.md), [07-30](briefings/2026-07-30.md)

- **oracle-manipulation** *(12 briefings)* — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [06-25](briefings/2026-06-25.md), [07-04](briefings/2026-07-04.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-23](briefings/2026-07-23.md), [07-28](briefings/2026-07-28.md)

- **price-manipulation** *(10 briefings)* — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-12](briefings/2026-07-12.md), [07-16](briefings/2026-07-16.md), [07-21](briefings/2026-07-21.md), [07-23](briefings/2026-07-23.md), [07-25](briefings/2026-07-25.md)

- **unverified-contract** *(7 briefings)* — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md), [07-27](briefings/2026-07-27.md)

- **upgradeability** *(6 briefings)* — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md)

- **reentrancy** *(4 briefings)* — [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-15](briefings/2026-07-15.md), [07-29](briefings/2026-07-29.md)

- **rounding** *(3 briefings)* — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md)

- **signature-replay** *(2 briefings)* — [06-14](briefings/2026-06-14.md), [07-22](briefings/2026-07-22.md)

- **integer-overflow** *(1 briefing)* — [06-15](briefings/2026-06-15.md)

- **front-running** *(1 briefing)* — [07-08](briefings/2026-07-08.md)

- **dos** *(1 briefing)* — [06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 48
- **Date range:** 2026-06-12 → 2026-07-30 (49 days; 2026-06-26 missing)
- **Top 3 bug classes:**
  1. `key-management` — 36 briefings (75% of all days)
  2. `logic-error` — 35 briefings (73% of all days)
  3. `access-control` — 24 briefings (50% of all days)
- **Cumulative July 2026 tracked losses:** ~$222M+
- **H1 2026 industry total:** $1.1B+ across 212 verified incidents (Blockaid, Jul 28 2026)

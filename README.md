# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-18](briefings/2026-07-18.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol (TBD), DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new; ~$100M ongoing |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 shuts down after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed; six incidents ongoing | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 by losses ($298M); BonkDAO launders $19M into "BONK 2.0" DAO | BonkDAO $20M (laundering), Bonzo Lend $9M | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances; OZ Wizard CVE day 28 | GMX V1 (recovery), BonkDAO $20M, Altura $39M | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026: wallet compromise #1 loss vector ($444M); Summer.fi laundered via Tornado Cash | Summer.fi (ongoing), BonkDAO (ongoing) | key-management, flash-loan, access-control, logic-error | ~$75M ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to MEV backrun | BonkDAO $20M, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG puts thousands of wallets at risk | Summer.fi $6M, Ill Bloom $5M cumulative | flash-loan, logic-error, key-management | ~$11M new; ~$51M ongoing |
| [2026-07-06](briefings/2026-07-06.md) | No new drain; IronWorm Rust npm worm (eBPF rootkit + Tor C2) JFrog autopsy; ResupplyFi ERC-4626 post-mortem published | IronWorm 37 npm packages, ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new; $48.6M ongoing |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion ($70B systemic); SlowMist: AI IDE markdown injection executes on Open Folder | Hexens/Aptos $70B-at-risk (patched), SlowMist AI IDE injection | logic-error, supply-chain, key-management | n/a new drains |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI "vibe-coded" Solidity as new CVE driver | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2: AI driving "vulnerability apocalypse" behind record 83-exploit quarter | ResupplyFi $9.6M, Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance loses $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K confirmed; ~$18.5M custody dispute |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and dev creds | CVE-2026-48558 SimpleHelp Djinn Stealer | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm pkgs | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M in dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter $775M | SecondFi $2.4M–$20M, Q2 close $775M | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new; Q2 $775M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M to supply-chain frontend injection; CVE-2026-12866 expr-eval CVSS-9.8 RCE threatens DAO portals | Polymarket $3M, CVE-2026-12866 | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes definitive Aztec escapeHatch() ZK circuit autopsy (generalizable witness-binding gap) | DARKNAVY Aztec autopsy | logic-error, access-control, supply-chain, key-management | n/a new |
| [2026-06-25](briefings/2026-06-25.md) | Taiko Bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU pool drained $1.1M (BNB token param desync) | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV $15M, ENS lookalike | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control overtakes smart-contract bugs as leading class | Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a strict 24h; Q2 ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19); VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem | Namada MASP $600K (catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K catch-up |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK inputs enabling $2.21M drain; CVSS-10 Joomla JCE in CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | No new drain; "abandoned-contract" pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalized | Quiet window | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a strict 24h |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs Jun 18 | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus "Mach-O Man" macOS kit harvesting crypto keychains | No new on-chain drains | access-control, key-management, supply-chain, upgradeability | n/a strict 24h |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge $8M (catch-up), Node.js CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict; ~$10.3M w/ catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing; OpenZeppelin Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal Protocol $915K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*(Sorted by number of briefings; each date links to that day's briefing)*

- **logic-error** (26 briefings) — [07-18](briefings/2026-07-18.md), [07-17](briefings/2026-07-17.md), [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-08](briefings/2026-07-08.md), [07-07](briefings/2026-07-07.md), [07-05](briefings/2026-07-05.md), [07-04](briefings/2026-07-04.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-25](briefings/2026-06-25.md), [06-24](briefings/2026-06-24.md), [06-22](briefings/2026-06-22.md), [06-21](briefings/2026-06-21.md), [06-20](briefings/2026-06-20.md), [06-19](briefings/2026-06-19.md), [06-17](briefings/2026-06-17.md), [06-16](briefings/2026-06-16.md), [06-15](briefings/2026-06-15.md), [06-14](briefings/2026-06-14.md), [06-12](briefings/2026-06-12.md)

- **key-management** (26 briefings) — [07-18](briefings/2026-07-18.md), [07-17](briefings/2026-07-17.md), [07-16](briefings/2026-07-16.md), [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-12](briefings/2026-07-12.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-07](briefings/2026-07-07.md), [07-06](briefings/2026-07-06.md), [07-05](briefings/2026-07-05.md), [07-04](briefings/2026-07-04.md), [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [07-01](briefings/2026-07-01.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-19](briefings/2026-06-19.md), [06-18](briefings/2026-06-18.md), [06-17](briefings/2026-06-17.md), [06-13](briefings/2026-06-13.md), [06-12](briefings/2026-06-12.md)

- **access-control** (19 briefings) — [07-17](briefings/2026-07-17.md), [07-16](briefings/2026-07-16.md), [07-15](briefings/2026-07-15.md), [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-08](briefings/2026-07-08.md), [07-03](briefings/2026-07-03.md), [07-01](briefings/2026-07-01.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-24](briefings/2026-06-24.md), [06-23](briefings/2026-06-23.md), [06-21](briefings/2026-06-21.md), [06-18](briefings/2026-06-18.md), [06-15](briefings/2026-06-15.md), [06-13](briefings/2026-06-13.md)

- **supply-chain** (15 briefings) — [07-18](briefings/2026-07-18.md), [07-15](briefings/2026-07-15.md), [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-11](briefings/2026-07-11.md), [07-06](briefings/2026-07-06.md), [07-05](briefings/2026-07-05.md), [07-01](briefings/2026-07-01.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-18](briefings/2026-06-18.md), [06-17](briefings/2026-06-17.md), [06-13](briefings/2026-06-13.md)

- **flash-loan** (12 briefings) — [07-17](briefings/2026-07-17.md), [07-14](briefings/2026-07-14.md), [07-12](briefings/2026-07-12.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md), [07-09](briefings/2026-07-09.md), [07-07](briefings/2026-07-07.md), [07-06](briefings/2026-07-06.md), [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [06-16](briefings/2026-06-16.md), [06-12](briefings/2026-06-12.md)

- **bridge-dvn** (11 briefings) — [07-18](briefings/2026-07-18.md), [07-04](briefings/2026-07-04.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-22](briefings/2026-06-22.md), [06-19](briefings/2026-06-19.md), [06-17](briefings/2026-06-17.md), [06-14](briefings/2026-06-14.md), [06-12](briefings/2026-06-12.md)

- **oracle-manipulation** (10 briefings) — [07-17](briefings/2026-07-17.md), [07-16](briefings/2026-07-16.md), [07-15](briefings/2026-07-15.md), [07-14](briefings/2026-07-14.md), [07-13](briefings/2026-07-13.md), [07-12](briefings/2026-07-12.md), [07-04](briefings/2026-07-04.md), [06-25](briefings/2026-06-25.md), [06-22](briefings/2026-06-22.md), [06-20](briefings/2026-06-20.md)

- **price-manipulation** (7 briefings) — [07-16](briefings/2026-07-16.md), [07-12](briefings/2026-07-12.md), [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-22](briefings/2026-06-22.md)

- **upgradeability** (6 briefings) — [07-16](briefings/2026-07-16.md), [07-15](briefings/2026-07-15.md), [07-03](briefings/2026-07-03.md), [06-20](briefings/2026-06-20.md), [06-18](briefings/2026-06-18.md), [06-13](briefings/2026-06-13.md)

- **unverified-contract** (6 briefings) — [07-04](briefings/2026-07-04.md), [07-02](briefings/2026-07-02.md), [06-24](briefings/2026-06-24.md), [06-21](briefings/2026-06-21.md), [06-20](briefings/2026-06-20.md), [06-12](briefings/2026-06-12.md)

- **reentrancy** (3 briefings) — [07-15](briefings/2026-07-15.md), [07-11](briefings/2026-07-11.md), [07-10](briefings/2026-07-10.md)

- **rounding** (3 briefings) — [07-06](briefings/2026-07-06.md), [06-16](briefings/2026-06-16.md), [06-15](briefings/2026-06-15.md)

- **front-running** (1 briefing) — [07-08](briefings/2026-07-08.md)

- **dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

- **integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

- **signature-replay** (1 briefing) — [06-14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 36
- **Date range:** 2026-06-12 → 2026-07-18 (37 days; one gap on Jun 26)
- **Top 3 most-frequent bug classes:**
  1. **logic-error** — 26 briefings (72% of days covered)
  2. **key-management** — 26 briefings (72% of days covered)
  3. **access-control** — 19 briefings (53% of days covered)
- **Total tracked losses (approximate):** $1B+ across full window; July 2026 alone ~$142M (PeckShield estimate)
- **Most-targeted chains:** Ethereum, Solana, Arbitrum, BNB Chain, cross-chain bridges

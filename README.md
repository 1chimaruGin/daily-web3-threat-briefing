# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-07-13](briefings/2026-07-13.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-13](briefings/2026-07-13.md) | No new drain in 24h; SlowMist H1 2026 report: 182 incidents, supply-chain #1 by loss ($298M); BonkDAO attacker launders $19M into "BONK 2.0" DAO | BonkDAO $20M (laundering), Bonzo Lend $9M (Supra patched) | `oracle-manipulation` `access-control` `logic-error` `key-management` `supply-chain` | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price inflation; Ill Bloom PRNG flaw keeps draining wallets ($5M+) | Bonzo Lend $9M, Ill Bloom $5M+ (ongoing) | `oracle-manipulation` `price-manipulation` `key-management` `flash-loan` | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances as attacker returns $37M; OZ Wizard CVE day 28 | GMX V1 $42M (recovery), BonkDAO $20M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | `reentrancy` `flash-loan` `access-control` `logic-error` `supply-chain` | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M, Summer.fi $6M, BonkDAO $20M, Altura $39M, ResupplyFi $9.6M | `reentrancy` `flash-loan` `access-control` `logic-error` `key-management` | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026: wallet compromise #1 loss vector ($444M); Summer.fi laundering via Tornado Cash | Summer.fi $6M ongoing, BonkDAO $20M ongoing | `key-management` `flash-loan` `access-control` `logic-error` | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4.4M governance buyout on Solana; MEV backrun drains $2M via illiquid Uniswap v3 pool | BonkDAO $20M governance attack, ETH MEV $2M | `access-control` `logic-error` `front-running` | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts thousands of wallets at risk | Summer.fi $6M, Ill Bloom PRNG $5M cumulative | `flash-loan` `logic-error` `key-management` | ~$11M new; ~$51M ongoing |
| [2026-07-06](briefings/2026-07-06.md) | No new drains Jul 5–6; IronWorm Rust npm worm (eBPF rootkit + Tor C2) JFrog autopsy; ResupplyFi ERC-4626 post-mortem public | IronWorm npm worm (37 packages), ResupplyFi post-mortem | `supply-chain` `flash-loan` `rounding` `key-management` | n/a new; ~$48M ongoing |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion ($70B at risk); SlowMist warns AI IDE markdown injection runs on Open Folder | Hexens/Aptos MoveVM (patched Feb 25), SlowMist AI IDE injection | `logic-error` `supply-chain` `key-management` | n/a new; ~$48M ongoing |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug — COO-tied DVN verifier, depositors locked; CSA formalizes AI "vibe-coded" Solidity as CVE-surge driver | Altura $39M, LendFi $5.2M oracle | `key-management` `bridge-dvn` `oracle-manipulation` `logic-error` `unverified-contract` | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 report warns AI drives "vulnerability apocalypse" | ResupplyFi $9.6M ERC-4626, Kinto Protocol $1.55M proxy-backdoor | `flash-loan` `price-manipulation` `upgradeability` `access-control` `key-management` | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts | Edel Finance $403K (wGOOGLx flash-loan) | `flash-loan` `price-manipulation` `unverified-contract` `key-management` | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 CVSS-10 SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets — CISA July 2 deadline | CVE-2026-48558 SimpleHelp (Djinn Stealer), GlassWorm macOS new wave | `key-management` `supply-chain` `access-control` | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat identity disputed, EMURGO denies; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm packages | `key-management` `supply-chain` `logic-error` `bridge-dvn` | ~$18.5M contested |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter: 83 hacks, $775M stolen | SecondFi $2.4M–$20M keygen | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE hits DAO governance portals | Polymarket $3M supply-chain inject, CVE-2026-12866 expr-eval | `supply-chain` `key-management` `logic-error` `access-control` | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy — generalizable ZK witness-binding gap | DARKNAVY Aztec circuit autopsy (technique) | `logic-error` `access-control` `supply-chain` `key-management` | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool $1.1M via token parameter desync | Taiko Bridge SGX key $1.7M, OLPC/LABUBU PancakeSwap $1.1M, mySwap Starknet $305K | `key-management` `bridge-dvn` `price-manipulation` `oracle-manipulation` `logic-error` | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike flaw | `logic-error` `unverified-contract` `access-control` | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time record: 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading class | (quarterly wrap — no new drains) | `access-control` `key-management` `bridge-dvn` `price-manipulation` | Q2: ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K (Jun 19 catch-up) | `logic-error` `bridge-dvn` `oracle-manipulation` `price-manipulation` | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla | `access-control` `logic-error` `unverified-contract` | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | No new drain; "abandoned-contract" pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry | (quiet 24h window) | `unverified-contract` `logic-error` `upgradeability` `oracle-manipulation` | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js 2 HIGH CVEs drop June 18 | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs | `bridge-dvn` `key-management` `logic-error` `dos` | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus "Mach-O Man" macOS kit active | (no new drains Jun 17–18) | `access-control` `key-management` `supply-chain` `upgradeability` | n/a new; EIP-7702 ~$8M cumulative |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M ZK bypass, Syscoin Bridge ~$8M catch-up | `logic-error` `bridge-dvn` `supply-chain` `key-management` | ~$2.1M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs incoming | Thetanuts Finance $2.1M flash-loan/rounding | `flash-loan` `rounding` `logic-error` | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning ~$45M in 2026 | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M | `integer-overflow` `rounding` `logic-error` `access-control` | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K forensics, AFI Protocol $480K | `bridge-dvn` `signature-replay` `logic-error` | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing; OZ Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 OZ Wizard | `key-management` `upgradeability` `access-control` `supply-chain` | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | `flash-loan` `logic-error` `key-management` `bridge-dvn` `unverified-contract` | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by number of briefings (most frequent first). Each date links to the briefing where that class appears.

**`logic-error`** (22 briefings) — [06-12](briefings/2026-06-12.md) · [06-14](briefings/2026-06-14.md) · [06-15](briefings/2026-06-15.md) · [06-16](briefings/2026-06-16.md) · [06-17](briefings/2026-06-17.md) · [06-19](briefings/2026-06-19.md) · [06-20](briefings/2026-06-20.md) · [06-21](briefings/2026-06-21.md) · [06-22](briefings/2026-06-22.md) · [06-24](briefings/2026-06-24.md) · [06-25](briefings/2026-06-25.md) · [06-27](briefings/2026-06-27.md) · [06-28](briefings/2026-06-28.md) · [06-29](briefings/2026-06-29.md) · [06-30](briefings/2026-06-30.md) · [07-04](briefings/2026-07-04.md) · [07-07](briefings/2026-07-07.md) · [07-08](briefings/2026-07-08.md) · [07-09](briefings/2026-07-09.md) · [07-10](briefings/2026-07-10.md) · [07-11](briefings/2026-07-11.md) · [07-13](briefings/2026-07-13.md)

**`key-management`** (22 briefings) — [06-12](briefings/2026-06-12.md) · [06-13](briefings/2026-06-13.md) · [06-17](briefings/2026-06-17.md) · [06-18](briefings/2026-06-18.md) · [06-19](briefings/2026-06-19.md) · [06-23](briefings/2026-06-23.md) · [06-25](briefings/2026-06-25.md) · [06-27](briefings/2026-06-27.md) · [06-28](briefings/2026-06-28.md) · [06-29](briefings/2026-06-29.md) · [06-30](briefings/2026-06-30.md) · [07-01](briefings/2026-07-01.md) · [07-02](briefings/2026-07-02.md) · [07-03](briefings/2026-07-03.md) · [07-04](briefings/2026-07-04.md) · [07-05](briefings/2026-07-05.md) · [07-06](briefings/2026-07-06.md) · [07-07](briefings/2026-07-07.md) · [07-09](briefings/2026-07-09.md) · [07-10](briefings/2026-07-10.md) · [07-12](briefings/2026-07-12.md) · [07-13](briefings/2026-07-13.md)

**`access-control`** (15 briefings) — [06-13](briefings/2026-06-13.md) · [06-15](briefings/2026-06-15.md) · [06-18](briefings/2026-06-18.md) · [06-21](briefings/2026-06-21.md) · [06-23](briefings/2026-06-23.md) · [06-24](briefings/2026-06-24.md) · [06-27](briefings/2026-06-27.md) · [06-28](briefings/2026-06-28.md) · [07-01](briefings/2026-07-01.md) · [07-03](briefings/2026-07-03.md) · [07-08](briefings/2026-07-08.md) · [07-09](briefings/2026-07-09.md) · [07-10](briefings/2026-07-10.md) · [07-11](briefings/2026-07-11.md) · [07-13](briefings/2026-07-13.md)

**`supply-chain`** (12 briefings) — [06-13](briefings/2026-06-13.md) · [06-17](briefings/2026-06-17.md) · [06-18](briefings/2026-06-18.md) · [06-27](briefings/2026-06-27.md) · [06-28](briefings/2026-06-28.md) · [06-29](briefings/2026-06-29.md) · [06-30](briefings/2026-06-30.md) · [07-01](briefings/2026-07-01.md) · [07-05](briefings/2026-07-05.md) · [07-06](briefings/2026-07-06.md) · [07-11](briefings/2026-07-11.md) · [07-13](briefings/2026-07-13.md)

**`flash-loan`** (10 briefings) — [06-12](briefings/2026-06-12.md) · [06-16](briefings/2026-06-16.md) · [07-02](briefings/2026-07-02.md) · [07-03](briefings/2026-07-03.md) · [07-06](briefings/2026-07-06.md) · [07-07](briefings/2026-07-07.md) · [07-09](briefings/2026-07-09.md) · [07-10](briefings/2026-07-10.md) · [07-11](briefings/2026-07-11.md) · [07-12](briefings/2026-07-12.md)

**`bridge-dvn`** (10 briefings) — [06-12](briefings/2026-06-12.md) · [06-14](briefings/2026-06-14.md) · [06-17](briefings/2026-06-17.md) · [06-19](briefings/2026-06-19.md) · [06-22](briefings/2026-06-22.md) · [06-23](briefings/2026-06-23.md) · [06-25](briefings/2026-06-25.md) · [06-29](briefings/2026-06-29.md) · [06-30](briefings/2026-06-30.md) · [07-04](briefings/2026-07-04.md)

**`oracle-manipulation`** (6 briefings) — [06-20](briefings/2026-06-20.md) · [06-22](briefings/2026-06-22.md) · [06-25](briefings/2026-06-25.md) · [07-04](briefings/2026-07-04.md) · [07-12](briefings/2026-07-12.md) · [07-13](briefings/2026-07-13.md)

**`price-manipulation`** (6 briefings) — [06-22](briefings/2026-06-22.md) · [06-23](briefings/2026-06-23.md) · [06-25](briefings/2026-06-25.md) · [07-02](briefings/2026-07-02.md) · [07-03](briefings/2026-07-03.md) · [07-12](briefings/2026-07-12.md)

**`unverified-contract`** (6 briefings) — [06-12](briefings/2026-06-12.md) · [06-20](briefings/2026-06-20.md) · [06-21](briefings/2026-06-21.md) · [06-24](briefings/2026-06-24.md) · [07-02](briefings/2026-07-02.md) · [07-04](briefings/2026-07-04.md)

**`upgradeability`** (4 briefings) — [06-13](briefings/2026-06-13.md) · [06-18](briefings/2026-06-18.md) · [06-20](briefings/2026-06-20.md) · [07-03](briefings/2026-07-03.md)

**`rounding`** (3 briefings) — [06-15](briefings/2026-06-15.md) · [06-16](briefings/2026-06-16.md) · [07-06](briefings/2026-07-06.md)

**`reentrancy`** (2 briefings) — [07-10](briefings/2026-07-10.md) · [07-11](briefings/2026-07-11.md)

**`dos`** (1 briefing) — [06-19](briefings/2026-06-19.md)

**`front-running`** (1 briefing) — [07-08](briefings/2026-07-08.md)

**`integer-overflow`** (1 briefing) — [06-15](briefings/2026-06-15.md)

**`signature-replay`** (1 briefing) — [06-14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 31
- **Date range:** 2026-06-12 → 2026-07-13 (32 calendar days; one gap on 2026-06-26)
- **Top 3 bug classes by briefing frequency:**
  1. `logic-error` — 22 briefings (71%)
  2. `key-management` — 22 briefings (71%)
  3. `access-control` — 15 briefings (48%)
- **2026 YTD context (H1 per SlowMist):** 182 incidents · ~$956M lost · 50% more incidents than H1 2025 · supply-chain = largest single loss category ($298M)
- **Running carry-forward exposure (July 13):** ~$75M across 6 active situations (BonkDAO $19M · Bonzo Lend $9M · Altura $39M · Summer.fi $6M · ResupplyFi $9.6M · GMX V1 ~$5M)

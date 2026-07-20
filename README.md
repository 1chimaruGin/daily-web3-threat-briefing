# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.  
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.  
**Latest briefing:** [2026-07-20](briefings/2026-07-20.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 opens with 35M-user wallet-extension PoC live; CoinDCX post-mortem confirms 6-day dwell + employee arrest | CoinDCX $44M post-mortem, PETS 2026 wallet-extension PoC, Across Solana event-spoofing disclosure | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$147M July MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist discloses macOS infostealer replacing Ledger/Trezor with fakes; PETS 2026 wallet-extension paper drops for 35M users | macOS wallet-replacement infostealer, PETS 2026 wallet-extension disclosures, Ill Bloom $5M+ sweeps | `key-management` `supply-chain` `logic-error` | ~$5M+ new; $147M July MTD |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked July 17 | CoinDCX $44M, Across Protocol Solana relayer (TBD), DeFiTuna $580K, BigONE $27M | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week; Ostium still halted | Cascade $1.34M | `access-control` `logic-error` `oracle-manipulation` `key-management` `flash-loan` | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum — third oracle attack in five days | Ostium $18–22M | `key-management` `oracle-manipulation` `price-manipulation` `access-control` `upgradeability` | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery | `upgradeability` `reentrancy` `access-control` `oracle-manipulation` `supply-chain` | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed; six incidents ongoing (~$78M unrecovered) | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M retained, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | `oracle-manipulation` `access-control` `logic-error` `supply-chain` `flash-loan` | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026 report: 182 incidents, supply-chain #1 by losses at $298M; BonkDAO attacker launders $19M into "BONK 2.0" DAO | BonkDAO $20M (laundering), Bonzo Lend $9M (Supra fix deployed) | `oracle-manipulation` `access-control` `logic-error` `key-management` `supply-chain` | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation; Ill Bloom PRNG sweeps continue | Bonzo Lend $9M, Ill Bloom $5M+ ongoing | `oracle-manipulation` `price-manipulation` `key-management` `flash-loan` | ~$14M new |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M compensation plan advances as attacker returns $37M; OZ Wizard CVE-2026-48054 day 28 | GMX V1 $42M (recovery/comp), Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | `reentrancy` `flash-loan` `access-control` `logic-error` `supply-chain` | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M, Summer.fi $6M, BonkDAO $20M, Altura $39M, ResupplyFi $9.6M | `reentrancy` `flash-loan` `access-control` `logic-error` `key-management` | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M) | Summer.fi (Tornado Cash), BonkDAO (exchanges) | `key-management` `flash-loan` `access-control` `logic-error` | ~$75M ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M, Ethereum MEV backrun $2M | `access-control` `logic-error` `front-running` | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts thousands at risk | Summer.fi $6M, Ill Bloom $5M cumulative | `flash-loan` `logic-error` `key-management` | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets full JFrog autopsy; ResupplyFi ERC-4626 post-mortem published | IronWorm npm worm (37 pkgs), ResupplyFi $9.6M post-mortem | `supply-chain` `flash-loan` `rounding` `key-management` | n/a new drains |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug threatening $70B; SlowMist warns AI IDE markdown injection | Hexens/Aptos MoveVM ($70B systemic, patched), SlowMist AI IDE markdown injection | `logic-error` `supply-chain` `key-management` | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI 'vibe-coded' Solidity risk | Altura $39M, LendFi $5.2M | `key-management` `bridge-dvn` `oracle-manipulation` `logic-error` `unverified-contract` | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M, Kinto Protocol $1.55M | `flash-loan` `price-manipulation` `upgradeability` `access-control` `key-management` | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks | Edel Finance $403K, June 2026 monthly wrap | `flash-loan` `price-manipulation` `unverified-contract` `key-management` | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto creds — CISA deadline | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX wave | `key-management` `supply-chain` `access-control` | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm pkgs | `key-management` `supply-chain` `logic-error` `bridge-dvn` | ~$18.5M disputed |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 closes as record with 83 hacks, $775M | SecondFi $2.4M–$20M, JaredFromSubway $7.5M Tornado Cash, Q2 record | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$22.5M new |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M supply-chain, CVE-2026-12866 expr-eval | `supply-chain` `key-management` `logic-error` `access-control` | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | Quiet 24h; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy showing generalizable ZK witness-binding gap | DARKNAVY Aztec circuit autopsy (technique) | `logic-error` `access-control` `supply-chain` `key-management` | n/a new |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; OLPC/LABUBU pool drained $1.1M on BNB | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | `key-management` `bridge-dvn` `price-manipulation` `oracle-manipulation` `logic-error` | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike | `logic-error` `unverified-contract` `access-control` | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M; access-control exploits overtake smart-contract bugs | Q2 2026 record: 83 incidents / $755M | `access-control` `key-management` `bridge-dvn` `price-manipulation` | n/a new |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem | Namada MASP $600K | `logic-error` `bridge-dvn` `oracle-manipulation` `price-manipulation` | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla | `access-control` `logic-error` `unverified-contract` | n/a new (catch-up) |
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy entry formalizes threat | — | `unverified-contract` `logic-error` `upgradeability` `oracle-manipulation` | n/a new |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js HIGH CVEs drop June 18 | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs | `bridge-dvn` `key-management` `logic-error` `dos` | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ real-world exploits; Lazarus 'Mach-O Man' macOS kit active | — | `access-control` `key-management` `supply-chain` `upgradeability` | n/a new |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M, Syscoin Bridge ~$8M catch-up, Node.js CVE | `logic-error` `bridge-dvn` `supply-chain` `key-management` | ~$2.1M new |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | `flash-loan` `rounding` `logic-error` | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning $45M claim | Flooring Protocol ~$500K, Unleash Protocol $3.9M | `integer-overflow` `rounding` `logic-error` `access-control` | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No June 14 drains confirmed; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K forensics, AFI Protocol $480K catch-up | `bridge-dvn` `signature-replay` `logic-error` | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OZ Wizard CVE-2026-48054 injects into test scaffolds | Humanity Protocol $36M (DPRK), CVE-2026-48054 OZ Wizard | `key-management` `upgradeability` `access-control` `supply-chain` | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient Finance $110K | `flash-loan` `logic-error` `key-management` `bridge-dvn` `unverified-contract` | ~$7.9M |

---

## 🏷️ Browse by bug class

*Sorted by number of briefings featuring each class (most frequent first). Each date links directly to that day's briefing.*

**`key-management`** — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md) **(30 briefings)**

**`logic-error`** — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md) **(28 briefings)**

**`access-control`** — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md) **(19 briefings)**

**`supply-chain`** — [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-18](briefings/2026-07-18.md), [07-19](briefings/2026-07-19.md), [07-20](briefings/2026-07-20.md) **(17 briefings)**

**`flash-loan`** — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md) **(12 briefings)**

**`bridge-dvn`** — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-17](briefings/2026-07-17.md), [07-18](briefings/2026-07-18.md), [07-20](briefings/2026-07-20.md) **(12 briefings)**

**`oracle-manipulation`** — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [07-04](briefings/2026-07-04.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md) **(9 briefings)**

**`price-manipulation`** — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-12](briefings/2026-07-12.md), [07-16](briefings/2026-07-16.md) **(7 briefings)**

**`upgradeability`** — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md) **(6 briefings)**

**`unverified-contract`** — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md) **(6 briefings)**

**`reentrancy`** — [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-15](briefings/2026-07-15.md) **(3 briefings)**

**`rounding`** — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md) **(3 briefings)**

**`front-running`** — [07-08](briefings/2026-07-08.md) **(1 briefing)**

**`dos`** — [06-19](briefings/2026-06-19.md) **(1 briefing)**

**`integer-overflow`** — [06-15](briefings/2026-06-15.md) **(1 briefing)**

**`signature-replay`** — [06-14](briefings/2026-06-14.md) **(1 briefing)**

---

## 📊 Stats

- **Total briefings:** 38 (2026-06-12 through 2026-07-20; no briefing for 2026-06-26)
- **Date range:** 2026-06-12 → 2026-07-20 (39 days)
- **Top 3 most-frequent bug classes:**
  1. `key-management` — 30 of 38 briefings (79%)
  2. `logic-error` — 28 of 38 briefings (74%)
  3. `access-control` — 19 of 38 briefings (50%)

> **Trend note:** `key-management` has appeared in every briefing since July 1. The 2026 threat landscape is dominated by off-chain key compromise (social engineering, malware, supply-chain) rather than pure smart-contract bugs — a shift well-documented by CertiK H1 2026 and SlowMist H1 2026 reports.

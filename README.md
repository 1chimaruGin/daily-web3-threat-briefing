# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-07-16](briefings/2026-07-16.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum; third oracle attack in five days | Ostium $18–22M, Kinto shutdown, Altura $39M | `key-management` `oracle-manipulation` `price-manipulation` `access-control` `upgradeability` | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns ~$37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery ($37M returned) | `upgradeability` `reentrancy` `access-control` `oracle-manipulation` `supply-chain` | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 (web3.py SSRF via EIP-3668 CCIP Read) fully disclosed Day 4; no new on-chain drain; six incidents ongoing | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M retained, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | `oracle-manipulation` `access-control` `logic-error` `supply-chain` `flash-loan` | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | No new drain; SlowMist H1 2026 report (182 incidents, supply-chain #1 at $298M); BonkDAO attacker launders $19M into "BONK 2.0" DAO | BonkDAO $20M (laundering), Bonzo Lend $9M (Supra fix deployed) | `oracle-manipulation` `access-control` `logic-error` `key-management` `supply-chain` | ~$75M |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-order-of-magnitude oracle price manipulation; Ill Bloom PRNG flaw keeps draining wallets ($5M+) | Bonzo Lend $9M, Ill Bloom $5M+ | `oracle-manipulation` `price-manipulation` `key-management` `flash-loan` | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new confirmed drain; GMX V1 $44M compensation plan advances as attacker returns $37M; OZ Wizard CVE Day 28 | GMX V1 $42M (recovery), BonkDAO $20M, Altura $39M, Summer.fi $6M, ResupplyFi $9.6M | `reentrancy` `flash-loan` `access-control` `logic-error` `supply-chain` | ~$75M |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty; four prior incidents active | GMX V1 $42M, Summer.fi $6M, BonkDAO $20M, Altura $39M, ResupplyFi $9.6M | `reentrancy` `flash-loan` `access-control` `logic-error` `key-management` | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M); Summer.fi $6M laundering confirmed | Summer.fi (Tornado Cash laundering), BonkDAO ongoing | `key-management` `flash-loan` `access-control` `logic-error` | ~$75M |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun via illiquid pool | BonkDAO $20M, Ethereum MEV backrun $2M | `access-control` `logic-error` `front-running` | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts thousands of software wallets at risk | Summer.fi $6M, Ill Bloom $5M cumulative | `flash-loan` `logic-error` `key-management` | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains Jul 5–6; IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets comprehensive JFrog autopsy; ResupplyFi post-mortem public | IronWorm npm worm (37 packages), ResupplyFi $9.6M post-mortem | `supply-chain` `flash-loan` `rounding` `key-management` | n/a new drains |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug threatening $70B; SlowMist warns AI IDE markdown injection executes on Open Folder | Hexens/Aptos MoveVM (patched), SlowMist AI IDE markdown injection, Miasma worm Cosmos SDK | `logic-error` `supply-chain` `key-management` | n/a ($70B theoretical, patched) |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI 'vibe-coded' Solidity as new CVE-surge driver | Altura $39M, LendFi $5.2M oracle manipulation | `key-management` `bridge-dvn` `oracle-manipulation` `logic-error` `unverified-contract` | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 final report warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M (laundering), Kinto $1.55M proxy-backdoor | `flash-loan` `price-manipulation` `upgradeability` `access-control` `key-management` | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts | Edel Finance $403K, June 2026 wrap 45 incidents $75.87M | `flash-loan` `price-manipulation` `unverified-contract` `key-management` | ~$403K confirmed |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and web3 dev creds — CISA July 2 patch deadline | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX, SecondFi/EMURGO custody standoff | `key-management` `supply-chain` `access-control` | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new confirmed drains; SecondFi's white-hat identity disputed as EMURGO denies knowing who secured $18.5M in ADA; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet Mastra npm (144 packages) | `key-management` `supply-chain` `logic-error` `bridge-dvn` | ~$18.5M |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter: 83 hacks, $775M stolen | SecondFi $2.4M–$20M, JaredFromSubway $7.5M Tornado Cash movement, Q2 record | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals | Polymarket $3M supply-chain, CVE-2026-12866 expr-eval | `supply-chain` `key-management` `logic-error` `access-control` | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing generalizable ZK witness-binding gap | DARKNAVY Aztec circuit autopsy (technique) | `logic-error` `access-control` `supply-chain` `key-management` | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB Chain | Taiko Bridge SGX key leak $1.7M, OLPC/LABUBU PancakeSwap $1.1M, mySwap CL Starknet $305K | `key-management` `bridge-dvn` `price-manipulation` `oracle-manipulation` `logic-error` | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing across major wallet UIs | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | `logic-error` `unverified-contract` `access-control` | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading attack class | Q2 2026 record 83 incidents / $755M | `access-control` `key-management` `bridge-dvn` `price-manipulation` | n/a (aggregate) |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain (Jun 19) masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem | Namada MASP $600K (catch-up) | `logic-error` `bridge-dvn` `oracle-manipulation` `price-manipulation` | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV | Aztec RollupProcessor $2.21M (analysis), CVE-2026-48907 Joomla JCE | `access-control` `logic-error` `unverified-contract` | n/a new; ~$2.21M Aztec |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes threat | (quiet window) | `unverified-contract` `logic-error` `upgradeability` `oracle-manipulation` | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs Jun 18 — patch all blockchain tooling | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs Jun 18 | `bridge-dvn` `key-management` `logic-error` `dos` | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains | (no new on-chain drains confirmed) | `access-control` `key-management` `supply-chain` `upgradeability` | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | `logic-error` `bridge-dvn` `supply-chain` `key-management` | ~$2.1M strict; ~$10.3M catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in a deprecated options vault; Node.js HIGH CVEs drop Jun 17 — patch before bots go live | Thetanuts Finance $2.1M | `flash-loan` `rounding` `logic-error` | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol's BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026 | Flooring Protocol ~$500K NFTs (catch-up), Unleash Protocol $3.9M (catch-up) | `integer-overflow` `rounding` `logic-error` `access-control` | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains confirmed; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M across three platforms | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | `bridge-dvn` `signature-replay` `logic-error` | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds | Humanity Protocol $36M (DPRK attribution), CVE-2026-48054 OZ Wizard | `key-management` `upgradeability` `access-control` `supply-chain` | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal Protocol $915K, NovaBox $107K, Ambient Finance $110K | `flash-loan` `logic-error` `key-management` `bridge-dvn` `unverified-contract` | ~$7.9M |

---

## 🏷️ Browse by bug class

*(Sorted by number of briefings each tag appears in — most frequent first)*

- **`logic-error`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **`key-management`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

- **`access-control`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-08](briefings/2026-07-08.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

- **`supply-chain`** — [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

- **`oracle-manipulation`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-14](briefings/2026-07-14.md), [2026-07-13](briefings/2026-07-13.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

- **`flash-loan`** — [2026-07-14](briefings/2026-07-14.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md), [2026-07-09](briefings/2026-07-09.md), [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

- **`bridge-dvn`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

- **`price-manipulation`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-12](briefings/2026-07-12.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

- **`upgradeability`** — [2026-07-16](briefings/2026-07-16.md), [2026-07-15](briefings/2026-07-15.md), [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

- **`unverified-contract`** — [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

- **`reentrancy`** — [2026-07-15](briefings/2026-07-15.md), [2026-07-11](briefings/2026-07-11.md), [2026-07-10](briefings/2026-07-10.md)

- **`rounding`** — [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

- **`front-running`** — [2026-07-08](briefings/2026-07-08.md)

- **`integer-overflow`** — [2026-06-15](briefings/2026-06-15.md)

- **`signature-replay`** — [2026-06-14](briefings/2026-06-14.md)

- **`dos`** — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 34 (2026-06-12 → 2026-07-16; one gap: 2026-06-26)
- **Date range:** June 12 – July 16, 2026 (35 days covered)
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 27 briefings
  2. `key-management` — 26 briefings
  3. `access-control` — 20 briefings
- **Active oracle attack wave (mid-July):** Bonzo Lend $9M (Jul 11) + Ostium $18–22M (Jul 15) — 2 oracle drains in 5 days; elevated hunter priority
- **Largest in-window incident:** GMX V1 $42M keeper-reentrancy drain (Jul 10, Arbitrum)
- **Largest unresolved lock:** Altura $39M (DVN verifier, Tron) — no recovery path announced

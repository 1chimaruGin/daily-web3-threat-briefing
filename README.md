# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-07-10](briefings/2026-07-10.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug Classes | $ at Risk |
|---|---|---|---|---|
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP $42M keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M, Summer.fi ongoing, BonkDAO ongoing, Altura ongoing | `reentrancy` `flash-loan` `access-control` `logic-error` | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M) | Summer.fi ongoing, BonkDAO ongoing | `key-management` `flash-loan` `access-control` `logic-error` | ~$75M ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO $20M governance buyout on Solana; Ethereum trader $2M same-block MEV backrun | BonkDAO $20M, MEV backrun $2M | `access-control` `logic-error` `front-running` | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi $6M FleetCommander vault accounting exploit; Ill Bloom PRNG $5M wallet drains | Summer.fi $6M, Ill Bloom PRNG $5M | `flash-loan` `logic-error` `key-management` | ~$11M |
| [2026-07-06](briefings/2026-07-06.md) | No new drains; IronWorm Rust npm worm (eBPF rootkit + Tor C2); ResupplyFi post-mortem | IronWorm npm worm (37 pkgs), ResupplyFi post-mortem | `supply-chain` `flash-loan` `rounding` `key-management` | n/a |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion $70B at systemic risk | Aptos MoveVM $70B systemic (patched) | `logic-error` `supply-chain` `key-management` | n/a new |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug; LendFi $5.2M oracle manipulation | Altura $39M, LendFi $5.2M | `key-management` `bridge-dvn` `oracle-manipulation` `logic-error` `unverified-contract` | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi $9.6M ERC-4626 laundering; Kinto Protocol $1.55M proxy-backdoor | ResupplyFi $9.6M, Kinto $1.55M | `flash-loan` `price-manipulation` `upgradeability` `access-control` `key-management` | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K wrapped-token flash-loan; AI-accelerated unverified-contract attacks | Edel Finance $403K | `flash-loan` `price-manipulation` `unverified-contract` `key-management` | ~$403K |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 CVSS 10.0 SimpleHelp RMM exploited; Djinn Stealer harvests crypto wallets | CVE-2026-48558 SimpleHelp (CISA KEV) | `key-management` `supply-chain` `access-control` | n/a |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat custody dispute; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi ADA dispute, Sapphire Sleet npm | `key-management` `supply-chain` `logic-error` `bridge-dvn` | ~$18.5M custody |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano $2.4M keygen flaw (up to $20M at risk); Q2 2026 record close | SecondFi $2.4M–$20M, Q2 record $775M | `key-management` `supply-chain` `bridge-dvn` `logic-error` | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket $3M supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M, CVE-2026-12866 | `supply-chain` `key-management` `logic-error` `access-control` | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy | DARKNAVY Aztec circuit autopsy | `logic-error` `access-control` `supply-chain` `key-management` | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko Bridge $1.7M SGX key leak to GitHub; LABUBU/OLPC $1.1M token parameter desync | Taiko $1.7M, OLPC/LABUBU $1.1M, mySwap $305K | `key-management` `bridge-dvn` `price-manipulation` `oracle-manipulation` `logic-error` | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot $15M counter-MEV honeypot; ENS lookalike wallet spoofing | JaredFromSubway MEV $15M | `logic-error` `unverified-contract` `access-control` | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 all-time record — 83 incidents, $755M; access-control overtakes smart-contract bugs | Q2 2026 83 incidents / $755M | `access-control` `key-management` `bridge-dvn` `price-manipulation` | n/a |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K | `logic-error` `bridge-dvn` `oracle-manipulation` `price-manipulation` | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() TurboVerifier accepts spoofed ZK inputs ($2.21M); Joomla CVSS-10 | Aztec $2.21M (analysis), CVE-2026-48907 Joomla | `access-control` `logic-error` `unverified-contract` | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; abandoned-contract pattern accounts for 4 of June's 16 incidents | (no new drains) | `unverified-contract` `logic-error` `upgradeability` `oracle-manipulation` | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained via dual validator+finality bypass (catch-up Jun 14) | 3-protocol bridge $127M | `bridge-dvn` `key-management` `logic-error` `dos` | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces $8M+ real exploits; Lazarus 'Mach-O Man' macOS kit | EIP-7702 cumulative $8M+ | `access-control` `key-management` `supply-chain` `upgradeability` | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect $2.1M L1/L2 proof-boundary bypass; Syscoin Bridge $8M SPV proof forgery | Aztec $2.1M, Syscoin $8M (catch-up) | `logic-error` `bridge-dvn` `supply-chain` `key-management` | ~$2.1M strict |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault | Thetanuts Finance $2.1M | `flash-loan` `rounding` `logic-error` | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring ~$500K, Unleash $3.9M | `integer-overflow` `rounding` `logic-error` `access-control` | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises bounty to $5M | Alephium $815K forensics, AFI $480K | `bridge-dvn` `signature-replay` `logic-error` | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Humanity Protocol $36M breach pinned on DPRK phishing; OZ Wizard CVE-2026-48054 | Humanity Protocol $36M, CVE-2026-48054 | `key-management` `upgradeability` `access-control` `supply-chain` | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium $1.34M fake LP tokens; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M | `flash-loan` `logic-error` `key-management` `bridge-dvn` `unverified-contract` | ~$7.9M |

---

## 🏷️ Browse by Bug Class

> Sorted by number of briefings containing the tag (most → least). Each date links directly to that day's briefing.

**`logic-error`** (23 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md)

**`key-management`** (20 briefings) — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md)

**`access-control`** (17 briefings) — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md)

**`bridge-dvn`** (10 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md)

**`supply-chain`** (10 briefings) — [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md)

**`flash-loan`** (8 briefings) — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md)

**`unverified-contract`** (6 briefings) — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md)

**`oracle-manipulation`** (5 briefings) — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-04](briefings/2026-07-04.md)

**`price-manipulation`** (5 briefings) — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md)

**`upgradeability`** (4 briefings) — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md)

**`rounding`** (3 briefings) — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md)

**`reentrancy`** (1 briefing) — [07-10](briefings/2026-07-10.md)

**`signature-replay`** (1 briefing) — [06-14](briefings/2026-06-14.md)

**`integer-overflow`** (1 briefing) — [06-15](briefings/2026-06-15.md)

**`dos`** (1 briefing) — [06-19](briefings/2026-06-19.md)

**`front-running`** (1 briefing) — [07-08](briefings/2026-07-08.md)

---

## 📊 Stats

| Metric | Value |
|---|---|
| **Total briefings** | 28 |
| **Date range** | 2026-06-12 → 2026-07-10 (29 days; one skip: Jun 26) |
| **#1 bug class** | `logic-error` — 23 / 28 briefings (82%) |
| **#2 bug class** | `key-management` — 20 / 28 briefings (71%) |
| **#3 bug class** | `access-control` — 17 / 28 briefings (61%) |
| **Largest single incident** | $127M cross-chain bridge ([2026-06-19](briefings/2026-06-19.md)) |
| **Most active chain** | Ethereum (present in nearly every briefing) |
| **Chains covered** | Ethereum, Arbitrum, Solana, BNB, Aptos, Cosmos, Polygon, Starknet, Cardano, Sui, Tron, Base, Optimism, Alephium, Syscoin |

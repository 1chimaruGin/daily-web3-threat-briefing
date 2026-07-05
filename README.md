# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-05](briefings/2026-07-05.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion that threatened $70B; SlowMist warns AI IDE markdown injection executes on Open Folder | Hexens/Aptos MoveVM type-confusion (patched), SlowMist AI IDE markdown injection, Miasma expands to Cosmos SDK Go modules | logic-error, supply-chain, key-management | n/a new drains; $70B theoretical (patched) |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI 'vibe-coded' Solidity as new CVE-surge driver | Altura $39M gold-vault, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 report warns AI driving "vulnerability apocalypse" | ResupplyFi $9.6M ERC-4626, Kinto Protocol $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts | Edel Finance $403K (wGOOGLx flash-loan), June 2026 monthly wrap 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K confirmed |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and web3 dev creds | CVE-2026-48558 SimpleHelp (Djinn Stealer), GlassWorm macOS OpenVSX wave, SecondFi/EMURGO custody standoff | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat identity disputed; EMURGO denies knowing who secured $18.5M ADA; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet Mastra npm (144 packages) | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M (custody dispute) |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter with 83 hacks and $775M stolen | SecondFi $2.4M–$20M keygen flaw, JaredFromSubway MEV $7.5M Tornado Cash | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals | Polymarket $3M supply-chain frontend injection, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new confirmed drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing generalizable ZK witness-binding gap | No new drains (technique disclosure: DARKNAVY Aztec autopsy) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB | Taiko Bridge SGX key leak $1.7M, OLPC/LABUBU PancakeSwap $1.1M, mySwap CL Starknet $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading attack class | Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | n/a new drains |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem | Namada MASP $600K (catch-up Jun 19) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; Joomla JCE CVSS-10 in CISA KEV | Aztec RollupProcessor $2.21M escapeHatch(), CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes the threat | No new drains (technique: abandoned-contract pattern) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 | Unnamed 3-protocol bridge $127M (catch-up Jun 14), Node.js HIGH CVEs Jun 18 | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit harvesting crypto team keychains | No new drains; EIP-7702 cumulative ~$8M+, Lazarus macOS campaign | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M ZK settlement bypass, Syscoin Bridge ~$8M (catch-up) | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict window |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17 | Thetanuts Finance $2.1M (flash-loan/rounding) | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026 | Flooring Protocol ~$500K NFTs (catch-up), Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds | Humanity Protocol $36M (DPRK attribution), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal Protocol $915K, NovaBox $107K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

**`logic-error`** — [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**`key-management`** — [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

**`supply-chain`** — [2026-07-05](briefings/2026-07-05.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

**`access-control`** — [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

**`bridge-dvn`** — [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**`oracle-manipulation`** — [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

**`price-manipulation`** — [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

**`flash-loan`** — [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

**`unverified-contract`** — [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

**`upgradeability`** — [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

**`signature-replay`** — [2026-06-14](briefings/2026-06-14.md)

**`integer-overflow`** — [2026-06-15](briefings/2026-06-15.md)

**`rounding`** — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

**`dos`** — [2026-06-19](briefings/2026-06-19.md)

**`front-running`** — *(no briefings yet)*

---

## 📊 Stats

- **Total briefings:** 23 (2026-06-12 through 2026-07-05; no briefing for 2026-06-26)
- **Date range:** June 12 – July 5, 2026 (24 days covered)
- **Top 3 most-frequent bug classes:**
  1. `logic-error` — 18 briefings
  2. `key-management` — 16 briefings
  3. `supply-chain` — 9 briefings
- **Largest single confirmed drain tracked:** Altura ~$39M (2026-07-04); largest systemic exposure: Aptos MoveVM $70B theoretical (patched, disclosed 2026-07-05)
- **Total Q2 2026 aggregate losses (context):** ~$755M across 83 incidents; YTD 2026 ~$972M

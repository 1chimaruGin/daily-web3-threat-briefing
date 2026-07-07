# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-07](briefings/2026-07-07.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG disclosure puts thousands of software wallets at risk | Summer.fi $6M, Ill Bloom $5M cumulative | flash-loan, logic-error, key-management | ~$11M new; ~$51M ongoing |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains Jul 5–6; IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets comprehensive JFrog autopsy; ResupplyFi ERC-4626 post-mortem now public | IronWorm npm worm (37 pkgs), ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new; ~$51M ongoing |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion bug that threatened $70B; SlowMist warns AI IDE markdown injection executes on Open Folder | Hexens/Aptos MoveVM (patched), SlowMist AI IDE injection, Miasma worm → Cosmos SDK | logic-error, supply-chain, key-management | n/a new drains; $70B theoretical (patched) |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier, depositors locked); CSA formalizes AI 'vibe-coded' Solidity as new CVE-surge driver | Altura $39M, LendFi $5.2M oracle manipulation | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 final report warns AI is driving "vulnerability apocalypse" | ResupplyFi $9.6M laundering, Kinto $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts | Edel Finance $403K, June 2026 wrap 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K confirmed drain |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and web3 dev creds | CVE-2026-48558 SimpleHelp RMM, GlassWorm macOS OpenVSX | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new confirmed drains; SecondFi/EMURGO white-hat identity disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO custody dispute, Sapphire Sleet 144 npm pkgs | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M in custody dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter with 83 hacks and $775M stolen | SecondFi $2.4M–$20M keygen flaw, JaredFromSubway MEV $7.5M Tornado Cash | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals | Polymarket $3M supply-chain injection, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing generalizable ZK witness-binding gap | DARKNAVY Aztec circuit autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB Chain | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs for first time | Q2 2026 record 83 incidents / $755M | access-control, key-management, bridge-dvn, price-manipulation | Q2 cumulative ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla CISA KEV | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain; 'abandoned-contract' pattern in 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalized | Quiet 24h window | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 | Unnamed 3-protocol bridge $127M (catch-up), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains | No new drains; EIP-7702 attack surface, Lazarus macOS kit | access-control, key-management, supply-chain, upgradeability | EIP-7702 cumulative ~$8M+ |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M, Syscoin Bridge ~$8M catch-up, Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict; ~$10.3M with catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17 | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M gross (~$139K net) |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026 | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains confirmed; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K forensics, AFI Protocol $480K catch-up | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M DPRK attribution, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

*(sorted by frequency — most briefings first)*

- **logic-error** — [2026-07-07](briefings/2026-07-07.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)
- **key-management** — [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-04](briefings/2026-07-04.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)
- **supply-chain** — [2026-07-06](briefings/2026-07-06.md), [2026-07-05](briefings/2026-07-05.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)
- **bridge-dvn** — [2026-07-04](briefings/2026-07-04.md), [2026-06-30](briefings/2026-06-30.md), [2026-06-29](briefings/2026-06-29.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)
- **access-control** — [2026-07-03](briefings/2026-07-03.md), [2026-07-01](briefings/2026-07-01.md), [2026-06-28](briefings/2026-06-28.md), [2026-06-27](briefings/2026-06-27.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)
- **flash-loan** — [2026-07-07](briefings/2026-07-07.md), [2026-07-06](briefings/2026-07-06.md), [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)
- **unverified-contract** — [2026-07-04](briefings/2026-07-04.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)
- **price-manipulation** — [2026-07-03](briefings/2026-07-03.md), [2026-07-02](briefings/2026-07-02.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)
- **upgradeability** — [2026-07-03](briefings/2026-07-03.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)
- **oracle-manipulation** — [2026-07-04](briefings/2026-07-04.md), [2026-06-25](briefings/2026-06-25.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)
- **rounding** — [2026-07-06](briefings/2026-07-06.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)
- **signature-replay** — [2026-06-14](briefings/2026-06-14.md)
- **integer-overflow** — [2026-06-15](briefings/2026-06-15.md)
- **dos** — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 25 (June 12 – July 7, 2026)
- **Date range:** 2026-06-12 → 2026-07-07 (26 calendar days; one gap: Jun 26)
- **Top 3 bug classes by frequency:**
  1. `logic-error` — 19 briefings
  2. `key-management` — 18 briefings
  3. `supply-chain` — 10 briefings
- **Largest single incident in window:** Altura ~$39M vault rug (2026-07-04)
- **Total confirmed losses within briefing window:** >$350M across covered incidents
- **Running July 2026 tally:** ~$6M (Summer.fi) + ongoing Altura $39M + ResupplyFi $9.6M

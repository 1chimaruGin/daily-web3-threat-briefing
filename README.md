# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-03](briefings/2026-07-03.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M through Tornado Cash; Immunefi Q2 final report warns AI is driving a "vulnerability apocalypse" behind record 83-exploit quarter. | ResupplyFi $9.6M ERC-4626 laundering, Kinto Protocol $1.55M proxy-backdoor | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance lost $403K to flash-loan wrapped-token exchange-rate manipulation; Chainalysis flags AI-accelerated attacks on unverified contracts losing $36.7M in H1. | Edel Finance $403K wGOOGLx flash-loan, June 2026 monthly wrap 45 incidents $75.87M | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets and web3 dev creds — CISA July 2 patch deadline. | CVE-2026-48558 SimpleHelp active exploitation, GlassWorm macOS, SecondFi update | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi's white-hat identity disputed as EMURGO denies knowing who secured $18.5M in ADA; Sapphire Sleet backdoors 144 Mastra npm packages. | SecondFi/EMURGO white-hat custody dispute, Sapphire Sleet 144 Mastra npm packages | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M ADA (disputed) |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 2026 closes as record quarter with 83 hacks and $775M stolen. | SecondFi $2.4M–$20M keygen flaw, JaredFromSubway $7.5M Tornado Cash movement | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M in supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO governance portals. | Polymarket $3M supply-chain frontend injection, CVE-2026-12866 expr-eval | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No confirmed new drains; DARKNAVY publishes definitive Aztec escapeHatch() circuit autopsy revealing generalizable ZK witness-binding gap. | DARKNAVY Aztec circuit autopsy (technique disclosure) | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge loses $1.7M after SGX signing key leaked to GitHub; LABUBU/OLPC pool drained $1.1M via token parameter desync on BNB Chain. | Taiko Bridge SGX key leak $1.7M, OLPC/LABUBU PancakeSwap $1.1M, mySwap CL $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing across major wallet UIs. | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs as leading attack class for first time. | Q2 2026 record 83 incidents / $755M (no new drains Jun 22–23) | access-control, key-management, bridge-dvn, price-manipulation | Q2 cumul. ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox post-mortem. | Namada MASP $600K (Jun 19 catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec's escapeHatch() autopsied — TurboVerifier accepts spoofed ZK public inputs enabling $2.21M drain; CVSS-10 Joomla JCE RCE in CISA KEV. | Aztec RollupProcessor $2.21M escapeHatch(), CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | No new 24h drain confirmed; "abandoned-contract" pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry formalizes the threat. | Abandoned-contract pattern; OWASP SC10:2026 (technique) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained June 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs June 18 — patch all blockchain tooling now. | Unnamed 3-protocol bridge $127M (catch-up Jun 14), Node.js HIGH CVEs Jun 18 | bridge-dvn, key-management, logic-error, dos | ~$127M (catch-up) |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ in real-world exploits; Lazarus 'Mach-O Man' macOS kit actively harvesting crypto team keychains. | EIP-7702 post-Pectra attack surfaces, Lazarus macOS Mach-O Man campaign | access-control, key-management, supply-chain, upgradeability | n/a |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect's deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today — patch all bots before going live. | Aztec Connect $2.1M ZK bypass, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$10.3M incl. catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to a flash-loan math flaw in a deprecated options vault; Node.js HIGH CVEs drop June 17 — patch before bots go live. | Thetanuts Finance $2.1M flash-loan / rounding flaw | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h window; Flooring Protocol's BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026. | Flooring Protocol ~$500K NFTs (catch-up Jun 8), Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new June 14 drains confirmed; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M across three platforms. | Alephium $815K bridge forensics, AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into generated test scaffolds. | Humanity Protocol $36M DPRK attribution, CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise. | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by number of briefings they appear in (most frequent first). Each date is a direct link.

**logic-error** (15 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md)

**key-management** (14 briefings) — [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [07-01](briefings/2026-07-01.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-19](briefings/2026-06-19.md), [06-18](briefings/2026-06-18.md), [06-17](briefings/2026-06-17.md), [06-13](briefings/2026-06-13.md), [06-12](briefings/2026-06-12.md)

**access-control** (10 briefings) — [07-03](briefings/2026-07-03.md), [07-01](briefings/2026-07-01.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-24](briefings/2026-06-24.md), [06-23](briefings/2026-06-23.md), [06-21](briefings/2026-06-21.md), [06-18](briefings/2026-06-18.md), [06-15](briefings/2026-06-15.md), [06-13](briefings/2026-06-13.md)

**bridge-dvn** (9 briefings) — [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-22](briefings/2026-06-22.md), [06-19](briefings/2026-06-19.md), [06-17](briefings/2026-06-17.md), [06-14](briefings/2026-06-14.md), [06-12](briefings/2026-06-12.md)

**supply-chain** (8 briefings) — [07-01](briefings/2026-07-01.md), [06-30](briefings/2026-06-30.md), [06-29](briefings/2026-06-29.md), [06-28](briefings/2026-06-28.md), [06-27](briefings/2026-06-27.md), [06-18](briefings/2026-06-18.md), [06-17](briefings/2026-06-17.md), [06-13](briefings/2026-06-13.md)

**unverified-contract** (5 briefings) — [07-02](briefings/2026-07-02.md), [06-24](briefings/2026-06-24.md), [06-21](briefings/2026-06-21.md), [06-20](briefings/2026-06-20.md), [06-12](briefings/2026-06-12.md)

**price-manipulation** (5 briefings) — [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [06-25](briefings/2026-06-25.md), [06-23](briefings/2026-06-23.md), [06-22](briefings/2026-06-22.md)

**flash-loan** (4 briefings) — [07-03](briefings/2026-07-03.md), [07-02](briefings/2026-07-02.md), [06-16](briefings/2026-06-16.md), [06-12](briefings/2026-06-12.md)

**upgradeability** (4 briefings) — [07-03](briefings/2026-07-03.md), [06-20](briefings/2026-06-20.md), [06-18](briefings/2026-06-18.md), [06-13](briefings/2026-06-13.md)

**oracle-manipulation** (3 briefings) — [06-25](briefings/2026-06-25.md), [06-22](briefings/2026-06-22.md), [06-20](briefings/2026-06-20.md)

**rounding** (2 briefings) — [06-16](briefings/2026-06-16.md), [06-15](briefings/2026-06-15.md)

**dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

**integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

**signature-replay** (1 briefing) — [06-14](briefings/2026-06-14.md)

---

## 📊 Stats

- **Total briefings:** 21
- **Date range:** 2026-06-12 → 2026-07-03 (22 calendar days; one gap: June 26)
- **Top 3 bug classes:** `logic-error` (15 briefings) · `key-management` (14) · `access-control` (10)
- **Largest single incident documented:** Drift Protocol $280M (social engineering / key-management) — see [06-23](briefings/2026-06-23.md)
- **Q2 2026 aggregate covered:** ~$755M across 83 incidents — worst quarter on record

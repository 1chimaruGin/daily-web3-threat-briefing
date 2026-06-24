# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.

**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.

**Latest briefing:** [2026-06-24](briefings/2026-06-24.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw enables on-chain identity spoofing | JaredFromSubway MEV honeypot $15M, ENS lookalike display flaw | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time quarterly record — 83 incidents, $755M lost; access-control exploits overtake smart-contract bugs for first time | Q2 2026 record 83 incidents / $755M (no new drains Jun 22–23) | access-control, key-management, bridge-dvn, price-manipulation | n/a (Q2 ~$755M) |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain masked by stale indexer; VWAP thin-liquidity oracle attack class detailed | Namada MASP $600K (Jun 19 catch-up) | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier accepts spoofed ZK inputs enabling $2.21M drain; Joomla JCE CVSS-10 RCE in CISA KEV | Aztec RollupProcessor $2.21M, CVE-2026-48907 Joomla JCE | access-control, logic-error, unverified-contract | n/a (no new Jun 20–21) |
| [2026-06-20](briefings/2026-06-20.md) | Quiet 24h; 'abandoned-contract' pattern accounts for 4 of June's 16 incidents; OWASP SC10:2026 proxy-upgradeability entry published | (no new drains Jun 19–20) | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass; Node.js drops 2 HIGH CVEs Jun 18 | Unnamed 3-protocol bridge $127M (BridgeLink $52M / CrossFlow $48M / Relay $27M), Node.js HIGH CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized with $8M+ real exploits; Lazarus 'Mach-O Man' macOS kit harvesting crypto team keychains | (no new drains Jun 17–18); EIP-7702 $8M+ cumulative | access-control, key-management, supply-chain, upgradeability | n/a (EIP-7702 ~$8M+) |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup loses $2.1M to L1/L2 proof-boundary bypass; Node.js HIGH CVE drops | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up), Node.js HIGH CVE | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M (strict); ~$10.3M with catch-up |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance loses $2.1M to flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs dropping Jun 17 | Thetanuts Finance $2.1M (flash-loan/rounding) | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet 24h; Flooring Protocol's BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent memory poisoning claimed $45M across 2026 | Flooring Protocol ~$500K NFTs, Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M |
| [2026-06-14](briefings/2026-06-14.md) | No new Jun 14 drains; Alephium's forged-VAA bridge-DVN kill chain detailed; Aave raises max bug bounty to $5M | Alephium $815K, AFI Protocol $480K (catch-up) | bridge-dvn, signature-replay, logic-error | ~$1.3M |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp pins Humanity Protocol's $36M breach on DPRK phishing chain; OpenZeppelin Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M (DPRK attribution), CVE-2026-48054 OZ Wizard | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge loses $5.4M to validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, NovaBox $107K, Ambient Finance $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Tags sorted by number of briefings they appear in (most frequent first). Click a date to jump to that day's full analysis.

**logic-error** (10 briefings) — [2026-06-24](briefings/2026-06-24.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**bridge-dvn** (6 briefings) — [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-14](briefings/2026-06-14.md), [2026-06-12](briefings/2026-06-12.md)

**access-control** (6 briefings) — [2026-06-24](briefings/2026-06-24.md), [2026-06-23](briefings/2026-06-23.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-15](briefings/2026-06-15.md), [2026-06-13](briefings/2026-06-13.md)

**key-management** (6 briefings) — [2026-06-23](briefings/2026-06-23.md), [2026-06-19](briefings/2026-06-19.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md), [2026-06-12](briefings/2026-06-12.md)

**unverified-contract** (4 briefings) — [2026-06-24](briefings/2026-06-24.md), [2026-06-21](briefings/2026-06-21.md), [2026-06-20](briefings/2026-06-20.md), [2026-06-12](briefings/2026-06-12.md)

**supply-chain** (3 briefings) — [2026-06-18](briefings/2026-06-18.md), [2026-06-17](briefings/2026-06-17.md), [2026-06-13](briefings/2026-06-13.md)

**upgradeability** (3 briefings) — [2026-06-20](briefings/2026-06-20.md), [2026-06-18](briefings/2026-06-18.md), [2026-06-13](briefings/2026-06-13.md)

**flash-loan** (2 briefings) — [2026-06-16](briefings/2026-06-16.md), [2026-06-12](briefings/2026-06-12.md)

**oracle-manipulation** (2 briefings) — [2026-06-22](briefings/2026-06-22.md), [2026-06-20](briefings/2026-06-20.md)

**price-manipulation** (2 briefings) — [2026-06-23](briefings/2026-06-23.md), [2026-06-22](briefings/2026-06-22.md)

**rounding** (2 briefings) — [2026-06-16](briefings/2026-06-16.md), [2026-06-15](briefings/2026-06-15.md)

**integer-overflow** (1 briefing) — [2026-06-15](briefings/2026-06-15.md)

**signature-replay** (1 briefing) — [2026-06-14](briefings/2026-06-14.md)

**dos** (1 briefing) — [2026-06-19](briefings/2026-06-19.md)

---

## 📊 Stats

- **Total briefings:** 13
- **Date range:** 2026-06-12 → 2026-06-24
- **Top bug classes by briefing count:**
  1. `logic-error` — 10 of 13 briefings (77%)
  2. `bridge-dvn`, `access-control`, `key-management` — 6 of 13 briefings each (46%)
- **Total confirmed $ at risk (named incidents only):** ~$199M+ across the series
- **Chains covered:** Ethereum, Solana, BNB, Sui, Cosmos, Arbitrum, Polygon, Alephium, Syscoin, cross-chain bridges

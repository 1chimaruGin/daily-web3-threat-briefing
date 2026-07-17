# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-17](briefings/2026-07-17.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|------|-------|-----------|-------------|-----------|
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain) drained $1.34M on Arbitrum; third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key on Arbitrum; third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 shuts down after proxy-backdoor exploit; GMX V1 hacker returns $37M keeping $5M bounty | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 web3.py SSRF via EIP-3668 CCIP Read fully disclosed; no new on-chain drain; six situations ongoing | BonkDAO $20M, Bonzo Lend $9M, GMX V1 $5M, Altura $39M | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 at $298M; BonkDAO launders $19M into BONK 2.0 DAO | BonkDAO $20M (laundering), Bonzo Lend $9M (Supra fix) | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M ongoing |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) $9M — 12-orders-of-magnitude oracle price manipulation via zeroed BLS signature | Bonzo Lend $9M, Ill Bloom $5M+ | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new; ~$75M ongoing |
| [2026-07-11](briefings/2026-07-11.md) | No new drain; GMX V1 $44M comp plan advances; OZ Wizard CVE-2026-48054 supply-chain risk day 28 | GMX V1, BonkDAO, Altura, Summer.fi, ResupplyFi (ongoing) | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M net unrecovered |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned funds for $5M bounty | GMX V1 $42M, Kinto $1.55M, BonkDAO $20M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M |
| [2026-07-09](briefings/2026-07-09.md) | No new major drain; CertiK H1 2026 flags wallet compromise as #1 loss vector ($444M); Summer.fi laundered | Summer.fi, BonkDAO (ongoing) | key-management, flash-loan, access-control, logic-error | ~$75M ongoing |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; Ethereum trader loses $2M to same-block MEV backrun | BonkDAO $20M, MEV backrun $2M | access-control, logic-error, front-running | ~$22M |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi $6M FleetCommander vault exploit; Ill Bloom PRNG disclosure puts thousands of wallets at risk | Summer.fi $6M, Ill Bloom $5M | flash-loan, logic-error, key-management | ~$11M new; ~$51M ongoing |
| [2026-07-06](briefings/2026-07-06.md) | No new on-chain drains; IronWorm Rust npm worm autopsy (eBPF rootkit + Tor C2); ResupplyFi post-mortem public | IronWorm 37 packages, ResupplyFi post-mortem | supply-chain, flash-loan, rounding, key-management | n/a new drains |
| [2026-07-05](briefings/2026-07-05.md) | Hexens discloses patched Aptos MoveVM type-confusion threatening $70B; SlowMist AI IDE markdown injection | Aptos MoveVM $70B systemic (patched), SlowMist AI IDE | logic-error, supply-chain, key-management | n/a new drains |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug (COO-tied DVN verifier); CSA formalizes AI vibe-coded Solidity as CVE-surge driver | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2 final warns AI driving vulnerability apocalypse | ResupplyFi $9.6M, Kinto $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M new |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token rate manipulation; AI-accelerated attacks on unverified contracts | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests crypto wallets | CVE-2026-48558 SimpleHelp RMM | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | No new drains; SecondFi white-hat custody disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi $18.5M (dispute), Sapphire Sleet npm | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M custody dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano keygen flaw drains $2.4M ($20M at risk); Q2 2026 closes as record quarter: 83 hacks, $775M | SecondFi $2.4M–$20M, Q2 record close | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new; Q2 $775M |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket $3M supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE threatens DAO portals | Polymarket $3M, CVE-2026-12866 | supply-chain, key-management, logic-error, access-control | ~$3M |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes definitive Aztec escapeHatch() ZK circuit autopsy | DARKNAVY Aztec ZK circuit autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko Bridge SGX key leak $1.7M; LABUBU/OLPC pool $1.1M token desync on BNB; mySwap Starknet $305K | Taiko $1.7M, OLPC $1.1M, mySwap $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike flaw in major wallet UIs | JaredFromSubway MEV $15M, ENS lookalike | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 sets all-time record: 83 incidents, $755M; access-control overtakes smart-contract bugs as #1 class | Q2 record 83 incidents $755M | access-control, key-management, bridge-dvn, price-manipulation | ~$755M Q2 cumulative |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain; VWAP thin-liquidity oracle attack class detailed via BlockSec YieldBlox | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() TurboVerifier spoofed ZK public inputs $2.21M; Joomla JCE CVSS-10 in CISA KEV | Aztec $2.21M (technical analysis) | access-control, logic-error, unverified-contract | n/a new |
| [2026-06-20](briefings/2026-06-20.md) | Quiet window; abandoned-contract pattern in 4 of June's 16 incidents; OWASP SC10:2026 upgradeability entry | Quiet 24h | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained via dual validator+finality bypass (Jun 14); Node.js 2 HIGH CVEs | Unnamed bridge $127M (catch-up Jun 14), Node.js CVEs | bridge-dvn, key-management, logic-error, dos | ~$127M catch-up |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ real exploits); Lazarus Mach-O Man macOS kit active | EIP-7702 cumulative $8M+, Lazarus macOS | access-control, key-management, supply-chain, upgradeability | ~$8M+ EIP-7702 cumulative |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect deprecated ZK-rollup $2.1M L1/L2 proof-boundary bypass; Syscoin Bridge $8M SPV forgery | Aztec Connect $2.1M, Syscoin Bridge $8M | logic-error, bridge-dvn, supply-chain, key-management | ~$10.3M |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs drop June 17 | Thetanuts $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain; AI agent $45M claim | Flooring Protocol ~$500K, Unleash Protocol $3.9M | integer-overflow, rounding, logic-error, access-control | ~$4.4M catch-up |
| [2026-06-14](briefings/2026-06-14.md) | No new drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K (forensics), AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M catch-up |
| [2026-06-13](briefings/2026-06-13.md) | Humanity Protocol $36M breach pinned on DPRK phishing; OZ Wizard CVE-2026-48054 injects code into test scaffolds | Humanity Protocol $36M, CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium $1.34M fake LP tokens on Solana; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by number of briefings each class appears in (most frequent first). Click a date to read that day's full write-up.

**key-management** (25 briefings) — [06-12](briefings/2026-06-12.md), [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-19](briefings/2026-06-19.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md)

**logic-error** (25 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-22](briefings/2026-06-22.md), [06-24](briefings/2026-06-24.md), [06-25](briefings/2026-06-25.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md), [07-05](briefings/2026-07-05.md), [07-07](briefings/2026-07-07.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md)

**access-control** (19 briefings) — [06-13](briefings/2026-06-13.md), [06-15](briefings/2026-06-15.md), [06-18](briefings/2026-06-18.md), [06-21](briefings/2026-06-21.md), [06-23](briefings/2026-06-23.md), [06-24](briefings/2026-06-24.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [07-01](briefings/2026-07-01.md), [07-03](briefings/2026-07-03.md), [07-08](briefings/2026-07-08.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md)

**supply-chain** (14 briefings) — [06-13](briefings/2026-06-13.md), [06-17](briefings/2026-06-17.md), [06-18](briefings/2026-06-18.md), [06-27](briefings/2026-06-27.md), [06-28](briefings/2026-06-28.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-01](briefings/2026-07-01.md), [07-05](briefings/2026-07-05.md), [07-06](briefings/2026-07-06.md), [07-11](briefings/2026-07-11.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md)

**flash-loan** (12 briefings) — [06-12](briefings/2026-06-12.md), [06-16](briefings/2026-06-16.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-06](briefings/2026-07-06.md), [07-07](briefings/2026-07-07.md), [07-09](briefings/2026-07-09.md), [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-12](briefings/2026-07-12.md), [07-14](briefings/2026-07-14.md), [07-17](briefings/2026-07-17.md)

**oracle-manipulation** (10 briefings) — [06-20](briefings/2026-06-20.md), [06-22](briefings/2026-06-22.md), [06-25](briefings/2026-06-25.md), [07-04](briefings/2026-07-04.md), [07-12](briefings/2026-07-12.md), [07-13](briefings/2026-07-13.md), [07-14](briefings/2026-07-14.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md), [07-17](briefings/2026-07-17.md)

**bridge-dvn** (10 briefings) — [06-12](briefings/2026-06-12.md), [06-14](briefings/2026-06-14.md), [06-17](briefings/2026-06-17.md), [06-19](briefings/2026-06-19.md), [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [06-29](briefings/2026-06-29.md), [06-30](briefings/2026-06-30.md), [07-04](briefings/2026-07-04.md)

**price-manipulation** (7 briefings) — [06-22](briefings/2026-06-22.md), [06-23](briefings/2026-06-23.md), [06-25](briefings/2026-06-25.md), [07-02](briefings/2026-07-02.md), [07-03](briefings/2026-07-03.md), [07-12](briefings/2026-07-12.md), [07-16](briefings/2026-07-16.md)

**upgradeability** (6 briefings) — [06-13](briefings/2026-06-13.md), [06-18](briefings/2026-06-18.md), [06-20](briefings/2026-06-20.md), [07-03](briefings/2026-07-03.md), [07-15](briefings/2026-07-15.md), [07-16](briefings/2026-07-16.md)

**unverified-contract** (6 briefings) — [06-12](briefings/2026-06-12.md), [06-20](briefings/2026-06-20.md), [06-21](briefings/2026-06-21.md), [06-24](briefings/2026-06-24.md), [07-02](briefings/2026-07-02.md), [07-04](briefings/2026-07-04.md)

**reentrancy** (3 briefings) — [07-10](briefings/2026-07-10.md), [07-11](briefings/2026-07-11.md), [07-15](briefings/2026-07-15.md)

**rounding** (3 briefings) — [06-15](briefings/2026-06-15.md), [06-16](briefings/2026-06-16.md), [07-06](briefings/2026-07-06.md)

**front-running** (1 briefing) — [07-08](briefings/2026-07-08.md)

**dos** (1 briefing) — [06-19](briefings/2026-06-19.md)

**signature-replay** (1 briefing) — [06-14](briefings/2026-06-14.md)

**integer-overflow** (1 briefing) — [06-15](briefings/2026-06-15.md)

---

## 📊 Stats

- **Total briefings:** 35
- **Date range:** 2026-06-12 → 2026-07-17 (35 days covered; one gap: 2026-06-26)
- **Top 3 most-frequent bug classes:**
  1. `key-management` — 25 briefings (71%)
  2. `logic-error` — 25 briefings (71%)
  3. `access-control` — 19 briefings (54%)
- **Largest single-day incident reported:** Unnamed 3-protocol bridge $127M ([2026-06-19](briefings/2026-06-19.md))
- **Most active attack chain:** Ethereum / Arbitrum (EVM) — present in virtually every briefing
- **Defining trend (mid-July 2026):** Oracle-class attacks — three exploits in five days (Bonzo Lend, Ostium, Cascade), $28M+ drained. Key theft + absent timestamp/plausibility bounding are the common thread.

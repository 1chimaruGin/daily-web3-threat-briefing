# 🛡️ Daily Web3 Threat Briefings

Automated daily security intelligence for blockchain / smart-contract bug bounty hunting. Generated every day at 11:00 JST.
**Scope:** EVM/Solidity · Solana/Rust · Cosmos/Move · cross-chain bridges — DeFi-prioritized.
**Latest briefing:** [2026-07-27](briefings/2026-07-27.md)

---

## 📅 Index (newest first)

| Date | TL;DR | Incidents | Bug classes | $ at risk |
|---|---|---|---|---|
| [2026-07-27](briefings/2026-07-27.md) | Triple-A losses revised to $12M; CertiK reports $124M in physical 'wrench attacks' in H1 2026 | Triple-A $12M (updated) | key-management, unverified-contract, access-control | ~$12M new; ~$208M MTD |
| [2026-07-26](briefings/2026-07-26.md) | Triple-A payment gateway loses $9.7M across 6 chains; Chainalysis Drift $285M durable-nonce post-mortem | Triple-A $9.7M | key-management, access-control | ~$9.7M new; ~$206M MTD |
| [2026-07-25](briefings/2026-07-25.md) | Lien Finance $542K via permissionless bond registration flaw; Injective npm advisory active | Lien Finance $542K | logic-error, price-manipulation, supply-chain | ~$542K new; ~$196M MTD |
| [2026-07-24](briefings/2026-07-24.md) | AFX Trade bridge drained $24.15M (validator keys); three simultaneous exploits = $35.55M on Jul 23 | AFX Trade $24.15M, Verus ETH bridge ~$7.4M, B² Network ~$4M | key-management, bridge-dvn | ~$35.55M new; ~$195M MTD |
| [2026-07-23](briefings/2026-07-23.md) | 42DAO BLC stablecoin depegged 99% via BTCB oracle manipulation on BNB Chain | 42DAO BLC $915K | oracle-manipulation, price-manipulation, key-management, bridge-dvn | ~$915K new; ~$159M MTD |
| [2026-07-22](briefings/2026-07-22.md) | Wanchain Cardano-BNB bridge drained $10–13M via signature amplification flaw (1 sig → 65,000×) | Wanchain Bridge $10–13M NIGHT | signature-replay, bridge-dvn, key-management | ~$10–13M new; ~$158M MTD |
| [2026-07-21](briefings/2026-07-21.md) | Allbridge Core drained $1.65M via Solana flash-loan pool-ratio attack (same bug as 2023 partial fix) | Allbridge Core $1.65M | flash-loan, price-manipulation, logic-error | ~$1.65M new; ~$148M MTD |
| [2026-07-20](briefings/2026-07-20.md) | PETS 2026 wallet-extension PoC code live (35M users); CoinDCX post-mortem: 6-day dwell, employee arrested | CoinDCX $44M post-mortem | key-management, supply-chain, bridge-dvn, logic-error | ~$147M MTD |
| [2026-07-19](briefings/2026-07-19.md) | SlowMist: macOS infostealer swaps Ledger/Trezor with fakes; PETS 2026 wallet-extension paper published | macOS wallet-replacement infostealer | key-management, supply-chain, logic-error | ~$5M+ Ill Bloom; $147M MTD |
| [2026-07-18](briefings/2026-07-18.md) | CoinDCX loses $44M to employee-malware key theft; Across Protocol Solana bridge relayer attacked | CoinDCX $44M, Across Protocol (TBD), DeFiTuna $580K, BigONE $27M | key-management, supply-chain, bridge-dvn, logic-error | ~$72M+ new |
| [2026-07-17](briefings/2026-07-17.md) | Cascade (Polychain-backed) drained $1.34M on Arbitrum — third Arbitrum perp hack in one week | Cascade $1.34M | access-control, logic-error, oracle-manipulation, key-management, flash-loan | ~$1.34M new; ~$100M tracked |
| [2026-07-16](briefings/2026-07-16.md) | Ostium Perp DEX loses $18–22M to compromised oracle signer key — third oracle attack in five days | Ostium $18–22M | key-management, oracle-manipulation, price-manipulation, access-control, upgradeability | ~$98M tracked |
| [2026-07-15](briefings/2026-07-15.md) | Kinto L2 announces full shutdown after proxy-backdoor exploit; GMX V1 hacker returns $37M | Kinto shutdown, GMX V1 partial recovery | upgradeability, reentrancy, access-control, oracle-manipulation, supply-chain | ~$80M tracked |
| [2026-07-14](briefings/2026-07-14.md) | CVE-2026-40072 web3.py SSRF via EIP-3668 CCIP Read fully disclosed; 6 incidents ongoing | CVE-2026-40072 web3.py SSRF | oracle-manipulation, access-control, logic-error, supply-chain, flash-loan | ~$78M tracked |
| [2026-07-13](briefings/2026-07-13.md) | SlowMist H1 2026: 182 incidents, supply-chain #1 at $298M; BonkDAO attacker launders $19M | BonkDAO $20M (laundering), Bonzo Lend $9M | oracle-manipulation, access-control, logic-error, key-management, supply-chain | ~$75M tracked |
| [2026-07-12](briefings/2026-07-12.md) | Bonzo Lend (Hedera) drained $9M via 12-orders-of-magnitude oracle price manipulation | Bonzo Lend $9M | oracle-manipulation, price-manipulation, key-management, flash-loan | ~$14M new; ~$75M tracked |
| [2026-07-11](briefings/2026-07-11.md) | GMX V1 compensation plan advances as $37M returned; OZ Wizard CVE-2026-48054 day 28 | GMX V1 $42M (recovery) | reentrancy, flash-loan, access-control, logic-error, supply-chain | ~$75M tracked |
| [2026-07-10](briefings/2026-07-10.md) | GMX V1 GLP pool drained $42M via keeper-reentrancy on Arbitrum; attacker returned for $5M bounty | GMX V1 $42M | reentrancy, flash-loan, access-control, logic-error, key-management | ~$107M tracked |
| [2026-07-09](briefings/2026-07-09.md) | CertiK H1 2026: wallet compromise is #1 loss vector ($444M); Summer.fi laundering via Tornado Cash | Summer.fi (ongoing), BonkDAO (ongoing) | key-management, flash-loan, access-control, logic-error | ~$75M tracked |
| [2026-07-08](briefings/2026-07-08.md) | BonkDAO loses $20M to $4M governance buyout on Solana; MEV backrun drains $2M via illiquid Uni v3 | BonkDAO $20M, ETH MEV backrun $2M | access-control, logic-error, front-running | ~$22M new |
| [2026-07-07](briefings/2026-07-07.md) | Summer.fi loses $6M to FleetCommander vault accounting exploit; Ill Bloom PRNG threatens software wallets | Summer.fi $6M, Ill Bloom PRNG $5M+ | flash-loan, logic-error, key-management | ~$11M new; ~$51M ongoing |
| [2026-07-06](briefings/2026-07-06.md) | IronWorm Rust npm worm (eBPF rootkit + Tor C2) gets JFrog autopsy; ResupplyFi post-mortem public | IronWorm npm (37 packages) | supply-chain, flash-loan, rounding, key-management | n/a new drains |
| [2026-07-05](briefings/2026-07-05.md) | Hexens: patched Aptos MoveVM type-confusion threatened $70B; SlowMist: AI IDE markdown injection | Hexens/Aptos MoveVM (patched), AI IDE markdown injection | logic-error, supply-chain, key-management | n/a new; $70B theoretical (patched) |
| [2026-07-04](briefings/2026-07-04.md) | Altura $39M gold-vault rug via COO-tied DVN verifier; CSA formalizes AI 'vibe-coded' Solidity risk | Altura $39M, LendFi $5.2M | key-management, bridge-dvn, oracle-manipulation, logic-error, unverified-contract | ~$44M new |
| [2026-07-03](briefings/2026-07-03.md) | ResupplyFi attacker launders $6.5M via Tornado Cash; Immunefi Q2 warns of AI "vulnerability apocalypse" | ResupplyFi $9.6M (laundering), Kinto Protocol $1.55M | flash-loan, price-manipulation, upgradeability, access-control, key-management | ~$11.15M new |
| [2026-07-02](briefings/2026-07-02.md) | Edel Finance $403K flash-loan wrapped-token exchange-rate attack; Chainalysis: $36.7M from unverified contracts | Edel Finance $403K | flash-loan, price-manipulation, unverified-contract, key-management | ~$403K new |
| [2026-07-01](briefings/2026-07-01.md) | CVE-2026-48558 (CVSS 10.0) SimpleHelp RMM exploited in-the-wild; Djinn Stealer harvests dev wallets | CVE-2026-48558, Djinn Stealer | key-management, supply-chain, access-control | n/a new drains |
| [2026-06-30](briefings/2026-06-30.md) | SecondFi white-hat custody disputed; Sapphire Sleet backdoors 144 Mastra npm packages | SecondFi/EMURGO dispute, Sapphire Sleet 144 npm | key-management, supply-chain, logic-error, bridge-dvn | ~$18.5M in custody dispute |
| [2026-06-29](briefings/2026-06-29.md) | SecondFi Cardano wallet keygen flaw drains $2.4M (up to $20M at risk); Q2 record: 83 hacks, $775M | SecondFi $2.4M–$20M | key-management, supply-chain, bridge-dvn, logic-error | ~$22.5M new; $775M Q2 |
| [2026-06-28](briefings/2026-06-28.md) | Polymarket loses $3M to supply-chain frontend injection; expr-eval CVE-2026-12866 CVSS-9.8 RCE | Polymarket $3M, CVE-2026-12866 | supply-chain, key-management, logic-error, access-control | ~$3M new |
| [2026-06-27](briefings/2026-06-27.md) | No new drains; DARKNAVY publishes Aztec escapeHatch() circuit autopsy revealing ZK witness-binding gap | DARKNAVY Aztec circuit autopsy | logic-error, access-control, supply-chain, key-management | n/a |
| [2026-06-25](briefings/2026-06-25.md) | Taiko L2 bridge $1.7M via SGX key leaked to GitHub; LABUBU/OLPC pool $1.1M via param desync | Taiko Bridge $1.7M, OLPC/LABUBU $1.1M, mySwap $305K | key-management, bridge-dvn, price-manipulation, oracle-manipulation, logic-error | ~$3.1M new |
| [2026-06-24](briefings/2026-06-24.md) | JaredFromSubway MEV bot drained $15M via counter-MEV honeypot; ENS lookalike identity spoofing | JaredFromSubway MEV $15M | logic-error, unverified-contract, access-control | ~$15M |
| [2026-06-23](briefings/2026-06-23.md) | Q2 2026 all-time record: 83 incidents, $755M; access-control overtakes smart-contract bugs as #1 class | Q2 2026 record | access-control, key-management, bridge-dvn, price-manipulation | Q2 ~$755M |
| [2026-06-22](briefings/2026-06-22.md) | Namada MASP $600K IBC logic drain; VWAP thin-liquidity oracle attack class via BlockSec YieldBlox post-mortem | Namada MASP $600K | logic-error, bridge-dvn, oracle-manipulation, price-manipulation | ~$600K |
| [2026-06-21](briefings/2026-06-21.md) | Aztec escapeHatch() autopsied — TurboVerifier spoof enables $2.21M drain; Joomla JCE CVSS-10 in KEV | Aztec $2.21M, CVE-2026-48907 Joomla | access-control, logic-error, unverified-contract | ~$2.21M |
| [2026-06-20](briefings/2026-06-20.md) | No new drain; 'abandoned-contract' pattern = 4 of June's 16 incidents; OWASP SC10:2026 proxy entry | Quiet window | unverified-contract, logic-error, upgradeability, oracle-manipulation | n/a |
| [2026-06-19](briefings/2026-06-19.md) | $127M cross-chain bridge drained Jun 14 via dual validator+finality bypass (catch-up); Node.js HIGH CVEs | Unnamed 3-protocol bridge $127M | bridge-dvn, key-management, logic-error, dos | ~$127M (catch-up) |
| [2026-06-18](briefings/2026-06-18.md) | EIP-7702 post-Pectra attack surfaces formalized ($8M+ real exploits); Lazarus Mach-O Man macOS kit | EIP-7702 cumulative $8M+ | access-control, key-management, supply-chain, upgradeability | ~$8M+ cumulative |
| [2026-06-17](briefings/2026-06-17.md) | Aztec Connect ZK-rollup $2.1M L1/L2 proof-boundary bypass; Node.js HIGH CVE drops today | Aztec Connect $2.1M, Syscoin Bridge ~$8M (catch-up) | logic-error, bridge-dvn, supply-chain, key-management | ~$2.1M strict window |
| [2026-06-16](briefings/2026-06-16.md) | Thetanuts Finance $2.1M flash-loan math flaw in deprecated options vault; Node.js HIGH CVEs incoming | Thetanuts Finance $2.1M | flash-loan, rounding, logic-error | ~$2.1M |
| [2026-06-15](briefings/2026-06-15.md) | Quiet window; Flooring Protocol BT404 packed-storage underflow enables phantom-balance NFT drain | Flooring Protocol ~$500K, Unleash Protocol $3.9M (catch-up) | integer-overflow, rounding, logic-error, access-control | ~$4.4M (catch-up) |
| [2026-06-14](briefings/2026-06-14.md) | No new drains; Alephium forged-VAA bridge-DVN kill chain detailed; Aave raises max bounty to $5M | Alephium $815K, AFI Protocol $480K | bridge-dvn, signature-replay, logic-error | ~$1.3M (catch-up) |
| [2026-06-13](briefings/2026-06-13.md) | Quantstamp attributes Humanity Protocol $36M to DPRK phishing; OZ Wizard CVE-2026-48054 code injection | Humanity Protocol $36M (DPRK), CVE-2026-48054 | key-management, upgradeability, access-control, supply-chain | ~$36M |
| [2026-06-12](briefings/2026-06-12.md) | Raydium drains $1.34M via fake LP tokens on legacy Solana pools; Gravity Bridge $5.4M validator key compromise | Raydium $1.34M, Gravity Bridge $5.4M, Haedal $915K, Ambient $110K | flash-loan, logic-error, key-management, bridge-dvn, unverified-contract | ~$7.9M |

---

## 🏷️ Browse by bug class

Sorted by frequency (most briefings first). Each date links to that day's briefing.

- **key-management** (32 briefings) — [Jun 12](briefings/2026-06-12.md), [Jun 13](briefings/2026-06-13.md), [Jun 17](briefings/2026-06-17.md), [Jun 18](briefings/2026-06-18.md), [Jun 19](briefings/2026-06-19.md), [Jun 23](briefings/2026-06-23.md), [Jun 25](briefings/2026-06-25.md), [Jun 27](briefings/2026-06-27.md), [Jun 28](briefings/2026-06-28.md), [Jun 29](briefings/2026-06-29.md), [Jun 30](briefings/2026-06-30.md), [Jul 1](briefings/2026-07-01.md), [Jul 2](briefings/2026-07-02.md), [Jul 3](briefings/2026-07-03.md), [Jul 4](briefings/2026-07-04.md), [Jul 5](briefings/2026-07-05.md), [Jul 6](briefings/2026-07-06.md), [Jul 7](briefings/2026-07-07.md), [Jul 9](briefings/2026-07-09.md), [Jul 10](briefings/2026-07-10.md), [Jul 12](briefings/2026-07-12.md), [Jul 13](briefings/2026-07-13.md), [Jul 16](briefings/2026-07-16.md), [Jul 17](briefings/2026-07-17.md), [Jul 18](briefings/2026-07-18.md), [Jul 19](briefings/2026-07-19.md), [Jul 20](briefings/2026-07-20.md), [Jul 22](briefings/2026-07-22.md), [Jul 23](briefings/2026-07-23.md), [Jul 24](briefings/2026-07-24.md), [Jul 26](briefings/2026-07-26.md), [Jul 27](briefings/2026-07-27.md)

- **logic-error** (30 briefings) — [Jun 12](briefings/2026-06-12.md), [Jun 14](briefings/2026-06-14.md), [Jun 15](briefings/2026-06-15.md), [Jun 16](briefings/2026-06-16.md), [Jun 17](briefings/2026-06-17.md), [Jun 19](briefings/2026-06-19.md), [Jun 20](briefings/2026-06-20.md), [Jun 21](briefings/2026-06-21.md), [Jun 22](briefings/2026-06-22.md), [Jun 24](briefings/2026-06-24.md), [Jun 25](briefings/2026-06-25.md), [Jun 27](briefings/2026-06-27.md), [Jun 28](briefings/2026-06-28.md), [Jun 29](briefings/2026-06-29.md), [Jun 30](briefings/2026-06-30.md), [Jul 4](briefings/2026-07-04.md), [Jul 5](briefings/2026-07-05.md), [Jul 7](briefings/2026-07-07.md), [Jul 8](briefings/2026-07-08.md), [Jul 9](briefings/2026-07-09.md), [Jul 10](briefings/2026-07-10.md), [Jul 11](briefings/2026-07-11.md), [Jul 13](briefings/2026-07-13.md), [Jul 14](briefings/2026-07-14.md), [Jul 17](briefings/2026-07-17.md), [Jul 18](briefings/2026-07-18.md), [Jul 19](briefings/2026-07-19.md), [Jul 20](briefings/2026-07-20.md), [Jul 21](briefings/2026-07-21.md), [Jul 25](briefings/2026-07-25.md)

- **access-control** (21 briefings) — [Jun 13](briefings/2026-06-13.md), [Jun 15](briefings/2026-06-15.md), [Jun 18](briefings/2026-06-18.md), [Jun 21](briefings/2026-06-21.md), [Jun 23](briefings/2026-06-23.md), [Jun 24](briefings/2026-06-24.md), [Jun 27](briefings/2026-06-27.md), [Jun 28](briefings/2026-06-28.md), [Jul 1](briefings/2026-07-01.md), [Jul 3](briefings/2026-07-03.md), [Jul 8](briefings/2026-07-08.md), [Jul 9](briefings/2026-07-09.md), [Jul 10](briefings/2026-07-10.md), [Jul 11](briefings/2026-07-11.md), [Jul 13](briefings/2026-07-13.md), [Jul 14](briefings/2026-07-14.md), [Jul 15](briefings/2026-07-15.md), [Jul 16](briefings/2026-07-16.md), [Jul 17](briefings/2026-07-17.md), [Jul 26](briefings/2026-07-26.md), [Jul 27](briefings/2026-07-27.md)

- **supply-chain** (18 briefings) — [Jun 13](briefings/2026-06-13.md), [Jun 17](briefings/2026-06-17.md), [Jun 18](briefings/2026-06-18.md), [Jun 27](briefings/2026-06-27.md), [Jun 28](briefings/2026-06-28.md), [Jun 29](briefings/2026-06-29.md), [Jun 30](briefings/2026-06-30.md), [Jul 1](briefings/2026-07-01.md), [Jul 5](briefings/2026-07-05.md), [Jul 6](briefings/2026-07-06.md), [Jul 11](briefings/2026-07-11.md), [Jul 13](briefings/2026-07-13.md), [Jul 14](briefings/2026-07-14.md), [Jul 15](briefings/2026-07-15.md), [Jul 18](briefings/2026-07-18.md), [Jul 19](briefings/2026-07-19.md), [Jul 20](briefings/2026-07-20.md), [Jul 25](briefings/2026-07-25.md)

- **bridge-dvn** (16 briefings) — [Jun 12](briefings/2026-06-12.md), [Jun 14](briefings/2026-06-14.md), [Jun 17](briefings/2026-06-17.md), [Jun 19](briefings/2026-06-19.md), [Jun 22](briefings/2026-06-22.md), [Jun 23](briefings/2026-06-23.md), [Jun 25](briefings/2026-06-25.md), [Jun 29](briefings/2026-06-29.md), [Jun 30](briefings/2026-06-30.md), [Jul 4](briefings/2026-07-04.md), [Jul 18](briefings/2026-07-18.md), [Jul 20](briefings/2026-07-20.md), [Jul 22](briefings/2026-07-22.md), [Jul 23](briefings/2026-07-23.md), [Jul 24](briefings/2026-07-24.md), [Jul 27](briefings/2026-07-27.md)

- **flash-loan** (13 briefings) — [Jun 12](briefings/2026-06-12.md), [Jun 16](briefings/2026-06-16.md), [Jul 2](briefings/2026-07-02.md), [Jul 3](briefings/2026-07-03.md), [Jul 6](briefings/2026-07-06.md), [Jul 7](briefings/2026-07-07.md), [Jul 9](briefings/2026-07-09.md), [Jul 10](briefings/2026-07-10.md), [Jul 11](briefings/2026-07-11.md), [Jul 12](briefings/2026-07-12.md), [Jul 14](briefings/2026-07-14.md), [Jul 17](briefings/2026-07-17.md), [Jul 21](briefings/2026-07-21.md)

- **oracle-manipulation** (11 briefings) — [Jun 20](briefings/2026-06-20.md), [Jun 22](briefings/2026-06-22.md), [Jun 25](briefings/2026-06-25.md), [Jul 4](briefings/2026-07-04.md), [Jul 12](briefings/2026-07-12.md), [Jul 13](briefings/2026-07-13.md), [Jul 14](briefings/2026-07-14.md), [Jul 15](briefings/2026-07-15.md), [Jul 16](briefings/2026-07-16.md), [Jul 17](briefings/2026-07-17.md), [Jul 23](briefings/2026-07-23.md)

- **price-manipulation** (10 briefings) — [Jun 22](briefings/2026-06-22.md), [Jun 23](briefings/2026-06-23.md), [Jun 25](briefings/2026-06-25.md), [Jul 2](briefings/2026-07-02.md), [Jul 3](briefings/2026-07-03.md), [Jul 12](briefings/2026-07-12.md), [Jul 16](briefings/2026-07-16.md), [Jul 21](briefings/2026-07-21.md), [Jul 23](briefings/2026-07-23.md), [Jul 25](briefings/2026-07-25.md)

- **unverified-contract** (7 briefings) — [Jun 12](briefings/2026-06-12.md), [Jun 20](briefings/2026-06-20.md), [Jun 21](briefings/2026-06-21.md), [Jun 24](briefings/2026-06-24.md), [Jul 2](briefings/2026-07-02.md), [Jul 4](briefings/2026-07-04.md), [Jul 27](briefings/2026-07-27.md)

- **upgradeability** (6 briefings) — [Jun 13](briefings/2026-06-13.md), [Jun 18](briefings/2026-06-18.md), [Jun 20](briefings/2026-06-20.md), [Jul 3](briefings/2026-07-03.md), [Jul 15](briefings/2026-07-15.md), [Jul 16](briefings/2026-07-16.md)

- **reentrancy** (3 briefings) — [Jul 10](briefings/2026-07-10.md), [Jul 11](briefings/2026-07-11.md), [Jul 15](briefings/2026-07-15.md)

- **rounding** (3 briefings) — [Jun 15](briefings/2026-06-15.md), [Jun 16](briefings/2026-06-16.md), [Jul 6](briefings/2026-07-06.md)

- **signature-replay** (2 briefings) — [Jun 14](briefings/2026-06-14.md), [Jul 22](briefings/2026-07-22.md)

- **dos** (1 briefing) — [Jun 19](briefings/2026-06-19.md)

- **front-running** (1 briefing) — [Jul 8](briefings/2026-07-08.md)

- **integer-overflow** (1 briefing) — [Jun 15](briefings/2026-06-15.md)

---

## 📊 Stats

- **Total briefings:** 45
- **Date range:** 2026-06-12 → 2026-07-27 (46 days; one day missing: Jun 26)
- **July 2026 MTD losses:** ~$208M across 25+ incidents
- **Top 3 most-frequent bug classes:**
  1. `key-management` — 32 briefings (71%)
  2. `logic-error` — 30 briefings (67%)
  3. `access-control` — 21 briefings (47%)
- **Highest-$ incident covered:** Unnamed 3-protocol bridge $127M catch-up (Jun 19 briefing)
- **Most active attack surface in July 2026:** Cross-chain bridges — AFX Trade $24.15M + Wanchain $10M + Verus $7.54M + Allbridge Core $1.65M = **~$43M from bridges alone**

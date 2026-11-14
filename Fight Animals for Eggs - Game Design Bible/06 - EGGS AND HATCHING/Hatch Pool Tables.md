---
title: Hatch Pool Tables
type: spec
category: eggs
status: proposed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - hatching
  - probability
---

# Hatch Pool Tables

> [!info] PROPOSED, generated
> The second random stage ([[Decision Register|D-015]]): an egg's rarity selects a pool, and the hatch selects one animal from that pool. Pools and weights are **PROPOSED**; the final pools are **UNDECIDED** ([[Open Questions#Q-018]]). Every pool below is verified by the generator to total 100%.

## Formula

```text
ClassWeight: Standard = 10, Scarce = 6, Elusive = 3
Tilt:        Standard = 0,  Scarce = 0.5, Elusive = 1.0
w_i  = ClassWeight_i × (1 + 1.0 × (P − 0.30) × Tilt_i)
Odds = w_i / Σ w (within the pool)
```

Hatch results are independent: no duplicate protection, no bias towards unowned animals, and no memory ([[Decision Register|D-018]], [[Independent Random Outcomes]]). Up to five eggs can be hatched at once ([[Decision Register|D-016]]); each egg is sampled separately.

## Pool summary

| Pool | Animals | Standard | Scarce | Elusive | Total base weight |
|---|---:|---:|---:|---:|---:|
| [[Common Egg]] | 12 | 8 | 2 | 2 | 98 |
| [[Uncommon Egg]] | 11 | 7 | 3 | 1 | 91 |
| [[Rare Egg]] | 10 | 7 | 2 | 1 | 85 |
| [[Epic Egg]] | 9 | 6 | 2 | 1 | 75 |
| [[Legendary Egg]] | 8 | 5 | 2 | 1 | 65 |
| [[Mythical Egg]] | 6 | 3 | 2 | 1 | 45 |
| [[Secret Egg]] | 4 | 2 | 1 | 1 | 29 |

## Common pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Rabbit]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Squirrel]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Hedgehog]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Raccoon]] | Scarce | 6 | 5.403% | 6.122% | 6.791% | 7.613% |
| [[Frog]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Duck]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Woodpecker]] | Elusive | 3 | 2.225% | 3.061% | 3.839% | 4.793% |
| [[Boar]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Goat]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Meerkat]] | Scarce | 6 | 5.403% | 6.122% | 6.791% | 7.613% |
| [[Zebra]] | Standard | 10 | 10.59% | 10.20% | 9.843% | 9.398% |
| [[Crab]] | Elusive | 3 | 2.225% | 3.061% | 3.839% | 4.793% |
| **Total** | | 98 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Uncommon pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Fox]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Owl]] | Scarce | 6 | 5.835% | 6.593% | 7.294% | 8.149% |
| [[Deer]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Badger]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Beaver]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Hyena]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Flamingo]] | Scarce | 6 | 5.835% | 6.593% | 7.294% | 8.149% |
| [[Cobra]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Monkey]] | Standard | 10 | 11.44% | 10.99% | 10.57% | 10.06% |
| [[Seal]] | Scarce | 6 | 5.835% | 6.593% | 7.294% | 8.149% |
| [[Penguin]] | Elusive | 3 | 2.403% | 3.297% | 4.123% | 5.131% |
| **Total** | | 91 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Rare pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Wolf]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Brown Bear]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Cheetah]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Kangaroo]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Leopard]] | Scarce | 6 | 6.197% | 7.059% | 7.868% | 8.872% |
| [[Toucan]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Peacock]] | Scarce | 6 | 6.197% | 7.059% | 7.868% | 8.872% |
| [[Octopus]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Walrus]] | Standard | 10 | 12.15% | 11.76% | 11.40% | 10.95% |
| [[Arctic Fox]] | Elusive | 3 | 2.552% | 3.529% | 4.447% | 5.586% |
| **Total** | | 85 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Epic pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Tiger]] | Standard | 10 | 13.83% | 13.33% | 12.87% | 12.30% |
| [[Gorilla]] | Standard | 10 | 13.83% | 13.33% | 12.87% | 12.30% |
| [[Crocodile]] | Standard | 10 | 13.83% | 13.33% | 12.87% | 12.30% |
| [[Rhino]] | Standard | 10 | 13.83% | 13.33% | 12.87% | 12.30% |
| [[Hippo]] | Scarce | 6 | 7.054% | 8.000% | 8.880% | 9.963% |
| [[Golden Eagle]] | Standard | 10 | 13.83% | 13.33% | 12.87% | 12.30% |
| [[Dolphin]] | Standard | 10 | 13.83% | 13.33% | 12.87% | 12.30% |
| [[Electric Eel]] | Scarce | 6 | 7.054% | 8.000% | 8.880% | 9.963% |
| [[Snow Leopard]] | Elusive | 3 | 2.905% | 4.000% | 5.019% | 6.273% |
| **Total** | | 75 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Legendary pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Lion]] | Standard | 10 | 16.05% | 15.38% | 14.77% | 14.03% |
| [[Elephant]] | Standard | 10 | 16.05% | 15.38% | 14.77% | 14.03% |
| [[Great White Shark]] | Standard | 10 | 16.05% | 15.38% | 14.77% | 14.03% |
| [[Orca]] | Standard | 10 | 16.05% | 15.38% | 14.77% | 14.03% |
| [[Narwhal]] | Scarce | 6 | 8.186% | 9.231% | 10.19% | 11.36% |
| [[Peregrine Falcon]] | Standard | 10 | 16.05% | 15.38% | 14.77% | 14.03% |
| [[Giant Panda]] | Scarce | 6 | 8.186% | 9.231% | 10.19% | 11.36% |
| [[Komodo Dragon]] | Elusive | 3 | 3.371% | 4.615% | 5.761% | 7.153% |
| **Total** | | 65 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Mythical pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Sabre-Tooth Tiger]] | Standard | 10 | 23.64% | 22.22% | 20.96% | 19.49% |
| [[Woolly Mammoth]] | Standard | 10 | 23.64% | 22.22% | 20.96% | 19.49% |
| [[Megalodon]] | Standard | 10 | 23.64% | 22.22% | 20.96% | 19.49% |
| [[Haast's Eagle]] | Scarce | 6 | 12.06% | 13.33% | 14.47% | 15.79% |
| [[Blue Whale]] | Scarce | 6 | 12.06% | 13.33% | 14.47% | 15.79% |
| [[Giant Squid]] | Elusive | 3 | 4.965% | 6.667% | 8.176% | 9.942% |
| **Total** | | 45 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Secret pool

| Animal | Class | Base weight | P = 0.0 | P = 0.3 (baseline) | P = 0.6 | P = 1.0 |
|---|---|---:|---:|---:|---:|---:|
| [[Mosasaurus]] | Standard | 10 | 36.76% | 34.48% | 32.47% | 30.12% |
| [[Quetzalcoatlus]] | Standard | 10 | 36.76% | 34.48% | 32.47% | 30.12% |
| [[Titanoboa]] | Scarce | 6 | 18.75% | 20.69% | 22.40% | 24.40% |
| [[Tyrannosaurus Rex]] | Elusive | 3 | 7.721% | 10.34% | 12.66% | 15.36% |
| **Total** | | 29 | **100.0000%** | **100.0000%** | **100.0000%** | **100.0000%** |

## Combined odds per egg roll

The chance that one egg roll eventually hatches a specific animal (rarity odds × pool share), ignoring merging. This is useful for the [[Ascension Expected Value Analysis]].

| Animal | Rarity | Per roll at P = 0.3 | Expected rolls (P = 0.3) | Per roll at P = 1.0 | Expected rolls (P = 1.0) |
|---|---|---:|---:|---:|---:|
| [[Rabbit]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Squirrel]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Hedgehog]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Raccoon]] | Common | 3.980% | 25 | 4.045% | 25 |
| [[Frog]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Duck]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Woodpecker]] | Common | 1.990% | 50 | 2.547% | 39 |
| [[Boar]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Goat]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Meerkat]] | Common | 3.980% | 25 | 4.045% | 25 |
| [[Zebra]] | Common | 6.633% | 15 | 4.994% | 20 |
| [[Crab]] | Common | 1.990% | 50 | 2.547% | 39 |
| [[Fox]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Owl]] | Uncommon | 1.451% | 69 | 2.081% | 48 |
| [[Deer]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Badger]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Beaver]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Hyena]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Flamingo]] | Uncommon | 1.451% | 69 | 2.081% | 48 |
| [[Cobra]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Monkey]] | Uncommon | 2.418% | 41 | 2.569% | 39 |
| [[Seal]] | Uncommon | 1.451% | 69 | 2.081% | 48 |
| [[Penguin]] | Uncommon | 0.7253% | 138 | 1.310% | 76 |
| [[Wolf]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Brown Bear]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Cheetah]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Kangaroo]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Leopard]] | Rare | 0.6353% | 157 | 1.201% | 83 |
| [[Toucan]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Peacock]] | Rare | 0.6353% | 157 | 1.201% | 83 |
| [[Octopus]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Walrus]] | Rare | 1.059% | 94 | 1.483% | 67 |
| [[Arctic Fox]] | Rare | 0.3176% | 315 | 0.7562% | 132 |
| [[Tiger]] | Epic | 0.4000% | 250 | 0.6818% | 147 |
| [[Gorilla]] | Epic | 0.4000% | 250 | 0.6818% | 147 |
| [[Crocodile]] | Epic | 0.4000% | 250 | 0.6818% | 147 |
| [[Rhino]] | Epic | 0.4000% | 250 | 0.6818% | 147 |
| [[Hippo]] | Epic | 0.2400% | 417 | 0.5522% | 181 |
| [[Golden Eagle]] | Epic | 0.4000% | 250 | 0.6818% | 147 |
| [[Dolphin]] | Epic | 0.4000% | 250 | 0.6818% | 147 |
| [[Electric Eel]] | Epic | 0.2400% | 417 | 0.5522% | 181 |
| [[Snow Leopard]] | Epic | 0.1200% | 833 | 0.3477% | 288 |
| [[Lion]] | Legendary | 0.1231% | 812 | 0.2458% | 407 |
| [[Elephant]] | Legendary | 0.1231% | 812 | 0.2458% | 407 |
| [[Great White Shark]] | Legendary | 0.1231% | 812 | 0.2458% | 407 |
| [[Orca]] | Legendary | 0.1231% | 812 | 0.2458% | 407 |
| [[Narwhal]] | Legendary | 0.0738% | 1,354 | 0.1991% | 502 |
| [[Peregrine Falcon]] | Legendary | 0.1231% | 812 | 0.2458% | 407 |
| [[Giant Panda]] | Legendary | 0.0738% | 1,354 | 0.1991% | 502 |
| [[Komodo Dragon]] | Legendary | 0.0369% | 2,708 | 0.1254% | 798 |
| [[Sabre-Tooth Tiger]] | Mythical | 0.0400% | 2,500 | 0.0849% | 1,178 |
| [[Woolly Mammoth]] | Mythical | 0.0400% | 2,500 | 0.0849% | 1,178 |
| [[Megalodon]] | Mythical | 0.0400% | 2,500 | 0.0849% | 1,178 |
| [[Haast's Eagle]] | Mythical | 0.0240% | 4,167 | 0.0688% | 1,454 |
| [[Blue Whale]] | Mythical | 0.0240% | 4,167 | 0.0688% | 1,454 |
| [[Giant Squid]] | Mythical | 0.0120% | 8,333 | 0.0433% | 2,309 |
| [[Mosasaurus]] | Secret | 0.00690% | 14,500 | 0.0160% | 6,267 |
| [[Quetzalcoatlus]] | Secret | 0.00690% | 14,500 | 0.0160% | 6,267 |
| [[Titanoboa]] | Secret | 0.00414% | 24,167 | 0.0129% | 7,737 |
| [[Tyrannosaurus Rex]] | Secret | 0.00207% | 48,333 | 0.00814% | 12,288 |

The sum of all 60 combined odds is 100% at every P, because every roll produces exactly one egg and every egg hatches exactly one animal.

## Related documents

[[Hatch System]] · [[Dynamic Luck Probability Tables]] · [[Probability Balancing]] · [[Implementation - Weighted Random Selection]] · [[Test Cases - Egg Rolls and Hatching]]

# Clean-room ceiling: CK, CK2, CK3, Rome, Europa Barbarorum

Written by Grok from iPhone, 2026-10-06. Agent research. Not a designer note. Not canon. Repo wins if James contradicts this.

This file is the far edge of the permissible direction. It records structures we may reimplement in original code. It does not copy source, text, unit stats, art, or data tables from Crusader Kings, Total War, or the Europa Barbarorum mod.

## What "as far as possible" means

A campaign is four layers. We can own all four if every name, number, and sentence is ours.

1. Clock. A season or a day advances. Production, growth, and travel resolve on that tick.
2. Place. A named region has an owner, a government band, a population, and a recruitment pool that depends on the band.
3. Force. A body of men is raised from a place, costs manpower and treasury, and takes time to arrive.
4. Gate. A reform or law flips when predicates are true: year, holdings, a person with a role. The reward is a new pool, not a copied unit list.

That is the shape shared by Crusader Kings, Rome: Total War, and the public Europa Barbarorum description (government buildings, regional versus factional recruitment, reform events tied to year and empire size). The expression is theirs. The shape is an idea.

Out of reach, on purpose:

- Decompiled binaries, unpacked game files, extracted meshes, audio, or maps.
- Europa Barbarorum unit rosters, descriptions, and stat lines. Those are the mod team's expression.
- Paradox or Creative Assembly event text, localization, and script files.
- A playable clone that a player would recognize as their game with the serial numbers filed off.

## What each source is allowed to teach

Crusader Kings 2, from public wiki and from James's 2026-09-23 play recollection:

- A levy is a share of a holding, scaled by law and by opinion, not an instant button.
- Tribal organization is a ladder. Council-like offices appear as the ladder rises. They are a poor fit for an Iron Age hall if copied as five feudal offices.
- Household staffing (wife, concubines, kinsmen) explodes unless gold, food, and distance constrain it.
- Gavelkind, not a building upkeep line, was the felt penalty.

Crusader Kings 3, public shape only:

- A contract is a bundle of obligations (levy share, tax share, war permission), not a single crown-authority slider.
- A scheme is a person, a target, a secrecy score, and a daily tick. We already have offices and a script seam in Suvorov. Schemes stay opt-in.

Rome: Total War, public shape only:

- Campaign turn and real-time battle are different clocks. The campaign does not need the battle simulator on day one.
- An army is a stack of units with a general. Movement spends a season. Recruitment spends a settlement building.

Europa Barbarorum, public wiki and Total War Center overview only:

- Government band changes what can be built and who can be recruited.
- Homeland band recruits the faction pool. An allied or client band recruits a local pool and installs a client ruler.
- A reform is a predicate over year, settlement count, and a person. Other factions wait on a world event.
- Area of recruitment is faction crossed with place, not a single global barracks tree.

Total War battles stay a later seat. This slice does not simulate melee.

## Original slice in this commit

`campaign_shape.py` is the structural core. Fictional polities only: Helvii, Senones, and a coastal league. No copied faction, no copied unit.

- Government bands: homeland, governed, allied, occupied.
- Recruitment: homeland and governed yield the faction pool. Allied yields the local pool plus a client ruler. Occupied yields a thin garrison only.
- Reform gate: year, settlement count, and a named reformer. Numbers are ours.
- Levy share: base times law times an opinion factor, floored by the law minimum. Coefficients are ours. The public CK2 formula is the analogy, not the table.
- Season tick: treasury from income, population growth, one manpower recovery step.

Tests cover the gates. They do not import Faction.py. The 2020 menu loop stays untouched.

## Where this does not go

Suvorov remains the engine. This repo is a consumer experiment. Do not port Clausewitz. Do not merge this PR. A stronger agent reviews before any merge, and James merges.

Next permissible steps, still clean-room: a travel graph with envoy delay, a client-ruler person bound to an allied place, and a season report the agent can play. Battle resolution stays a separate seat.

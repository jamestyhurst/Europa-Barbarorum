"""Clean-room campaign shape. Original names and numbers.

Inspired by the public shape of province government, regional recruitment,
reform gates, and levy willingness. Not a port of Europa Barbarorum,
Rome: Total War, or Crusader Kings.
"""

from __future__ import annotations

HOMELAND = "homeland"
GOVERNED = "governed"
ALLIED = "allied"
OCCUPIED = "occupied"

BANDS = (HOMELAND, GOVERNED, ALLIED, OCCUPIED)

# Original coefficients. Not a published game table.
LAW_MINIMUM = {
    "loose": 0.0,
    "custom": 0.15,
    "sworn": 0.4,
    "muster": 0.7,
}


def recruitment_pool(band, faction_units, local_units):
    if band in (HOMELAND, GOVERNED):
        return list(faction_units)
    if band == ALLIED:
        return list(local_units)
    if band == OCCUPIED:
        return list(faction_units[:1])
    raise ValueError(f"unknown band: {band}")


def client_ruler_installed(band):
    return band == ALLIED


def reform_ready(year, settlements, has_reformer, year_gate=172, settlement_gate=12):
    return year >= year_gate and settlements >= settlement_gate and has_reformer


def levy_share(base, law, opinion):
    if law not in LAW_MINIMUM:
        raise ValueError(f"unknown law: {law}")
    opinion = max(-100, min(100, opinion))
    willingness = 0.5 + (opinion / 200.0)
    share = base * willingness
    floor = base * LAW_MINIMUM[law]
    return max(floor, share)


def season_tick(treasury, income, population, growth=1.02):
    return treasury + income, int(population * growth)

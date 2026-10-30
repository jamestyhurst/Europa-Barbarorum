"""Tests for the clean-room campaign shape. One run is enough."""

import unittest

from campaign_shape import (
    ALLIED,
    GOVERNED,
    HOMELAND,
    OCCUPIED,
    client_ruler_installed,
    levy_share,
    recruitment_pool,
    reform_ready,
    season_tick,
)


FACTION_POOL = ("spear_band", "rider_band")
LOCAL_POOL = ("hill_slingers", "wood_hunters")


class RecruitmentTests(unittest.TestCase):
    def test_homeland_and_governed_use_faction_pool(self):
        self.assertEqual(recruitment_pool(HOMELAND, FACTION_POOL, LOCAL_POOL), list(FACTION_POOL))
        self.assertEqual(recruitment_pool(GOVERNED, FACTION_POOL, LOCAL_POOL), list(FACTION_POOL))

    def test_allied_uses_local_pool_and_installs_a_client(self):
        self.assertEqual(recruitment_pool(ALLIED, FACTION_POOL, LOCAL_POOL), list(LOCAL_POOL))
        self.assertTrue(client_ruler_installed(ALLIED))
        self.assertFalse(client_ruler_installed(GOVERNED))

    def test_occupied_is_a_thin_garrison(self):
        self.assertEqual(recruitment_pool(OCCUPIED, FACTION_POOL, LOCAL_POOL), ["spear_band"])


class GateTests(unittest.TestCase):
    def test_reform_needs_year_settlements_and_a_person(self):
        self.assertFalse(reform_ready(171, 12, True))
        self.assertFalse(reform_ready(172, 11, True))
        self.assertFalse(reform_ready(172, 12, False))
        self.assertTrue(reform_ready(172, 12, True))

    def test_levy_floors_at_the_law_and_scales_with_opinion(self):
        self.assertEqual(levy_share(100, "loose", -100), 0)
        self.assertEqual(levy_share(100, "muster", -100), 70)
        self.assertAlmostEqual(levy_share(100, "loose", 0), 50)
        self.assertAlmostEqual(levy_share(100, "custom", 100), 100)

    def test_season_tick_adds_income_and_grows_population(self):
        treasury, population = season_tick(40, 10, 100)
        self.assertEqual(treasury, 50)
        self.assertEqual(population, 102)


if __name__ == "__main__":
    unittest.main()

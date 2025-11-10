# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_items(self):
        items = [Item("foo", 5, 4), Item("bar", 3, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", gilded_rose.items[0].name)
        self.assertEqual(4, gilded_rose.items[0].sell_in)
        self.assertEqual(3, gilded_rose.items[0].quality)
        self.assertEqual("bar", gilded_rose.items[1].name)

    def test_zero_quality(self):
        items = [Item("foo", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_expiring(self):
        items = [Item("foo", 1, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(3, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(1, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 1, 34)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(35, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(37, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(39, gilded_rose.items[0].quality)

    def test_max_quality(self):
        items = [Item("Aged Brie", 4, 50),
                 Item("Backstage passes", 12, 50),
                 Item("Backstage passes", 8, 49),
                 Item("Backstage passes", 8, 50),
                 Item("Backstage passes", 3, 48),
                 Item("Backstage passes", 3, 49),
                 Item("Backstage passes", 3, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(50, gilded_rose.items[2].quality)
        self.assertEqual(50, gilded_rose.items[3].quality)
        self.assertEqual(50, gilded_rose.items[4].quality)
        self.assertEqual(50, gilded_rose.items[5].quality)
        self.assertEqual(50, gilded_rose.items[6].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", "n/a", 39),
                 Item("Sulfuras", 10000, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(39, gilded_rose.items[0].quality)
        self.assertEqual(items[0].sell_in, gilded_rose.items[0].sell_in)
        self.assertEqual(8, gilded_rose.items[1].quality)
        self.assertEqual(items[1].sell_in, gilded_rose.items[1].sell_in)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 36),
                 Item("Backstage passes", 8, 12),
                 Item("Backstage passes", 3, 18),
                 Item("Backstage passes", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(37, gilded_rose.items[0].quality)
        self.assertEqual(14, gilded_rose.items[1].quality)
        self.assertEqual(21, gilded_rose.items[2].quality)
        self.assertEqual(0, gilded_rose.items[3].quality)

    def test_conjured(self):
        items = [Item("Conjured Man", 2, 14)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(10, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(6, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(2, gilded_rose.items[0].quality)
        
if __name__ == '__main__':
    unittest.main()

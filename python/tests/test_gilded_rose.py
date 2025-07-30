# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_no_items_when_no_items_are_passed(self):
        items = []
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([], gilded_rose.items)

    def test_sulfuras_doesnt_age_when_update_quality_is_called(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 1, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(len(gilded_rose.items), 1)
        
        first_item = gilded_rose.items[0]
        self.assertEqual(first_item.name, sulfuras)
        self.assertEqual(first_item.quality, 1)
        self.assertEqual(first_item.sell_in, 1)

    def test_conjured_mana_cake_ages_when_update_quality_is_called(self):
        name = "Conjured Mana Cake"
        items = [Item(name, 0, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(len(gilded_rose.items), 1)
        
        first_item = gilded_rose.items[0]
        self.assertEqual(first_item.name, name)
        self.assertEqual(first_item.quality, 0)
        self.assertEqual(first_item.sell_in, -1)

    def test_quality_doesnt_change_given_backstage_pass(self):
        name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(name, 1, 50)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(len(gilded_rose.items), 1)
        
        first_item = gilded_rose.items[0]
        self.assertEqual(first_item.name, name)
        self.assertEqual(first_item.sell_in, 0)
        self.assertEqual(first_item.quality, 50)

class ItemTest(unittest.TestCase):
    def test_aged_brie(self):
        name = "Aged Brie"
        item = Item(name, None, None)

        self.assertEqual(item.name, name)
        self.assertEqual(item.quality, None)
        self.assertEqual(item.sell_in, None)

    def test_error_when_quality_none(self):
        with self.assertRaises(TypeError):
            Item(None, None, None)

    def test_error_when_quality_is_negative_one(self):
        with self.assertRaises(TypeError):
            Item(None, 0, -1)

    def test_error_when_quality_is_zero(self):
        with self.assertRaises(TypeError):
            Item(None, 0, 0)

    def test_error_when_sell_in_is_none(self):
        with self.assertRaises(TypeError):
            Item(None, None, 1)


if __name__ == '__main__':
    unittest.main()

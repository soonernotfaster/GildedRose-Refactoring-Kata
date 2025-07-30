# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_no_items_when_no_items_are_passed(self):
        items = []
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([], gilded_rose.items)

    def test_item_ages_when_update_quality_is_called(self):
        items = [Item(None, 0, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(len(gilded_rose.items), 1)
        
        first_item = gilded_rose.items[0]
        self.assertEqual(first_item.name, None)
        self.assertEqual(first_item.quality, 0)
        self.assertEqual(first_item.sell_in, -1)

class ItemTest(unittest.TestCase):
    def test_aged_brie(self):
        item = Item("Aged Brie", None, None)

        self.assertEqual(item.name, "Aged Brie")
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

import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose(unittest.TestCase):

    def test_normal_item(self):
        item = Item("foo", 10, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(9, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_aged_brie(self):
        item = Item("Aged Brie", 5, 10)

        GildedRose([item]).update_quality()

        self.assertEqual(11, item.quality)

    def test_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)

        GildedRose([item]).update_quality()

        self.assertEqual(80, item.quality)

    def test_backstage_pass(self):
        item = Item(
            "Backstage passes to a TAFKAL80ETC concert",
            8,
            20
        )

        GildedRose([item]).update_quality()

        self.assertEqual(22, item.quality)

    def test_expired_backstage_pass(self):
        item = Item(
            "Backstage passes to a TAFKAL80ETC concert",
            0,
            20
        )

        GildedRose([item]).update_quality()

        self.assertEqual(0, item.quality)

    def test_conjured(self):
        item = Item("Conjured", 5, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(18, item.quality)


if __name__ == "__main__":
    unittest.main()

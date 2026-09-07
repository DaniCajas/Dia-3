class ItemHandler:
    def update(self, item):
        raise NotImplementedError


class NormalItemHandler(ItemHandler):
    def update(self, item):
        item.sell_in -= 1

        degradation = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - degradation)


class AgedBrieHandler(ItemHandler):
    def update(self, item):
        item.sell_in -= 1

        increase = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + increase)


class BackstagePassHandler(ItemHandler):
    def update(self, item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
            return

        if item.sell_in < 5:
            increment = 3
        elif item.sell_in < 10:
            increment = 2
        else:
            increment = 1

        item.quality = min(50, item.quality + increment)


class SulfurasHandler(ItemHandler):
    def update(self, item):
        pass


class ConjuredHandler(ItemHandler):
    def update(self, item):
        item.sell_in -= 1

        degradation = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degradation)


def get_handler(item):
    handlers = {
        "Aged Brie": AgedBrieHandler(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassHandler(),
        "Sulfuras, Hand of Ragnaros": SulfurasHandler(),
        "Conjured": ConjuredHandler(),
    }

    return handlers.get(item.name, NormalItemHandler())

# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            delta_quality = -1
            if "sulfuras" in item.name.lower():
                continue
            elif "aged brie" in item.name.lower():
                delta_quality = 1
            elif "backstage passes" in item.name.lower():
                delta_quality = 1
                if item.sell_in < 11:
                    delta_quality += 1
                if item.sell_in < 6:
                    delta_quality += 1
            if item.sell_in < 1:
                if "aged brie" in item.name.lower():
                    delta_quality += 1
                elif "backstage passes" in item.name.lower():
                    delta_quality = -item.quality
                else:
                    delta_quality -= 1

            if "conjured" in item.name.lower():
                delta_quality *= 2

            item.quality += delta_quality

            if item.quality > 50:
                item.quality = 50
            elif item.quality < 0:
                item.quality = 0

            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

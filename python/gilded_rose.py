# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "aged brie" not in item.name.lower() and "backstage passes" not in item.name.lower():
                if item.quality > 0:
                    if "sulfuras" not in item.name.lower():
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if "backstage passes" in item.name.lower():
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if "sulfuras" not in item.name.lower():
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if "aged brie" not in item.name.lower():
                    if "backstage passes" not in item.name.lower():
                        if item.quality > 0:
                            if "sulfuras" not in item.name.lower():
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

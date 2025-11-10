# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def _is_brie(item):
        return item.name[:9] == "Aged Brie"

    @staticmethod
    def _is_backstage_pass(item):
        return item.name[:16] == "Backstage passes"

    @staticmethod
    def _is_sulfuras(item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    @staticmethod
    def _is_conjured(item):
        return item.name[:8] == "Conjured"

    @staticmethod
    def _is_expired(item):
        return item.sell_in < 1

    def _update_aged_brie_quality(self, brie):
        brie.quality += 1
        if self._is_expired(brie):
            brie.quality += 1

    def _update_backstage_passes_quality(self, b_pass):
        if self._is_expired(b_pass):
            b_pass.quality = 0
            return

        backstage_pass_quality_increase1 = 10
        backstage_pass_quality_increase2 = 5

        b_pass.quality += 1
        if b_pass.sell_in < backstage_pass_quality_increase1 + 1:
            b_pass.quality += 1
        if b_pass.sell_in < backstage_pass_quality_increase2 + 1:
            b_pass.quality += 1

    def _update_normal_item_quality(self, item):
        item.quality -= 1 + self._is_conjured(item)
        if self._is_expired(item):
            item.quality -= 1 + self._is_conjured(item)

    @staticmethod
    def _impose_quality_bounds(item):
        quality_max = 50
        quality_min = 0

        if item.quality > quality_max:
            item.quality = quality_max
        elif item.quality < quality_min:
            item.quality = quality_min

    @staticmethod
    def _update_sell_in(item):
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if self._is_sulfuras(item):
                continue
            elif self._is_brie(item):
                self._update_aged_brie_quality(item)
            elif self._is_backstage_pass(item):
                self._update_backstage_passes_quality(item)
            else:
                self._update_normal_item_quality(item)

            self._impose_quality_bounds(item)

            self._update_sell_in(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

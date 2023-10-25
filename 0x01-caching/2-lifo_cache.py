#!/usr/bin/env python3
"""Defines LIFOCahe class
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Represents LIFOCache object's properties and methods
    """
    def __init__(self):
        """Initializes the instance with basic properties
        """
        super().__init__()

    def put(self, key, item):
        """Assigns an item with the required key to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                k, v = self.cache_data.popitem()
                self.cache_data[key] = item
                print("DISCARD: {}".format(k))
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Retrieves value related to given key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

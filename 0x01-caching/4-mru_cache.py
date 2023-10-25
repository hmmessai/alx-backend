#!/usr/bin/env python3
"""Defines LRUCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Represents LRUCahe object's properties and methods
    """
    def __init__(self):
        """Initializes instance with basic properties
        """
        super().__init__()

    def put(self, key, item):
        """Assigns item to cache_data with the given key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    del self.cache_data[key]
                    self.cache_data[key] = item
                else:
                    k, v = self.cache_data.popitem()
                    print("DISCARD: {}".format(k))
                    self.cache_data[key] = item
            elif key in self.cache_data.keys():
                del self.cache_data[key]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Retrieves value contained in cache with given key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

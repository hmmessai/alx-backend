#!/usr/bin/env python3
"""Defines FIFOCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Represents FIFOCache class properties and methods
    """
    def __init__(self):
        """Initializes the instance with required properties
        """
        super().__init__()

    def put(self, key, item):
        """Assign item with the specified key to cache_data
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                for k, v in self.cache_data.items():
                    discarded = k
                    del self.cache_data[k]
                    break
                self.cache_data[key] = item
                print("DISCARD: {}".format(discarded))
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Retrieves value the key holds in the cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

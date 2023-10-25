#!/usr/bin/env python3
"""Define BasicCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Represents BasicCache class properties and methods
    """
    def __init__(self):
        """Intialize the instance with some properties
        """
        super().__init__()

    def put(self, key, item):
        """Assign item with key to cache_data dictionary
        """
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value the key holds
        """
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

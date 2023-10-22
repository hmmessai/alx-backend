#!/usr/bin/env python3
"""
Implements pagination using class Server
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the page for the specified values
        """
        assert type(page) == int, "page must be integer"
        assert type(page_size) == int, "page_size must be integer"
        assert page > 0, "page must be greater than zero"
        assert page_size > 0, "page_size must be greater than zero"

        def index_range(page, page_size):
            """
            Returns the start and stop indexes of a page
            """

            total_page = (page * page_size) - 1
            start = 0
            end = page_size

            for i in range(0, total_page, page_size):
                start = i
                end = i + page_size

            return (start, end)

        start, end = index_range(page, page_size)
        req_page = []

        if end > len(self.dataset()) and start > len(self.dataset()):
            return req_page

        for i in range(start, end):
            req_page.append(self.dataset()[i])

        return req_page

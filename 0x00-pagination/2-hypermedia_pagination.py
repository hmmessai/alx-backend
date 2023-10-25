#!/usr/bin/env python3
"""
Implements pagination using class Server
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)
        req_page = []

        if end > len(self.dataset()) and start > len(self.dataset()):
            return req_page

        for i in range(start, end):
            try:
                req_page.append(self.dataset()[i])
            except Exception:
                pass

        return req_page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves information about a page
        """
        data_len = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(data_len / page_size)
        next_page = page + 1 if ((page + 1) <= total_pages) else None
        prev_page = page - 1 if ((page - 1) >= 1) else None

        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }

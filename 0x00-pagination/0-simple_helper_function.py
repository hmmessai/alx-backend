#!/usr/bin/env python3
"""
Defines the index_range function
"""


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

#!/usr/bin/env python3
"""
Defines the index_range function
"""


def index_range(page, page_size):
    """
    Return tuple of size two containing a start index
    and end index corresponding to the range of indexes to return
    in a list for those partiular pagination parameters
    """
    total_page = (page * page_size) - 1
    start = 0
    end = page_size

    for i in range(0, total_page, page_size):
        start = i
        end = i + page_size

    return (start, end)

#!/usr/bin/env python3
"""Import async_generator from previous task"""
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension():
    """takes function and returns random number"""
    return [i async for i in async_generator()]

#!/usr/bin/env python3
"""Import async_comprehension from the previous file"""
import asyncio
import time

async_comprehension = __import__('1_async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times parallell"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start

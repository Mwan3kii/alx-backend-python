#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays_res = []

    for delay in delays:
        if not delays_res:
            delays_res.append(delay)
        else:
            for i in range(len(delays_res)):
                if delay < delays_res[i]:
                    delays_res.insert(i, delay)
                    break
            else:
                delays_res.append(delay)
    return delays_res

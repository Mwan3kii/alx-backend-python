#!/usr/bin/env python3
"""Take the code from wait_n and alter it into task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns delay results"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delay_res = []

    for delay in delays:
        if not delay_res:
            delay_res.append(delay)
        else:
            for i in range(len(delay_res)):
                if delay < delay_res[i]:
                    delay_res.insert(i, delay)
                    break
            else:
                delay_res.append(delay)
    
    return delay_res
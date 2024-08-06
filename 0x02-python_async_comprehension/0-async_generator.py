#!/usr/bin/env python3
"""Coroutine called async generator"""
import asyncio
import random


async def async_generator():
    """yield random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

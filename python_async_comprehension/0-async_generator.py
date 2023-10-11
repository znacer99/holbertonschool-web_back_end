#!/usr/bin/env python3
"""
an asynchronous generator that yields random numbers
after an asynchronous delay.
"""
import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

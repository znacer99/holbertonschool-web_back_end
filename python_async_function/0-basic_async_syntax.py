#!/usr/bin/env python3
"""
wait random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous couroutine that waits for a random delay
    """

    delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(delay)
    return delay

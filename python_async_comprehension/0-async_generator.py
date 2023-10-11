#!/usr/bin/env python3
"""
an asynchronous generator that yields random numbers
after an asynchronous delay.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    asyncio generator bla bla bla
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

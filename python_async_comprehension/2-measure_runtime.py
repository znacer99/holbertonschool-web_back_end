#!/usr/bin/env python3
"""
async comprehension
"""

import time
from typing import List, Generator
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure runtime tarararara
    """
    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    total = end - start
    return total

#!/usr/bin/env python3
"""
wait_n
"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    concurrent coroutines bla bla bla
    """
    x = await asyncio.gather(*[wait_random(max_delay) for y in range(n)])
    return sorted(x)

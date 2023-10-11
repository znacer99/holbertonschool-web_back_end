#!/usr/bin/env python3
"""
task_wait_n
"""

from typing import List
task_wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays
    """
    delay = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
        delays = sorted(delays)
    return delays

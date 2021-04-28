#!/usr/bin/env python3
"""asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay.
    """
    num = random.random() * max_delay
    await asyncio.sleep(num)
    return num

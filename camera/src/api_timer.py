import asyncio
from main import get_average

async def timer(seconds):
    await asyncio.sleep(seconds)
    newAverage = get_average
    if(newAverage != 0):
        print('new value')

async def run_async_timer():
    task = asyncio.create_task(timer(1))
    await task

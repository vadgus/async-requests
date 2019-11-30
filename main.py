import asyncio
from time import time
from aiohttp import ClientSession


async def run(url, index):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response_data = await response.read()
            # print(response_data)
            print('%d: %f' % (index, time()))


loop = asyncio.get_event_loop()

tasks = []
url = "https://www.google.com/?hash="
for i in range(1000):
    url = url + "1"
    task = asyncio.ensure_future(run(url.format(i), i))
    tasks.append(task)

start = time()
loop.run_until_complete(asyncio.wait(tasks))

print("\n%s seconds" % str(time() - start))

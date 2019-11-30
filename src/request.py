import asyncio
from time import time
from aiohttp import ClientSession


class Request:
    _amount = 0

    _start = None
    _tasks = []
    _read = 0

    def run(self, amount: int) -> bool:
        if isinstance(amount, int) and amount > 0:
            self._amount = amount
            loop = asyncio.get_event_loop()

            url = "https://www.google.com/?hash="
            for i in range(self._amount):
                url = url + "1"
                task = asyncio.ensure_future(self._request(url.format(i), i))
                self._tasks.append(task)

            self._start = time()
            loop.run_until_complete(asyncio.wait(self._tasks))

            print("\n%s seconds" % str(time() - self._start))

        return self._amount == self._read

    async def _request(self, url, index):
        async with ClientSession() as session:
            async with session.get(url) as response:
                # response_data = await response.read()
                # print(response_data)
                await response.read()
                self._read += 1
                print('%d: %f' % (index, time()))

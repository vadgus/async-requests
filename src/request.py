import asyncio
from time import time
from aiohttp import ClientSession


class Request:
    _amount = 0

    _loop = None
    _start = None
    _tasks = []
    _read = 0

    def run(self, amount: int) -> bool:
        if isinstance(amount, int) and amount > 0:
            self._amount = amount

            url = "https://www.google.com/?hash="
            for i in range(self._amount):
                url = url + "1"
                task = asyncio.ensure_future(self._request(url.format(i), i))
                self._tasks.append(task)

            self._start = time()
            self.get_loop().run_until_complete(asyncio.wait(self._tasks))

            print("\n%s seconds" % str(time() - self._start))

        return self._amount == self._read

    def get_loop(self):
        if not self._loop:
            self._loop = asyncio.get_event_loop()
        return self._loop

    async def _request(self, url, index):
        async with ClientSession() as session:
            async with session.get(url) as response:
                # response_data = await response.read()
                # print(response_data)
                await response.read()
                self._read += 1
                print('%d: %f' % (index, time()))

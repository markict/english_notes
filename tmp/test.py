#! coding:utf-8


import asyncio
from yeelib import search_bulbs

from yeelib import search_bulbs


@asyncio.coroutine
def turn_all_lights_on(bulbs):
    while True:
        for b in bulbs.values():
            asyncio.Task(b.send_command("set_power",
                                        ["off", "sudden", 40]))
        yield from asyncio.sleep(10)


def main():
    loop = asyncio.get_event_loop()
    bulbs = loop.run_until_complete(search_bulbs())
    loop.create_task(turn_all_lights_on(bulbs))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()


if __name__ == '__main__':
    main()

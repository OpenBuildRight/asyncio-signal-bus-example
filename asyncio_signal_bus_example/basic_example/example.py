import asyncio
import json
import random

from asyncio_signal_bus import SignalBus

BUS = SignalBus()


@BUS.publisher(topic_name="foo")
async def foo_publisher(arg: str):
    signal = {"message": arg}
    await asyncio.sleep(random.randint(1, 100) / 50)
    print(f"publishing {json.dumps(signal)}")
    return signal


@BUS.subscriber(topic_name="foo")
async def foo_subscriber_0(signal: dict[str, str]):
    print(f"foo subscriber 0 received {json.dumps(signal)}")


@BUS.subscriber(topic_name="foo")
async def foo_subscriber_1(signal: dict[str, str]):
    print(f"foo subscriber 1 received {json.dumps(signal)}")


async def main():
    inputs = [f"message:{i}" for i in range(10)]
    async with BUS:
        await asyncio.gather(*[foo_publisher(x) for x in inputs])


if __name__ == "__main__":
    asyncio.run(main())

import asyncio, time

async def say(what, delay):
    await asyncio.sleep(delay)
    print (what)

loop = asyncio.get_event_loop()
print(f"started at {time.strftime('%X')}")

loop.run_until_complete(say("''Hello", 5))
print(f"started at {time.strftime('%X')}")

loop.close()
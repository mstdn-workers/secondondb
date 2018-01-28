import h1don
import asyncio


mstdn = h1don.h1don()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(asyncio.gather(
    mstdn.get_LTL_stream(),
    mstdn.heartbeat_check()
))
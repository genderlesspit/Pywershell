import asyncio

from pywershell import PywershellLive
from pywershell import pywersl

async def debug():
    await PywershellLive()
    _ = await pywersl

if __name__ == "__main__":
    asyncio.run(debug())
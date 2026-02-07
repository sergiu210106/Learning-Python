import asyncio
import random

# This simulates a slow API call
async def fetch_weather():
    print("1. Fetching Weather... waiting")
    await asyncio.sleep(2)  # Simulates 2 seconds network delay
    print("   -> Weather received!")
    return "Sunny, 72°F"

# This simulates a medium-speed API call
async def fetch_stocks():
    print("2. Fetching Stocks... waiting")
    await asyncio.sleep(1.5)
    print("   -> Stocks received!")
    return "AAPL: $150"

# This simulates a very slow API call
async def fetch_news():
    print("3. Fetching News... waiting")
    await asyncio.sleep(3)
    print("   -> News received!")
    return "Python 4.0 released!"
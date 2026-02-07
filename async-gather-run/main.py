'''
the sequential implementation: awaiting all line by line
'''

from fetch_data import *
async def get_dashboard_sequential(): 
    start = asyncio.get_event_loop().time()
    
    weather = await fetch_weather()
    stocks = await fetch_stocks()
    news = await fetch_news()
    
    end = asyncio.get_event_loop().time()
    
    print(f"\n All data collected:")
    print(f"1. {weather}")
    print(f"2. {stocks}")
    print(f"3. {news}")
    print(f"Total time: {end - start:.2f} second\n")
    
async def get_dashboard_concurrent():
    start = asyncio.get_event_loop().time()

    results = await asyncio.gather(fetch_weather(), fetch_stocks(), fetch_news())
    
    end = asyncio.get_event_loop().time()
    
    print(f"\n All data collected:")
    print(f"1. {results[0]}")
    print(f"2. {results[1]}")
    print(f"3. {results[2]}")
    print(f"Total time: {end - start:.2f} second\n")

if __name__ == '__main__':
    asyncio.run(get_dashboard_sequential())
    asyncio.run(get_dashboard_concurrent())
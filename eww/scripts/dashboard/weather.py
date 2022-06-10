import python_weather
import asyncio
import json
import warnings
import sys

async def getweather(city="Berlin"):
    client = python_weather.Client()

    weather = await client.find(city)
    weather = weather.current

    json_str = [city, weather.sky_text, str(weather.temperature) + "\N{DEGREE SIGN}C" ]
    
    print(json.dumps(json_str))

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":

    # fine to ignore in this case
    # https://github.com/pytest-dev/pytest-asyncio/issues/212
    warnings.filterwarnings("ignore", category=DeprecationWarning) 

    loop = asyncio.get_event_loop()

    if len(sys.argv) < 2:
        loop.run_until_complete(getweather())
    else:
        loop.run_until_complete(getweather(sys.argv[1]))
 
        
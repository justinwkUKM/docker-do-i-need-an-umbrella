from models.location import Location
import httpx


async def get_live_weather(location: Location):
    url = f'https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}&units=imperial'
    if location.state:
        url += f'&state={location.state}'
    print(location)

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        print(resp.status_code)
        # print(resp.text)
        data = resp.json()

    return data

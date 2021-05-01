
import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services import live_weather_service


router = fastapi.APIRouter()


# @router.get("/api/umbrella")
# def do_i_need_an_umbrella(city: str, state: Optional[str] = None, country: str = "us"):
#     return {"city": city}

@router.get("/api/umbrella", response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    data = await live_weather_service.get_live_weather(location=location)

    weather = data.get('weather', {})
    category = weather.get('category', "UNKNOWN")
    forecast = data.get('forecast', {})
    temp = forecast.get('temp', 0)

    bring = category.lower().strip() in {'rain', 'mist'}

    return UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)


# @router.get("/api/bring_umbrella")
# def bring_umbrella(umbrella_status: UmbrellaStatus):


@router.get("/api/umbrella_test")
def do_i_need_an_umbrella_test():
    return {"message": "here is your umbrella"}

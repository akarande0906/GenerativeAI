from mcp.server.fastmcp import FastMCP



# Create an MCP server
mcp = FastMCP("Simple MCP Server")

def main():
    mcp.run()

''' To be uncommented 
def _get_lat_long(city: str) -> tuple:
    """Get latitude and longitude for a given city."""
    # Hardcoded here. Needs to be better handled.
    latlong_endpoint = "https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    response = requests.get(latlong_endpoint.format(city=city))
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return (data['results'][0]['latitude'], data['results'][0]['longitude'])
    return (None, None)


def _get_weather(city: str) -> dict:

    # Get Lat Long from City name
    lat, long = _get_lat_long(city)
    if lat is not None and long is not None:
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

        # Hardcoded here. Needs to be better handled.
        weather_endpoint = "https://api.open-meteo.com/v1/forecast"

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = weather_endpoint
        params = {
            "latitude": lat,
            "longitude": long,
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "hourly": "temperature_2m",
            "current": ["temperature_2m", "wind_speed_10m"],
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation: {response.Elevation()} m asl")
        print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

        # Process current data. The order of variables needs to be the same as requested.
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        current_wind_speed_10m = current.Variables(1).Value()

        print(f"\nCurrent time: {current.Time()}")
        print(f"Current temperature_2m: {current_temperature_2m}")
        print(f"Current wind_speed_10m: {current_wind_speed_10m}")

        return {"Current Temperature": current_temperature_2m,
                "Current Wind Speed": current_wind_speed_10m}
    else:
        return "Sorry could not retrieve weather data for the specified city."

'''

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a weather resource
@mcp.resource("weather://{city}")
def get_weather(city: str) -> dict:
    """Get weather information for a given city"""
    return {"message": "Weather data functionality is currently disabled."}
    #return _get_weather(city)


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

if __name__ == "__main__":
    main()

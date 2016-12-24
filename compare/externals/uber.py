from uber_rides.session import Session
from uber_rides.client import UberRidesClient

def get_client():
    session = Session(server_token='SL_F7jj5JnXsdsVIBwzlEKSfX_LrjC8sot9x-lt0')
    client = UberRidesClient(session)
    return client

def get_estimate(start_lat,
                 start_lon,
                 end_lat,
                 end_lon,
                 seat_count=1):
    client = get_client()
    response = client.get_price_estimates(
        start_latitude=start_lat,
        start_longitude=start_lon,
        end_latitude=end_lat,
        end_longitude=end_lon,
        seat_count=seat_count
    )
    estimate = response.json.get('prices')
    return estimate

def get_products(current_lat,current_lon):
    client = get_client()
    products = client.get_products(latitude=current_lat,longitude=current_lon)
    return products
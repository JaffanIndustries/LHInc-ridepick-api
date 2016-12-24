from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session
from lyft_rides.client import LyftRidesClient

def _get_client():
    client_id = "qGNpATtQ5Fam"
    client_secret = "jfVQT7BlCVaRCueoaxA9rBznCX3lLzVr"
    auth_flow = ClientCredentialGrant(client_id=client_id, client_secret=client_secret, scopes="public")
    session = auth_flow.get_session()
    client = LyftRidesClient(session)
    return client

def get_estimates(start_lat,
                 start_lon,
                 end_lat,
                 end_lon):

    client = _get_client()
    response = client.get_cost_estimates(start_latitude=start_lat,start_longitude=start_lon,end_latitude=end_lat,end_longitude=end_lon)
    estimate = response.json.get('cost_estimates')
    return estimate

def get_products(current_lat, current_lon):

    client = _get_client()
    response = client.get_ride_types(latitude=current_lat, longitude=current_lon)
    all_products = response.json.get('ride_types')
    return all_products

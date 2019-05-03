import requests

api_base = 'https://maps.googleapis.com/maps/api/'
api_key = 'API-KEY'


def get_elevation(lat, lon):
    response = requests \
        .get(api_base + 'elevation/json?locations=' + str(lat) + ',' + str(lon+5) + '|' + str(lat+5) + ',' + str(
        lon) + '&key=' + api_key) \
        .json()
    return response['results']


print(get_elevation(-22.8712294, -41.9822979))

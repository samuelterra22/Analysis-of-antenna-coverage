from srtm import Srtm1HeightMapCollection
from srtm.base_coordinates import RasterBaseCoordinates
from haversine import haversine, Unit
from math import pi, cos

from src.main.python.support.physical_constants import r_earth

srtm1_data = Srtm1HeightMapCollection()
srtm1_data.build_file_index()
srtm1_data.load_area(RasterBaseCoordinates.from_file_name("S22W045"), RasterBaseCoordinates.from_file_name("S22W046"))


def get_altitude(lat: float, long: float) -> int:
    return srtm1_data.get_altitude(latitude=lat, longitude=long)


def calc_distance(point_1: tuple, point_2: tuple, unit=Unit.METERS) -> float:
    return haversine(point_1, point_2, unit=unit)


def get_new_lat_lng(latitude: float, longitude: float, dx: float = 3, dy: float = 3) -> tuple:
    new_latitude = latitude + (round(dy / r_earth, 6)) * (round(180 / pi, 6))
    new_longitude = longitude + (round(dx / r_earth, 6)) * (round(180 / pi, 6)) / cos(round(latitude * pi / 180, 6))
    return tuple(((new_latitude), (new_longitude)))
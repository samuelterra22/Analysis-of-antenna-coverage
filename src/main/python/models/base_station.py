#!/usr/bin/env python


class BaseStation:
    def __init__(self, data):
        self.status = data["status"]
        self.entity = data["entity"]
        self.num_fistel = data["num_fistel"]
        self.num_service = data["num_service"]
        self.num_ato = data["num_ato"]
        self.num_station = data["num_station"]
        self.address = data["address"]
        self.uf = data["uf"]
        self.cod_country = data["cod_country"]
        self.emission = data["emission"]
        self.initial_frequency = data["initial_frequency"]
        self.final_frequency = data["final_frequency"]
        self.azimute = data["azimute"]
        self.cod_station_type = data["cod_station_type"]
        self.cod_antenna_type = data["cod_antenna_type"]
        self.cod_equipment_antenna = data["cod_equipment_antenna"]
        self.gain_antenna = data["gain_antenna"]
        self.gain_coast_front_antenna = data["gain_coast_front_antenna"]
        self.lifting_angle_antenna = data["lifting_angle_antenna"]
        self.half_power_angle = data["half_power_angle"]
        self.polarization = data["polarization"]
        self.height = data["height"]
        self.cod_equipment_transmitter = data["cod_equipment_transmitter"]
        self.transmission_power = data["transmission_power"]
        self.latitude = data["latitude"]
        self.longitude = data["longitude"]
        self.first_license_date = data["first_license_date"]

    def __repr__(self):
        return str(self.__dict__)

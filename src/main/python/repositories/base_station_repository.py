#!/usr/bin/env python
from src.main.python.Exceptions.ApplicationException import ApplicationException
from src.main.python.repositories.contracts.base_station_repository_interface import (
    BaseStationRepositoryInterface,
)
from src.main.python.models.base_station import BaseStation


class BaseStationRepository(BaseStationRepositoryInterface):
    def get_all(self):
        """
        Return all BaseState elements
        :return:
        """
        try:
            return BaseStation.get()
        except BaseException:
            e = ApplicationException()
            print(e)
            return []

    def find_one_by_id(self, id):
        """
        This function return a base station row filtered by id.
        :param id: Id of base station in database
        :return: Return a BaseStation element
        """
        try:
            return BaseStation.get_by_id(id)
        except:
            return None

    def find_one_by(self, criteria):
        # Implementation here
        pass

    def store(self, data):
        bs = BaseStation(
            status=data['status'],
            entity=data['entity'],
            num_fistel=data['num_fistel'],
            num_service=data['num_service'],
            num_ato=data['num_ato'],
            num_station=data['num_station'],
            address=data['address'],
            uf=data['uf'],
            cod_country=data['cod_country'],
            emission=data['emission'],
            initial_frequency=data['initial_frequency'],
            final_frequency=data['final_frequency'],
            azimute=data['azimute'],
            cod_station_type=data['cod_station_type'],
            cod_antenna_type=data['cod_antenna_type'],
            cod_equipment_antenna=data['cod_equipment_antenna'],
            gain_antenna=data['gain_antenna'],
            gain_coast_front_antenna=data['gain_coast_front_antenna'],
            lifting_angle_antenna=data['lifting_angle_antenna'],
            half_power_angle=data['half_power_angle'],
            polarization=data['polarization'],
            height=data['height'],
            cod_equipment_transmitter=data['cod_equipment_transmitter'],
            transmission_power=data['transmission_power'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            first_license_date=data['first_license_date'],
        )
        return bs.save()

    def update(self, data, id):
        bs = BaseStation.get_by_id(id)
        bs.status = data['status']
        bs.entity = data['entity']
        bs.num_fistel = data['num_fistel']
        bs.num_service = data['num_service']
        bs.num_ato = data['num_ato']
        bs.num_station = data['num_station']
        bs.address = data['address']
        bs.uf = data['uf']
        bs.cod_country = data['cod_country']
        bs.emission = data['emission']
        bs.initial_frequency = data['initial_frequency']
        bs.final_frequency = data['final_frequency']
        bs.azimute = data['azimute']
        bs.cod_station_type = data['cod_station_type']
        bs.cod_antenna_type = data['cod_antenna_type']
        bs.cod_equipment_antenna = data['cod_equipment_antenna']
        bs.gain_antenna = data['gain_antenna']
        bs.gain_coast_front_antenna = data['gain_coast_front_antenna']
        bs.lifting_angle_antenna = data['lifting_angle_antenna']
        bs.half_power_angle = data['half_power_angle']
        bs.polarization = data['polarization']
        bs.height = data['height']
        bs.cod_equipment_transmitter = data['cod_equipment_transmitter']
        bs.transmission_power = data['transmission_power']
        bs.latitude = data['latitude']
        bs.longitude = data['longitude']
        bs.first_license_date = data['first_license_date']

        return bs.save()

    def delete(self, id):
        # Implementation here
        pass

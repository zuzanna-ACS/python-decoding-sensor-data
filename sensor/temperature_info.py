# Module 3: Work with integer data from temperature sensor
from house_info import HouseInfo


class TemperatureData(HouseInfo):
    def get_data(self, field, room=0):
        field_info = self.get_data_by_area(field, room)
        data = []
        for rec in field_info:
            # Convert string of integers into actual integers based 10
            data.append(int(rec, 10))
        return data

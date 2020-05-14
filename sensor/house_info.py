from load_data import load_sensor_data

class HouseInfo(object):
    def __init__(self, data):
        self.data = data
        

    def get_data_by_room(self, field, room=0):
        field_data = []
        # loop over records
        for record in self.data:
            # filter data by room
            if room == 0:                           # take all room
                field_data.append(record[field])
            elif room == int(record['room']):       # select room
                field_data.append(record[field])
        return field_data
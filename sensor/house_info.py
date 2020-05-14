from datetime import date

class HouseInfo(object):
    def __init__(self, data):
        self.data = data
        

    def get_data_by_area(self, field, area=0):
        field_data = []
        # loop over records
        for record in self.data:
            # filter data by area
            if area == int(record['area']):       # select area
                field_data.append(record[field])
            elif area == 0:
                field_data.append(record[field])
        return field_data
    
    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []
        # loop over records
        for record in self.data:
            # filter data by date
            if str(rec_date.strftime("%m/%d/%y")) == record['date']:       # select area
                field_data.append(record[field])
                # print(record['date'], str(rec_date.strftime("%m/%d/%y")))

        return field_data
# Runner script for all modules
from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import date,datetime
from humidity_info import HumidityData
from statistics import mean
from particle_count_info import ParticleData


##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))

# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id",rec_area = test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))
test_date = datetime.strptime("5/9/20","%m/%d/%y")
recs = house_info.get_data_by_date("id",rec_date=test_date)
print("\nHouse sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))

# Module 3 code here:


# Module 4 code here:
# humidity_data = HumidityData(data)
# particle_data = ParticleData(data)

# recs = humidity_data.get_data_by_area(rec_area=test_area)
# print("\nHouse Humidity sensor records for area {} = {}".format(test_area, len(recs)))
# print("\tAverage: {} humidity".format(mean(recs)))

# recs = humidity_data.get_data_by_date(rec_date=test_date)
# print("House Humidity sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
# print("\tAverrage: {} humidity".format(mean(recs)))

# recs = particle_data.get_data_by_area(rec_area=test_area)
# print("\nHouse Particle sensor records for area {} = {}".format(test_area, len(recs)))
# concentrations = particle_data.get_data_concentrations(data=recs)
# print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
# print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
# print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

# recs = particle_data.get_data_by_date(rec_date=test_date)
# print("\nHouse Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
# concentrations = particle_data.get_data_concentrations(data=recs)
# print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
# print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
# print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))
# Module 5 code here:
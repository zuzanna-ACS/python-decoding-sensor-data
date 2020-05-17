# Runner script for all modules
from load_data import load_sensor_data          # module 2
from house_info import HouseInfo
from datetime import date, datetime
from temperature_info import TemperatureData    # module 3
from humidity_info import HumidityData          # module 4
from statistics import mean
from particle_count_info import ParticleData          # module 5

#######################################
# Do not remove these two lines
# if you do, it will break the unittest
data = []                   # list to store data read from files
print("Sensor Data App")
#######################################

# Module 1
data = load_sensor_data()
# print(f"Loaded records {len(data)}")
print("Loaded records: {}".format(len(data)))

# Module 2
house_info = HouseInfo(data)
recs = house_info.get_data_by_area("id", rec_area=1)
print("House sensor records for area 1 = {}".format(len(recs)))

test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date("id", rec_date = test_date)
print("House sensor records for date: {} = {}".format(test_date.date(), len(recs)))
 
# Module 3
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=1)
print("House Temperature sensor records for area 1 = {}".format(len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

# test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = temperature_data.get_data_by_date(rec_date=test_date)
print("House Temperature sensor records for date: {} = {}".format(
    test_date.strftime("%m/%d/%y"), len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

# Module 4
humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=1)
print("House Humidity sensor records for area 1 = {}".format(len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))

# test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = humidity_data.get_data_by_date(rec_date=test_date)
print("House Humidity sensor records for date: {} = {}".format(
    test_date.strftime("%m/%d/%y"), len(recs)))
print("\tAverrage: {} humdity".format(mean(recs)))

# Module 5
particle_data = ParticleData(data)
# recs = particle_data.get_data_concentrations(data = particle_data.get_data_by_area(rec_area=1))
recs = particle_data.get_data_by_area(rec_area=1)
print("House Particle sensor records for area 1 = {}".format(len(recs)))
recs = particle_data.get_data_concentrations(data = particle_data.get_data_by_area(rec_area=1))
print("\tGood Air Quality Recs: {}".format(recs["good"]))
print("\tModerate Air Quality Recs: {}".format(recs["moderate"]))
print("\tBad Air Quality Recs: {}".format(recs["bad"]))

# test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = particle_data.get_data_by_date(rec_date=test_date)
print("House Particle sensor records for date: {} = {}".format(
    test_date.strftime("%m/%d/%y"), len(recs)))
recs = particle_data.get_data_concentrations(data = particle_data.get_data_by_date(rec_date=test_date))
print("\tGood Air Quality Recs: {}".format(recs["good"]))
print("\tModerate Air Quality Recs: {}".format(recs["moderate"]))
print("\tBad Air Quality Recs: {}".format(recs["bad"]))
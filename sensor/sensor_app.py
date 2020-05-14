# Runner script for all modules
from load_data import load_sensor_data           # Module 1 
from house_info import HouseInfo                 # Module 2
from datetime import date, datetime
from temperature_info import TemperatureData     # Module 3
from humidity_info import HumidityData           
from statistics import mean
from particle_count_info import ParticleData     # Module 4
from energy_info import EnergyData               # Module 5

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
house_info = HouseInfo(data)       # Create instance of HouseInfo

recs = house_info.get_data_by_area("id", area=1)
print("House sensor records for area 1 = {}".format(len(recs)))

rec_date = datetime.strptime("5/9/2020", "%m/%d/%Y")
recs = house_info.get_data_by_date("id", rec_date)
print("House sensor records for {} = {}".format(
       rec_date.date(), len(recs)))

# Module 3
print("\nProcessing Temperature Information")
house_temp = TemperatureData(data)
room1_temp = house_temp.get_data("temperature", 1)
room2_temp = house_temp.get_data("temperature", 2)
rooms_temp = house_temp.get_data("temperature")
print(f"Max Room 1 {max(room1_temp)}, min {min(room1_temp)}, avg {mean(room1_temp)}, records {len(room1_temp)}")
print(f"Max Room 2 {max(room2_temp)}, min {min(room2_temp)}, avg {mean(room2_temp)}, records {len(room2_temp)}")
print(f"Rooms Avg {mean(rooms_temp)}, records {len(rooms_temp)}")

print("\nProcessing Humidity Information")
house_humi = HumidityData(data)
room1_humi = house_humi.get_data("humidity", 1)
room2_humi = house_humi.get_data("humidity", 2)
rooms_humi = house_humi.get_data("humidity")
print(f"Max Room 1 {max(room1_humi)}%, min {min(room1_humi)}%, avg {mean(room1_humi)}%, records {len(room1_humi)}")
print(f"Max Room 2 {max(room2_humi)}%, min {min(room2_humi)}%, avg {mean(room2_humi)}%, records {len(room2_humi)}")
print(f"Rooms Avg {mean(rooms_humi)}%, records {len(rooms_humi)}")

# Module 4
print("\nProcessing ParticleCounter Information")
house_pc = ParticleData(data)
rooms_pc = house_pc.get_data("particulate")
rooms_aq = house_pc.get_concentrations(rooms_pc)
print("Good Air Quality Recs: {0}".format(rooms_aq["good"]))
print("Moderate Air Quality Recs: {0}".format(rooms_aq["moderate"]))
print("Bad Air Quality Recs: {0}".format(rooms_aq["bad"]))

# Module 5
print("\nProcessing Energy Consumption")
house_energy = EnergyData(data)
rooms_energy = house_energy.get_data("energy_usage")
print("Rooms records {0}".format(len(rooms_energy)))

energy = house_energy.calculate_energy_usage(rooms_energy)
print("Energy Consumption: {0:.2E} watts ".format(energy))
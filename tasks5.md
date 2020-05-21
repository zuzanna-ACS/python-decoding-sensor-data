# Decoding Data App

- [Decoding Data App](#decoding-data-app)
  - [Status](#status)
  - [Module 5: Analyze Energy Usage Data](#module-5-analyze-energy-usage-data)
    - [Local Verification Instructions](#local-verification-instructions)
    - [Task 1: Create EnergyData Class](#task-1-create-energydata-class)
    - [Task 2: Get Energy Data](#task-2-get-energy-data)
    - [Task 3: Convert Energy Data](#task-3-convert-energy-data)
    - [Task 4: Filter Energy Usage Data Records by Area and Date](#task-4-filter-energy-usage-data-records-by-area-and-date)
    - [Task 5: Get Total Energy Usage](#task-5-get-total-energy-usage)
    - [Task 6: Get Energy Data by Area with sensor_app](#task-6-get-energy-data-by-area-with-sensorapp)
    - [Task 7: Get Energy Data by Date with sensor_app](#task-7-get-energy-data-by-date-with-sensorapp)

## Status

Draft.

## Module 5: Analyze Energy Usage Data

### Local Verification Instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module5`

---

### Task 1: Create EnergyData Class

<!-- @pytest.mark.test_energy_create_class_module5 -->

The final data field we analyze is the energy usage. In this module, you will create a `EneryData` class that will process the energy consumption. Again, we will reuse a lot of the code writting so far.

To start, open the file called `energy_info.py` in the `sensor` folder.

At the top of the file, import `HouseInfo` from the `house_info` module.

Create a child class called `EnergyData` that inherits the properties and methods from the `HouseInfo` class.

Still in the `EnergyData` class, create two class contants to help us process the energy data.

The first constant is called `ENERGY_PER_BULB` and has the value of `0.2`.

The second contant is called `ENERGY_BITS` and it is set to the hexadecimal number `0x0F0`

create a private method called `_convert_data()` with two parameters, `self`, and `data`. This method will help us convert the temperature data.

In the body of the `_convert_area()` method, create a variable called `recs` and set it to an empty `list`.

---

### Task 2: Get Energy Data

<!-- @pytest.mark.test_energy_get_energy_method_module5 -->

Still in the `EnergyData` class, create a private method called `_get_energy()` with two parameters, `self`, and `rec`. This method will help us extract the energy data information from `energy_usage` data field.

Note: The `rec` input parameter is a string. This string represent the energy usage in hexadecimal notation form.

The `energy_sage` field comes as a 3 hexadecimal number (12 bits) form e.g `"0xfef"`. However, only the middle hex number (bits: 4-7 with index notation) represents the energy usage. In order to extract these bits, we will use [bitwise operations](https://docs.python.org/3/library/stdtypes.html?highlight=bitwise#bitwise-operations-on-integer-types)

To extract the energy information, three steps are required:

1) Update the value of `rec` by converting the `rec` string to an integer using `int()` constructor passing `rec` and `16` as the two arguments. Now that you have an integer, you can apply bitwise operations.

2) Isolate the energy bits by "anding" the `rec` integer with the `ENERGY_BITS` constant. This operation should clear all the bits from the first and third nibble.

3) Then, right shift the `rec` variable 4 bits.

Finally, your method should return `rec` at the very end of the method.

---

### Task 3: Convert Energy Data

<!-- @pytest.mark.test_energy_convert_method_module5 -->

Still in the `EnergyData` class, create a another private method called `_convert_data()` with two parameters, `self`, and `data`. This method will help us convert the energy data.

In the body of the `_convert_area()` method, create a variable called `recs` and set it to an empty `list`.

On a new line, create a `for` loop to iterate over `data` list. Use `rec` as your iterator variable.

Note: The `data` input parameter is a `list` of strings. These strings represent percentages of energy usage in hexadecimal form.

In the body of the `for` loop, convert the `rec` string values using the `_get_energy` private method, then, append them to `recs`.

Finally, your method should return `recs` (outside of the `for` loop, and the very end of the method).

---

### Task 4: Filter Energy Usage Data Records by Area and Date

<!-- @pytest.mark.test_energy_by_area_and_date_methods_module5 -->

Next, we are going to override `get_data_by_area` and `get_data_by_date` methods from the parent class.

At the top of the file, import `date` and `datetime` from the `datetime` module.

This time, when you call the parent `get_data_by_area` or `get_data_by_date` methods, use `"energy_usage"` as the filter value.

The methods should look like this:

```python
def get_data_by_area(self, rec_area=0):
    recs = super().get_data_by_area("energy_usage", rec_area)
    return self._convert_data(recs)

def get_data_by_date(self, rec_date=date.today()):
    recs = super().get_data_by_date("energy_usage", rec_date)
    return self._convert_data(recs)
```

---

### Task 5: Get Total Energy Usage

<!-- @pytest.mark.test_energy_calculate_usage_method_module5 -->

Next, add another method to the `EnergyData` class and called it `calculate_energy_usage`. The method should take two input paremeters, `self` and `data`. The purpose of this method is to take a list of energy usage values, calculate the cost per light bulb usage, and return the sum of all the values in the data list.

On a new line in the method, define a variable called `total_energy` and set sum of all converted values in the `data` list. To achieve this, call the [sum](https://docs.python.org/3/library/functions.html?highlight=sum#sum) built in function. This function should take a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20comprehension#list-comprehensions) as the only argument. The list comprehension should use `field` as the expression variable. The `field` variable should be multiply by the `ENERGY_PER_BULB` constant.

Finally, return the `total_energy` variable at the end of the method.

---

### Task 6: Get Energy Data by Area with sensor_app

<!-- @pytest.mark.test_sensor_app_energy_info_by_area_module5 -->

Open the `sensor_app.py` file in the `sensor` directory. At the top of the file, from the `energy_info` module, `import` `EnergyData`.

At the bottom of the file,  create an instance of the `EnergyData` class, and assign it to a variable named `energy_data`. Pass `data` as the input argument to the `EnergyData` constructor.

Create a variable called `recs` and set it to the `get_data_by_area()` method of the `particle_data` object. The `get_data_by_area()` method should take `rec_area=1` as the only argument.

Next, print the length of the `recs` list by area.

```python
print("\nHouse Energy sensor records for area 1 = {}".format(len(recs)))
```

Create a variable called `total_energy` and set it to the `calculate_energy_usage` method of the `energy_data` object passing the `data=recs` as the only argument.

Next, print each of the total energy usage.

```python
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output

House Energy sensor records for area 1 = 1000
        Energy Usage: 1.5e+03 Watts
```

FYI: the app will not validate your `print()` statements.

---

### Task 7: Get Energy Data by Date with sensor_app

<!-- @pytest.mark.test_sensor_app_energy_info_by_date_module5 -->

Still in the `sensor_app` file, set the `recs` variable to the return value of `get_data_by_date()` method of the `energy_data` object. The method takes `rec_date=test_date` as the only argument.

Next, print the `test_date` using the `strftime()` passing `"%m/%d/%y"` as the first argument, and the length of the `recs` list.

```python
print("House Energy sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
```

Create a variable called `total_energy` and set it to the `calculate_energy_usage` method of the `energy_data` object passing the `data=recs` as the only argument.

Next, print each of the total energy usage.

```python
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output
House Energy sensor records for area 1 = 1000
        Energy Usage: 1.5e+03 Watts
House Energy sensor records for date: 05/09/20 = 20
        Energy Usage: 1.9e+01 Watts
```

FYI: the app will not validate your `print()` statements.

---

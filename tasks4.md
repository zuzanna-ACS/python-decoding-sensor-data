# Decoding Data App

- [Decoding Data App](#decoding-data-app)
  - [Status](#status)
  - [Module 4: Analyze Humidity and Particle Concentration Data](#module-4-analyze-humidity-and-particle-concentration-data)
    - [Local Verification Instructions](#local-verification-instructions)
    - [Task 1: Create HumdidityData Class](#task-1-create-humdiditydata-class)
    - [Task 2: Convert Humidity Data](#task-2-convert-humidity-data)
    - [Task 3: Filter Humidity Data Records by Area](#task-3-filter-humidity-data-records-by-area)
    - [Task 4: Filter Humidity Data Records by Date](#task-4-filter-humidity-data-records-by-date)
    - [Task 5: Get Humidity Data by Area with sensor_app](#task-5-get-humidity-data-by-area-with-sensorapp)
    - [Task 6: Get Humidity Data by Date with sensor_app](#task-6-get-humidity-data-by-date-with-sensorapp)
    - [Task 7: Create ParticleData Class](#task-7-create-particledata-class)
    - [Task 8: Convert Particle Count Data](#task-8-convert-particle-count-data)
    - [Task 9: Filter Particle Count Data Records by Area and Date](#task-9-filter-particle-count-data-records-by-area-and-date)
    - [Task 10: Get Particle Count Concentrations](#task-10-get-particle-count-concentrations)
    - [Task 11: Return Particle Count Concentrations](#task-11-return-particle-count-concentrations)
    - [Task 12: Get Particle Data by Area with sensor_app](#task-12-get-particle-data-by-area-with-sensorapp)
    - [Task 13: Get Particle Data by Date with sensor_app](#task-13-get-particle-data-by-date-with-sensorapp)

## Status

Draft.

## Module 4: Analyze Humidity and Particle Concentration Data

### Local Verification Instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module4`

---

### Task 1: Create HumdidityData Class

<!-- @pytest.mark.test_humidity_create_class_module4 -->

Now that most of the heavy lifting has been done, in this module, you will create a `HumidityData` and `ParticleData` classes that will process the humidity and particle count data fields. We will reuse a lot of the code writting so far.

To start, open the file called `humidity_info.py` in the `sensor` folder.

At the top of the file, import `HouseInfo` from the `house_info` module.

Create a child class called `HumidityData` that inherits the properties and methods from the `HouseInfo` class.

Still in the `HumidityData` class, create a private method called `_convert_data()` with two parameters, `self`, and `data`. This method will help us convert the humidity data.

In the body of the `_convert_area()` method, create a variable called `recs` and set it to an empty `list`.

---

### Task 2: Convert Humidity Data

<!-- @pytest.mark.test_humidity_convert_loop_module4 -->

On a new line in the `_convert_data` method, create a `for` loop to iterate over `data`. Use `rec` as your iterator variable.

Note: The `data` input parameter is a `list` of strings. These strings represent percentages of humidity in floating point numeric form. You should use the [float() constructor](https://docs.python.org/3/library/functions.html?highlight=int#float) to convert these numbers.

In the body of the `for` convert the `rec` string values to float and multiply it by 100, then, append them to `recs`.

Finally, your method should return `recs` (outside of the `for` loop, and the very end of the method).

---

### Task 3: Filter Humidity Data Records by Area

<!-- @pytest.mark.test_humidity_by_area_method_module4 -->

Next, we are going to override `get_data_by_area` method from the parent class.

Here, we are going to repeat the process we did for the `TemperatureClass`. Create a method called `get_data_by_area()` with two parameters, `self` and `rec_area`. The `rec_area` parameter should have a default value of `0`, which translates to all records. The purpose of this method is to filter the humdity data by the `"area"` field. In this method `rec_area` maps to the `"area"` data column.

This method should be almost identical to the one you created for the `TemperatureData` class, with the exception of the field input argument. This time, use `"humidity"` as the filter value.

The method should look like this:

```python
def get_data_by_area(self, rec_area=0):
    recs = super().get_data_by_area("humidity", rec_area)
    return self._convert_data(recs)
```

---

### Task 4: Filter Humidity Data Records by Date

<!-- @pytest.mark.test_humidity_by_date_method_module4 -->

Similarly, we are going to override `get_data_by_date` method from the parent class.

At the top of the file, import `date` and `datetime` from the `datetime` module. See [date information](https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.date) and [datetime information](https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime)

We are going to repeat the process we did for the `TemperatureClass`. In the `HumidityData` class, create another method called `get_data_by_date()` with two parameters, `self`, and `rec_date`. The `rec_date` parameter should have a default value to today's day. You can accomplish this using the `date` module. The purpose of this method is to filter the humidity data by the `"date"` field. In this method, `rec_date` maps to the `"date"` data column.

This method should be almost identical to the one you created for the `TemperatureData` class, with the exception of the field input argument. This time, use `"humidity"` as the filter value.

The method should look like this:

```python
def get_data_by_date(self, rec_date=date.today()):
    recs = super().get_data_by_date("humidity", rec_date)
    return self._convert_data(recs)
```

---

### Task 5: Get Humidity Data by Area with sensor_app

<!-- @pytest.mark.test_sensor_app_temp_info_by_area_module4 -->

Open the `sensor_app.py` file in the `sensor` directory. At the top of the file, from the `humidity_info` module, `import` `HumidityData`.

At the bottom of the file,  create an instance of the `HumidityData` class, and assign it to a variable named `humidity_data`. Pass `data` as the input argument to the `HumidityData` constructor.

Next, create a variable called `recs` and set it to the `get_data_by_area()` method of the `humidity_data` object. The `get_data_by_area()` method should take `rec_area=1` as the only argument.

Next, print the length of the `recs` list by area. Then, print the arithmetic mean of the `recs` values. To calculate the arithmetic mean, at the top of the file, from the `stattistics` module, `import` `mean`.

```python
print("\nHouse Humidity sensor records for area 1 = {}".format(len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output

House Humidity sensor records for area 1 = 1000
  Average: 60.19 humidity
```

FYI: the app will not validate your `print()` statements.

---

### Task 6: Get Humidity Data by Date with sensor_app

<!-- @pytest.mark.test_sensor_app_temp_info_by_area_module4 -->

Still in the `sensor_app` file, set the `recs` variable to the return value of `get_data_by_date()` method of the `humidity_data` object. The method takes `rec_date=test_date` as the only argument.

Next, print the `test_date` using the `strftime()` passing `"%m/%d/%y"` as the first argument, and the length of the `recs` list. Then, print the average of the `recs` records.

```python
print("House Humidity sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
print("\tAverrage: {} humdity".format(mean(recs)))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output

House Humidity sensor records for area 1 = 1000
        Average: 60.19 humidity
House Humidity sensor records for date: 05/09/20 = 20
        Averrage: 54.8 humdity
```

FYI: the app will not validate your `print()` statements.

---

### Task 7: Create ParticleData Class

<!-- @pytest.mark.test_particle_create_class_module4 -->

Now, it is time to work on the `ParticleData` class. To start, open the file called `particle_count_info.py` in the `sensor` folder.

At the top of the file, import `HouseInfo` from the `house_info` module.

Create a child class called `ParticleData` that inherits the properties and methods from the `HouseInfo` class.

Still in the `ParticleData` class, create a private method called `_convert_data()` with two parameters, `self`, and `data`. This method will help us convert the particle data.

In the body of the `_convert_area()` method, create a variable called `recs` and set it to an empty `list`.

---

### Task 8: Convert Particle Count Data

<!-- @pytest.mark.test_particle_convert_loop_module4 -->

On a new line in the `_convert_data` method, create a `for` loop to iterate over `data`. Use `rec` as your iterator variable.

Note: The `data` input parameter is a `list` of strings. These strings represent particle concentrations in the air. The values are stored in scientific notation. To ceovnert this values, use the [float() constructor](https://docs.python.org/3/library/functions.html?highlight=int#float) to convert these numbers.

In the body of the `for` convert the `rec` string values to float and append them to `recs`.

Finally, your method should return `recs` (outside of the `for` loop, and the very end of the method).

---

### Task 9: Filter Particle Count Data Records by Area and Date

<!-- @pytest.mark.test_particle_by_area_and_date_methods_module4 -->

Next, we are going to override `get_data_by_area` and `get_data_by_date` methods from the parent class.

At the top of the file, import `date` and `datetime` from the `datetime` module.

This time, when you call the parent `get_data_by_area` or `get_data_by_date` methods, use `"particulate"` as the filter value.

The methods should look like this:

```python
def get_data_by_area(self, rec_area=0):
    recs = super().get_data_by_area("particulate", rec_area)
    return self._convert_data(recs)

def get_data_by_date(self, rec_date=date.today()):
    recs = super().get_data_by_date("particulate", rec_date)
    return self._convert_data(recs)
```

---

### Task 10: Get Particle Count Concentrations

<!-- @pytest.mark.test_particle_get_concentration_method_module4 -->

Next, add another method to the `ParticleData` class and called it `get_data_concentrations`. The method should take two input paremeters, `self` and `data`. The purpose of this method is to take a list of particle data values, and group the data based on particle concentration on the air.

On a new line in the method, define a dictionary called `particulate` and set the initial values for three keys: `"good"`, `"moderate"`, and `"bad"` all of them to the value of zero.

When the particle concentration is 50.0 units or less, then, it is considered `"good"`. When the concentration is more than 50.0 but up to 100.0, it is considered `"moderate"`. Anything above 100.0 is considered `"bad"`.

---

### Task 11: Return Particle Count Concentrations

<!-- @pytest.mark.test_particle_get_concentration_for_module4 -->

Create a loop over the `data` list using `rec` as the iterator.

In the body of the `for` loop,  update the `particulate` dictionary with the number of instances the `rec` value falls under the `"good"`, `"moderate"`, or `"bad"` category.

Finally, your method should return `particulate` (outside of the `for` loop, and the very end of the method)

---

### Task 12: Get Particle Data by Area with sensor_app

<!-- @pytest.mark.test_sensor_app_particle_info_by_area_module4 -->

Open the `sensor_app.py` file in the `sensor` directory. At the top of the file, from the `particle_count_info` module, `import` `ParticleData`.

At the bottom of the file,  create an instance of the `ParticleData` class, and assign it to a variable named `particle_data`. Pass `data` as the input argument to the `ParticleData` constructor.

Create a variable called `recs` and set it to the `get_data_by_area()` method of the `particle_data` object. The `get_data_by_area()` method should take `rec_area=1` as the only argument.

Next, print the length of the `recs` list by area.

```python
print("\nHouse Particle sensor records for area 1 = {}".format(len(recs)))
```

Create a variable called `concentrations` and set it to the `get_data_concentrations` method of the `particle_data` object passing the `data=recs` as the only argument.

Next, print each of the concentrations.

```python
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output

House Particle sensor records for area 1 = 1000
      Good Air Quality Recs: 284
      Moderate Air Quality Recs: 334
      Bad Air Quality Recs: 382
```

FYI: the app will not validate your `print()` statements.

---

### Task 13: Get Particle Data by Date with sensor_app

<!-- @pytest.mark.test_sensor_app_particle_info_by_date_module4 -->

Still in the `sensor_app` file, set the `recs` variable to the return value of `get_data_by_date()` method of the `humidity_data` object. The method takes `rec_date=test_date` as the only argument.

Next, print the `test_date` using the `strftime()` passing `"%m/%d/%y"` as the first argument, and the length of the `recs` list.

```python
print("\nHouse Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
```

Create a variable called `concentrations` and set it to the `get_data_concentrations` method of the `particle_data` object passing the `data=recs` as the only argument.

Next, print each of the concentrations by the test date.

```python
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output
House Particle sensor records for area 1 = 1000
        Good Air Quality Recs: 284
        Moderate Air Quality Recs: 334
        Bad Air Quality Recs: 382

House Particle sensor records for date: 05/09/20 = 20
        Good Air Quality Recs: 0
        Moderate Air Quality Recs: 0
        Bad Air Quality Recs: 20
```

FYI: the app will not validate your `print()` statements.

---

# Decoding Data App

- [Decoding Data App](#decoding-data-app)
  - [Status](#status)
  - [Module 3: Analyze Temperature](#module-3-analyze-temperature)
    - [M3: Local Verification Instructions](#m3-local-verification-instructions)
    - [M3: Task 1: Import HouseInfo](#m3-task-1-import-houseinfo)
    - [M3: Task 2: Create TempeartureData Class](#m3-task-2-create-tempearturedata-class)
    - [M3: Task 3: Convert Temperature Data](#m3-task-3-convert-temperature-data)
    - [M3: Task 4: Filter Temperature Data Records by Area](#m3-task-4-filter-temperature-data-records-by-area)
    - [M3: Task 5: Return Transformed Temperature Data Records by Area](#m3-task-5-return-transformed-temperature-data-records-by-area)
    - [M3: Task 6: Filter Temperature Data Records by Date](#m3-task-6-filter-temperature-data-records-by-date)
    - [M3: Task 7: Return Transformed Temperature Data Records by Date](#m3-task-7-return-transformed-temperature-data-records-by-date)
    - [M3: Task 8: Get Temperature Data by Area with sensor_app](#m3-task-8-get-temperature-data-by-area-with-sensorapp)
    - [M3: Task 8: Get Temperature Data by Date with sensor_app](#m3-task-8-get-temperature-data-by-date-with-sensorapp)

## Status

Draft.

## Module 3: Analyze Temperature

### M3: Local Verification Instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module3`

---

### M3: Task 1: Import HouseInfo
<!-- @pytest.mark.test_temperature_import_module3 -->

In this module, you will create a `TemperatureData` class that will process the temperature data fields.

To start, open the file called `temperature_info.py` in the `sensor` folder.

At the top of the file, import `HouseInfo` from the `house_info` module.

---

### M3: Task 2: Create TempeartureData Class

<!-- @pytest.mark.test_temperature_create_class_module3 -->

Create a child class called `TemperatureData` that inherits the properties and methods from the `HouseInfo` class.

Still in the `TemperatureData` class, create a private method called `_convert_data()` with two parameters, `self`, and `data`. This method will help us convert the temperature data.

In the body of the `_convert_area()` method, create a variable called `recs` and set it to an empty `list`.

---

### M3: Task 3: Convert Temperature Data

<!-- @pytest.mark.test_temperature_convert_loop_module3 -->

On a new line in the `_convert_data` method, create a `for` loop to iterate over `data`. Use `rec` as your iterator variable.

Note: The `data` input parameter is a `list` of strings. These strings are integers base 10 with the temperatures measurements. You should use the [int() constructor](https://docs.python.org/3/library/functions.html?highlight=int#int) to convert these numbers.

In the body of the `for` convert the `rec` string values to integers with base 10 and append them to `recs`.

Finally, your method should return `recs` (outside of the `for` loop, and the very end of the method).

---

### M3: Task 4: Filter Temperature Data Records by Area

<!-- @pytest.mark.test_temperature_by_area_method_module3 -->

Next, we are going to override `get_data_by_area` method from the parent class.

Create a method called `get_data_by_area()` with two parameters, `self` and `rec_area`. The `rec_area` parameter should have a default value of `0`, which translates to all records. The purpose of this method is to filter the temperature data by the `"area"` field. In this method `rec_area` maps to the `"area"` data column.

In the body of the `get_data_by_area()` method, create a variable called `recs` and set it to the parent `get_data_by_area` method. Pass `"temperature"` as the first argument, and `rec_area` input parameter as the second argument. Hint: parent class methods can be access by using [super](https://docs.python.org/3/library/functions.html?highlight=super#super).

---

### M3: Task 5: Return Transformed Temperature Data Records by Area

<!-- @pytest.mark.test_temperature_by_area_method_return_module3 -->

Still in the `get_data_by_area` method, `return` a call to the `_convert_data` private method passing `recs` as the only argument.

---

### M3: Task 6: Filter Temperature Data Records by Date

<!-- @pytest.mark.test_temperature_by_date_method_module3 -->

Similarly, we are going to override `get_data_by_date` method from the parent class.

Still in the `TemperatureData` class, create another method called `get_data_by_date()` with two parameters, `self`, and `rec_date`. The `rec_date` parameter should have a default value to today's day. You can accomplish this using the `date` module. The purpose of this method is to filter the temperature data by the `"date"` field. In this method, `rec_date` maps to the `"date"` data column.

At the top of the file, import `date` and `datetime` from the `datetime` module. See [date information](https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.date) and [datetime information](https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime)

In the body of the `get_data_by_date()` method, create a variable called `recs` and set it to the parent `get_data_by_date` method. Pass `"temperature"` as the first input argument, and `rec_date` input parameter as the second argument. Hint: parent class methods can be accss by using [super](https://docs.python.org/3/library/functions.html?highlight=super#super).

---

### M3: Task 7: Return Transformed Temperature Data Records by Date

<!-- @pytest.mark.test_temperature_by_date_method_return_module3 -->

Still in the `get_data_by_date` method, `return` a call to the `_convert_data` private method passing `recs` as the only argument.

### M3: Task 8: Get Temperature Data by Area with sensor_app

<!-- @pytest.mark.test_sensor_app_temp_info_by_area_module3 -->

Open the `sensor_app.py` file in the `sensor` directory. At the top of the file, from the `temperature_info` module, `import` the `TemperatureData`. 

At the bottom of the file,  create an instance of the `TemperatureData` class, and assign it to a variable named `temperature_data`. Pass `data` as the input argument to the `TemperatureData` constructor.

Next, create a variable called `recs` and set it to the `get_data_by_area()` method of the `temperature_data` object. The `get_data_by_area()` method should take `rec_area=1` as the only argument.

Print the length of the `recs` list, also, print the maximum and minimum values in the `recs` list.

```python
print("\nHouse Temperature sensor records for area 1 = {}".format(len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
... # previous output

House Temperature sensor records for area 1 = 1000
        Maximum: 80, Minimum: 60 temperatures
```

FYI: the app will not validate your `print()` statements.

---
---

### M3: Task 8: Get Temperature Data by Date with sensor_app

<!-- @pytest.mark.test_sensor_app_temp_info_by_date_module3 -->

Still in the `sensor_app` file, set the `recs` variable to the return value of `get_data_by_date()` method of the `temperature_data` object. The method takes `rec_date=test_date` as the only argument.

Print the `test_date` using the `strftime()` passing `"%m/%d/%y"` as the first argument, and the length of the `recs` list. Also print the maximum and minimum values in the `recs` list.

```python
print("\nHouse Temperature sensor records for area 1 = {}".format(len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output does not includes previous tasks:

```bash
...

House Temperature sensor records for area 1 = 1000
        Maximum: 80, Minimum: 60 temperatures

House Temperature sensor records for date: 05/09/20 = 20
        Maximum: 82, Minimum: 80 temperatures
```

FYI: the app will not validate your `print()` statements.
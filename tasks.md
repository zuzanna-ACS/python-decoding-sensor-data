# Decoding Data App

- [Decoding Data App](#decoding-data-app)
  - [Status](#status)
  - [Module 1: Load Sensor Data From Files](#module-1-load-sensor-data-from-files)
    - [Local verification instructions](#local-verification-instructions)
    - [M1: Task 1: Import os, glob, and csv](#m1-task-1-import-os-glob-and-csv)
    - [M1: Task 2: Create a Function to parse the data](#m1-task-2-create-a-function-to-parse-the-data)
    - [M1: Task 3: Sensor Data File Management](#m1-task-3-sensor-data-file-management)
    - [M1: Task 4: Read Data Files](#m1-task-4-read-data-files)
    - [M1: Task 5: Load Data Records](#m1-task-5-load-data-records)
    - [M1: Task 6: Get Sensor Data with sensor_app](#m1-task-6-get-sensor-data-with-sensorapp)
  - [Module 2: The HomeData Class](#module-2-the-homedata-class)
    - [Local Verification Instructions](#local-verification-instructions-1)
    - [M2: Task 1: Create a Class](#m2-task-1-create-a-class)
    - [M2: Task 2: Create Method to Select Data by Area](#m2-task-2-create-method-to-select-data-by-area)
    - [M2: Task 3: Filter Data Records by Area](#m2-task-3-filter-data-records-by-area)
    - [M2: Task 4: Create Method to Select Data by Date](#m2-task-4-create-method-to-select-data-by-date)
    - [M2: Task 5: Filter Data Records by Date](#m2-task-5-filter-data-records-by-date)
    - [M2: Task 6: Get HouseInfo Data by Area with sensor_app](#m2-task-6-get-houseinfo-data-by-area-with-sensorapp)
    - [M2: Task 7: Get HouseInfo Data by Date with sensor_app](#m2-task-7-get-houseinfo-data-by-date-with-sensorapp)
  - [Module 3: Analyze Temperature and Humidity Data](#module-3-analyze-temperature-and-humidity-data)
  - [Module 4: Analyze Air Quality Data](#module-4-analyze-air-quality-data)
  - [Module 5: Analyze Energy Consumption Data](#module-5-analyze-energy-consumption-data)

## Status

Draft.

## Module 1: Load Sensor Data From Files

In this first module, you will write a function to load the sensor data stored in the data files. The sensor data is stored in CSV files

### Local verification instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module1`

### M1: Task 1: Import os, glob, and csv

[//]:# (@pytest.mark.test_load_data_import_module1)

The dataset for this project is stored in several CSV files found in the `dataset` folder. It represents the data from a device with multiple sensors. The data was collected at random times over a period of days. The records include measurements of temperature, humidity, energy consumption, and particle count in the air over a given area. The data is collected over a period of 24 hours.  

To start, open the file called `load_data.py` in the `sensor` folder.

At the top of the file, create three import statements for `os`, `glob`, and `csv`. These libraries will allow us to work with a collection of files.

### M1: Task 2: Create a Function to parse the data

[//]:# (@pytest.mark.test_load_data_load_sensor_func_module1)

Create a function called `load_sensor_data()` that has no parameters.
In the body of the `load_sensor_data()` function, create a variable called `sensor_data` and set it to an empty list.

### M1: Task 3: Sensor Data File Management

[//]:# (@pytest.mark.test_load_data_sensor_files_module1)

Next, create a variable called `sensor_files` that is set to a call to the `glob.glob()` function.

Pass the glob function a single argument, a call to the `os.path.join()` function.

In turn pass `os.path.join()` three arguments: `os.getcwd()`, `"datasets"`, and `"*.csv"`.

Your statement should look like this:

```python
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
```

### M1: Task 4: Read Data Files

[//]:# (@pytest.mark.test_load_data_read_files_module1)

The `sensor_files` object contains a list of file names i.e. ['SENSOR_ROOM2', 'SENSOR_ROOM1']

To read the sensor data of these files, three steps are required:

1) Create one `for` loop that loops through `sensor_files` using `sensor_file` as the iterator variable.

2) In the body of this loop use a `with` statement to `open` the `sensor_file` and set the alias to `data_file`.

3) In the `with` body, set a variable called `data_reader` equal to `csv.DictReader()`. Pass in the current `data_file` as the first argument, and set the `delimiter=','` as the second argument. The `data_reader` will contain a list of ordered dictionaries with the sensor data records.

### M1: Task 5: Load Data Records

[//]:# (@pytest.mark.test_load_data_load_recs_module1)

Now that you have access to the data in each file, the next step is to load each record into the `sensor_data` list.

Within the `with`, create a second `for` loop to `data_file` to get access to each record. Use `row` as your iterator variable.

Inside the body of the second `for` loop, append each `row` record to the `sensor_data` list (you created this list earlier in the _Create a Function to Parse the Data_ task).

Finally, your function should return `sensor_data` (outside of all `for` loops, and the very end of the function).

### M1: Task 6: Get Sensor Data with sensor_app

[//]:# (@pytest.mark.test_sensor_app_load_data_return_module1)

Let's set up the command line interface (CLI). Open the `sensor_app.py` file in the `sensor` directory of the project.

At the top of the file, from the `load_data` module, `import` the `load_sensor_data` function.

Then, below the two initial lines of code provided in the file

```python
data = 0
print("Sensor Data App")
```

set the `data` variable equal to `load_sensor_data()`.

Print the length of the `data` list using the [formatted string](https://docs.python.org/3/library/string.html#formatstrings) form  `str.format()`. Remember, each data file contains 1000 records. So your output should look similar to this:

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output:

<!-- TODO: Update information in content tools -->
```bash
Sensor Data App
Loaded records: 2000
```

FYI: the app will not validate your `print()` statements.

---
---

## Module 2: The HomeData Class

---

### Local Verification Instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module2`

---

### M2: Task 1: Create a Class

<!-- @pytest.mark.test_house_info_create_class_module2 -->

In this module, you will create a `HomeInfo` class that will help us process the sensor data records. This class will later serve as base class for other classes.

To start, open the file called `house_info.py` in the `sensor` folder.

Create a class called `HomeInfo`. Next, create a `HomeInfo` class constructor with two parameters, `self` and `data`.

In the body of the constructor, assign the `data` input parameter to a class attribute with the same name. Hint: class attributes are prefixed with `self`.

---

### M2: Task 2: Create Method to Select Data by Area

<!-- @pytest.mark.test_house_info_get_data_by_area_module2 -->

Still in the `HouseInfo` class, create a method called `get_data_by_area()` with three parameters, `self`, `field`, and `rec_area`. The `rec_area` parameter should have a default value of `0`, which translates to all records. The purpose of this method is to filter data by `rec_area` key and `field` value.

***Note: The valid `field` values are the column names of the data files in the `datasets` folder***.

In the body of the `get_data_by_area` method, create a variable called `field_data` and set it to an empty `list`.

---

### M2: Task 3: Filter Data Records by Area

<!-- @pytest.mark.test_house_info_get_data_by_area_loop_module2 -->

On a new line in the `get_data_by_area` method, create a `for` loop to iterate over `self.data`. Use `record` as your iterator variable.

Remember that `self.data` class variable is a `list` of dictionaries.

Now, in the body of the `for` loop, create a control structure with the following rules:

- If the method is called with two arguments
  - select the records (key = area) that matches the `rec_area` input parameter
  - append to the `field_data` list the value of the record which `key` equals the `field` input parameter..
- If the method is called with one argument, the default `rec_data` values is used. In this case `0` means all records.
  - select all records
  - append to the `field_data` list the value of the record which `key` equals the `field` input parameter.

Finally, your method should return `field_data` (outside of the `for` loop, and the very end of the method).

---

### M2: Task 4: Create Method to Select Data by Date

<!-- @pytest.mark.test_house_info_get_data_by_date_module2 -->

Still in the `HouseInfo` class, create another method called `get_data_by_date()` with three parameters, `self`, `field`, and `rec_date`. The `rec_date` parameter should have a default value to today's day. You can accomplish this using the `date` module.

At the top of the file, import `date` and `datetime` from the `datetime` module. See [date information](https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.date) and [datetime information](https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime)

In the body of the `get_data_by_date` method, create a variable called `field_data` and set it to an empty `list`.

---

### M2: Task 5: Filter Data Records by Date

<!-- @pytest.mark.test_house_info_get_data_by_date_loop_module2 -->

On a new line in the `get_data_by_date` method, create a `for` loop to iterate over `self.data`. Use `record` as your iterator variable.

Now, in the body of the `for` loop, create an:wa
 `if` statement that selects those records whose `date` key matches the `rec_date` input parameter.

In order to compare `record['date']` field, which is a string, to a `rec_date` which is date object, a casting of the `rec_date` object is required. This could be achieve with the [strftime](https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.date.strftime) method. The `strftime()` should take date format `"%m/%d/%y"`, which is the format of your data.

Append the value of the record which `key` equals the `field` input parameter to the `field_data` list.

Finally, your method should return `field_data` (outside of the `for` loop, and the very end of the method).

---

### M2: Task 6: Get HouseInfo Data by Area with sensor_app

<!-- @pytest.mark.test_sensor_app_house_info_by_area_module2 -->

Open the `sensor_app.py` file in the `sensor` directory of the project, and add the following code:

At the top of the file, from the `house_info` module, `import` the `HouseInfo`.

At the bottom of the file,  create an instance of the `HouseInfo` class and call it `house_info`. The `HouseInfo` should take the `data` list as the argument.

Next, create a variable called `recs` and set it to the return value of `get_data_by_area()` method of the `house_info` object. The `get_data_by_area()` method should take `"id"` as the first argument, and `rec_area=1` as the second argument.

To test it, print the length of the `recs` list using the [formatted string](https://docs.python.org/3/library/string.html#formatstrings) form. 

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output including previous tasks:

```bash
Sensor Data App
Loaded records: 2000
House sensor records for area 1 = 1000
```

FYI: the app will not validate your `print()` statements, so you may test other scenarios to filter other data.

---

### M2: Task 7: Get HouseInfo Data by Date with sensor_app

<!-- @pytest.mark.test_sensor_app_house_info_by_date_module2 -->

Still in the `sensor_app` file, add the following code:

At the top of the file, from the `datetime` module, `import` the `date` and `datetime`.

At the bottom of the file, create a variable called `temp_date` and set it to the call of `datetime.strptime()` which takes `"5/9/20"` as the first argument, and "`%m/%d/%y"` as the second argument.

Next, set the `recs` variable to the return value of `get_data_by_date()` method of the `house_info` object. The method takes `"id"` as the first argument, and `rec_date=temp_date` as the second argument.

To test it, print the length of the `recs` list using the [formatted string](https://docs.python.org/3/library/string.html#formatstrings) form.

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output including previous tasks:

```bash
Sensor Data App
Loaded records: 2000
House sensor records for area 1 = 1000
House sensor records for 2020-05-09 = 20
```

FYI: the app will not validate your `print()` statements, so you may test other scenarios to filter other data.

---
---

## Module 3: Analyze Temperature and Humidity Data

---
---

## Module 4: Analyze Air Quality Data

---
---

## Module 5: Analyze Energy Consumption Data

---
---


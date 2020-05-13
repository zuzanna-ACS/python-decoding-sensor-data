# Module 1 - The Sensor Class

- [Module 1 - The Sensor Class](#module-1---the-sensor-class)
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
    - [M2: Task 1: Import load_sensor_data](#m2-task-1-import-loadsensordata)
    - [M2: Task 2: Create a Class](#m2-task-2-create-a-class)
    - [M2: Task 3:](#m2-task-3)
    - [M2: Task 4:](#m2-task-4)
  - [Module 3: Analyze Temperature Data](#module-3-analyze-temperature-data)
  - [Module 4: Analyze Humidity Data](#module-4-analyze-humidity-data)
  - [Module 5: Analyze Air Quality Data](#module-5-analyze-air-quality-data)
  - [Module 6: Analyze Energy Consumption Data](#module-6-analyze-energy-consumption-data)

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

At the top,  from the `load_data` module, `import` the `load_sensor_data` function.

Define variable called `data` and set it equal to `load_sensor_data()`.

Print the length of the `data` list using the [formatted string](https://docs.python.org/3/library/string.html#formatstrings) form  `str.format()`. Remember, each data file contains 1000 records. So your output should look like this:

```bash
Loaded records: [2000]
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

## Module 2: The HomeData Class

### Local Verification Instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module2`

### M2: Task 1: Import load_sensor_data

[//]:# (@pytest.mark.test_house_info_import_module2)

In this module, you will create a `HomeData` class that will help us process the sensor data records.

To start, open the file called `house_info.py` in the `sensor` folder. At the top of the file, import `load_sensor_data` from the `load_info` module.

### M2: Task 2: Create a Class

[//]:# (@pytest.mark.test_house_info_create_class_module2)

Below the import you just wrote, create a class called `HomeData`. Next, create a `HomeData` class constructor that accepts two arguments `self` and `data`.

In the constructor, assign the `data` input parameter to a class attribute with the same name. Hint: class attributes are prefixed with self.

### M2: Task 3:

### M2: Task 4:

## Module 3: Analyze Temperature Data

## Module 4: Analyze Humidity Data

## Module 5: Analyze Air Quality Data

## Module 6: Analyze Energy Consumption Data

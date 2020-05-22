# Decoding Data App

- [Decoding Data App](#decoding-data-app)
  - [Status](#status)
  - [Module 2: The HomeData Class](#module-2-the-homedata-class)
    - [Local Verification Instructions](#local-verification-instructions)
    - [M2: Task 1: Create a Class](#m2-task-1-create-a-class)
    - [M2: Task 2: Create Method to Select Data by Area](#m2-task-2-create-method-to-select-data-by-area)
    - [M2: Task 3: Filter Data Records by Area](#m2-task-3-filter-data-records-by-area)
    - [M2: Task 4: Create Method to Select Data by Date](#m2-task-4-create-method-to-select-data-by-date)
    - [M2: Task 5: Filter Data Records by Date](#m2-task-5-filter-data-records-by-date)
    - [M2: Task 6: Get HouseInfo Data by Area with sensor_app](#m2-task-6-get-houseinfo-data-by-area-with-sensorapp)
    - [M2: Task 7: Get HouseInfo Data by Date with sensor_app](#m2-task-7-get-houseinfo-data-by-date-with-sensorapp)

## Status

Draft.

## Module 2: The HomeData Class

---

### Local Verification Instructions

To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module2`

---

### M2: Task 1: Create a Class

<!-- @pytest.mark.test_house_info_create_class_module2 -->

In this module, you will create a `HouseInfo` class that will help us process the sensor data records. This class will later serve as base class for other classes.

To start, open the file called `house_info.py` in the `sensor` folder.

Create a class called `HouseInfo`. Next, create a `HouseInfo` class constructor with two parameters, `self` and `data`.

In the body of the constructor, assign the `data` input parameter to a class attribute with the same name. Hint: class attributes are prefixed with `self`.

---

### M2: Task 2: Create Method to Select Data by Area

<!-- @pytest.mark.test_house_info_get_data_by_area_module2 -->

Still in the `HouseInfo` class, create a method called `get_data_by_area()` with three parameters, `self`, `field`, and `rec_area`. The `rec_area` parameter should have a default value of `0`, which translates to all records. The purpose of this method is to filter the data using `rec_area` as the key, and `field` as the value.

***Note: The valid `field` values are the column names of the data files in the `datasets` folder***.

In the body of the `get_data_by_area()` method, create a variable called `field_data` and set it to an empty `list`.

---

### M2: Task 3: Filter Data Records by Area

<!-- @pytest.mark.test_house_info_get_data_by_area_loop_module2 -->

On a new line in the `get_data_by_area` method, create a `for` loop to iterate over `self.data`. Use `record` as your iterator variable.

Note: The `self.data` class variable is a `list` of dictionaries. The dictionary keys are equal to the columns names in the data files. e.g. when the `field` input parameter is set to `"id"` then, the `record[field]` value corresponds to the `"id"` column values. In this method, the `rec_area` variable maps to `'area'` column values.

In the body of the `for` loop, select records according to the following control structures:

- Create an if statement that is true when `rec_area` is equal to 0
  - In the body of the `if`, append to the `record[field]` values to the `field_data` list.

- Create an else if statement that is true when `rec_area` is equal to `record['area']` value. In order to compare the `rec_area` integer object to the `record['area']` string object, the later needs to be converted to an integer using the [int() constructor](https://docs.python.org/3/library/functions.html?highlight=int#int).
  - In the body of the `elif`, append to the `record[field]` values to the `field_data` list.


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

Note: In this method, the `rec_date` input parameter maps to `'date'` column values.

Now, in the body of the `for` loop, create an `if` statement that's true when the current record's `date` is equal to `rec_date`. In order to compare `record['date']` string object to `rec_date` which is date object, convert `rec_date` to string using the [strftime method](https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.date.strftime) method. The `strftime()` should take date format `"%m/%d/%y"`, which is the format of your data.



In the body of the if statement, append to `field_data` the dictionary values whose record key is equal to `field` input parameter.

Finally, your method should return `field_data` (outside of the `for` loop, and the very end of the method).

---

### M2: Task 6: Get HouseInfo Data by Area with sensor_app

<!-- @pytest.mark.test_sensor_app_house_info_by_area_module2 -->


Open the `sensor_app.py` file in the `sensor` directory. At the top of the file, from the `house_info` module, `import` the `HouseInfo`.


At the bottom of the file,  create an instance of the `HouseInfo` class, and assign it to a variable named `house_info`. Pass the `HouseInfo` constructor `data` as its argument.

Next, create a variable called `recs` and set it to the `get_data_by_area()` method of the `house_info` object. The `get_data_by_area()` method should take `"id"` as the first argument, and `rec_area=1` as the second argument.

Print the length of the `recs` list using the formatted string:

```python
print("\nHouse sensor records for area 1 = {}".format(len(recs)))
```

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

FYI: the app will not validate your `print()` statements.

---

### M2: Task 7: Get HouseInfo Data by Date with sensor_app

<!-- @pytest.mark.test_sensor_app_house_info_by_date_module2 -->

Still in the `sensor_app` file, at the top of the file, from the `datetime` module, `import` the `date` and `datetime`.

At the bottom of the file, create a variable called `test_date` and set it to the call of `datetime.strptime()` which takes `"5/9/20"` as the first argument, and "`%m/%d/%y"` as the second argument.

Next, set the `recs` variable to the return value of `get_data_by_date()` method of the `house_info` object. The method takes `"id"` as the first argument, and `rec_date=test_date` as the second argument.

Print the `test_date` using the `strftime()` passing `"%m/%d/%y"` as the input parameter, and the length of the `recs` list using the formatted string:

```python
print("House sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
```

To preview your app, open a terminal at the root of the project and run the following command:

```bash
python sensor/sensor_app.py
```

Sample output including previous tasks:

```bash
Sensor Data App
Loaded records: 2000

House sensor records for area 1 = 1000
House sensor records for date: 05/09/20 = 20
```

FYI: the app will not validate your `print()` statements.


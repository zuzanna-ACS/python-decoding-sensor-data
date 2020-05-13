import pytest
import json


@pytest.mark.test_house_info_import_module2
def test_house_info_import_module2(parse):

    # from load_data import load_sensor_data

    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_import = house_info.from_imports(
        "load_data", "load_sensor_data")
    assert house_info_import, "Are you importing `load_sensor_data` from load_data?"


@pytest.mark.test_house_info_create_class_module2
def test_house_info_create_class_module2(parse):
    # class HouseInfo():
    #     def __init__(self, data):
    #         self.data = data

    house_info = parse("house_info")
    assert house_info.success, house_info.message

    
    # house_info_class = house_info.get_by_name("class", "HouseInfo")
    # assert (
    #     house_info_class.exist
    # ), "Have you created a class called `Site` in the `site.py` file?"
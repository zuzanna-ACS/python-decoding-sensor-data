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

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    class_init = house_info.class_("HouseInfo").method("__init__")
    assert class_init.exists(), "Are you defining a constructor called `__init__`?"
    
    class_init_q = house_info.query("class HouseInfo(): ??")
    test_method = "__init__"
    class_init_arguments= (
        class_init_q.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "__init__",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "data",
                "args_args_1_annotation": "nil",
            }
        )
        .exists()
    )
    assert (
        class_init_arguments
    ), """Are you defining a constructor for the `HouseInfo` class?
        Are you declaring the correct name and number of parameters?"""
    
    # Check for assignment 
    self_data_exists = (
        class_init_q.def_args_(test_method).match(
            {
                "body_0_type": "Assign",
                "body_0_targets_0_type": "Attribute",
                "body_0_targets_0_value_type": "Name",
                "body_0_targets_0_value_id": "self",
                "body_0_targets_0_attr": "data",
                "body_0_value_type": "Name",
                "body_0_value_id": "data",
            }
        )
        .exists()
    )
    assert (
        self_data_exists
    ), """Are you assigning the correct value to `self.data`?"""
    
    
@pytest.mark.test_house_info_get_data_by_room_module2
def test_house_info_get_data_by_room_module2(parse):
    
    # def get_data_by_room(self, field, room=0):
        # data = []
    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    data_by_room = house_info.class_("HouseInfo").method("get_data_by_room")
    assert data_by_room.exists(), "Are you defining a method called `get_data_by_room?"

    test_method = "get_data_by_room"
    data_by_room_arguments= (
        house_info_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": test_method,
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "field",
                "args_args_1_annotation": "nil",
                "args_args_2_type": "arg",
                "args_args_2_arg": "room",
                "args_args_2_annotation": "nil",
                "args_vararg": "nil",
                "args_kwarg": "nil",
                "args_defaults_0_type": "Constant",
                "args_defaults_0_value": 0,
            }
        )
        .exists()
    )
    assert (
        data_by_room_arguments
    ), """Are you defining a method `get_data_by_room` 
        with the correct name and number of parameters?
        Are you setting the third parameter's default value to zero?"""

    
    data_list = (
        data_by_room.assign_().match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "field_data",
                "value_type": "List"
            }
        )
        .exists()
    )
    assert (
        data_list
    ), "Are you creating a variable called `field_data` set equal to an empty list?"


@pytest.mark.test_house_info_get_data_by_room_loop_module2
def test_house_info_get_data_by_room_loop_module2(parse):
    
    #     for record in self.data:
    #         if room == 0:                           # take all room
    #             field_data.append(record[field])
    #         elif room == int(record['room']):       # select room
    #             field_data.append(record[field])
    #     return field_data

    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    data_by_room = house_info.class_("HouseInfo").method("get_data_by_room")
    assert data_by_room.exists(), "Are you defining a method called `get_data_by_room?"

    test_method = "get_data_by_room"
    first_for = (
        data_by_room.for_().match(
            {

                "target_type": "Name",
                "target_id": "record",
                "iter_type": "Attribute",
                "iter_value_type": "Name",
                "iter_value_id": "self",
                "iter_attr": "data"
            }
        )
        .exists()
    )
    assert (
        first_for
    ), """Do you have a `for` loop, looping through `self.data`? 
        Is the current loop value called `record`?"""

    print("1)", json.dumps(house_info_class.def_args_(test_method).n, indent=4))  # TODO Remove
    print("2)", json.dumps(data_by_room.for_().n, indent=4))  # TODO Remove
    # assert False

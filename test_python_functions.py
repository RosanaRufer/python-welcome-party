from python_functions import append_element_to_list

def test_append_value_to_list():
    result = append_element_to_list(element = 3, list = [1, 2])
    assert result == [1, 2, 3]

def test_append_value_one():
    result = append_element_to_list(element = 12)
    assert result == [12]

def test_append_value_two():
    result = append_element_to_list(element = 42)
    # assert result == [42]
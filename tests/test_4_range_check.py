test_list = ['Blue', 'Green', 'Yellow', 'Red', 'Orange']

def range_check(input_type, list_type, return_direction, continue_direction):
    con_type = int(input_type)
    if con_type not in range(1,(len(list_type))+1):
        main_variable = return_direction
    if con_type in range(1, (len(list_type)) + 1):
        con_type -= 1
        main_variable = continue_direction
    return main_variable, con_type

def test_correct_range_normal_input(): #common case
    result1, result2 = range_check("2", test_list, 'x', 'y')
    assert result1, result2 == ('y', '1')

def test_out_of_range_normal_input(): #common case
    result1, result2 = range_check("5", test_list, 'x', 'y')
    assert result1, result2 == ('x', '5')

def test_out_of_range_negative_integer(): #corner case
    result1, result2 = range_check('-1', test_list, 'x', 'y')
    assert result1, result2 == ('x', '-1')
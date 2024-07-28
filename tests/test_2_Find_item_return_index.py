#Test 2, check for item string return index of item
dog = {"Animal": "Dog", "Color": "Blue"}
cat = {"Animal": "Cat", "Color": "Yellow"}
hippo = {"Animal" : "Hippo", "Color": "Gray"}
giraffe = {"Animal" : "Giraffe", "Color": "Red"}
monkey = {"Animal" : "Monkey", "Color" : "Brown"}
whale = {"Animal" : "Whale", "Color" : "Blue"}

test_list = [dog, cat, hippo, giraffe, monkey, whale]

def check_for_item_return_index(input_type, list_type, key_type, return_direction, continue_direction):
    try:
        find_name_of_dict_item = next(item for item in list_type if item[key_type].lower() == input_type.lower())
        con_type = list_type.index(find_name_of_dict_item)
        main_variable = continue_direction
    except StopIteration:
        con_type = ""
        main_variable = return_direction
    return main_variable, con_type

def test_correct_index_for_word_in_list_key_type_1(): #Common case with upper case input
    result_1, result_2 = check_for_item_return_index("CAT", test_list, 'Animal', "x", "y")
    assert result_1, result_2 == (1, "y") 

def test_correct_index_for_word_in_list_key_type_2(): #Common case with lower case input
    result_1, result_2 = check_for_item_return_index("red", test_list, "Color", "x", "y")
    assert result_1, result_2 == (3, "y")

def test_error_thrown_if_not_found(): #Common case with item not present
    result_1, result_2 = check_for_item_return_index("dolphin", test_list, "Animal", "x", "y")
    assert result_1, result_2 == ("", "x")

def test_error_thrown_if_user_inputs_digits(): #Edge case where user inputs digits
    result_1, result_2 = check_for_item_return_index("4", test_list, 'Animal', "x", "y")
    assert result_1, result_2 == ("", "x")

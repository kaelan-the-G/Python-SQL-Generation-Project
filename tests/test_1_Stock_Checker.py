#Test 1: Stock Must be integer function
def stock_checker(stock_input, return_direction, continue_direction):
    if stock_input.isdigit() == False:
        main_variable = return_direction
    if stock_input.isdigit() == True:
        main_variable = continue_direction
    return main_variable

def test_stock_checker_word(): #Corner case
    result = stock_checker("pollywog", "x", "y")
    assert result == "x"

def test_stock_checker_spaced_integers(): #Corner case
    result = stock_checker("1 3 6 7", "x", "y")
    assert result == "x"

def test_stock_checker_words_and_numbers(): #Corner case
    result = stock_checker("1dog", "x", "y")
    assert result == "x"

def test_stock_checker_integer(): #Common case
    result = stock_checker("5", "x", "y")
    assert result == "y"

def test_stock_checker_massive_number(): #Edge case
    big_number = str(10 * 100000000)
    result = stock_checker(big_number, "x", "y")
    assert result == "y"

def test_stock_checker_decimal(): #Corner case
    result = stock_checker("0.001", "x", "y")
    assert result == "x"


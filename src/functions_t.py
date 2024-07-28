#Importing all nessecary modules and variables I have stored in other files

import csv
from Input_Modules import(main_valid_inputs)
import pymysql
import os
from dotenv import load_dotenv

#Loading dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

#I have grouped the following functions on being related to structure and presentation that is globally present throughout the project code

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def error_print_and_list_after_clear_screen(error_print, input_type):
    if error_print == "ynf":
        print(error_messages(input_type, "not found"))
    if error_print == "yr":
        print(error_messages(input_type, "range"))
    if error_print == "yg":
        print(error_messages(input_type, "general"))

def error_messages(input_type, message_type):
    if message_type == "general":
        error_message = f"""    
ERROR -----------------------------       
                                         
    "{input_type}" is not recognized
    Please try again: 

"""
    if message_type == "price":
        error_message = f"""
ERROR -----------------------------
                                          
    "{input_type}" not recognized as a valid price
    Price must be a number
    For including pence use a period (.) after pounds

    Please try again"""
    if message_type == "range":
        error_message = f"""
ERROR -----------------------------
                                          
    There is no number {input_type} currently in the list
    Please try again
→ """
    if message_type == "adder":
        error_message = f"""
ERROR -----------------------------
                                          
    There is no number {input_type} currently in the list
    Ignoring
"""
    if message_type == "not found":
        error_message = f"""
ERROR -----------------------------
                                          
    "{input_type}" not found
    Please try again
→ """
    if message_type == "stock data":
        error_message = f"""
ERROR -----------------------------
                                          
    "{input_type}" not an integer
    Non integer values for stock will result in database mulfunction
    Please enter current inventory as an integer
→ """
    if message_type == "connection":
        error_message ="""
ERROR -----------------------------
                                          
    Could not connect to database
    Please seek technical assistance
"""
    if message_type == "table not found":
        if input_type == "p":
            error_message = """
ERROR -----------------------------
                                          
    Could not find Cafe_Products in database
    Please seek technical assistance
"""
        if input_type == "c":
            error_message = """
ERROR -----------------------------
                                          
    Could not find couriers in database
    Please seek technical assistance
"""
        if input_type == "o":
            error_message = """
ERROR -----------------------------
                                          
    Could not find all_orders in database
    Please seek technical assistance
"""
    return error_message

def return_selector(changing_repeat, sort_check):
    if changing_repeat == "":
        if sort_check == "p":
            main_variable = input_cleaner(input("""
What next?
                     
    > Return to Products Menu (P)
    > Main Menu (M)
    > Orders Menu (O)
    > Customers Menu (L)
    > Couriers Menu (C)
    > Exit Program (E) 
    
Choose Option → """))
        if sort_check == "o":
            main_variable = input_cleaner(input("""
What next?
                     
    > Return to Orders Menu (O)
    > Main Menu (M)
    > Products Menu (P)
    > Customers Menu (L)
    > Couriers Menu (C)
    > Exit Program (E) 
    
Choose Option → """))
        if sort_check == "c":
            main_variable = input_cleaner(input("""
What next?
                     
    > Return to Couriers Menu (C)
    > Main Menu (M)
    > Products Menu (P)
    > Customers Menu (L)
    > Orders Menu (O)
    > Exit Program (E) 
    
Choose Option → """))
            
        if sort_check == "u":
            main_variable = input_cleaner(input("""
What next?
                     
    > Return to Customers Menu (L)
    > Main Menu (M)
    > Products Menu (P)
    > Couriers Menu (C)
    > Orders Menu (O)
    > Exit Program (E) 
    
Choose Option → """))
    if changing_repeat == "op":
        main_variable = input_cleaner(input(f"""
What next?

    > View current orders by courier (A)
    > View current orders by status (S)                                               
    > Return to Orders Menu (O)
    > Main Menu (M)
    > Products Menu (P)
    > Couriers Menu (C)
    > Customers Menu (L)
    > Exit Program (E) 

Choose Option → """))
    
    if changing_repeat != "":
        if sort_check == "p":
            main_variable = input_cleaner(input(f"""
What next?

    > {changing_repeat}                       
    > Return to Products Menu (P)
    > Main Menu (M)
    > Orders Menu (O)
    > Couriers Menu (C)
    > Customers Menu (L)
    > Exit Program (E) 

Choose Option → """))
        if sort_check == "o":
            main_variable = input_cleaner(input(f"""
What next?

    > {changing_repeat}                       
    > Return to Orders Menu (O)
    > Main Menu (M)
    > Products Menu (P)
    > Couriers Menu (C)
    > Customers Menu (L)
    > Exit Program (E) 

Choose Option → """))
        if sort_check == "c":
            main_variable = input_cleaner(input(f"""
What next?

    > {changing_repeat}                       
    > Return to Couriers Menu (C)
    > Main Menu (M)
    > Products Menu (P)
    > Orders Menu (O)
    > Customers Menu (L)
    > Exit Program (E) 

Choose Option → """))
        if sort_check == "u":
            main_variable = input_cleaner(input(f"""
What next?

    > {changing_repeat}                       
    > Return to Customers Menu (L)
    > Main Menu (M)
    > Products Menu (P)
    > Orders Menu (O)
    > Couriers Menu (C)
    > Exit Program (E) 

Choose Option → """))
    while main_variable not in main_valid_inputs:
       main_variable = input(error_messages(main_variable, "general"))
    return main_variable

def line_break():
    line = "|------------------------------------------------------------------------------------------------------------------------------------------------------|"
    print(line)

def sub_menu_cap(menu_type, changing_repeat, optional_additional_message):
    if optional_additional_message != "":
        print(f"\n{optional_additional_message}")
    main_variable = return_selector(changing_repeat, menu_type)
    return main_variable

def input_cleaner(input_type):
    removed_exclamation = input_type.replace("!", "")
    period_removed = removed_exclamation.replace(".", "")
    lower_case_input = removed_exclamation.lower()
    striped_input = lower_case_input.strip()
    input_type = striped_input
    return input_type

def cancel_option(input_type, return_direction, continue_direction):
    if input_type == "x":
        main_variable = return_direction
        clear_screen()
    else:
        main_variable = continue_direction
    return main_variable

def price_input_cleaner(input_type):
    strip_input = input_type.strip()
    pound_sign_removed = strip_input.replace("£", "")
    input_type = pound_sign_removed
    return input_type

def repeating_input_or_cancel(input_message, clean_option, return_direction, continue_direction):
    if clean_option == "y":
        new_input_type = input_cleaner(input(f"{input_message}: "))
    if clean_option == "n":
        new_input_type = (input(f"{input_message}: ")).strip()
    if clean_option == "p":
        new_input_type = price_input_cleaner(input(f"{input_message}: "))
    quick_cell = "QC"
    while quick_cell == "QC":
        main_variable, quick_cell = cancel_option(new_input_type, return_direction, continue_direction), ""
    return main_variable, new_input_type

#I group grouped the following functions based on being more related to functionality than structure or presentation but are also more or less globally used

def stock_checker(stock_input, return_direction, continue_direction):
    if stock_input.isdigit() == False:
        print(error_messages(stock_input,"stock data"))
        main_variable = return_direction
    if stock_input.isdigit() == True:
        main_variable = continue_direction
    return main_variable

def range_check(input_type, list_type, return_direction, continue_direction):
    con_type = int(input_type)
    if con_type not in range(1,(len(list_type))+1):
        main_variable = return_direction
        error_print = "yr"
    if con_type in range(1, (len(list_type)) + 1):
        con_type -= 1
        main_variable = continue_direction
        error_print = ""
    return main_variable, con_type, error_print

def check_for_item_return_index(input_type, list_type, key_type, return_direction, continue_direction):
    try:
        find_name_of_dict_item = next(item for item in list_type if item[key_type].lower() == input_type.lower())
        con_type = list_type.index(find_name_of_dict_item)
        error_print = ""
        main_variable = continue_direction
    except StopIteration:
        con_type = ""
        error_print = "ynf"
        main_variable = return_direction
    return main_variable, con_type, error_print

def automated_data_find_sort(input_type, list_type, key_type, return_direction, continue_direction):
    if input_type.isdigit() == True:
        main_variable, con_type, error_print = range_check(input_type, list_type, return_direction, continue_direction)
    if input_type.isdigit() == False:
        main_variable, con_type, error_print = check_for_item_return_index(input_type, list_type, key_type, return_direction, continue_direction)
    return main_variable, con_type, error_print

def price_checker(price_input_type, return_direction, remain_cell):
    numbers_checker = price_input_type.replace(".", "") 
    if numbers_checker.isdigit() == False:
        print(error_messages(price_input_type, "price"))
        main_variable, price_input_type = return_direction, ""
    if numbers_checker.isdigit() == True:
        price_input_type = f"{(float(price_input_type)):.2f}"
        main_variable = remain_cell
    return main_variable, price_input_type

def import_csv(path):
    with open(path, "r") as ALL_1:
        csv_import_formating = csv.DictReader(ALL_1)
        list_type= list()
        for row in csv_import_formating:
            list_type.append(row)
    return list_type

def export_csv(path, list_type, continue_direction):
    with open(path, "w") as save_data:
        try:
            csv_format = csv.DictWriter(save_data, fieldnames = list_type[0].keys())
            csv_format.writeheader()
            csv_format.writerows(list_type)
            main_variable = continue_direction
        except IndexError:
            main_variable = continue_direction
    return main_variable

def product_adder(new_or_edit, return_direction, continue_direction, cafe):
    from number_gen import numbers_1_to_1000
    new_or_edit_clean = input_cleaner(new_or_edit)
    split_for_index_select = new_or_edit_clean.split(" ")
    con_int_list = []
    for i in range(len(numbers_1_to_1000)):
        if numbers_1_to_1000[i] in split_for_index_select:
            con_int = int(numbers_1_to_1000[i])
            con_int -= 1
            con_int_list += [con_int]
            main_variable = continue_direction
    for item in split_for_index_select:
        if item.isdigit() == True:
            con_item = int(item)
            if con_item > 1000:
                print(error_messages(item, "adder"))
            if con_item <= 1000:
                if con_item not in range(len(cafe) + 1):
                    print(error_messages(item, "adder"))
                    con_int_list.remove(con_item - 1)
    if con_int_list == []:
        print(error_messages(new_or_edit, "general"))
        products_to_add = ""
        main_variable = return_direction
    else:
        con_int_list = sorted(con_int_list)
        products_to_add_b_con = list()
        for con_int in con_int_list:
            products_to_add_b_con += [cafe[con_int]['Label']]
            Cafe_Products = call_Cafe_Products()
            new_stock = convert_stock_to_int_and_subract(con_int)
            update_row_x_in_table_x('Stock', new_stock, Cafe_Products[con_int]['ID'], 'Cafe_Products', 'Product_ID')
        x = 0
        list_with_numbers = list()
        while x in range(len(products_to_add_b_con)):
            numbered_items = f"{x+1}. {products_to_add_b_con[x]}"
            list_with_numbers += [numbered_items]
            x += 1
        list_w_numbers_J = ",".join(str(element) for element in list_with_numbers)
        str_w_numbers_s = list_w_numbers_J.strip()
        no_commas = str_w_numbers_s.replace(",", " ")
        products_to_add = no_commas
        print(products_to_add)
    return main_variable, products_to_add

def in_case_of_empty_lists(list_type, blank_list_message, return_direction, continue_direction, list_message_type):
    line_break()
    no_continue_options = [[], "connection", "table not found"]
    if list_type == []:
        clear_screen()
        line_break()
        print(blank_list_message)
        only_now = "n"
        main_variable = return_direction
    if list_type == "connection":
        print("ERROR: Could not connect to database, please seek technical assistance")
        only_now = "n"
        main_variable = return_direction
    if list_type == "table not found":
        print(f"ERROR: Could not find {list_message_type} in database, please seek technical assistance")
        main_variable = return_direction
        only_now = "n"
    if list_type not in no_continue_options:
        main_variable = continue_direction
        only_now = "y"
    return main_variable, only_now

#Functions specifically for the orders menu

def save_and_exit_function():
    line_break()
    Cafe_Products = call_Cafe_Products()
    couriers = call_couriers()
    all_orders = call_all_orders()
    print("\nChecking for changes...\nSaving changes...\nExiting\n")
    main_variable = "exit and save 1"
    main_variable = export_csv("data/Cafe Products.csv", Cafe_Products, "exit and save 2")
    if main_variable == "exit and save 2":
        main_variable = export_csv("data/Orders.csv", all_orders, "exit and save 3")
        if main_variable == "exit and save 3":
            main_variable = export_csv("data/Couriers.csv", couriers, "we're done here")
    return main_variable

def print_orders_by_courier():
    all_orders = call_all_orders()
    list_courier_names = list()
    for order in all_orders:
        list_courier_names += [order['Courier']]
    list_without_duplicates = []
    [list_without_duplicates.append(x) for x in list_courier_names if x not in list_without_duplicates]
    courier_x_orders = list()
    x = 0
    print("\nOrders being delivered by... \n")
    while x in range(len(list_without_duplicates)):
        for order in all_orders:
            if order['Courier'] == list_without_duplicates[x]:
                courier_x_orders += [order]
        print(f"{list_without_duplicates[x]}:\n")
        order_courier_list_generator(courier_x_orders)
        courier_x_orders = list()
        x += 1

def print_orders_by_status():
    all_orders = call_all_orders()
    only_current_orders = list()
    for item in all_orders:
        if item['Status'] != 'Delivered':
            only_current_orders += [item]
    status_list = ['Preparing', 'Ready For Pickup', 'In Transit', "Delivered"]
    order_status_lists = list()
    print("\nOrders with status...\n")
    x = 0
    while x in range(len(status_list)):
        for order in only_current_orders:
            if order['Status'] == status_list[x]:
                order_status_lists += [order]
        print(f"{status_list[x]}:\n")
        order_status_list_generator(order_status_lists)
        order_status_lists = list()
        x += 1

def order_courier_adder(return_in_structure, continue_direction):
    main_variable = "f"
    added_courier_variable, error_print = "", ""
    while main_variable == "f":
        couriers = call_couriers()
        clear_screen()
        error_print_and_list_after_clear_screen(error_print, added_courier_variable)
        up_or_norm_list("Current", "couriers", "(Name : Phone Number)", "c")
        main_variable, added_courier_variable = repeating_input_or_cancel("Type courier number or name to choose a new courier for this order", "y", return_in_structure, "f1")
        while main_variable == "f1":
            main_variable, con_int_type, error_print = automated_data_find_sort(added_courier_variable, couriers, 'Name', "f", "f2")
            if main_variable == "f2":
                new_order_courier = (couriers[con_int_type])['Name']
                main_variable = continue_direction
                return main_variable, new_order_courier

#List generator functions: These functions both print the lists numerically for the user's viewing and provide various headers and keys for reading them.

def products_list_generator():
    Cafe_Products = call_Cafe_Products()
    for item in Cafe_Products:
        item["Price"] = f"{(float(item["Price"])):.2f}"
    for index, item in enumerate(Cafe_Products, 1):
        print(f"{index}. {item['Label']} : {item['Price']}£ : {item['Stock']}")

def order_list_generator():
    all_orders = call_all_orders()
    for index, item in enumerate(all_orders, 1):
        print(f"{index}.\nName: {item['Name']}\nAddress: {item['Address']}\nPhone Number: {item['Phone']}\nCourier: {item['Courier']}\nStatus: {item['Status']}\nProducts: {item['Items']}\n")

def order_courier_list_generator(courier_x_orders):
    for index, item in enumerate(courier_x_orders, 1):
        print (f"{index}.\nName: {item['Name']}\nAddress: {item['Address']}\nPhone Number: {item['Phone']}\nStatus: {item['Status']}\nProducts: {item['Items']}\n")

def order_status_list_generator(order_status_lists):
    for index, item in enumerate(order_status_lists, 1):
        print (f"{index}.\nName: {item['Name']}\nAddress: {item['Address']}\nPhone Number: {item['Phone']}\nCourier: {item['Courier']}\nProducts: {item['Items']}\n")

def courier_list_generator():
    for index, item in enumerate (call_couriers(), 1):
        print(f"{index}. {item['Name']} : {item['Phone']}")

def customer_list_generator():
    for index, item in enumerate (call_customers(), 1):
        print(f"{index}. {item['Name']} : {item['Address']} : {item['Phone']}")

def up_or_norm_list(header1, header2, read_key, gen_func_type):
    print(f"\n{header1} {header2}: {read_key}\n")
    if gen_func_type == "p":
        products_list_generator()
        print("\n")
    if gen_func_type == "o":
        order_list_generator()
        print("\n")
    if gen_func_type == "c":
        courier_list_generator()
        print("\n")
    if gen_func_type == "u":
        customer_list_generator()
        print("\n")

#Specific SQL and database functions

def call_couriers():
    try:
        with pymysql.connect(
                host = host_name,
                user = user_name,
                password = user_password,
                database = database_name
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM couriers")
                    base = list(cursor.fetchall())
                    couriers = list()
                    x = 0
                    while x in range(len(base)):
                        courier_database_id = base[x][0]
                        name_of_courier = base[x][1]
                        phone_number_of_courier = base[x][2]
                        courier_dict = {
                            'ID' : courier_database_id,
                            'Name' : name_of_courier,
                            'Phone' : phone_number_of_courier,
                        }
                        couriers += [courier_dict]
                        x += 1
    except pymysql.err.ProgrammingError:
        couriers = "table not found"
    except pymysql.err.OperationalError:
        couriers = "connection"     
    return couriers

def call_Cafe_Products():
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Cafe_Products")
                base = list(cursor.fetchall())
                Cafe_Products = list()
                x = 0
                while x in range(len(base)):
                    product_database_ID = base[x][0]
                    product_label = base[x][1]
                    product_price = base[x][2]
                    product_stock = base[x][3]
                    product_dict = {
                        'ID' : product_database_ID,
                        'Label' : product_label,
                        'Price' : product_price,
                        'Stock' : product_stock
                    }
                    Cafe_Products += [product_dict]
                    x += 1
    except pymysql.err.ProgrammingError:
        Cafe_Products = "table not found"
    except pymysql.err.OperationalError:
        Cafe_Products = "connection"
    return Cafe_Products

def call_customers():
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM customers")
                base = list(cursor.fetchall())
                customers = list()
                x = 0
                while x in range(len(base)):
                    customer_ID = base[x][0]
                    cus_name = base[x][1]
                    cus_add = base[x][2]
                    cus_phone = base[x][3]
                    customer_dict = {
                        'ID' : customer_ID,
                        'Name' : cus_name,
                        'Address' : cus_add,
                        'Phone' : cus_phone
                    }
                    customers += [customer_dict]
                    x += 1
    except pymysql.err.ProgrammingError:
        customers = "table not found"
    except pymysql.err.OperationalError:
        customers = "connection"
    return customers         

def convert_status_id_to_status_name(order_status_base):
    with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM order_status_options")
                columns = cursor.fetchall()
                for column in columns:
                    if column[0] == order_status_base:
                        order_status = column[1]
    return order_status

def convert_status_name_to_status_id(status_base):
    with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM order_status_options")
                columns = cursor.fetchall()
                for column in columns:
                    if column[1] == status_base:
                        status_ID= column[0]
    return status_ID

def call_all_orders():
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM all_orders")
                base = list(cursor.fetchall())
                all_orders = list()
                x = 0
                while x in range(len(base)):
                    order_database_ID = base[x][0]
                    customer_Name = base[x][1]
                    customer_Address = base[x][2]
                    customer_phone = base[x][3]
                    order_courier_name = base[x][4]
                    order_status_base = base[x][5]
                    order_products = base[x][6]
                    order_status = convert_status_id_to_status_name(order_status_base)
                    quick_test_dict = {
                    'ID' : order_database_ID,
                    'Name' : customer_Name,
                    'Address' : customer_Address,
                    'Phone' : customer_phone,
                    'Courier' : order_courier_name,
                    'Status' : order_status,
                    'Items' : order_products
                }
                    all_orders += [quick_test_dict]
                    x += 1
    except pymysql.err.ProgrammingError:
        all_orders = "table not found"
    except pymysql.err.OperationalError:
        all_orders = "connection"
    return all_orders

def restore_products_using_csv_to_database():
    Cafe_Products = import_csv("data/cafe_products_undo_option.csv")
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
    ) as connection:
        with connection.cursor() as cursor:
            for item in Cafe_Products:
                add_SQL = """
                INSERT INTO `Cafe_Products` (`Label`, `Price`, `Stock`)
                VALUES (%s, %s, %s);
                """
                values = ((item['Label']),(item['Price']),(item['Stock']))
                cursor.execute(add_SQL, values)
                connection.commit()

def restore_orders_using_csv_to_database():
    all_orders = import_csv("data/orders_undo_option.csv")
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
    ) as connection:
        with connection.cursor() as cursor:
            for item in all_orders:
                add_SQL = """
                INSERT INTO `all_orders` (`customer_Name`, `customer_Address`, `customer_Phone`, `courier_name`, `status_ID`, `Items`)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
                con_status = convert_status_name_to_status_id(item['Status'])
                values = ((item['Name']), (item['Address']), (item['Phone']), (item['Courier']), con_status, (item['Items']))
                cursor.execute(add_SQL, values)
                connection.commit()

def restore_couriers_using_csv_to_database():
    couriers = import_csv("data/couriers_undo_option.csv")
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
    ) as connection:
        with connection.cursor() as cursor:
            for item in couriers:
                add_SQL = """
                INSERT INTO `couriers` (`Name`, `Phone`)
                VALUES (%s, %s);
                """
                values = ((item['Name']),(item['Phone']))
                cursor.execute(add_SQL, values)
                connection.commit()

def restore_customers_using_csv_to_database():
    customers = import_csv("data/customers_undo_option.csv")
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
    ) as connection:
        with connection.cursor() as cursor:
            for item in customers:
                add_SQL = """
                INSERT INTO `customers` (`Name`, `Address`, `Phone`)
                VALUES (%s, %s, %s);
                """
                values = ((item['Name']), (item['Address']), (item['Phone']))
                cursor.execute(add_SQL, values)
                connection.commit()
        
def add_Product(new_product, new_price, new_stock, continue_direction):
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                insert_SQL = """
                INSERT INTO `Cafe_Products` (`Label`, `Price`, `Stock`)
                VALUES (%s, %s, %s);
                """
                values = (new_product, new_price, new_stock)
                cursor.execute(insert_SQL, values)
                connection.commit()
        main_variable = continue_direction
    except pymysql.err.ProgrammingError:
        print(error_messages("p", "table not found"))
        main_variable = "p"
    except pymysql.err.OperationalError:
        print(error_messages("", "connection"))
        main_variable = "p"
    return(main_variable)

def add_order(new_order_name, new_order_address, new_order_phone, new_order_courier, products_to_add):
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                insert_SQL = """
                INSERT INTO `all_orders` (`customer_Name`, `customer_Address`, `customer_Phone`, `courier_name`, `status_ID`, `Items`)
                VALUES (%s, %s, %s, %s, '1', "%s");
                """
                values = (new_order_name, new_order_address, new_order_phone, new_order_courier, products_to_add)
                cursor.execute(insert_SQL, values)
                connection.commit()
        main_variable = "r7"
    except pymysql.err.ProgrammingError:
        print(error_messages("o", "table not found"))
        main_variable = "o"
    except pymysql.err.OperationalError:
        print(error_messages("", "connection"))
        main_variable = "o"
    return main_variable 

def add_courier(new_courier_name, new_courier_phone, continue_direction):
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                insert_SQL = """
                INSERT INTO `couriers` (`Name`, `Phone`)
                VALUES (%s, %s);
                """
                values = (new_courier_name, new_courier_phone)
                cursor.execute(insert_SQL, values)
                connection.commit()
        main_variable = continue_direction
    except pymysql.err.ProgrammingError:
        print(error_messages("c", "table not found"))
        main_variable = "c"
    except pymysql.err.OperationalError:
        print(error_messages("", "connection"))
        main_variable = "c"
    return main_variable

def add_customer(new_customer_name, new_customer_address, new_customer_phone, continue_direction):
    try:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        ) as connection:
            with connection.cursor() as cursor:
                insert_SQL = """
                INSERT INTO `customers` (`Name`, `Address`, `Phone`)
                VALUES (%s, %s, %s);
                """
                values = (new_customer_name, new_customer_address, new_customer_phone)
                cursor.execute(insert_SQL, values)
                connection.commit()
        main_variable = continue_direction
    except pymysql.err.ProgrammingError:
        print(error_messages("c", "table not found"))
        main_variable = "c"
    except pymysql.err.OperationalError:
        print(error_messages("", "connection"))
        main_variable = "c"
    return main_variable

def update_row_x_in_table_x(key_type, update_data, item_ID, table_name, ID_name):
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
    ) as connection:
        with connection.cursor() as cursor:
            update_SQL = f"""
            UPDATE `{table_name}` SET
            `{key_type}` = %s
            WHERE `{ID_name}` = '{item_ID}';
            """
            values = (update_data)
            cursor.execute(update_SQL, values)
            connection.commit()

def convert_stock_to_int_and_subract(con_int):
    Cafe_Products = call_Cafe_Products()
    stock_before = Cafe_Products[con_int]['Stock']
    stock_before_int = int(stock_before)
    stock_after = stock_before_int - 1
    return stock_after

def delete_function_cover_all(deletion_input_type, continue_direction, item_ID, table_name, ID_name):
    if deletion_input_type == "all":
        delete_all_x(table_name)
        main_variable = continue_direction
    if deletion_input_type != "all":
        delete_one_row_from_table_x(item_ID, table_name, ID_name)
        main_variable = continue_direction
    return main_variable

def delete_one_row_from_table_x(item_ID, table_name, ID_name):
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
    ) as connection:
        with connection.cursor() as cursor:
            delete_row_SQL = f"""
            DELETE FROM `{table_name}`
            WHERE `{ID_name}` = '{item_ID}';
            """
            cursor.execute(delete_row_SQL)
            connection.commit()

def delete_all_x(table_name):
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name
        ) as connection:
        with connection.cursor() as cursor:
            delete_ALL_SQL = f"""
            DELETE FROM `{table_name}`;
            """
            cursor.execute(delete_ALL_SQL)
            connection.commit()
    
def if_all(list_type, continue_direction, return_direction, type_of, path):
    yes_list = ['y', 'yes', 'yep', 'sure', 'yeah', 'for sure']
    no_list = ['n', 'no', 'nope', 'nuh uh', 'hell no', 'na', 'nah']
    no_and_yes_list = (yes_list + no_list)
    main_variable = "if"
    while main_variable == "if":
        main_variable, are_you_sure = repeating_input_or_cancel((f"\nAre you sure you want to delete all {type_of}? (Y/N)\n"), "y", return_direction, "if1")
        while main_variable == "if1":
            if are_you_sure in yes_list:
                main_variable = export_csv(path, list_type, continue_direction)
            if are_you_sure in no_list:
                main_variable = return_direction
            if are_you_sure not in no_and_yes_list:
                print(error_messages(are_you_sure, "general"))
                main_variable = "if"
    return main_variable

def customer_from_scratch():
    from Input_Modules import (yes_list, no_list, no_and_yes_list)
    main_variable = "cfs"
    while main_variable == "cfs":
        main_variable, new_order_name = repeating_input_or_cancel("Name", "n", "cfsx", "cfs1")
        if main_variable == "cfsx":
                new_order_name = ""
                new_order_address = ""
                new_order_phone = ""
                main_variable = "rx"
        while main_variable == "cfs1":
            main_variable, new_order_address = repeating_input_or_cancel("Address", "n", "cfs", "cfs2")
            while main_variable == "cfs2":        
                main_variable, new_order_phone = repeating_input_or_cancel("Phone", "n", "cfs1", "cfs3")
                while main_variable == "cfs3":
                    save_Q = input_cleaner(input("\nAdd to saved customers? (Y/N)\n→ : "))
                    main_variable = "cfs4"
                    while main_variable == "cfs4":
                        if save_Q in yes_list:
                            main_variable = add_customer(new_order_name, new_order_address, new_order_phone, "r1")
                        if save_Q in no_list:
                            main_variable = "r1"
                        if save_Q not in no_and_yes_list:
                            print(error_messages(save_Q, "general"))
                            main_variable = "cfs3"
    return main_variable, new_order_name, new_order_address, new_order_phone

def customer_from_saved():
    main_variable = "cfdx"
    customer_pick, error_print = "", ""
    while main_variable == "cfdx":
        customers = call_customers()
        clear_screen()
        error_print_and_list_after_clear_screen(error_print, customer_pick)
        up_or_norm_list("Saved", "customers", "(Name : Address : Phone Number)", "u")
        main_variable = "cfd"
        while main_variable == "cfd":
            main_variable, customer_pick = repeating_input_or_cancel("Type customer name or number to choose\n→ ", "y", "cfdxx", "cfd1")
            if main_variable == "cfdxx":
                new_order_name = ""
                new_order_address = ""
                new_order_phone = ""
                main_variable = "rx"
            while main_variable == "cfd1":
                main_variable, con_int, error_print = automated_data_find_sort(customer_pick, customers, 'Name', "cfdx", "cfd2")
                while main_variable == "cfd2":
                    new_order_name = customers[con_int]['Name']
                    new_order_address = customers[con_int]['Address']
                    new_order_phone = customers[con_int]['Phone']
                    main_variable = "r1"
    return main_variable, new_order_name, new_order_address, new_order_phone, error_print
    

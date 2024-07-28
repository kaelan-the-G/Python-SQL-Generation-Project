#Importing all functions and menus from seperate modules

from functions_t import (error_messages, return_selector, line_break, input_cleaner, price_input_cleaner, cancel_option, automated_data_find_sort, 
price_checker, sub_menu_cap,repeating_input_or_cancel, product_adder, in_case_of_empty_lists, up_or_norm_list, save_and_exit_function, 
print_orders_by_courier, print_orders_by_status, order_courier_adder, call_Cafe_Products, call_couriers, stock_checker, add_Product, update_row_x_in_table_x, 
delete_function_cover_all, if_all, restore_products_using_csv_to_database, add_courier, restore_couriers_using_csv_to_database, call_all_orders, 
add_order, restore_orders_using_csv_to_database, call_customers, add_customer, restore_customers_using_csv_to_database, customer_from_saved, customer_from_scratch,
clear_screen, error_print_and_list_after_clear_screen)
from Menu_Formats import(main_menu, main_menu_options, product_options_menu, order_menu, couriers_menu, customers_menu)
import msvcrt
from Input_Modules import(valid_product_menu_running_options, valid_order_menu_running_options, valid_customer_input_options ,valid_courier_input_options, valid_exit_input_options, main_valid_inputs, main_menu_inputs, undo_delete_all)
#Main running code ⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄
main_variable = "m123"
#Main menu ---------------------------------------------------------------------------------------
if main_variable == "m123":
    print(main_menu)
    print("\nPress any key to continue...\n")
    msvcrt.getch()
while main_variable in main_valid_inputs:
    while main_variable in main_menu_inputs:
        clear_screen()
        main_variable = input_cleaner(input(main_menu_options))
        only_now = "y"
        while main_variable not in main_valid_inputs:
            main_variable = input_cleaner(input(error_messages(main_variable, "general")))
    while main_variable in valid_product_menu_running_options:
        if only_now == "y":
            clear_screen()
            only_now = "n"
        product_menu_selection = input_cleaner(input(product_options_menu))
        from Input_Modules import(all_product_menu_choosing_inputs, product_menu_option_0_inputs, product_menu_option_1_inputs, product_menu_option_2_inputs, product_menu_option_3_inputs, product_menu_option_4_inputs)
        while product_menu_selection not in all_product_menu_choosing_inputs:
            product_menu_selection = input_cleaner(input(error_messages(product_menu_selection, "general")))
        if product_menu_selection in product_menu_option_0_inputs:
            main_variable = "m"
        if product_menu_selection in product_menu_option_1_inputs:
            main_variable, only_now = in_case_of_empty_lists(call_Cafe_Products(), "No avaliable products", "p", "r", "Cafe_Products")
            if main_variable == "r":
                clear_screen()
                up_or_norm_list("Avaliable", "products", "(Label : Price : Stock)", "p")
                main_variable = sub_menu_cap("p", "", "")
        if product_menu_selection in product_menu_option_2_inputs:
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                line_break()
                main_variable = "r1"
                while main_variable == "r1":
                    main_variable, new_product = repeating_input_or_cancel("\nEnter the name of new product:\n→ ", "n", "p", "r2")
                    while main_variable == "r2":
                        main_variable, new_price = repeating_input_or_cancel("\nEnter the price of new product\n→ ", "p", "r1", "r3")
                        while main_variable == "r3":
                            main_variable, new_price = price_checker(new_price, "r2", "r4")
                            while main_variable == "r4":
                                main_variable, new_stock = repeating_input_or_cancel("\nEnter current stock\n→ ", "y", "r2", "r5")
                                while main_variable == "r5":
                                    main_variable = stock_checker(new_stock, "r4", "r6")
                                    while main_variable == "r6":
                                        main_variable = add_Product(new_product, new_price, new_stock, "r7")
                                        while main_variable == "r7":
                                            main_variable = sub_menu_cap("p",  "Add another product (R)", (f"{new_product} added to avaliable products"))
        if product_menu_selection in product_menu_option_3_inputs: 
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                update_base, error_print = "", ""
                main_variable, only_now = in_case_of_empty_lists(call_Cafe_Products(), "No avaliable products", "p", "r1", "Cafe_Products")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, update_base)
                    up_or_norm_list("Avaliable", "products", "(Label : Price : Stock)", "p")
                    main_variable, update_base = repeating_input_or_cancel("\nEnter product name or number in list to choose:\n → ", "y", "p", "r2")
                    while main_variable == "r2":
                        main_variable, con_int, error_print = automated_data_find_sort(update_base, call_Cafe_Products(), 'Label', "r1", "r3")
                        while main_variable == "r3":
                            main_variable, price_or_label = repeating_input_or_cancel("\nDo you want to change the price, label or stock? (P/L/S)\n→ ", "y", "r1", "r4")
                            while main_variable == "r4":
                                from Input_Modules import (price_choose_inputs, label_choose_inputs, stock_choose_inputs, either_or_price_label_stock)
                                if price_or_label in price_choose_inputs:
                                    price_change = price_input_cleaner(input("\nEnter new price\n → "))
                                    key_type, update_data = "Price", price_change.replace("£", "")
                                    main_variable = "r5"
                                if price_or_label in label_choose_inputs:
                                    label_change = (input("\nEnter new label\n → ")).strip()
                                    key_type, update_data = "Label", label_change
                                    main_variable = "r5"
                                if price_or_label in stock_choose_inputs:
                                    stock_change = (input("\nEnter current stock\n → ")).strip()
                                    key_type, update_data = "Stock", stock_change
                                    main_variable = "r5"
                                if price_or_label not in either_or_price_label_stock:
                                    print(error_messages(price_or_label, "general"))
                                    main_variable = "r3"
                                while main_variable == "r5":
                                    main_variable = cancel_option(update_data, "r3", "r6")
                                    while main_variable == "r6":
                                        if key_type == "Price":
                                            main_variable, update_data = price_checker(update_data, "r4", "r7")
                                        if key_type == "Stock":
                                            main_variable = stock_checker(update_data, "r4", "r7")
                                        if key_type == "Label":
                                            main_variable = "r7"
                                        while main_variable == "r7":
                                            Cafe_Products = call_Cafe_Products()
                                            item_ID = Cafe_Products[con_int]['ID']
                                            update_row_x_in_table_x(key_type, update_data, item_ID, "Cafe_Products", "Product_ID")
                                            main_variable = sub_menu_cap("p",  "Edit another product (R)", (f"{Cafe_Products[con_int]['Label']} {key_type} has been updated to {update_data} in avaliable products"))
        if product_menu_selection in product_menu_option_4_inputs:
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                item_to_delete, error_print = "", ""
                Cafe_Products = call_Cafe_Products()
                main_variable, only_now = in_case_of_empty_lists(Cafe_Products, "No avaliable products", "p", "r1", "Cafe_Products")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, item_to_delete)
                    up_or_norm_list("Avaliable", "products", "(Label : Price : Stock)", "p")
                    main_variable, item_to_delete = repeating_input_or_cancel('\nEnter item to delete: (Enter "all" to delete all)\n\n→ ', "y", "p", "r2")
                    while main_variable == "r2":
                        if item_to_delete == "all":
                            main_variable = if_all(Cafe_Products, "r3", "r1", "products", "data/cafe_products_undo_option.csv")
                            item_ID, con_int = "", 0
                        else:
                            main_variable, con_int, error_print = automated_data_find_sort(item_to_delete, Cafe_Products, 'Label', "r1", "r3")                       
                        while main_variable == "r3":
                            item_ID = Cafe_Products[con_int]['ID']
                            main_variable = delete_function_cover_all(item_to_delete, "r4", item_ID, "Cafe_Products", "Product_ID")
                            while main_variable == "r4":
                                if item_to_delete == "all":
                                    main_variable = sub_menu_cap("p", "Undo delete all products (U)", "All products deleted")    
                                else:
                                    main_variable = sub_menu_cap("p", "Delete another product (R)", (f"{Cafe_Products[con_int]['Label']} has been deleted from avaliable products"))
                                while main_variable in undo_delete_all:
                                    restore_products_using_csv_to_database()
                                    main_variable = sub_menu_cap("p", "Delete Product (R)", "Products restored")    
    while main_variable in valid_order_menu_running_options:
        if only_now == "y":
            clear_screen()
            only_now = "n"
        from Input_Modules import(orders_menu_option_0_inputs, orders_menu_option_1_inputs, orders_menu_option_2_inputs, orders_menu_option_3_inputs, orders_menu_option_4_inputs, orders_menu_option_5_inputs, all_order_menu_choosing_inputs)
        order_menu_selection = input_cleaner(input(order_menu))
        while order_menu_selection not in all_order_menu_choosing_inputs:
            order_menu_selection = input_cleaner(input(error_messages(order_menu_selection, "general")))
        if order_menu_selection in orders_menu_option_0_inputs:
            main_variable = "m"
        if order_menu_selection in orders_menu_option_1_inputs:
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                all_orders = call_all_orders()
                main_variable, only_now = in_case_of_empty_lists(all_orders, "No Current Orders", "o", "r1", "all_orders")
                while main_variable == "r1":
                    up_or_norm_list("Current", "orders", "", "o")
                    main_variable = "r2"
                    while main_variable == "r2":
                        main_variable = return_selector("op", "")
                        if main_variable == "a":
                            clear_screen()
                            print_orders_by_courier()
                            main_variable = "r2"
                        if main_variable == "s":
                            clear_screen()
                            print_orders_by_status()
                            main_variable = "r2"
        if order_menu_selection in orders_menu_option_2_inputs:
            from Input_Modules import(yes_list, no_list, no_and_yes_list)
            main_variable = "r"
            while main_variable.lower() == "r":
                clear_screen()
                main_variable, only_now = in_case_of_empty_lists(call_couriers(), "\nNo current couriers\nAdd couriers to add orders\n", "o", "rx", "")
                all_orders = call_all_orders()
                while main_variable == "rx":
                    main_variable, new_or_saved = repeating_input_or_cancel("Add from saved customers? (Y/N)\n→ ", "y", "o", "rx1")
                    while main_variable == "rx1":
                        if new_or_saved in yes_list:
                            main_variable, new_order_name, new_order_address, new_order_phone, error_print = customer_from_saved()
                        if new_or_saved in no_list:
                            main_variable, new_order_name, new_order_address, new_order_phone = customer_from_scratch()
                        if new_or_saved not in no_and_yes_list:
                            print(error_messages(new_or_saved, "general"))
                            main_variable = "rx"
                        while main_variable == "r1":
                            main_variable, new_order_courier = order_courier_adder("r", "r2") 
                            while main_variable == "r2":
                                up_or_norm_list("Avaliable", "products", "(Label : Price : Stock)", "p")
                                main_variable, new_order_products = repeating_input_or_cancel("Add one or more products to order by using only product numbers seperated by single spaces\n→ ", "y", "r1", "r3")
                                while main_variable == "r3":
                                    clear_screen()
                                    main_variable, products_to_add = product_adder(new_order_products, "r2", "r4", call_Cafe_Products())
                                    while main_variable == "r4":
                                        main_variable = add_order(new_order_name, new_order_address, new_order_phone, new_order_courier, products_to_add)
                                        main_variable = sub_menu_cap("o", "Add another order (R)", (f"Order for {new_order_name} has been added"))          
        if order_menu_selection in orders_menu_option_3_inputs:
            main_variable = "r"
            while main_variable == "r":
                order_chosen, error_print = "", ""
                all_orders = call_all_orders()
                main_variable, only_now = in_case_of_empty_lists(all_orders, "No current orders", "o", "r1", "all_orders")
                while main_variable.lower() == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, order_chosen)
                    up_or_norm_list("Current", "orders", "", "o")
                    main_variable = "r2"
                    while main_variable == "r2":
                        main_variable, order_chosen = repeating_input_or_cancel("Enter order number or customer name to choose order", "y","o", "r3")
                        while main_variable == "r3":
                            main_variable, con_int, error_print = automated_data_find_sort(order_chosen, all_orders, 'Name', "r1", "rx1")
                            while main_variable == "rx1":
                                error_print, what_status, main_variable = "", "", "r4"
                                while main_variable == "r4":
                                    old_status_name = all_orders[con_int]['Status']
                                    clear_screen()
                                    error_print_and_list_after_clear_screen(error_print, what_status)
                                    main_variable, what_status = repeating_input_or_cancel("\nInput new status\n\nReady for pickup (R)\nIn transit (T)\nDelivered (D)\n\nChoose option: ", "y", "r2", "r5")
                                    while main_variable == "r5":
                                        from Input_Modules import (ready_for_pickup_inputs, in_transit_inputs, delivered_inputs, valid_status_change_options)
                                        if what_status not in valid_status_change_options:
                                            error_print = "yg"
                                            main_variable = "r4"
                                        if what_status in ready_for_pickup_inputs:
                                            status_ID = 2
                                            main_variable = "r6"
                                        if what_status in in_transit_inputs:
                                            status_ID = 3
                                            main_variable = "r6"
                                        if what_status in delivered_inputs:
                                            status_ID = 4
                                            main_variable = "r6"
                                        while main_variable == "r6":
                                            item_ID = all_orders[con_int]['ID']
                                            update_row_x_in_table_x('status_ID', status_ID, item_ID, 'all_orders', 'Order_ID')
                                            up_ord = call_all_orders()
                                            new_status = up_ord[con_int]['Status']
                                            main_variable = sub_menu_cap('o', "Change another order status (R)", (f"Status of order for {up_ord[con_int]['Name']} updated from {old_status_name} to {new_status}"))
        if order_menu_selection in orders_menu_option_4_inputs:
            main_variable ="r"
            while main_variable.lower() == "r":
                error_print, order_pick = "", ""
                all_orders = call_all_orders()
                main_variable, only_now = in_case_of_empty_lists(all_orders, "No current orders", "o", "r1", "all_orders")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, order_pick)
                    up_or_norm_list("Current", "orders", "", "o")
                    main_variable, order_pick = repeating_input_or_cancel("Enter order number or customer name to choose order", "y", "o", "r2")
                    while main_variable == "r2":
                        main_variable, con_int, error_print = automated_data_find_sort(order_pick, all_orders, 'Name', "r1", "y")
                        while main_variable == "y":
                            main_variable, what_key_to_change = repeating_input_or_cancel("\nPick an option below:\nName (N)\nAddress (A)\nPhone Number (P)\nCourier (C)\nOrder Items (I)\n\n→ ", "y", "r1", "y1")
                            while main_variable == "y1":
                                from Input_Modules import(order_name_change, order_address_change, order_phone_change, order_courier_change, order_items_change, valid_detail_change_options)
                                if what_key_to_change not in valid_detail_change_options:
                                    print(error_messages(what_key_to_change, "general"))
                                    main_variable = "y"
                                if what_key_to_change in order_name_change:
                                    key_type = 'customer_Name'
                                    main_variable, new_name = repeating_input_or_cancel("Enter updated Name", "n", "y", "y2")
                                    update_data = new_name
                                if what_key_to_change in order_address_change:
                                    key_type = 'customer_Address'
                                    main_variable, new_address = repeating_input_or_cancel("Enter updated Address", "n", "y", "y2")
                                    update_data = new_address
                                if what_key_to_change in order_phone_change:
                                    key_type = 'customer_Phone'
                                    main_variable, new_phone_number = repeating_input_or_cancel("Enter updated Phone Number", "n", "y", "y2")
                                    update_data = new_phone_number
                                if what_key_to_change in order_courier_change:
                                    key_type = 'courier_name'
                                    main_variable, new_order_courier = order_courier_adder("y", "y2")
                                    update_data = new_order_courier
                                if what_key_to_change in order_items_change:
                                    key_type = 'order_products'
                                    up_or_norm_list("Avaliable", "products", "(Label : Price : Stock)", "p")
                                    print("\nTo update order products include all items of changed order, not only additions\n")
                                    main_variable, product_order_update_input = repeating_input_or_cancel("Update order products by using only product list numbers seperated by single spaces", "y", "y", "yI1")
                                    if main_variable == "yI1":
                                        main_variable, new_products_for_order = product_adder(product_order_update_input, "y1", "yI2", call_Cafe_Products())
                                        if main_variable == "yI2":
                                            update_data = new_products_for_order
                                            main_variable = "y2"
                                while main_variable == "y2":
                                    old_order_name = all_orders[con_int]['Name']
                                    item_ID = all_orders[con_int]['ID']
                                    update_row_x_in_table_x(key_type, update_data, item_ID, 'all_orders', 'order_ID')
                                    main_variable = "y3"
                                    while main_variable == "y3":
                                        order_message = f"{key_type} of order for {old_order_name} changed to {update_data}"
                                        print(order_message)
                                        main_variable, another_change = repeating_input_or_cancel("\nChange another part of this order? (Y/N)", "y", "y1", "y4")
                                        while main_variable == "y4":
                                            if another_change == "y":
                                                main_variable = "y"
                                            if another_change == "n":
                                                main_variable = "n"
                                            while main_variable == "n":
                                                main_variable = sub_menu_cap("o", "Edit another order (R)", "")
        if order_menu_selection in orders_menu_option_5_inputs:
            main_variable = "r"
            while main_variable == "r":
                all_orders = call_all_orders()
                what_order_to_delete, error_print = "", ""
                main_variable, only_now = in_case_of_empty_lists(all_orders, "No current orders", "o", "r1", "all_orders")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, what_order_to_delete)
                    up_or_norm_list("Current", "orders", "", "o")
                    main_variable, what_order_to_delete = repeating_input_or_cancel('\nEnter order to delete(Enter "all" to delete all)\n\n', "y", "o", "r2")
                    while main_variable == "r2":
                        if what_order_to_delete == "all":
                            item_ID, con_int = "", 0
                            main_variable = if_all(all_orders, "r3", "r1", "all_orders", "data/orders_undo_option.csv")
                        if what_order_to_delete != "all":
                            main_variable, con_int, error_print = automated_data_find_sort(what_order_to_delete, all_orders, 'Name', "r1", "r3")
                        while main_variable == "r3":
                            if what_order_to_delete != "all":
                                item_ID = all_orders[con_int]['ID']
                            main_variable = delete_function_cover_all(what_order_to_delete, "r4", item_ID, 'all_orders', 'order_ID')
                            while main_variable == "r4":
                                if what_order_to_delete == "all":
                                    main_variable = sub_menu_cap("o", "Undo delete all orders (U)", "All orders deleted")
                                if what_order_to_delete != "all":
                                    main_variable = sub_menu_cap("o", "Delete another order (R)", (f"{all_orders[con_int]['Name']} has been deleted from current orders"))
                                while main_variable in undo_delete_all:
                                    restore_orders_using_csv_to_database()
                                    main_variable = sub_menu_cap("o", "Delete order (R)", "Orders restored")
    while main_variable in valid_courier_input_options:
        if only_now == "y":
            clear_screen()
            only_now = "n"
        couriers_sub_menu_selection = input_cleaner(input(couriers_menu))
        from Input_Modules import(couriers_menu_option_0_inputs, couriers_menu_option_1_inputs, couriers_menu_option_2_inputs, couriers_menu_option_3_inputs, couriers_menu_option_4_inputs, all_courier_menu_choosing_inputs)
        while couriers_sub_menu_selection not in all_courier_menu_choosing_inputs:
            couriers_sub_menu_selection = input(error_messages(couriers_sub_menu_selection, "general"))
        if couriers_sub_menu_selection in couriers_menu_option_0_inputs:
            main_variable = "m"
        if couriers_sub_menu_selection in couriers_menu_option_1_inputs:
            main_variable, only_now = in_case_of_empty_lists(call_couriers(), "No current couriers", "c", "r1", "couriers")
            while main_variable == "r1":
                clear_screen()
                up_or_norm_list("Current", "couriers", "(Name : Phone number)", "c")
                main_variable = sub_menu_cap("c", "", "")
        if couriers_sub_menu_selection in couriers_menu_option_2_inputs:
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                line_break()
                main_variable = "r1"
                while main_variable == "r1":
                    main_variable, new_courier_name = repeating_input_or_cancel("\nEnter the full name of new courier:\n→ ", "n", "c", "r2")
                    while main_variable == "r2":
                        main_variable, new_courier_phone = repeating_input_or_cancel("Enter courier's phone number:\n→ ", "n", "r1", "r3")
                        while main_variable == "r3":
                            main_variable = add_courier(new_courier_name, new_courier_phone, "r4")
                            while main_variable == "r4":
                                only_now = "y"
                                main_variable = sub_menu_cap("c", "Add another courier(R)", f"{new_courier_name} added to current couriers")
        if couriers_sub_menu_selection in couriers_menu_option_3_inputs:
            main_variable = "r"
            while main_variable == "r":
                courier_update, error_print = "", ""
                couriers = call_couriers()
                main_variable, only_now = in_case_of_empty_lists(couriers, "No current couriers", "c", "r1", "couriers")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, courier_update)
                    up_or_norm_list("Current", "couriers", "(Name : Phone Number)", "c")
                    main_variable, courier_update = repeating_input_or_cancel("\nEnter courier name or number to update\n → ", "y", "c", "r2")
                    while main_variable == "r2":
                        main_variable, con_int, error_print = automated_data_find_sort(courier_update, couriers, 'Name', "r1", "r3")
                        while main_variable == "r3":
                            main_variable, name_or_phone = repeating_input_or_cancel("\nDo you want to change courier name or phone number? (N/P)\n→ ", "y", "r1", "r4")
                            while main_variable == "r4":
                                from Input_Modules import (name_choose_inputs_c, phone_choose_inputs_c, either_or_name_phone_c)
                                if name_or_phone in name_choose_inputs_c:
                                    name_change = (input("\nEnter edited name\n→ : ")).strip()
                                    key_type, update_data = "Name", name_change
                                    main_variable = "r5"
                                if name_or_phone in phone_choose_inputs_c:
                                    phone_change = (input("Enter new phone number\n→ : ")).strip()
                                    key_type, update_data = "Phone", phone_change
                                    main_variable = "r5"
                                if name_or_phone not in either_or_name_phone_c:
                                    print(error_messages(name_or_phone, "general"))
                                    main_variable = "r3"
                                while main_variable == "r5":
                                    main_variable = cancel_option(update_data, "r3", "r6")
                                    while main_variable == "r6":
                                        item_ID = couriers[con_int]['ID']
                                        update_row_x_in_table_x(key_type, update_data, item_ID, "couriers", "courier_ID")
                                        main_variable = sub_menu_cap("c",  "Edit another courier (R)", (f"{couriers[con_int]['Name']} {key_type} has been updated to {update_data} in current couriers"))
        if couriers_sub_menu_selection in couriers_menu_option_4_inputs:
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                couriers = call_couriers()
                courier_deletion, error_print = "", ""
                main_variable, only_now = in_case_of_empty_lists(couriers, "No current couriers", "c", "r1", "couriers")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, courier_deletion)
                    up_or_norm_list("Current", "couriers", "(Name : Phone Number)", "c")
                    main_variable, courier_deletion = repeating_input_or_cancel('\nEnter courier name or number to delete: (Enter "all" to delete all)\n\n → ', "y", "c", "r2")
                    while main_variable == "r2":
                        if courier_deletion == "all":
                            main_variable = if_all(couriers, "r3", "r1", "couriers", "data/couriers_undo_option.csv")
                            item_ID, con_int = "", 0
                        else:
                            main_variable, con_int, error_print = automated_data_find_sort(courier_deletion, couriers, 'Name', "r1", "r3")
                        while main_variable == "r3":
                            item_ID = couriers[con_int]['ID']
                            main_variable = delete_function_cover_all(courier_deletion, "r4", item_ID, "couriers", "courier_ID")
                            while main_variable == "r4":
                                if courier_deletion == "all":
                                    main_variable = sub_menu_cap("c", "Undo delete all couriers (U)", "All couriers deleted")
                                else:
                                    main_variable = sub_menu_cap("c", "Delete another courier (R)", (f"{couriers[con_int]['Name']} has been deleted from current couriers"))
                                while main_variable in undo_delete_all:
                                    restore_couriers_using_csv_to_database()
                                    main_variable = sub_menu_cap("c", "Delete courier (R)", "Couriers restored")   
    while main_variable in valid_customer_input_options:
        if only_now == "y":
            clear_screen()
            only_now = "n"
        customers_sub_menu_selection = input_cleaner(input(customers_menu))
        from Input_Modules import(customers_menu_option_0_inputs, customers_menu_option_1_inputs, customers_menu_option_2_inputs, customers_menu_option_3_inputs, customers_menu_option_4_inputs, all_customer_menu_choosing_inputs)
        while customers_sub_menu_selection not in all_customer_menu_choosing_inputs:
            customers_sub_menu_selection = input(error_messages(customers_sub_menu_selection, "general"))
        if customers_sub_menu_selection in customers_menu_option_0_inputs:
            main_variable = "m"
        if customers_sub_menu_selection in customers_menu_option_1_inputs:
            main_variable = "r"
            while main_variable == "r":
                main_variable, only_now = in_case_of_empty_lists(call_customers(), "No current customers", "l", "r1", "customers")
                while main_variable == "r1":
                    clear_screen()
                    up_or_norm_list("Saved", "customers", "(Name : Address : Phone Number)", "u")
                    main_variable = sub_menu_cap("u", "", "")
        if customers_sub_menu_selection in customers_menu_option_2_inputs:
            main_variable = "r"
            while main_variable == "r":
                clear_screen()
                line_break()
                main_variable = "r1"
                while main_variable == "r1":
                    main_variable, new_customer_name = repeating_input_or_cancel("\nEnter the full name of new customer:\n→ ", "n", "l", "r2")
                    while main_variable == "r2":
                        main_variable, new_customer_address = repeating_input_or_cancel("\nEnter customer address:\n→ ", "n", "r1", "r3")
                        while main_variable == "r3":
                            main_variable, new_customer_phone = repeating_input_or_cancel("\nEnter customer phone number:\n→ ", "n", "r2", "r4")
                            while main_variable == "r4":
                                main_variable = add_customer(new_customer_name, new_customer_address, new_customer_phone, "r5")
                                while main_variable == "r5":
                                    only_now = "y"
                                    main_variable = sub_menu_cap("u", "Add another customer (R)", f"{new_customer_name} added to saved customers")
        if customers_sub_menu_selection in customers_menu_option_3_inputs:
            main_variable = "r"
            update_base, error_print = "", ""
            while main_variable == "r":
                customer_update, error_print = "", ""
                customers = call_customers()
                main_variable, only_now = in_case_of_empty_lists(customers, "No saved customers", "l", "r1", "customers")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, customer_update)
                    up_or_norm_list("Saved", "customers", "(Name : Address : Phone Number)", "u")
                    main_variable, customer_update = repeating_input_or_cancel("\nEnter customer name or number to update\n→ ", "y", "l", "r2")
                    while main_variable == "r2":
                        main_variable, con_int, error_print = automated_data_find_sort(customer_update, customers, 'Name', "r1", "r3")
                        while main_variable == "r3":
                            main_variable, or_nap = repeating_input_or_cancel("\nDo you want to change Name (N), Address (A), or Phone (P)?\n→ ", "y", "r1", "r4")
                            while main_variable == "r4":
                                from Input_Modules import (name_choose_inputs_u, address_choose_inputs_u, phone_choose_inputs_u, customer_edit_options)
                                if or_nap in name_choose_inputs_u:
                                    name_change = (input("\nEnter updated name\n→ : ")).strip()
                                    key_type, update_data = 'Name', name_change
                                    main_variable = "r5"
                                if or_nap in address_choose_inputs_u:
                                    address_change = (input("\nEnter updated address\n→ : ")).strip()
                                    key_type, update_data = 'Address', address_change
                                    main_variable = "r5"
                                if or_nap in phone_choose_inputs_u:
                                    phone_change = input("\nEnter updated phone number\n→ : ").strip()
                                    key_type, update_data = 'Phone', phone_change
                                    main_variable = "r5"
                                if or_nap not in customer_edit_options:
                                    print(error_messages(or_nap, "general"))
                                    main_variable = "r3"
                                while main_variable == "r5":
                                    main_variable = cancel_option(update_data, "r3", "r6")
                                    while main_variable == "r6":
                                        item_ID = customers[con_int]['ID']
                                        update_row_x_in_table_x(key_type, update_data, item_ID, "customers", "customer_ID")
                                        main_variable = sub_menu_cap("u", "Edit another customer (U)", (f"{customers[con_int]['Name']} {key_type} has been updated to {update_data} in saved customers"))
        if customers_sub_menu_selection in customers_menu_option_4_inputs:
            main_variable = "r"
            while main_variable == "r":
                customers = call_customers()
                customer_deletion, error_print = "", ""
                main_variable, only_now = in_case_of_empty_lists(customers, "No saved customers", "l", "r1", "customers")
                while main_variable == "r1":
                    clear_screen()
                    error_print_and_list_after_clear_screen(error_print, customer_deletion)
                    up_or_norm_list("Saved", "customers", "(Name : Address : Phone Number)", "u")
                    main_variable, customer_deletion = repeating_input_or_cancel('Enter the customer name or number to delete: (Enter "all" to delete all)\n\n→ ', "y", "l", "r2")
                    while main_variable == "r2":
                        if customer_deletion == "all":
                            main_variable = if_all(customers, "r3", "r1", "customers", "data/customers_undo_option.csv")
                            item_ID, con_int = "", 0
                        else:
                            main_variable, con_int, error_print = automated_data_find_sort(customer_deletion, customers, 'Name', "r1", "r3")
                        while main_variable == "r3":
                            item_ID = customers[con_int]['ID']
                            main_variable = delete_function_cover_all(customer_deletion, "r4", item_ID, "customers", "customer_ID")
                            while main_variable == "r4":
                                if customer_deletion == "all":
                                    main_variable = sub_menu_cap("u", "Undo delete all customers (U)", "All customers deleted")
                                else: 
                                    main_variable = sub_menu_cap("u", "Delete another customer (R)", (f"{customers[con_int]['Name']} has been deleted from saved customers"))
                                while main_variable in undo_delete_all:
                                    restore_customers_using_csv_to_database()
                                    main_variable = sub_menu_cap("u", "Delete customer (R)", "Customers restored")
    if main_variable in valid_exit_input_options:
        main_variable = save_and_exit_function()
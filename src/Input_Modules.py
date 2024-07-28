valid_product_menu_running_options = ["p", "1","products","products please", "products bruh", "products menu bruh","product", "product menu","return to products menu",
"return to products","return to p","return p","r p","rp","r product", "r products", "return products","return product","products menu", "products menu please",
"go to products menu", "go to products", "yo products","products yo","please product", "please products", "products fr", "return to products menu", "return to product menu", 
"hook me up with the product menu", "hook me up with the products menu","option p","option 1"]

valid_order_menu_running_options = ["o", "2", "orders","orders bruh", "orders menu bruh","order", "orders please", "order menu", "return to orders menu","return to order menu",
"return o","return","r orders","r orders menu","orders menu",  "orders menu please", "go to orders menu", "go to orders", "please order","please orders", "orders fr", 
"yo orders","orders yo","orders bro", "return to orders menu", "return to order menu", "hook me up with the order menu", "hook me up with the orders menu", "option o", "option 2"]

valid_courier_input_options = ["c", "3","courier","couriers", "couriers menu","option 3","option c","courier bro","couriers bro","take me to the couriers menu","take me to couriers",
"go to couriers","couriers bruh", "courier bruh", "couriers fr","courier fr","couriers ong","courier ong","couriers on god","just take me to couriers","couriers now","courier menu"]

valid_customer_input_options = ["l", "4", "customer", "customers", "customers menu," "option 4", "option u", "customer bro", "customers bro", "take me to the customers menu", "take me to customers",
"go to customers", "customers bruh", "customer bruh", "customers fr", "customer fr", "customers ong", "customer ong", "customers on god", "just take me to customers", "customers now", "customer menu"]
 
valid_exit_input_options = ["e", "5","exit", "exit program", "please exit", "please exit program", "close", "please close","close program", "please close program", 
"quit", "please quit", "quit program","please quit program", "bruh exit","bruh just exit", "bruh just exit fr","just exit fr", "shutdown", "shut down",]

main_menu_inputs = ["m123", "m", "main", "main menu", "return to main menu", "go back to main menu","go back to main", 
"main menu bruh", "main menu bro", "main menu fr", "hook me up with the main menu", "x"]

product_menu_option_0_inputs = ["0", "return to main menu", "return", "main", "main menu", "go back", "i didn't mean to go to products", 
"i didn't mean to go to the products menu", "i didn't mean to go to the product menu", "x"]
product_menu_option_1_inputs = ["1", "show avaliable products", "print products", "products list", 
"show product list", "product list", "show products list", "show list", "list show", "show products"]
product_menu_option_2_inputs = ["2", "add product", "add new", "create", "add new product", "new product", "create new"]
product_menu_option_3_inputs = ["3", "update product", "update", "rewrite", "change product name", "fix product", "update existing product", "update existing", "edit product"]
product_menu_option_4_inputs = ["4", "delete product", "delete", "product deletion", "remove", "remove product"]

orders_menu_option_0_inputs = ["0", "return to main menu", "return", "main", "main menu", "go back", "i didn't mean to go to orders", 
"i didn't mean to go to the orders menu", "i didn't mean to go to the order menu", "x"]
orders_menu_option_1_inputs = ["1", "show current orders", "show orders", "show list", "print orders", "current orders", "list orders", "order list", "orders list", "current orders list", "list current orders",
"view", "read"]
orders_menu_option_2_inputs = ["2", "add an order", "order add", "add orders", "add order", "new order"]
orders_menu_option_3_inputs = ["3" , "update order status"]
orders_menu_option_4_inputs = ["4", "change details", "edit details", "details", "edit details", "fix details", "order detail change", "orders detail change", "change order detail", "change order details", "change detail", "change details"]
orders_menu_option_5_inputs = ["5", "delete", "order delete", "order deletion" "delete order", "delete orders", "remove", "remove order", "remove orders", "order removal", "cancel order", "order cancelation", "cancel"]

all_order_menu_choosing_inputs = (orders_menu_option_0_inputs + orders_menu_option_1_inputs +
orders_menu_option_2_inputs + orders_menu_option_3_inputs + orders_menu_option_4_inputs +
orders_menu_option_5_inputs)

couriers_menu_option_0_inputs = ["0", "return to main menu", "return", "main", "main menu", "go back", "i didn't mean to go to couriers", 
"i didn't mean to go to the couriers menu", "i didn't mean to go to the courier menu", "m", "x"]
couriers_menu_option_1_inputs = ["1", "show avaliable couriers", "print couriers", "couriers list", "show current customers",
"show courier list", "courier list", "show couriers list", "show list", "list show", "view all", "view all couriers", "view", "read"]
couriers_menu_option_2_inputs = ["2", "add courier", "add new", "create", "add new courier", "new courier", "add couriers"]
couriers_menu_option_3_inputs = ["3", "update courier", "update", "rewrite", "change courier name", "fix courier", "update existing courier", "update existing", "edit courier",
"edit", "update"]
couriers_menu_option_4_inputs = ["4", "delete courier", "delete", "courier deletion", "remove", "remove courier", "courier delete"]

customers_menu_option_0_inputs = ["0", "return to main menu", "return", "main", "menu", "go back", "i didn't mean to go to customers",
"i didn't mean to go to the customers menu", "i didn't mean to go to the customer menu", "m", "x"]
customers_menu_option_1_inputs = ["1", "show customers", "show current customers", "show avaliable customers", "print customers", "customers list",
"show customer list", "customer list", "show customers list", "show list", "list show", "view all", "view all customers", "view", "read"]
customers_menu_option_2_inputs = ["2", "add customer", "add customers", "add new customers", "add new customer", "add customers", "new customer", "new", "add"]
customers_menu_option_3_inputs = ["3", "update customer", "update", "rewrite", "change customer name", "fix customer", "update existing customer", "update existing", "edit customer"]
customers_menu_option_4_inputs = ["4", "delete customer", "delete", "customer deletion", "customer delete", "remove", "remove customer"]

all_customer_menu_choosing_inputs = (customers_menu_option_0_inputs + customers_menu_option_1_inputs + customers_menu_option_2_inputs + customers_menu_option_3_inputs + customers_menu_option_4_inputs)

all_product_menu_choosing_inputs = (product_menu_option_0_inputs + product_menu_option_1_inputs + 
product_menu_option_2_inputs + product_menu_option_3_inputs + product_menu_option_4_inputs)

all_courier_menu_choosing_inputs = (couriers_menu_option_0_inputs + couriers_menu_option_1_inputs + couriers_menu_option_2_inputs +
couriers_menu_option_3_inputs + couriers_menu_option_4_inputs)

price_choose_inputs = ["price", "i want to change the price", "change price", "price change", "p", "change product price", "product change price", "product price change", "update price"]
label_choose_inputs = ["label", "i want to change the label", "change label", "label change", "l", "change product label", "product change label", "product label change", "update label"]
stock_choose_inputs = ["stock", "i want to change the stock", "change stock", "stock change", "s", "change product stock", "product change stock", "product stock change", "update stock"]
either_or_price_label_stock = (price_choose_inputs + label_choose_inputs + stock_choose_inputs)

name_choose_inputs_c = ["name", "i want to change the name", "change name", "name change", "n", "change courier name", "courier change name", "courier name change"]
phone_choose_inputs_c = ["phone", "i want to change the phone number", "phone number", "i want to change the phone", "change phone", "phone change", "p", "change courier phone", "courier phone number change"]
either_or_name_phone_c = (name_choose_inputs_c + phone_choose_inputs_c)

undo_delete_all = ["i didn't mean to delete all", "u", "undo", "undo delete all", "undo deletion", "undo delete"]

ready_for_pickup_inputs = ['ready for pickup', 'order is ready for pickup', 'ready', 'r', 'pickup']
in_transit_inputs = ['on the way', 't', "it's on it's way", 'in transit', 'transit', 'in-transit']
delivered_inputs = ['d', 'delivered', 'order complete', 'complete', 'order has been delivered', 'done']
valid_status_change_options = (ready_for_pickup_inputs + in_transit_inputs + delivered_inputs)

order_name_change = ['name', 'n', 'change order name', 'order name change', 'change name', 'update name']
order_address_change = ['a', 'address', 'change order address', 'order address change', 'change address', 'update address']
order_phone_change = ['p', 'phone', 'phone number', 'change order phone', 'order phone change', 'change order phone number', 'order phone number change', 'update phone', 'update phone number']
order_courier_change = ['c', 'courier', 'change order courier', 'order courier change', 'change courier', 'update courier']
order_items_change = ['i', 'items', 'change order items', 'order items change', 'change items', 'update order items', 'updates items', 'order items']
valid_detail_change_options = (order_name_change + order_address_change + order_phone_change + order_courier_change + order_items_change)

name_choose_inputs_u = ["name", "i want to change the name", "change name", "name change", "n", "change customer name", "customer change name", "customer name change"]
phone_choose_inputs_u = ["phone","phone number", "i want to change the phone number", "i want to change the phone", "change phone", "phone change", "p", "change customer phone", "customer phone number change"]
address_choose_inputs_u = ["address", "i want to change the address", "change address", "address change", "a", "change customer address", "customer address change", "update phone", "update phon number"]
customer_edit_options = (name_choose_inputs_u + phone_choose_inputs_u + address_choose_inputs_u)

main_valid_inputs = (valid_product_menu_running_options + valid_order_menu_running_options + valid_courier_input_options +
main_menu_inputs + all_customer_menu_choosing_inputs + valid_exit_input_options+["r"] + undo_delete_all + ["a"] + ["s"] + valid_customer_input_options)

yes_list = ['y', 'yes', 'yep', 'sure', 'yeah', 'for sure']
no_list = ['n', 'no', 'nope', 'nuh uh', 'hell no', 'na', 'nah']
no_and_yes_list = (yes_list + no_list)


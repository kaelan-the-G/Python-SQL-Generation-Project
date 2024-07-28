**Overview: (Project background and client requirements)**

This program is primarily designed to manage orders for a cafe/bistro type business looking to get into orders and deliveries. 

It allows the user to create and track products, employeed couriers, orders and saved customers. 

Once any information is created and imputed it is then stored in a database, as well as being saved to a local CSV file upon exiting the program in a standard way. (I.e. The user enters the correct input for exiting rather than killing the program before it can save.) dfhuierhg

Once there are products and couriers available in the program orders can then be added which contain customer names, addresses, phone numbers as well as the order’s current status (‘Preparing, ‘Ready For Pickup’, ‘In Transit’, ‘Delivered’), the courier assigned to the order, and the products being delivered.

In the order sub menu the orders can be printed by status or courier for tracking current deliveries.

Customers can be added from scratch upon which the program will prompt the user, asking if they want to save the customer to a list of saved customers. If the user enters a yes input the program will add the new order’s customer name, address and phone number to the database as well.

If saved customers are already present in the program’s working memory when adding orders, the program will prompt the user with a question asking if they would like to add a customer from this saved customer data for efficient use when serving repeat customers.

Upon adding an order each product added to the order will have its stock subtracted by one from the given product’s inventory.

The program does not allow for multiple of the same product per order but does allow for multiple products of different kinds.

The orders menu has an option to quickly choose an order and change the status and a separate sub menu for other order edits/updates.

If an order is deleted before it is delivered the product stock will not be readded, assuming prepared food would be unusable.

A customer sub menu allows the user to add and view saved customers directly.

All sub menus also allow the user to update or delete data from the database.
The program offers the option to delete every saved item of a specific set of data simultaneously, and an undo option for after doing this. If the user decides to delete all items from either products, orders, couriers or customers a backup csv is exported just in case. Upon undoing this action, all the information will be restored to the database.

If at any time the user wishes to cancel or return to a previous input they can enter **x**.

**How to use:**

1. Before running make sure the modules pymysql and python-dotenv are installed in your python environment. This can be done with the following commands.

 - **py -m pip install pymysql**

 - **py -m pip install python-dotenv**

2. If running this program from an interface such as VSCode or PyCharm make sure you are running it out of the folder containing the sub-folders, data, src, notes and tests. Running it out of a wider directory will cause errors with the relative paths used in the program. If running the program out of a terminal, first navigate to this directory using:  **cd <your-path-here>**, and then: **cd src**.

3. Once in the correct directory either run the program from the editor or use the command: **py Kaelan_mini_project_final.py** in the terminal.

4. Instructions are clearly presented within the program itself in terms of inputs while using. The cancel feature is only explained once in the main menu. “If at any time you want to cancel type x.” To avoid error messages try to be aware of your spelling but the program will strip user input and ignore case sensitivity. There is the possibility of multiple acceptable inputs in the program (such as either “yes” or “y”) yet the most effective and least likely to cause errors is simply inputting the main options given. (Shown in brackets such as (P), (L), (they do not need to be uppercase))

5. Make sure to use the in-built exit function within the program instead of killing it if you want the save data to be saved locally in addition to the database.

6. The program is designed to keep running regardless of incorrect user input.

**How to run unit tests:**

1. As long as pymlsql is installed (Instructions in: how to use, above.), simply opening a terminal in the right directory and entering the command **py -m pytest**, will run the program unit tests.

**Project reflections:**

How did my design go about meeting the project requirements?

The requirements of the project definitely are met including all optional stretch goals. I would say however that in a real situation there are a few additional things that would be needed. (Such as the option for multiple quantities of an individual product in an order.)

I would say however that early on in the project I definitely overdid it with some of the options and features I wanted available in the project such as it accepting multiple inputs for the same option. (Which really would be unnecessary once a user was more familiar with using the program.)

I structured each sub menu with a lot of nested ifs and whiles and I have functions which fulfill the specific tasks in each. It would take too much detail to describe all of them but in a concise way the structure of my code is highly nested.

I would say that the unit tests were a bit of an afterthought. I definitely wasn’t really operating in a test driven development workflow. The unit tests I have are quite simple and don’t cover some of the more complex functions I have. 

**How did you guarantee the project’s requirements?**

I have some unit tests yet the way I guaranteed functionality was mostly through running the program and trying as many paths and user input possibilities as possible (and as many edge/corner cases as possible). If a bug came up I would then look for the cause and fix it. Then just checking the saved data. In future a far less frustrating way of doing this would be unit tests and a focus on test driven development.

**If I had more time, what is one thing I would improve on?**

I would do test driven development rather than coding first. This would save frustration and time later. I would also learn more about the mock() function and testing in general, I feel this is an area I need improvement in.

**What did I most enjoy implementing?**

I enjoyed figuring out a way to get the program to accept either names or indexes as ways of picking items in the products, orders, customers and courier lists. Although I do see that technically it wasn't a requirement, it was still fun to learn and finally get working in implementation. I also really enjoyed creating and using functions once I started to better understand them.

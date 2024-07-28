#Inputs for these functions are given by the programmer so we only really have to consider common case here

import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

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

def test_preparing_is_1():
    result = convert_status_name_to_status_id('Preparing')
    assert result == 1

def test_ready_is_2():
    result = convert_status_name_to_status_id('Ready For Pickup')
    assert result == 2

def test_transit_is_3():
    result = convert_status_name_to_status_id('In Transit')
    assert result == 3

def test_transit_is_4():
    result = convert_status_name_to_status_id('Delivered')
    assert result == 4

def test_1_is_preparing():
    result = convert_status_id_to_status_name(1)
    assert result == "Preparing"

def test_2_is_ready():
    result = convert_status_id_to_status_name(2)
    assert result == "Ready For Pickup"

def test_3_is_transit():
    result = convert_status_id_to_status_name(3)
    assert result == "In Transit"

def test_4_is_delivered():
    result = convert_status_id_to_status_name(4)
    assert result == "Delivered"
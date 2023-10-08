"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# connect to db
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Anna450053!'
)


try:
    with conn:
        with conn.cursor() as cur:
            with open('C:/Users/Lena/PycharmProjects/postgres-homeworks/homework-1/north_data/customers_data.csv', 'r', newline="", encoding='UTF-8') as file:
                customers_reader = csv.reader(file)
                next(customers_reader)
                for row in customers_reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)

            with open('C:/Users/Lena/PycharmProjects/postgres-homeworks/homework-1/north_data/employees_data.csv', 'r', newline="", encoding='UTF-8') as file:
                employee_reader = csv.reader(file)
                next(employee_reader)
                for r in employee_reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", r)

            with open('C:/Users/Lena/PycharmProjects/postgres-homeworks/homework-1/north_data/orders_data.csv', 'r', newline="", encoding='UTF-8') as file:
                orders_reader = csv.reader(file)
                next(orders_reader)
                for l in orders_reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", l)
finally:
    conn.close()

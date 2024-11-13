"""
Основной модуль для вызова функций из модулей functions_1.py и functions_2.py.
"""

from functions_1 import process_order, calculate_total, validate_customer
from functions_2 import find_customer_in_db, apply_discount, submit_order

if __name__ == "__main__":
    # Вызов функций из functions_1.py
    print(process_order(10))
    print(calculate_total(5, 20))
    print(validate_customer(123))

    # Вызов функций из functions_2.py
    print(find_customer_in_db("Sergei Shilov"))
    print(apply_discount(1000, 10))
    print(submit_order(500))
"""
Модуль с примерами функций 1-3.
"""

from exceptions import InvalidOrderValue, CalculationError

# 1. Функция без обработки исключений
def process_order(order_value):
    """Обрабатывает заказ, выбрасывает исключение при отрицательном значении"""
    if order_value < 0:
        raise InvalidOrderValue("Значение заказа не может быть отрицательным.")
    return order_value * 10

# 2. Функция с общим обработчиком исключений
def calculate_total(amount, price):
    """Выполняет расчет общей стоимости, обрабатывает исключения общего типа."""
    try:
        total = amount * price
        if total < 0:
            raise CalculationError("Общая стоимость не может быть отрицательной.")
        return total
    except Exception as e:
        print(f"Ошибка при расчете: {e}")
        return 0

# 3. Функция с finally
def validate_customer(customer_id):
    """Проверяет существование клиента и всегда закрывает соединение с БД."""
    try:
        if customer_id <= 0:
            raise ValueError("ID клиента должен быть положительным числом.")
        # Имитация проверки в БД
        if customer_id != 123:
            raise KeyError("Клиент не найден.")
        return "Клиент найден."
    except Exception as e:
        print(f"Ошибка проверки клиента: {e}")
        return "Ошибка"
    finally:
        print("Соединение с БД закрыто.")
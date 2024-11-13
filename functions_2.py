"""
Модуль с примерами функций 4-7.
"""

from exceptions import OrderError, CustomerNotFound, InvalidOrderValue
from exceptions import InvalidOrderValue, CalculationError

# 4. Функция с несколькими обработчиками исключений
def find_customer_in_db(customer_name):
    """Ищет клиента в БД по имени и выбрасывает разные исключения."""
    try:
        if not customer_name:
            raise ValueError("Имя клиента не может быть пустым.")
        if customer_name == "Unknown":
            raise CustomerNotFound("Клиент не найден.")
        if customer_name.isdigit():
            raise InvalidOrderValue("Имя клиента не может быть числом.")
        return "Клиент успешно найден."
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except CustomerNotFound as e:
        print(f"Ошибка поиска: {e}")
    except InvalidOrderValue as e:
        print(f"Ошибка валидации: {e}")
    finally:
        print("Завершение поиска клиента.")

# 5. Функция с генерацией исключений
def apply_discount(price, discount):
    """Применяет скидку к цене и обрабатывает все исключения внутри функции."""
    try:
        if discount < 0 or discount > 100:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")
        if price < 0:
            raise CalculationError("Цена не может быть отрицательной.")
        discounted_price = price - (price * discount / 100)
        return discounted_price
    except ValueError as e:
        print(f"Ошибка скидки: {e}")
    except CalculationError as e:
        print(f"Ошибка цены: {e}")
    finally:
        print("Завершение применения скидки.")

# 6. Пример использования пользовательского исключения
def create_order(order_value):
    """Создает заказ, выбрасывает исключение при неверном значении заказа."""
    if order_value <= 0:
        raise InvalidOrderValue("Значение заказа должно быть положительным.")
    return f"Заказ на сумму {order_value} создан успешно."

# 7. Функция с обработкой пользовательского исключения
def submit_order(order_value):
    """Отправляет заказ, обрабатывает исключение InvalidOrderValue."""
    try:
        order = create_order(order_value)
        return order
    except InvalidOrderValue as e:
        print(f"Ошибка создания заказа: {e}")
    finally:
        print("Завершение отправки заказа.")
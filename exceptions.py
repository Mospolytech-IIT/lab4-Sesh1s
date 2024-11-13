"""
Модуль с пользовательскими исключениями.
"""

class OrderError(Exception):
    """Базовый класс исключений для заказов."""
    pass

class InvalidOrderValue(OrderError):
    """Исключение при неверном значении заказа."""
    pass

class CalculationError(Exception):
    """Ошибка при выполнении расчетов."""
    pass

class CustomerNotFound(Exception):
    """Исключение, если клиент не найден в базе."""
    pass
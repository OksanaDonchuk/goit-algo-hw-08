import heapq
from typing import List

def min_cost_connecting_cables(cables: List[int]) -> int:
    """
    Обчислює мінімальні витрати на з'єднання кабелів.
    
    Алгоритм використовує мінімальну купу для поступового об'єднання найкоротших кабелів,
    забезпечуючи оптимальний порядок з'єднання.

    Args:
        cables (List[int]): Список довжин кабелів.

    Returns:
        int: Мінімальна сума витрат на з'єднання всіх кабелів.
    """
    if not cables:
        return 0  # Якщо немає кабелів, витрати = 0
    if len(cables) == 1:
        return 0  # Один кабель не потребує з'єднання

    # Створюємо мінімальну купу
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)

        # Витрати на з'єднання
        cost = first_cable + second_cable
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [10, 2, 6, 12]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_connecting_cables(cables))
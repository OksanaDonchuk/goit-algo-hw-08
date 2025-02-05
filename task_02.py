import heapq
from typing import List

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків у один відсортований список.

    Використовує структуру даних "мінімальна купа" (heap) для ефективного злиття.

    Алгоритм:
    1. Додаємо перші елементи кожного списку в heap.
    2. Дістаємо мінімальний елемент та додаємо наступний елемент з того ж підсписку.
    3. Повторюємо процес, поки всі елементи не опрацьовані.

    Складність: O(N log k), де 
        - N — загальна кількість елементів у всіх списках,
        - k — кількість списків.

    Args:
        lists (List[List[int]]): Список відсортованих списків.

    Returns:
        List[int]: Відсортований об'єднаний список.
    """
    min_heap = []
    
    # Додаємо перші елементи кожного списку в купу
    for i, lst in enumerate(lists):
        if lst:  # Переконуємося, що список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)
    
    merged_list = []
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        # Додаємо наступний елемент із цього ж списку в купу (якщо є)
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list

# Приклад використання:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
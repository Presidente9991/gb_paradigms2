"""
Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки.
Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
Входные данные:
Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
Координаты начальной и конечной точки.
Выходные данные:
Массив координат пути или сообщение об ошибке.
"""


def search_path(array, start_path, end_path):
    if len(array) == 0 or len(array[0]) == 0:
        return None

    start_row, start_col = start_path
    end_row, end_col = end_path
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    visited = [[False for _ in range(len(array[i]))] for i in range(len(array))]

    def dfs(row, col, history):
        if (
                row < 0
                or row >= len(array)
                or col < 0
                or col >= len(array[row])
                or visited[row][col]
                or array[row][col] == 1
        ):
            return None
        history = history.copy()

        visited[row][col] = True
        history.append((row, col))

        if row == end_row and col == end_col:
            return history

        for sum_row, sum_col in directions:
            new_history = dfs(row + sum_row, col + sum_col, history)
            if new_history is not None:
                return new_history

        return None

    return dfs(start_row, start_col, [])


array_maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
]
start = (4, 1)
end = (4, 3)

path = search_path(array_maze, start, end)
if path:
    print(path)
else:
    print("Невозможно найти путь")

import json

class NutrientSolutionCalculator:
    def __init__(self):
        # Загрузка данных о растворе и удобрениях из файлов
        with open("tuja.txt", "r") as solution_file:
            self.solution_data = json.load(solution_file)

        with open("fertilizers.txt", "r") as fertilizers_file:
            self.fertilizers_data = [json.loads(line) for line in fertilizers_file]

        # Заданные элементы в растворе и их требуемые значения
        self.target_elements = self.solution_data["elements"]

        # Доступные удобрения и их содержание элементов
        self.available_fertilizers = {fertilizer["name"]: fertilizer["elements"] for fertilizer in self.fertilizers_data}

        # Ограничение на количество удобрений
        self.max_fertilizers = 8

        # Начальное приближение состава удобрений
        self.initial_fertilizers = {fertilizer_name: 0 for fertilizer_name in self.available_fertilizers.keys()}

    # Функция для расчета отклонения
    def deviation(self, fertilizers):
        total_elements = {element: 0 for element in self.target_elements.keys()}
        for fertilizer_name, amount in fertilizers.items():
            for element, value in self.available_fertilizers[fertilizer_name].items():
                total_elements[element] += value * amount
        return sum(max(abs(total_elements[element] - self.target_elements[element]["min"]), abs(total_elements[element] - self.target_elements[element]["max"])) for element in self.target_elements)

    # Метод градиентного спуска с ограничениями
    def gradient_descent_with_constraints(self, initial_fertilizers, max_iter=3000, tolerance=1e-5, step_size=0.01):
        current_fertilizers = initial_fertilizers.copy()
        for _ in range(max_iter):
            gradient = {fertilizer_name: 0 for fertilizer_name in self.available_fertilizers.keys()}
            # Вычисляем градиент
            for fertilizer_name, amount in current_fertilizers.items():
                current_fertilizers[fertilizer_name] += tolerance
                upper_deviation = self.deviation(current_fertilizers)
                current_fertilizers[fertilizer_name] -= 2 * tolerance
                lower_deviation = self.deviation(current_fertilizers)
                gradient[fertilizer_name] = (upper_deviation - lower_deviation) / (2 * tolerance)
                current_fertilizers[fertilizer_name] += tolerance
            # Обновляем состав удобрений с учетом ограничений
            for fertilizer_name, amount in current_fertilizers.items():
                # Ограничиваем количество удобрения, чтобы оно не становилось отрицательным
                if current_fertilizers[fertilizer_name] - step_size * gradient[fertilizer_name] < 0:
                    current_fertilizers[fertilizer_name] = 0
                else:
                    current_fertilizers[fertilizer_name] -= step_size * gradient[fertilizer_name]
            # Проверяем условие останова
            if all(abs(gradient[fertilizer_name]) < tolerance for fertilizer_name in self.available_fertilizers.keys()):
                break
        return current_fertilizers

    # Функция для форматирования раствора в строку
    @staticmethod
    def format_solution(solution):
        solution_string = ""
        for element, content in solution.items():
            solution_string += f"{element}: {round(content, 2)}, "
        return solution_string.rstrip(", ")    
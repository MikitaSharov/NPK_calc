class NutrientSolutionCalculator:
    @staticmethod
    def calculate_solution(nutrient_solution, fertilizers):
        # Создаем копию значений содержания элементов для изменений
        solution_content = nutrient_solution.elements.copy()
        # Проходим по приоритетным элементам и удовлетворяем их требования
        priority_elements = ['N', 'P', 'K', 'Mg', 'Ca', 'S']
        for element in priority_elements:
            min_content, max_content = nutrient_solution.get_element_content(element)
            current_content = solution_content[element]
            optimal_content = (min_content + max_content) / 2
            best_fertilizer = None
            best_evaluation = float('inf')  # Инициализируем максимальной оценкой
            for fertilizer in fertilizers:
                if fertilizer.element == element:
                    fertilizer_content = fertilizer.content_percent / 100
                    # Проверяем, не превысили ли мы максимальное содержание элемента
                    if current_content + fertilizer_content <= max_content:
                        # Оцениваем подходящесть удобрения
                        evaluation = evaluate_fertilizer(fertilizer, current_content, min_content, max_content)
                        # Если удобрение лучше предыдущего, сохраняем его
                        if evaluation < best_evaluation:
                            best_fertilizer = fertilizer
                            best_evaluation = evaluation
            # Если нашли подходящее удобрение, добавляем его содержание в раствор
            if best_fertilizer:
                fertilizer_content = best_fertilizer.content_percent / 100
                solution_content[element] += fertilizer_content
        # Возвращаем полученный питательный раствор
        return solution_content

# Вспомогательная функция для оценки подходящести удобрения
def evaluate_fertilizer(fertilizer, current_content, min_content, max_content):
    """
    Оценка подходящести удобрения для элемента.
    Чем меньше разница между текущим содержанием элемента и его оптимальным значением,
    тем выше оценка.
    """
    element = fertilizer.element
    # Обработка случаев с оксидами
    oxides_conversion = {'K2O': ('K', 0.83), 'P2O5': ('P', 0.44), 'MgO': ('Mg', 0.6), 'CaO': ('Ca', 0.71), 'SO3': ('S', 0.4)}
    if element in oxides_conversion:
        # Преобразуем оксид в соответствующий элемент
        element, conversion_factor = oxides_conversion[element]
        current_content *= conversion_factor
    # Получаем требуемое содержание элемента в питательном растворе
    optimal_content = (min_content + max_content) / 2
    # Оцениваем подходящесть удобрения
    difference = abs(optimal_content - current_content)
    return difference

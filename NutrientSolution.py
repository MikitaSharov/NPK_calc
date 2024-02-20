class NutrientSolution:
    def __init__(self, name):
        self.name = name
        self.elements = {
            'N': {'min': 0, 'max': 0},
            'P': {'min': 0, 'max': 0},
            'K': {'min': 0, 'max': 0},
            'Mg': {'min': 0, 'max': 0},
            'Ca': {'min': 0, 'max': 0},
            'S': {'min': 0, 'max': 0},
            'Fe': {'min': 0, 'max': 0},
            'Mn': {'min': 0, 'max': 0},
            'Cu': {'min': 0, 'max': 0},
            'Zn': {'min': 0, 'max': 0},
            'B': {'min': 0, 'max': 0},
            'Mo': {'min': 0, 'max': 0}
        }

    def set_element_content(self, element, min_content, max_content=None):
        if element in self.elements:
            if max_content is None:
                max_content = min_content
            self.elements[element]['min'] = min_content
            self.elements[element]['max'] = max_content
        else:
            print(f"Ошибка: Элемент {element} не найден в списке элементов питательного раствора.")

    def get_element_content(self, element):
        if element in self.elements:
            return self.elements[element]['min'], self.elements[element]['max']
        else:
            print(f"Ошибка: Элемент {element} не найден в списке элементов питательного раствора.")
            return None, None

    def display_solution(self):
        print(f"Содержание элементов в питательном растворе '{self.name}' (мг/л): " +
          ", ".join([f"{element}: {content_range['min']}-{content_range['max']}" 
                     for element, content_range in self.elements.items()]))

# Пример использования класса NutrientSolution
# solution = NutrientSolution("Раствор для помидоров")
# solution.set_element_content('N', 50, 75)
# solution.set_element_content('P', 25, 40)
# solution.set_element_content('K', 70)
# solution.display_solution()

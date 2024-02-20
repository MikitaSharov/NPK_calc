from NutrientSolutionIO import NutrientSolutionIO
from NutrientSolution import NutrientSolution

class NutrientSolutionInput:
    @staticmethod
    def input_nutrient_solution_manually_and_save():
        name = input("Введите название питательного раствора: ")
        solution = NutrientSolution(name)  # Здесь вызываем конструктор класса NutrientSolution
        print("Введите данные о содержании элементов в питательном растворе:")
        for element in solution.elements:
            min_content = float(input(f"Минимальное содержание {element} (мг/л): "))
            max_content = float(input(f"Максимальное содержание {element} (мг/л): "))
            solution.set_element_content(element, min_content, max_content)
        filename = input("Введите имя файла для сохранения питательного раствора: ")
        NutrientSolutionInput.save_solution_to_file(solution, filename)
        print(f"Питательный раствор '{solution.name}' сохранен в файл '{filename}'.")
        return solution

    @staticmethod
    def input_nutrient_solution_from_file(filename):
        return NutrientSolutionIO.load_from_file(filename)

    @staticmethod
    def save_solution_to_file(solution, filename):
        NutrientSolutionIO.save_to_file(solution, filename)
        print(f"Питательный раствор '{solution.name}' сохранен в файл '{filename}'.")

    @staticmethod
    def load_solution_from_file(filename):
        solution = NutrientSolutionIO.load_from_file(filename)
        print(f"Питательный раствор '{solution.name}' загружен из файла '{filename}'.")
        return solution

    @staticmethod
    def menu():
        print("Меню:")
        print("1. Ввести питательный раствор вручную и сохранить в файл")
        print("2. Загрузить питательный раствор из файла")
        choice = input("Выберите действие (1/2): ")
        if choice == '1':
            return NutrientSolutionInput.input_nutrient_solution_manually_and_save()
        elif choice == '2':
            filename = input("Введите имя файла: ")
            return NutrientSolutionInput.input_nutrient_solution_from_file(filename)
        else:
            print("Неверный ввод.")
            return None

# Пример использования сохранения и загрузки данных из файла
# solution = NutrientSolutionInput.menu()
# if solution:
#     loaded_solution = NutrientSolutionInput.load_solution_from_file('nutrient_solution.json')
#     loaded_solution.display_solution()

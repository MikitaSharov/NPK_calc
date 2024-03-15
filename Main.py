from NutrientSolutionInput import NutrientSolutionInput
from FertilizerInput import FertilizerInput
from NutrientSolutionCalculator import NutrientSolutionCalculator


def main():
    nutrient_solution = NutrientSolutionInput.menu()
    if nutrient_solution:
        fertilizers = FertilizerInput.menu()
        if fertilizers:
            calculator = NutrientSolutionCalculator(nutrient_solution)
            optimal_fertilizers = calculator.gradient_descent_with_constraints(calculator.initial_fertilizers)
            print("Оптимальный состав удобрений:")
            for fertilizer, amount in optimal_fertilizers.items():
                print(f"{fertilizer}: {round(amount * 100, 0)} mg/l")
            # Рассчет получившегося раствора
            print("\nПолучившийся питательный раствор:")
            calculated_solution = {}
            for fertilizer_name, amount in optimal_fertilizers.items():
                for element, value in calculator.available_fertilizers[fertilizer_name].items():
                    calculated_solution[element] = calculated_solution.get(element, 0) + value * amount
            # Форматирование раствора в строку и вывод
            print(calculator.format_solution(calculated_solution))
    print(NutrientSolutionInput.format_solution(nutrient_solution))


if __name__ == "__main__":
    main()

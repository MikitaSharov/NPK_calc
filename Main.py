from NutrientSolutionInput import NutrientSolutionInput
from FertilizerInput import FertilizerInput
from NutrientSolutionCalculator import NutrientSolutionCalculator

def main():
    nutrient_solution = NutrientSolutionInput.menu()
    if nutrient_solution:
        NutrientSolutionInput.save_solution_to_file(nutrient_solution, 'nutrient_solution.json')
        fertilizers = FertilizerInput.input_fertilizers()
        calculated_solution = NutrientSolutionCalculator.calculate_solution(nutrient_solution, fertilizers)
        print("\nРассчитанный питательный раствор:")
        for element, content in calculated_solution.items():
            print(f"{element}: {content}")

if __name__ == "__main__":
    main()

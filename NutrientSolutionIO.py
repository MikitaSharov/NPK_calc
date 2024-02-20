import json
from NutrientSolution import NutrientSolution

class NutrientSolutionIO:
    @staticmethod
    def save_to_file(nutrient_solution, filename):
        with open(filename, 'w') as f:
            json.dump({'name': nutrient_solution.name, 'elements': nutrient_solution.elements}, f)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            nutrient_solution = NutrientSolution(data['name'])
            nutrient_solution.elements = data['elements']
            return nutrient_solution
        
import json
from NutrientSolution import NutrientSolution
from Fertilizer import Fertilizer

class IO:
    @staticmethod
    def save_solution_to_file(nutrient_solution, filename):
        with open(filename, 'w') as f:
            json.dump({'name': nutrient_solution.name, 'elements': nutrient_solution.elements}, f)

    @staticmethod
    def load_solution_from_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            nutrient_solution = NutrientSolution(data['name'])
            nutrient_solution.elements = data['elements']
            return nutrient_solution
    
    @staticmethod
    def save_fertilizers_to_file(fertilizers, filename):
        with open(filename, 'w') as f:
            for fertilizer in fertilizers:
                json.dump({'id': fertilizer.id, 'name': fertilizer.name, 'elements': fertilizer.elements}, f)
                f.write('\n')

    @staticmethod
    def load_fertilizers_from_file(filename):
        fertilizers = []
        with open(filename, 'r') as f:
            for line in f:
                data = json.loads(line)
                fertilizer = Fertilizer(data['id'], data['name'], data['elements'])
                fertilizers.append(fertilizer)
        return fertilizers

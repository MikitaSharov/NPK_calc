from Fertilizer import Fertilizer

class FertilizerInput:
    @staticmethod
    def input_fertilizers():
        print("Введите данные об удобрениях:")
        fertilizers = []
        while True:
            name = input("Название удобрения (для завершения введите 'q'): ")
            if name.lower() == 'q':
                break
            elements = {}
            print(f"Введите данные об элементах для удобрения '{name}':")
            while True:
                element = input("Элемент (для завершения введите 'done'): ")
                if element.lower() == 'done':
                    break
                content_grams = float(input(f"Содержание в граммах удобрения для элемента {element}: "))
                elements[element] = content_grams
            fertilizer = Fertilizer(len(fertilizers) + 1, name, elements)
            fertilizers.append(fertilizer)
        return fertilizers
    
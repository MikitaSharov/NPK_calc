from Fertilizer import Fertilizer
from IO import IO

class FertilizerInput:
    @staticmethod
    def input_fertilizers_manually_and_save():
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
                content_grams = float((input(f"Содержание в граммах удобрения для элемента {element}: ")).replace(',','.'))
                elements[element] = content_grams
            fertilizer = Fertilizer(len(fertilizers) + 1, name, elements)
            fertilizers.append(fertilizer)
        
        filename = input("Введите имя файла для сохранения удобрений: ")
        IO.save_fertilizers_to_file(fertilizers, filename)
        return fertilizers

    @staticmethod
    def input_fertilizers_from_file():
        filename = input("Введите имя файла с удобрениями: ")
        return IO.load_fertilizers_from_file(filename)

    @staticmethod
    def menu():
        print("Меню:")
        print("1. Ввести удобрения вручную и сохранить в файл")
        print("2. Загрузить удобрения из файла")
        choice = input("Выберите действие (1/2): ")
        if choice == '1':
            return FertilizerInput.input_fertilizers_manually_and_save()
        elif choice == '2':
            return FertilizerInput.input_fertilizers_from_file()
        else:
            print("Неверный ввод.")
            return None

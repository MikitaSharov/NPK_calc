class Fertilizer:
    def __init__(self, id, name, elements):
        self.id = id
        self.name = name
        self.elements = elements

    def display_fertilizer(self):
        print(f"ID: {self.id}")
        print(f"Удобрение: {self.name}")
        print("Элементы:")
        for element, content_grams in self.elements.items():
            print(f" - {element}: {content_grams} г")

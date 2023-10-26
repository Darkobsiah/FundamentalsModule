class Zoo:
    def __init__(self):
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.__animals = 0

    def add_animal(self, species, name):
        self.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {name_of_the_zoo}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {name_of_the_zoo}: {self.fishes}\nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {name_of_the_zoo}: {self.birds}\nTotal animals: {self.__animals}"


animal = Zoo()
name_of_the_zoo = input()
n_number = int(input())
for line in range(n_number):
    specie, name_of_animal = input().split()
    animal.add_animal(specie, name_of_animal)
final_specie = input()
print(animal.get_info(final_specie))
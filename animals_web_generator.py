import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    name = animal['name']  # Assuming name is always given
    print(f"Name: {name}")
    if 'diet' in animal['characteristics'].keys():
        diet = animal['characteristics']['diet']
        print(f"Diet: {diet}")
    if 'locations' in animal.keys():
        print(f"Location: {animal['locations'][0]}")
        # print(", ".join(animal['locations'])) <- all locations
    if 'type' in animal['characteristics'].keys():
        animal_type = animal['characteristics']['type']
        print(f"Type: {animal_type}")
    print()


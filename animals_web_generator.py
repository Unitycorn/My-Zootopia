import json

HTML_TEMPLATE_FILE = 'animals_template.html'
NEW_HML_FILE = 'animals.html'
REPLACE_STRING = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_html_template(template):
    """ Loads an HTML template file """
    html_data = open(template, "r")
    html_content = html_data.read()
    html_data.close()
    return html_content


def serialize_animal(animal_obj):
    """ Serializes an animal object, returns HTML-string"""
    output = ''
    output += '<li class="cards__item">\n'
    name = animal_obj['name']  # Assuming name is always given
    output += f"<div class='card__title'>{name}</div>\n"
    output += '<p class="card__text">\n'
    output += "<ul class='card_list'>\n"
    if 'skin_type' in animal_obj['characteristics'].keys():
        skin = animal_obj['characteristics']['skin_type']
        output += f"<li><strong>Skin type:</strong> {skin}</li>\n"
    if 'diet' in animal_obj['characteristics'].keys():
        diet = animal_obj['characteristics']['diet']
        output += f"<li><strong>Diet:</strong> {diet}</li>\n"
    if 'locations' in animal_obj.keys():
        output += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"
        # print(", ".join(animal['locations'])) <- all locations
    if 'type' in animal_obj['characteristics'].keys():
        animal_type = animal_obj['characteristics']['type']
        output += f"<li><strong>Type:</strong> {animal_type}</li>\n"
    if 'lifespan' in animal_obj['characteristics'].keys():
        lifespan = animal_obj['characteristics']['lifespan']
        output += f"<li><strong>Lifespan:</strong> {lifespan}</li>\n"
    output += "</ul>\n</p>\n</li>\n"
    return output


def write_html_file(content, path):
    """ Writes an HTML file """
    with open(path, 'w') as file:
        file.write(content)
    file.close()


def get_user_selection(types):
    """Ask for skin type to either add all animals to the string or just a specified type"""
    while True:
        print("\nPlease select a skin type from the following list:")
        for skin_type in types:
            print(skin_type)
        selection = input("or 'All' for all animals: ").capitalize()
        if selection == 'All' or selection in types:
            return selection


def main():
    """
    1. Loads data from JSON file and serializes the objects within into an HTML-string
    2. Gets HTML from template and replaces specified part with HTML-string
    3. Writes new HTML into file
    """
    animals_data = load_data('animals_data.json')
    serialized_data = ''
    skin_types = []
    for animal in animals_data:
        if ('skin_type' in animal['characteristics'].keys()
                and animal['characteristics']['skin_type'] not in skin_types):
            skin_types.append(animal['characteristics']['skin_type'])
    selection = get_user_selection(skin_types)
    for animal in animals_data:
        if selection == 'All' or animal['characteristics']['skin_type'] == selection:
            serialized_data += serialize_animal(animal)
    altered_html_content = load_html_template(HTML_TEMPLATE_FILE).replace(REPLACE_STRING, serialized_data)
    write_html_file(altered_html_content, NEW_HML_FILE)
    print("File: " + NEW_HML_FILE + " saved!")


if __name__ == '__main__':
    main()

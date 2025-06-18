import json

HTML_TEMPLATE_FILE = 'animals_template.html'
NEW_HML_FILE = 'animals.html'
REPLACE_STRING = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_html_template():
    """ Loads a HTML template file """
    html_data = open(HTML_TEMPLATE_FILE, "r")
    html_content = html_data.read()
    html_data.close()
    return html_content


def get_animals_info():
    """ Reads information from JSON file and returns them as a string"""
    output = ''
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        name = animal['name']  # Assuming name is always given
        output += f"<div class='card__title'>{name}</div>\n"
        output += '<p class="card__text">'
        if 'diet' in animal['characteristics'].keys():
            diet = animal['characteristics']['diet']
            output += f"<strong>Diet:</strong> {diet}<br />\n"
        if 'locations' in animal.keys():
            output += f"<strong>Location:</strong> {animal['locations'][0]}<br />\n"
            # print(", ".join(animal['locations'])) <- all locations
        if 'type' in animal['characteristics'].keys():
            animal_type = animal['characteristics']['type']
            output += f"<strong>Type:</strong> {animal_type}<br />\n"
        output += "</p>\n</li>\n"
    return output


html_content_with_animals = load_html_template().replace(REPLACE_STRING, get_animals_info())

with open(NEW_HML_FILE, 'w') as file:
    file.write(html_content_with_animals)
file.close()

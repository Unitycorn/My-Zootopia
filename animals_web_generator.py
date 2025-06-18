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
    if 'diet' in animal_obj['characteristics'].keys():
        diet = animal_obj['characteristics']['diet']
        output += f"<strong>Diet:</strong> {diet}<br />\n"
    if 'locations' in animal_obj.keys():
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br />\n"
        # print(", ".join(animal['locations'])) <- all locations
    if 'type' in animal_obj['characteristics'].keys():
        animal_type = animal_obj['characteristics']['type']
        output += f"<strong>Type:</strong> {animal_type}<br />\n"
    if 'lifespan' in animal_obj['characteristics'].keys ():
        lifespan = animal_obj['characteristics']['lifespan']
        output += f"<strong>Lifespan:</strong> {lifespan}<br />\n"
    output += "</p>\n</li>\n"
    return output


def write_html_file(content, path):
    """ Writes an HTML file """
    with open(path, 'w') as file:
        file.write(content)
    file.close()


def main():
    """
    1. Loads data from JSON file and serializes the objects within into an HTML-string
    2. Gets HTML from template and replaces specified part with HTML-string
    3. Writes new HTML into file
    """
    animals_data = load_data('animals_data.json')
    serialized_data = ''
    for animal in animals_data:
        serialized_data += serialize_animal(animal)
    altered_html_content = load_html_template(HTML_TEMPLATE_FILE).replace(REPLACE_STRING, serialized_data)
    write_html_file(altered_html_content, NEW_HML_FILE)


if __name__ == '__main__':
    main()

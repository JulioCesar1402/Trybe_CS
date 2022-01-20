import json


def read_pokemons_file(path):
    with open(path) as file:
        pokemons = json.load(file)["results"]
        return pokemons


def filter_by_choose_type(type, file):
    quantity_of_pokemons_by_type = dict()
    quantity_of_pokemons_by_type[type] = 0

    for pokemon in file:
        for pokemon_type in pokemon["type"]:
            if type in pokemon_type:
                quantity_of_pokemons_by_type[type] += 1
    return quantity_of_pokemons_by_type


def save_types_quantity_of_pokemons(read_file, name_new_file):
    with open(name_new_file, "w") as file:
        count_pokemons = dict()
        for pokemon in read_file:
            for type in pokemon["type"]:
                if type in count_pokemons:
                    count_pokemons[type] += 1
                else:
                    count_pokemons[type] = 1
        json.dump({"results": count_pokemons}, file, indent=4)


if __name__ == "__main__":
    # pokemons = read_pokemons_file("pokemons.json")
    types = read_pokemons_file("quantity_of_pokemons_by_type.json")
    print(types)
    # input_type = input("Choose a type: ")
    # print(filter_by_choose_type(input_type, pokemons))
    # save_types_quantity_of_pokemons(
    #     pokemons, "quantity_of_pokemons_by_type.json"
    # )

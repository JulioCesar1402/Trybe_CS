import pytest
import json
from unittest.mock import mock_open, patch
import os
from filter_by_type import (
    filter_by_choose_type,
    save_types_quantity_of_pokemons,
    read_pokemons_file,
)


@pytest.fixture
def pokemons():
    """Exemplos de pokemons"""
    return {
        "results": [
            {
                "name": "Bulbasaur",
                "type": ["Grass", "Poison"],
            },
            {
                "name": "Charmander",
                "type": ["Fire"],
            },
        ]
    }


def test_read_pokemons_file(pokemons):
    pokemon_json = json.dumps(pokemons)
    with patch("builtins.open", mock_open(read_data=pokemon_json)):
        assert read_pokemons_file("dummy") == pokemons["results"]


def test_filter_by_choose_type(pokemons):
    assert filter_by_choose_type("Grass", pokemons["results"]) == {"Grass": 1}


def test_save_types_quantity_of_pokemons(pokemons):
    file_name = "test_type_pokemon.json"
    save_types_quantity_of_pokemons(pokemons["results"], file_name)
    data = {
        "Grass": 1,
        "Poison": 1,
        "Fire": 1,
    }
    assert read_pokemons_file(file_name) == data
    os.remove(file_name)

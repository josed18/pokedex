# pokedex api

API to get information of the Pokémon and their evolutions

## pre requirements

* Python3.6

## installation

### create virtualenv

`virtualenv env`

### activate virtual env

`source env/bin/activate`

### install requirements

`pip install -r requirements.txt`


### run migrate to database

`python manage.py migrate

## run server

`python manage.py runserver`

## Examples

### get information from a pokemon

`-GET /pokemon/<name>/`

example:

`-GET /pokemon/charmeleon/`

response example

``` json
{
    "id": 5,
    "name": "charmeleon",
    "height": "1.10",
    "weight": "19.00",
    "external_id": 5,
    "stats": [
        {
            "base": 80,
            "stat_name": "speed"
        },
        {
            "base": 65,
            "stat_name": "special-defense"
        },
        {
            "base": 80,
            "stat_name": "special-attack"
        },
        {
            "base": 58,
            "stat_name": "defense"
        },
        {
            "base": 64,
            "stat_name": "attack"
        },
        {
            "base": 58,
            "stat_name": "hp"
        }
    ],
    "evolutions": [
        {
            "id": 6,
            "name": "charizard",
            "evolutions": []
        }
    ],
    "preevolution": {
        "id": 4,
        "name": "charmander",
        "preevolution": null
    }
}
```
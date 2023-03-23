import requests

token = 'e63c1c259d6f50aa6c225a83f611d53d'

response = requests.post('https://pokemonbattle.me:9104/trainers/reg', 
                         headers= {'Content-Type': 'application/json', "trainer_token": token,},
                         json={"trainer_token": token,
                               "email": "ge314n@dolnikov.ru",
                               "password": "Iloveqa1"
}) 

response_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', 
                         headers= {'Content-Type': 'application/json', "trainer_token": token,},
                         json={
    "trainer_token": token
}) 


print(response_confirm.text)

add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                         headers= {'Content-Type': 'application/json', "trainer_token": token,},
                         json={ "name" : "зеленый",
                                "photo" : "https://dolnikov.ru/pokemons/albums/010.png"
}) 

print(add_pokemon_response.text)

put_pokemon_response = requests.put('https://pokemonbattle.me:9104/pokemons', 
                         headers= {'Content-Type': 'application/json', "trainer_token": token,},
                         json={"pokemon_id": "6626",
                               "name": "Artorias",
                               "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}) 

print(put_pokemon_response.text)

add_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
                         headers= {'Content-Type': 'application/json', "trainer_token": token,},
                         json={"pokemon_id": "6626"
}) 

print(add_pokeball_response.text)
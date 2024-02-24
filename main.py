import requests

pokemon_file = open("pokemon.txt", "a+")
pokemon_list = []
url = 'https://pokeapi.co/api/v2/pokemon/{}/'

read_add = input("What do you want to do? [read/add]")
if read_add == "read":
    pokemon_file.seek(0)
    contents = pokemon_file.read()
    if len(contents) > 0:
        print("Your pokemon so far:")
        print(contents)
    else:
        print("You have no pokemon added so far.")
elif read_add == "add":
    while True:
        pokemon_number = input("What is the Pokemon's ID? ")
        pokemon_list.append(pokemon_number)
        should_continue = input("Would you like to add another? [y/n] ") == "y"
        if not should_continue:
            break


    print(pokemon_list)

    for id in pokemon_list:
        response = requests.get(url.format(id))
        pokemon = response.json()
        pokemon_file.write(f"NAME: {pokemon['name']}\nID: {id}\n\nMOVES:\n")
        moves = pokemon['moves']
        for move in moves:
            pokemon_file.write(f"- {move['move']['name']}\n")
        pokemon_file.write("\n")    


pokemon_file.close()        

    
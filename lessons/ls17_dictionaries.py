"""Examples of dictionaries. """

#Establish a tye with dict[key type, value type]
# Empty dictionary literal is {}
players: dict[str, int] = {}

#Insert a new key-value pair
# Reference keys inside subscription notation, associated values are assigned

players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4 #This is intentionally off by 1
players["Bacot"] = players["Bacot"] + 1
print(players)

#for..in loops will give you each key one by one

for player_name in players:
    print(f"{player_name} -> {players[player_name]}")

#Dictionary Literal
#You can have keys and values of any types!
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[23] = "Jordan"
print(jerseys)
print(jerseys[2])

#The pop method allows you to remove a key-value pair by its key
# method returns the value associated with the popped key
popped_name: str = jerseys.pop(23)
print(popped_name)
print(jerseys)

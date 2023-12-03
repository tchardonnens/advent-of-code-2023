with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

res = []

possible_game = {
    "red": 12,
    "green": 13,
    "blue": 14
  }

# each line is a new game with its throws
for line in lines:

  # split the line into the game number and the rest
  game = line.split(":")[0]
  game = game.split(" ")[1] # Game id
  rest = line.split(":")[1] # List of throws

  # split the rest into the different throws
  throws = rest.split(";")

  # The Elf would first like to know which games would have been possible if the 
  # bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?


  # make a dictionnary out of the throws
  game_dict = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for throw in throws:
    # split the throw into the color and the number
    pairs = throw.split(",")
    pairs = [pair.strip() for pair in pairs]
    for pair in pairs:
      color = pair.split(" ")[1]
      number = int(pair.split(" ")[0])
      if number > game_dict[color]:
        game_dict[color] = number
    
  is_possible = True
  for color in game_dict.keys():
    if game_dict[color] > possible_game[color]:
      is_possible = False
  if is_possible:
    res.append(int(game))
  
print(sum(res))

## Part 2
        

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

res = []

possible_game = {
    "red": 12,
    "green": 13,
    "blue": 14
  }

# each line is a new game with its throws
for line in lines:

  # split the line into the game number and the rest
  game = line.split(":")[0]
  game = game.split(" ")[1] # Game id
  rest = line.split(":")[1] # List of throws

  # split the rest into the different throws
  throws = rest.split(";")

  # make a dictionnary out of the throws
  game_dict = {
    "red": 20000,
    "green": 20000,
    "blue": 20000
  }

  for throw in throws:
    # split the throw into the color and the number
    pairs = throw.split(",")
    pairs = [pair.strip() for pair in pairs]
    for pair in pairs:
      color = pair.split(" ")[1]
      number = int(pair.split(" ")[0])
      if number < game_dict[color]:
        game_dict[color] = number
    
    game_score = 1
    for color in game_dict.keys():
      game_score = game_score * game_dict[color]
    print(game_score)
  res.append(int(game_score))
  
print(sum(res))
        

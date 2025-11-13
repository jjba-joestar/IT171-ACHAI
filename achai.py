player_dave = 0
player_matthew = 0

treasure_x = 1
treasure_y = 3
game_running = True
print("Welcome to Achai's Maze")
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")


while game_running:
    move = input("Enter move: (w to move up/s to move down/a to move left/d to move to right, or quit): ").lower()
    moved = True
    
    if move == 'w':
        player_matthew += 1
    elif move == 's':
        player_matthew -= 1
    elif move == 'd':
        player_dave += 1
    elif move == 'a':
        player_dave -= 1

    elif move == 'quit':
        game_is_running = False
        print("You quitted the game")
        moved = False

    else:
        print("Invalid move")
        moved = False
    
    print(f"Player position: ({player_dave}, {player_matthew})")

    if player_dave == treasure_x and player_matthew == treasure_y:
        print("You have reached the treasure")

        break




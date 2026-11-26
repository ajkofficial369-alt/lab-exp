# Sticks Game

sticks = 16
player = 1

print("Welcome to the Sticks Game!")
print("Rules: Pick 1, 2, or 3 sticks.")
print("The player who takes the last stick loses.\n")

while sticks > 0:

    print("Remaining sticks:", sticks)

    try:
        pick = int(input("Player " + str(player) + ", pick 1, 2, or 3 sticks: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Validate input
    if pick < 1 or pick > 3:
        print("Invalid choice! Pick only 1, 2, or 3 sticks.")
        continue

    if pick > sticks:
        print("Invalid choice! Only", sticks, "sticks remaining.")
        continue

    sticks -= pick

    # Check losing condition
    if sticks == 0:
        print("\nPlayer", player, "took the last stick and loses!")
        break

    # Switch player
    if player == 1:
        player = 2
    else:
        player = 1

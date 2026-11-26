import random

def monty_hall_simulation(trials):

    stay_wins = 0
    switch_wins = 0

    for _ in range(trials):

        doors = [0, 0, 0]

        # Place the car randomly
        car_position = random.randint(0, 2)
        doors[car_position] = 1

        # Player's initial choice
        player_choice = random.randint(0, 2)

        # Host opens a door containing a goat
        remaining_doors = [
            i for i in range(3)
            if i != player_choice and doors[i] == 0
        ]

        host_opens = random.choice(remaining_doors)

        # Switch to the other unopened door
        switch_choice = [
            i for i in range(3)
            if i != player_choice and i != host_opens
        ][0]

        # Check outcomes
        if doors[player_choice] == 1:
            stay_wins += 1

        if doors[switch_choice] == 1:
            switch_wins += 1

    # Calculate winning percentages
    stay_percentage = (stay_wins / trials) * 100
    switch_percentage = (switch_wins / trials) * 100

    # Display results
    print("Monty Hall Simulation Results after", trials, "trials:")
    print("Staying: Wins =", stay_wins,
          ", Winning Percentage =", round(stay_percentage, 2), "%")

    print("Switching: Wins =", switch_wins,
          ", Winning Percentage =", round(switch_percentage, 2), "%")


# Main program
trials = int(input("Enter number of trials: "))

monty_hall_simulation(trials)

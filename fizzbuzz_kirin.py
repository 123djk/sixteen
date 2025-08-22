import random

def monty_hall_simulation(num_trials):
    wins_stay = 0
    wins_switch = 0

    for _ in range(num_trials):
        doors = [0, 1, 2]
        winning_door = random.choice(doors)
        player_choice = random.choice(doors)
        
        if player_choice == winning_door:
            wins_stay += 1
            
        available_doors_for_host = [d for d in doors if d != player_choice and d != winning_door]
        door_opened_by_host = random.choice(available_doors_for_host)
        
        remaining_door = [d for d in doors if d != player_choice and d != door_opened_by_host][0]
        
        if remaining_door == winning_door:
            wins_switch += 1

    stay_percentage = (wins_stay / num_trials) * 100
    switch_percentage = (wins_switch / num_trials) * 100

    print("---------------------------------------")
    print("Simulation")
    print(f"Total {num_trials:,}times repeate")
    print("--------------------------------------------")
    print(f"{'Strategy':<15}{'success time':>15}{'success rate':>10}")
    print("--------------------------------------------")
    print(f"{'Choose stay (Stay)':<15}{wins_stay:>15}{stay_percentage:>10.2f}%")
    print(f"{'Choose change (Switch)':<15}{wins_switch:>15}{switch_percentage:>10.2f}%")
    print("--------------------------------------------")

monty_hall_simulation(100000)
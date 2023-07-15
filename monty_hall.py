##write simple monty hall problem simulation
import random


def monty_hall_problem(n_doors=3, decision='switch', n_sim=100):
    if n_doors < 3:
        raise ValueError('n_doors must be greater than 2')
    
    # final result placeholder
    result = []

    for i in range(n_sim):
        # generate n doors
        car_idx = random.randint(0, n_doors-1)
        doors = ['goat'] * n_doors
        doors[car_idx] = 'car'

        # randomize door order
        random.shuffle(doors)
        doors_dict = {i: doors[i] for i in range(len(doors))}

        # randomly choose a door
        chosen_door_idx = random.randint(0,n_doors-1)
        first_choice = doors[chosen_door_idx]

        # remove the other door with goat
        other_goat_idx = [i for i, j in doors_dict.items() if i != chosen_door_idx and j == 'goat'][0]
        doors.pop(other_goat_idx)

        if decision == 'switch':
            if first_choice == 'goat':
                result.append('car')
            else:
                result.append('goat')
        else:
            result.append(first_choice)

    # get the number of car
    car = result.count('car')

    return car/n_sim

print(monty_hall_problem(n_doors=3, decision='switch', n_sim=100000))
print(monty_hall_problem(n_doors=3, decision='stay', n_sim=100000))
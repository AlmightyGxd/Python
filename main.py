### Py Project

import random
import time
from yaspin import yaspin

level_list = [1, 2, 3, 4, 5]
level = 1

decision_list = ["Lost", "Victory"]
output = random.choice(decision_list)

while True:
    choice = input("Enter choice \n"
                   "1. Fight \n"
                   "2. Run Away \n"
                   "3. Call reinforcements \n"
                   "4. Surrender \n")

    if choice == '1':
        print("You've chosen to fight!")
        time.sleep(5)
        print(random.choice(decision_list))
        if output == 'Victory':
            print(f'Congratulations you won; You are now level: {level + random.choice(level_list)}')
        elif output == 'Lost':
            print(f'You lost! Level down by: {level - random.choice((level_list))}')

    elif choice == '2':
        print("You've ran away!")
        print(f'You went down a level! {level - 1}')

    elif choice == '3':
        print("Reinforcements called!")
        print("You must now wait 60 seconds")
        with yaspin():
            time.sleep(3)

        @yaspin(text="Loading...")
        def some_operations():
            time.sleep(3)


        some_operations
        chance = random.randint(1, 10)
        if chance < 5:
            print("Reinforcements are not coming!")
        elif chance > 5:
            print("Reinforcements have arrived!")

    elif choice == '4':
        print("You've surrendered!")
        print("You've lost the fight!")
    break

else:
    print("Invalid choice")



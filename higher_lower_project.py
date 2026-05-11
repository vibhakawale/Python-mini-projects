import random
from game_data import data
from art import logo,vs

print(logo)

win = True

def generate_random():
    num = random.choice(data)
    return num

first = generate_random()
second = generate_random()
count = 0
while win:

    print("Compare A: ", first["name"], ", a ", first["description"], ", from", first["country"])
    print(vs)
    print("Against B: ", second["name"], ", a ", second["description"], ", from", second["country"])

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if first == second:
        second = generate_random()
    if first["follower_count"] > second["follower_count"]:
        if guess == "a":
            count += 1
            first = second
            second = generate_random()
            print("Yes, You are Right! Current score: ", count)
        else:
            print("Sorry that's wrong. Final score: " , count )
            win = False
    else:
        if guess == "b":
            count += 1
            first = second
            second = generate_random()
            print("Yes, You are Right! Current score: ", count)
        else:
            print("Sorry that's wrong. Final score: ", count)
            win = False

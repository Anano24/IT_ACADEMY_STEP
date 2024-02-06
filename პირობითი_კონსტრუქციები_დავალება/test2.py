import random

life = 5
number_to_guess = random.randint(1, 10)

while life > 0:
    guess = int(input("შეიყვანეთ რიცხვი: "))

    if guess == number_to_guess:
        print("შენ გაიმარჯვე!")
        break
    elif guess < number_to_guess:
        print("რიცხვი ნაკლებია, კიდევ სცადე")
        life -= 1
    elif guess > number_to_guess:
        print("რიცხვი მეტია, კიდევ სცადე")
        life -= 1
else:
    print("წააგე")

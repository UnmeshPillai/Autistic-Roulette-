import random

print("Welcome to the Autistic Roulette")
print("This time the RNG is not broken")
print("Your Goal is to win ₹10000000")
print("Let's see if you make it big")

balance = 10000

while True:
    if balance <= 0:
        print("Ok game over!")
        print("Lesson : don't gamble like your mama did 15 years ago!")
        print("Call this helpline: 9999 666 555 (yes this is a real helpline)")
        print("QUIT GAMBLING TODAY")
        break

    if balance == 10000000:
        print("99% of gamblers quit before winning big")
        print("You are the 1%, so Good job!")
        print("You win!")
        break

    print("\nBalance = ₹", balance)
    print("Please bet Your Amount :")
    bet = input()

    if not bet.isdigit():
        print("Are you nuts?")
        continue

    better_bet = int(bet)
    if better_bet > balance or better_bet == 0:
        print("Stop right there you smart shit")
        continue

    print("Moving Ahead")
    print("Ok! Your bet is ₹", better_bet)

    print("Now choose : odd or even")
    evenodd = input()
    newevenodd = evenodd.strip().lower()

    if newevenodd not in ["odd", "even"]:
        print("You need help")
        continue
    else:
        print("Alright moving ahead!")

    print("Ok! now choose your color : red / black :")
    color = input()
    new_color = str(color).strip().lower()

    if new_color not in ["red", "black"]:
        exit("Locating IP address for the following offence.....")
    else:
        print("Aight, so you chose", new_color)

    comnog = random.randint(1, 36)
    comcolor = random.choice(["red", "black"])

    def fateofgame(number):
        return "even" if number % 2 == 0 else "odd"

    def fateofcolor(color):
        return color

    comevenodd = fateofgame(comnog)
    betcolor = fateofcolor(comcolor)

    print("\nRoulette rolled:", comnog, "-", comcolor)

    if comevenodd == newevenodd and new_color == betcolor:
        print("You win")
        balance += better_bet
    else:
        print("You lose")
        balance -= better_bet

    print("New Balance = ₹", balance)

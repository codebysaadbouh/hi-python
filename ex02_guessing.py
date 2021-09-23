import random


# Let's create the methods we will need

def give_guessing_number(min, max):
    guessing_number_m = random.randint(min, max)
    return guessing_number_m


def request_number(min, max):
    given_number_int = min - 1
    while given_number_int < min or given_number_int > max:
        given_number_str = input(f'Rentrez un nombre compris entre {min} et {max} : ')
        try:
            given_number_int = int(given_number_str)
            if given_number_int < min or given_number_int > max:
                print(f'Le nombre doit être compris {min} entre  et {max} !')
                given_number_int = 0
            else:
                return given_number_int
        except ValueError:
            print('ERREUR : Rentrez un nombre valide svp !')


def play_the_game(chance_number_f, number_given_by_user_f, guessing_number_f, min, max):
    while chance_number_f > 0:
        print(f"Nombre de chance : {chance_number_f}")
        number_given_by_user_f = request_number(min, max)
        if guessing_number_f < number_given_by_user_f:
            print(f"Attention {number_given_by_user_f} est PLUS PETIT que le numéro de devinette !")
        elif guessing_number_f > number_given_by_user_f:
            print(f"Attention {number_given_by_user_f} est PLUS GRAND que le numéro de devinette !")
        else:
            print(f"BRAVO ! Vous avez trouvé le numéro de devinette !")
            break

        chance_number_f -= 1

        if chance_number_f == 0:
            print("NUL ! Pas de chance")
            print(f"C'etait {guessing_number_f} le numéro de devinette ;-)")


# We define the rules

min_number = 1
max_number = 20
guessing_number = give_guessing_number(min_number, max_number)
number_given_by_user = guessing_number - 1
chance_number = 5

# Let's play to game
play_the_game(chance_number, number_given_by_user, guessing_number, min_number, max_number)



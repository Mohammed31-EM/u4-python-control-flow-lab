

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()



def check_letter():
    letter = input("Enter a single letter (a-z or A-Z): ").strip()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid entry. Please enter a single alphabetical character.")
        return

    lower_letter = letter.lower()

    if lower_letter in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")
check_letter()


def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number for your age.")
        return

    if age < 0:
        print("Age cannot be negative. Nice try, time traveler.")
        return

    voting_age = 18 
    if age >= voting_age:
        print(f"At {age}, you are eligible to vote.")
    else:
        print(f"At {age}, you are not old enough to vote yet.")
check_voting_eligibility()



def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number for the dog's age.")
        return

    if age < 0:
        print("A dog can't have a negative age. Unless it’s a sci-fi puppy from the future.")
        return

    if age == 0:
        dog_years = 0
    elif age == 1:
        dog_years = 10
    elif age == 2:
        dog_years = 20
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")
calculate_dog_years()


def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold not in ["yes", "no"] or raining not in ["yes", "no"]:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")
weather_advice()



def determine_season():
    month_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    month_input = input("Enter the month of the year (Jan - Dec): ").strip().lower()
    day_input = input("Enter the day of the month: ").strip()

    if month_input not in month_map:
        print("Invalid month. Please enter a three-letter abbreviation (e.g., Jan, Feb, Mar).")
        return

    try:
        day = int(day_input)
        if day < 1 or day > 31:
            print("Invalid day. Must be between 1 and 31.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for the day.")
        return

    month = month_map[month_input]

    if (month == 12 and day >= 21) or month in [1, 2] or (month == 3 and day <= 19):
        season = "Winter"
    elif (month == 3 and day >= 20) or month in [4, 5] or (month == 6 and day <= 20):
        season = "Spring"
    elif (month == 6 and day >= 21) or month in [7, 8] or (month == 9 and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

    display_month = month_input.capitalize()
    print(f"{display_month} {day} is in {season}.")
determine_season()




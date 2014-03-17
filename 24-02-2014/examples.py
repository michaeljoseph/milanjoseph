#from cli.helpers import ask, this_year
from datetime import datetime

INSULT_LIMIT = 20


def ask(question):
    return raw_input('%s ' % question)


def this_year():
    return datetime.now().year


def calculate_age(year_of_birth):
    return this_year() - year_of_birth


def print_name_age_and_insult(name, age):
    message = ("Hello %s!\n"
               "You're going to be %d years old this year!\n"
               "Nice Job!\n\n" % (name, age))

    if age > INSULT_LIMIT:
        message += "Man you're old!\nOld as garlic balls."
    else:
        message += 'Ah, young, fresh meat!'
    print(message)


def main():
    author = 'Written By Michael Alexander Lindsay Joseph\n'
    print(author)

    # ask for name
    name = ask('What is..... your name?')
    # ask for year of birth
    yob = int(ask('What year were you born?'))
    # make fun
    age = calculate_age(yob)

    print_name_age_and_insult(name, age)

if __name__ == '__main__':
    main()

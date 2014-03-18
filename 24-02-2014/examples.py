from datetime import datetime

INSULT_LIMIT = 20


def ask(question):
    """Asks the user a question and returns their answer"""
    return raw_input('%s ' % question)


def this_year():
    """Returns the current year as an integer"""
    return datetime.now().year

    return raw_input('%s ' % question)


def calculate_age(year_of_birth):
    """Calculate age from year of birth"""
    return this_year() - year_of_birth


def print_name_age_and_insult(name, age):
    """Prints your name, age, encouraging message and then an insult"""
    message = ("Hello %s!\n"
               "You're going to be %d years old this year!\n"
               "Nice Job!\n\n" % (name, age))

    if age > INSULT_LIMIT:
        message += "Man you're old!\nOld as garlic balls."
    else:
        message += 'Ah, young, fresh meat!'
    print(message)


def main():
    """Main program entrypoint"""
    author = 'Written By Michael Alexander Lindsay Joseph\n'
    print(author)
    print('Prepare to answer some questions:\n\n')

    name = ask('What is your name?')
    yob = int(ask('What year were you born?'))
    age = calculate_age(yob)

    print_name_age_and_insult(name, age)

if __name__ == '__main__':
    main()

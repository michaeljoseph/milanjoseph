from datetime import datetime


def ask(question):
    return raw_input('%s ' % question)


def this_year():
    return datetime.now().year



from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])


project = [Project(name=random_string("name", 10), status=random.choice(['development', 'release', 'stable', 'obsolete']),
           view_state=random.choice(['public', 'private']), description=random_string("description", 20))
           for i in range(1)]

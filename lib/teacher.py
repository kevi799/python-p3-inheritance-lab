
from user import User

import random

class Teacher(User):
    knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
    ]
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def teach(self):
        a_knowledge = random.randint(0, len(self.knowledge))
        random_knowledge = self.knowledge[a_knowledge]
        return random_knowledge

Muriithi = Teacher('Madam', 'Muriithi')
print(Muriithi.teach())
#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge = []):
        self.knowledge = knowledge
        super().__init__(first_name, last_name)
    
    def learn(self, value):
        self.knowledge = str(value)
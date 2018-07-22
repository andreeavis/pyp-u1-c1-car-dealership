import pytest
from argparse import Namespace

class Person(object):
    def __init__(self, first_name, last_name, email):
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
        

# defines sub-class (the parameters is the main Class)
class Customer(Person):
  # this is actually not needed -
  # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
  # first_name, last_name, email are variables of the class 
  def __init__(self, first_name, last_name, email):
    # super() calls the information from the Class 
    super().__init__(first_name, last_name, email)
    
  # defines the function is_employee as false (as the Customer is not employee)
  def is_employee(self):
    return False 
  

class Employee(Person):
    def __init__(self, first_name, last_name, email):
      super().__init__(first_name, last_name, email)
      
    def is_employee(self):
      return True

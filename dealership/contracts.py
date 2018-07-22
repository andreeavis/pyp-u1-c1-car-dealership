import pytest
from argparse import Namespace

from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self, vehicle, customer):
      #super().__init__(vehicle, customer)
      self.vehicle = vehicle
      self.customer = customer
    

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments): 
      super(BuyContract, self).__init__(vehicle, customer)
      self.monthly_payments = monthly_payments
        
    def total_value(self):
      total_value_with_customer = self.vehicle.sale_price() + (self.vehicle.interest_rate * self.monthly_payments * self.vehicle.sale_price() / 100)    
      if self.customer.is_employee():
        discount = 0.9
        total_value_with_customer = total_value_with_customer * discount
      return total_value_with_customer
           
    def monthly_value(self):
      monthly_value = self.total_value() / self.monthly_payments
      return monthly_value
           
      
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
      super(LeaseContract, self).__init__(vehicle, customer)
      self.length_in_months = length_in_months

    def total_value(self):
      total_value_with_customer = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.lease_multiplier / self.length_in_months)
      if self.customer.is_employee():
        discount = 0.9
        total_value_with_customer = total_value_with_customer * discount
      return total_value_with_customer
    
    def monthly_value(self):
      monthly_value = self.total_value() / self.length_in_months
      return monthly_value
    
    
   
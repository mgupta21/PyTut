#!/usr/bin/python
__author__ = 'Mayank'


class Company(object):
    def __init__(self):
        self.employees = []
        self.departments = []

    def add_employee(self, employee, department):
        assert employee not in self.employees
        if department not in self.departments:
            self.departments.append(department)
        self.employees.append(employee)

    def get_head_count_for(self, department):
        return self.departments[department].memberCount

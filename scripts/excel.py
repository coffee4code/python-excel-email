#!/usr/bin/python

import datetime
import xlrd
import config
from scripts.user import User
from scripts.util import Util


class Excel:

    now = ''
    path = ''
    sheet_index = 0
    book = ''
    sheet = ''
    start_line = 0

    def __init__(self, path, sheet_index):

        self.now = datetime.datetime.now()
        self.path = path
        self.sheet_index = sheet_index - 1

    def open(self):
        self.book = xlrd.open_workbook(self.path)
        self.sheet = self.book.sheet_by_index(self.sheet_index)

    def start(self, start_line):
        self.start_line = start_line - 1

    def read(self):

        result = []
        for rx in range(self.start_line, self.sheet.nrows):
            data = User()

            data.employee_year = self.now.year
            data.employee_month = self.now.month
            data.employee_email = self.sheet.cell_value(rx, Util.col_to_num(config.format_employee_email, True))
            data.employee_name = self.sheet.cell_value(rx, Util.col_to_num(config.format_employee_name, True))
            data.employee_department = self.sheet.cell_value(rx, Util.col_to_num(config.format_employee_department, True))
            data.employee_workday = self.sheet.cell_value(rx, Util.col_to_num(config.format_employee_workday, True))
            data.employee_attendance = self.sheet.cell_value(rx, Util.col_to_num(config.format_employee_attendance, True))
            data.wage_base = self.sheet.cell_value(rx, Util.col_to_num(config.format_wage_base, True))
            data.wage_allowance = self.sheet.cell_value(rx, Util.col_to_num(config.format_wage_allowance, True))
            data.wage_reward = self.sheet.cell_value(rx, Util.col_to_num(config.format_wage_reward, True))
            data.wage_everyday = self.sheet.cell_value(rx, Util.col_to_num(config.format_wage_everyday, True))
            data.wage_total = self.sheet.cell_value(rx, Util.col_to_num(config.format_wage_total, True))
            data.deductions_absence = self.sheet.cell_value(rx, Util.col_to_num(config.format_deductions_absence, True))
            data.deductions_sick_leave = self.sheet.cell_value(rx, Util.col_to_num(config.format_deductions_sick_leave, True))
            data.deductions_other = self.sheet.cell_value(rx, Util.col_to_num(config.format_deductions_other, True))
            data.deductions_social_security = self.sheet.cell_value(rx, Util.col_to_num(config.format_deductions_social_security, True))
            data.deductions_provident_fund = self.sheet.cell_value(rx, Util.col_to_num(config.format_deductions_provident_fund, True))
            data.deductions_personal_tax = self.sheet.cell_value(rx, Util.col_to_num(config.format_deductions_personal_tax, True))
            data.final_amount = self.sheet.cell_value(rx, Util.col_to_num(config.format_final_amount, True))

            result.append(data)

        return result

import os
from jinja2 import Environment, FileSystemLoader


class User:
    employee_year = ''
    employee_month = ''
    employee_email = ''
    employee_name = ''
    employee_department = ''
    employee_workday = ''
    employee_attendance = ''

    wage_base = ''
    wage_allowance = ''
    wage_reward = ''
    wage_everyday = ''
    wage_total = ''

    deductions_absence = ''
    deductions_sick_leave = ''
    deductions_other = ''
    deductions_social_security = ''
    deductions_provident_fund = ''
    deductions_personal_tax = ''

    final_amount = ''

    def __init__(self):
        self.employee_year = ''
        self.employee_month = ''
        self.employee_email = ''
        self.employee_name = ''
        self.employee_department = ''
        self.employee_workday = ''
        self.employee_attendance = ''

        self.wage_base = ''
        self.wage_allowance = ''
        self.wage_reward = ''
        self.wage_everyday = ''
        self.wage_total = ''

        self.deductions_absence = ''
        self.deductions_sick_leave = ''
        self.deductions_other = ''
        self.deductions_social_security = ''
        self.deductions_provident_fund = ''
        self.deductions_personal_tax = ''

        self.final_amount = ''

    def check(self):
        if self.wage_everyday:
            self.wage_everyday = round(self.wage_everyday, 2)

    def to_template(self, template_type):

        template_path = os.path.abspath("templates/")
        env = Environment(loader=FileSystemLoader(template_path))
        template_name = "mail.text.tpl" if template_type == 'text' else "mail.html.tpl"

        template = env.get_template(template_name)
        template = template.render(
            employee_year=self.employee_year,
            employee_month=self.employee_month,
            employee_name=self.employee_name,
            employee_department=self.employee_department,
            employee_workday=self.employee_workday,
            employee_attendance=self.employee_attendance,
            wage_base=self.wage_base,
            wage_allowance=self.wage_allowance,
            wage_reward=self.wage_reward,
            wage_everyday=self.wage_everyday,
            wage_total=self.wage_total,
            deductions_absence=self.deductions_absence,
            deductions_sick_leave=self.deductions_sick_leave,
            deductions_other=self.deductions_other,
            deductions_social_security=self.deductions_social_security,
            deductions_provident_fund=self.deductions_provident_fund,
            deductions_personal_tax=self.deductions_personal_tax,
            final_amount=self.final_amount
        )
        return template

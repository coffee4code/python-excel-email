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

    def to_template_text(self):
        template = '''\
            你好，{0}年{1}月工资表明细如下，请注意查收，如果在工资方面有任何疑问，请及时反馈！

            |======================================================================
            | 员工信息
            |-----------------------------------------------------------------------------------------------------------------------
            |    年度：{0}
            |    月份：{1}
            |    姓名：{2}
            |    部门：{3}
            |    满勤天数：{4}
            |    实际出勤：{5}
            |======================================================================
            | 应发项目
            |-----------------------------------------------------------------------------------------------------------------------
            |    基本工资：{6}
            |    岗位津贴：{7}
            |    奖金：{8}
            |    日工资：{9}
            |    应发合计：{10}
            |======================================================================
            | 扣除项目
            |-----------------------------------------------------------------------------------------------------------------------
            |    缺勤扣款：{11}
            |    病事假扣款：{12}
            |    其他扣款：{13}
            |    社保个人部分：{14}
            |    公积金个人部分：{15}
            |    个税：{16}
            |======================================================================
            |实发项目
            |-----------------------------------------------------------------------------------------------------------------------
            |    实发工资：{17}
            |======================================================================
        '''
        template = template.format(
            self.employee_year,
            self.employee_month,
            self.employee_name,
            self.employee_department,
            self.employee_workday,
            self.employee_attendance,
            self.wage_base,
            self.wage_allowance,
            self.wage_reward,
            self.wage_everyday,
            self.wage_total,
            self.deductions_absence,
            self.deductions_sick_leave,
            self.deductions_other,
            self.deductions_social_security,
            self.deductions_provident_fund,
            self.deductions_personal_tax,
            self.final_amount
        )
        return template

    def to_template_html(self):
        template = """\
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
                    <meta name="viewport" content="width=device-width, initial-scale=1"/>
                    <title>汇誉财经邮件</title>
                    <style type="text/css">
                        table {{
                            table-layout: fixed;
                            border-collapse: collapse;
                            border: none;
                            width: 100%;
                        }}
                        td {{
                            border: solid windowtext 1pt;
                            border-collapse: collapse;
                            padding: 0 10px;
                        }}
                        .container {{
                            max-width: 900px;
                            margin: 0 auto;
                        }}
                        .item-line td {{
                            background: #FBE5D6;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <br />
                        <h4>你好，{0}年{1}月工资表明细如下，请注意查收，如果在工资方面有任何疑问，请及时反馈！</h4>
                        <br />
                        <table border="1" cellspacing="0" cellpadding="0" width="100%">
                            <tbody>
                            <tr class="item-line">
                                <td width="100%" colspan="9" valign="top">
                                    <p align="center">
                                        <strong>
                                            <span>员工信息</span>
                                        </strong>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td valign="top">
                                    <p>
                                        <span>年度</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{0}</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>月份</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{1}</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>姓名</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>{2}</span>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td valign="top">
                                    <p>
                                        <span>部门</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>{3}</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>满勤天数</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{4}</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>实际出勤</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">{5}</span>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-line">
                                <td width="100%" colspan="9" valign="top">
                                    <p align="center">
                                        <strong>
                                            <span>应发项目</span>
                                        </strong>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td valign="top">
                                    <p>
                                        <span>基本工资</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{6}</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>岗位津贴</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{7}</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>奖金</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">{8}</span>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td valign="top">
                                    <p>
                                        <span>日工资</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{9}</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>应发合计</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{10}</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">&nbsp;</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">&nbsp;</span>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-line">
                                <td width="100%" colspan="9" valign="top">
                                    <p align="center">
                                        <strong>
                                            <span>扣除项目</span>
                                        </strong>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>缺勤扣款</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">{11}</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>病事假扣款</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{12}</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>其他扣款</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">{13}</span>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>社保个人部分</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">{14}</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span>公积金个人部分</span>
                                    </p>
                                </td>
                                <td colspan="2" valign="top">
                                    <p>
                                        <span lang="EN-US">{15}</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span>个税</span>
                                    </p>
                                </td>
                                <td valign="top">
                                    <p>
                                        <span lang="EN-US">{16}</span>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-line">
                                <td width="100%" colspan="9" valign="top">
                                    <p align="center">
                                        <strong>
                                            <span>实发项目</span>
                                        </strong>
                                    </p>
                                </td>
                            </tr>
                            <tr class="item-cells">
                                <td valign="top">
                                    <p>
                                        <span>实发工资</span>
                                    </p>
                                </td>
                                <td colspan="8" valign="top">
                                    <p>
                                        <span lang="EN-US">{17}</span>
                                    </p>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </body>
                </html>
            """
        template = template.format(
            self.employee_year,
            self.employee_month,
            self.employee_name,
            self.employee_department,
            self.employee_workday,
            self.employee_attendance,
            self.wage_base,
            self.wage_allowance,
            self.wage_reward,
            self.wage_everyday,
            self.wage_total,
            self.deductions_absence,
            self.deductions_sick_leave,
            self.deductions_other,
            self.deductions_social_security,
            self.deductions_provident_fund,
            self.deductions_personal_tax,
            self.final_amount
        )
        return template

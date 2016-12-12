<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>汇誉财经邮件</title>
    <style type="text/css">
        table {
            table-layout: fixed;
            border-collapse: collapse;
            border: none;
            width: 100%;
        }
        td {
            border: solid windowtext 1pt;
            border-collapse: collapse;
            padding: 0 10px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        .item-line td {
            background: #FBE5D6;
        }
    </style>
</head>
<body>
    <div class="container">
        <br />
        <h4>你好，{{ employee_year }}年{{ employee_month }}月工资表明细如下，请注意查收，如果在工资方面有任何疑问，请及时反馈！</h4>
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
                        <span lang="EN-US">{{ employee_year }}</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>月份</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span lang="EN-US">{{ employee_month }}</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span>姓名</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>{{ employee_name }}</span>
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
                        <span>{{ employee_department }}</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>满勤天数</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span lang="EN-US">{{ employee_workday }}</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span>实际出勤</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span lang="EN-US">{{ employee_attendance }}</span>
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
                        <span lang="EN-US">{{ wage_base }}</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>岗位津贴</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span lang="EN-US">{{ wage_allowance }}</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span>奖金</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span lang="EN-US">{{ wage_reward }}</span>
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
                        <span lang="EN-US">{{ wage_everyday }}</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>应发合计</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span lang="EN-US">{{ wage_total }}</span>
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
                        <span lang="EN-US">{{ deductions_absence }}</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span>病事假扣款</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span lang="EN-US">{{ deductions_sick_leave }}</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>其他扣款</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span lang="EN-US">{{ deductions_other }}</span>
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
                        <span lang="EN-US">{{ deductions_social_security }}</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span>公积金个人部分</span>
                    </p>
                </td>
                <td colspan="2" valign="top">
                    <p>
                        <span lang="EN-US">{{ deductions_provident_fund }}</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span>个税</span>
                    </p>
                </td>
                <td valign="top">
                    <p>
                        <span lang="EN-US">{{ deductions_personal_tax }}</span>
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
                        <span lang="EN-US">{{ final_amount }}</span>
                    </p>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</body>
</html>

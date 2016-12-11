#!/usr/bin/python

import os
import config
import time
from scripts import client
from scripts import excel
from scripts import util

sheet = excel.Excel(os.path.abspath(config.excel_path), config.excel_sheet_index)
sheet.start(config.excel_sheet_start_line)
sheet.open()
data = sheet.read()
count = len(data)

util.log_separator()
util.log_text("检测到 %s 条待发数据" % count)

for index in range(count):

    user = data[index]
    user.check()
    text_template = user.to_template_text()

    util.log_separator()
    util.log_text("第 %s 条数据：\r\n" % str(int(index)+1))
    util.log_text("\t姓名：%s\t邮件：%s" % (user.employee_name, user.employee_email))
    util.log_separator()
    util.log_text(text_template)
    util.log_separator()
    answer = util.prompt_question("是否发送？发送输入（Y），取消输入（N）：")

    if answer:
        util.log_text("正在发送第 %s 条数据......" % str(int(index)+1))
        mailer = client.Client()
        mailer.server(config.server_name, config.server_port, config.server_debug)
        mailer.auth(config.sender_email, config.sender_password)
        mailer.subject('%s年%s月工资条' % (user.employee_year, user.employee_month))
        mailer.message_text(text_template)
        mailer.message_html(user.to_template_html())

        mailer.receiver(user.employee_email)
        mailer.send()
        time.sleep(config.sender_sleeper)

    util.log_text("取消发送第 %s 条数据" % str(int(index)+1))


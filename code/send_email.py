#!/usr/bin/python3
# coding=utf-8


"""
完成发布 发送邮件给测试
"""


__author__ = 'LCD'


import smtplib
from email.mime.text import MIMEText
from email.header import Header

def email_send(fname, fpwd, toname, smtp, app_address=''):
    subject = """
    <p>新的测试包已经上传</p>
    <p><a href="%s">测试包链接:%s</a></p>
    """ % (app_address.replace("https", "http"), app_address.replace("https", "http"))
    # Https 会有时发送失败
    msg = MIMEText(subject, 'html', 'utf-8')
    msg['from'] = fname
    msg['to'] = ",".join(toname)
    msg['subject'] = Header('新的测试包已经上传', 'utf-8')
    print('---------->发送邮件')
    try:
        server = smtplib.SMTP_SSL()
        server.connect(smtp)
        server.login(fname, fpwd)
        server.sendmail(fname, toname, msg.as_string())
        server.quit()
    except Exception as e:
        print('---------->发送邮件失败')
        raise Exception('发送邮件失败')
    else:
        print('----------> 发送邮件成功')
    finally:
        pass
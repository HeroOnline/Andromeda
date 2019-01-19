#!/usr/bin/python3
# coding=utf-8


"""
完成发布 发送邮件给测试
"""


__author__ = 'LCD'


import smtplib
from email.mime.text import MIMEText
from email.header import Header


# imageurl = 'http://b.hiphotos.baidu.com/baike/c0%3Dbaike60%2C5%2C5%2C60%2C20/sign=0c4c4cd82834349b600b66d7a8837eab/c83d70cf3bc79f3dd1bd49f2baa1cd11738b2997.jpg'
imageurl = 'http://image.yy.com/yywebalbumbs2bucket/8bed64d5b4b441788126d90842cd7466_1435907497575.jpg'

def email_send(fname, fpwd, toname, smtp, app_address='', name='', log='无'):
    global imageurl
    subject = """
    <!DOCTYPE html>
    <html>
    <head> 
    <meta charset="utf-8"> 
    <title>新包上传(runoob.com)</title> 
    </head>
    <body>
    
    <p><h2>🇨🇳 新的iOS测试包已上传 🇨🇳 </h2></p>
    <p><h3><a href="%s">点我下载:%s</a></h2></p>
    <p><h3>项目：%s</h3></p>
    <p>更新日志：%s</p>
    <p><img src="%s"></p>
    </body>
    </html>
    """ % (app_address.replace("https", "http"), app_address.replace("https", "http"), name, log, imageurl)
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



# if __name__ == '__main__':
#     email_send('@126.com', '', ['565726319@qq.com'], 'smtp.126.com', 'http://www.baidu.com', '客户端')
import MySQLdb
connection = MySQLdb.connect(
                host="192.168.1.5",# 数据库IP地址
                user="user1",     #  mysql用户名
                passwd="Mima123$",      # mysql用户登录密码
                db="byhy" ,        # 数据库名
                # 如果数据库里面的文本是utf8编码的，
                #charset指定是utf8
                charset = "utf8")
c = connection.cursor()

c.execute(f"delete from s_tudens where id>10  ")

connection.commit()
import pymysql
import readConfig as readConfig

# 在配置文件下面读取mysql数据库
localReadConfig = readConfig.ReadConfig()
host = '192.168.150.33'
port = 3306
port_3308 = 3308
username = 'root'
password = 'hnjing&@test'
charset = 'utf8'

class MySQL():
    # 初始化连接mall----分支环境
    def connect_mall(self, conn):
        mall = localReadConfig.get_db_mall('database_mall')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=mall,
            charset=charset
        )
        return conn

    def connect_mall1(self, conn):
        mall1 = localReadConfig.get_db_mall1('database_mall1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=mall1,
            charset=charset
        )
        return conn


    # 连接ps数据库----主干环境
    def connect_ps(self, conn):
        ps = localReadConfig.get_db_ps('database_ps')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=ps,
            charset=charset
        )
        return conn

    # 连接ps1数据库----分支环境
    def connect_ps1(self, conn):
        ps1 = localReadConfig.get_db_ps1('database_ps1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=ps1,
            charset=charset
        )
        return conn

    # 连接bi数据库----主干环境
    def connect_bi(self, conn):
        bi = localReadConfig.get_db_bi('database_bi')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=bi,
            charset=charset
        )
        return conn

    # 连接bi1数据库----分支环境
    def connect_bi1(self, conn):
        bi1 = localReadConfig.get_db_bi1('database_bi1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=bi1,
            charset=charset
        )
        return conn

    # 连接platform数据库----主干环境
    def connect_platform(self, conn):
        platform = localReadConfig.get_db_platform('database_platform')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=platform,
            charset=charset
        )
        return conn

    # 连接platform数据库----分支环境
    def connect_platform1(self, conn):
        platform1 = localReadConfig.get_db_platform1('database_platform1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=platform1,
            charset=charset
        )
        return conn


    # 连接protal数据库----主干环境
    def connect_portal(self, conn):
        portal = localReadConfig.get_db_portal('database_portal')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=portal,
            charset=charset
        )
        return conn

    # 连接protal1数据库----分支环境
    def connect_portal1(self, conn):
        portal1 = localReadConfig.get_db_portal1('database_portal1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=portal1,
            charset=charset
        )
        return conn

    # 连接os数据库----分支环境
    def connect_os1(self, conn):
        os = localReadConfig.get_db_os1('database_os1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=os,
            charset=charset
        )
        return conn

    # 连接os数据库----主干环境
    def connect_os(self, conn):
        os1 = localReadConfig.get_db_os('database_os')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=os,
            charset=charset
        )
        return conn

    # 连接empos数据库----主干环境
    def connect_empos(self, conn):
        empos = localReadConfig.get_db_empos('database_empos')
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=empos,
            charset=charset
        )
        return conn

    # 连接empos数据库----分支环境
    def connect_empos1(self, conn):
        empos1 = localReadConfig.get_db_empos1('database_empos1')
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=empos1,
            charset=charset
        )
        return conn
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


class MySQL:
    # 初始化连接mall----分支环境
    @staticmethod
    def connect_mall():
        mall = localReadConfig.get_db_mall()
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=mall,
            charset=charset
        )
        return conn

    @staticmethod
    def connect_mall1():
        mall1 = localReadConfig.get_db_mall1()
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
    @staticmethod
    def connect_ps():
        ps = localReadConfig.get_db_ps()
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
    @staticmethod
    def connect_ps1():
        ps1 = localReadConfig.get_db_ps1()
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
    @staticmethod
    def connect_bi():
        bi = localReadConfig.get_db_bi()
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
    @staticmethod
    def connect_bi1():
        bi1 = localReadConfig.get_db_bi1()
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
    @staticmethod
    def connect_platform():
        platform = localReadConfig.get_db_platform()
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
    @staticmethod
    def connect_platform1():
        platform1 = localReadConfig.get_db_platform1()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=platform1,
            charset=charset
        )
        return conn

    # 连接pro_tal数据库----主干环境
    @staticmethod
    def connect_portal():
        portal = localReadConfig.get_db_portal()
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=portal,
            charset=charset
        )
        return conn

    # 连接pro_tal数据库----分支环境
    @staticmethod
    def connect_portal1():
        portal1 = localReadConfig.get_db_portal1()
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
    @staticmethod
    def connect_os1():
        os = localReadConfig.get_db_os1()
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
    @staticmethod
    def connect_os():
        os1 = localReadConfig.get_db_os()
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=os,
            charset=charset
        )
        return conn

    # 连接emp_os数据库----主干环境
    @staticmethod
    def connect_emp_os():
        os_emp = localReadConfig.get_db_empos()
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=os_emp,
            charset=charset
        )
        return conn

    # 连接emp_os数据库----分支环境
    @staticmethod
    def connect_emp_os1():
        os1_emp = localReadConfig.get_db_empos1()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=os1_emp,
            charset=charset
        )
        return conn

    # 连接order数据库----分支环境
    @staticmethod
    def connect_order1():
        order1 = localReadConfig.get_db_order1()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=order1,
            charset=charset
        )
        return conn

    # 连接open_api数据库----主干环境
    @staticmethod
    def connect_open_api():
        open_api = localReadConfig.get_db_open_api()
        conn = pymysql.connect(
            host=host,
            port=port_3308,
            user=username,
            passwd=password,
            db=open_api,
            charset=charset
        )
        return conn

    # 连接open_api数据库----分支环境
    @staticmethod
    def connect_open_api1():
        open_api = localReadConfig.get_db_open_api1()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=open_api,
            charset=charset
        )
        return conn
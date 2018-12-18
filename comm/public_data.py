import pymysql
import readConfig

# 在配置文件下面读取mysql数据库
localReadConfig = readConfig.ReadConfig()
host = localReadConfig.get_db_host()
port = int(localReadConfig.get_db_port())
username = localReadConfig.get_db_username()
password = localReadConfig.get_db_password()
charset = 'utf8'


class MySQL:
    # 初始化连接mall
    @staticmethod
    def connect_mall():
        mall = localReadConfig.get_db_mall()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=mall,
            charset=charset
        )
        return conn

    # 连接ps数据库
    @staticmethod
    def connect_ps():
        ps = localReadConfig.get_db_ps()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=ps,
            charset=charset
        )
        return conn

    # 连接bi数据库
    @staticmethod
    def connect_bi():
        bi = localReadConfig.get_db_bi()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=bi,
            charset=charset
        )
        return conn

    # 连接platform数据库----主干环境
    @staticmethod
    def connect_platform():
        platform = localReadConfig.get_db_platform()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=platform,
            charset=charset
        )
        return conn

    # 连接pro_tal数据库
    @staticmethod
    def connect_portal():
        portal = localReadConfig.get_db_portal()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=portal,
            charset=charset
        )
        return conn

    # 连接os数据库
    @staticmethod
    def connect_os():
        os = localReadConfig.get_db_os()
        conn = pymysql.connect(
            host=host,
            port=port,
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
            port=port,
            user=username,
            passwd=password,
            db=os_emp,
            charset=charset
        )
        return conn

    # 连接order数据库
    @staticmethod
    def connect_order():
        order = localReadConfig.get_db_order()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=order,
            charset=charset
        )
        return conn

    # 连接open_api数据库----主干环境
    @staticmethod
    def connect_open_api():
        open_api = localReadConfig.get_db_open_api()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=open_api,
            charset=charset
        )
        return conn

    # 连接content_fair数据库----主干环境
    @staticmethod
    def connect_content_fair():
        db_content = localReadConfig.get_db_content()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=db_content,
            charset=charset
        )
        return conn

    # 连接content_fair数据库----主干环境
    @staticmethod
    def connect_finance():
        db_finance = localReadConfig.get_db_finance()
        conn = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=db_finance,
            charset=charset
        )
        return conn


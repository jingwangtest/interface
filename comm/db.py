import pymysql
import types


class MySQL:
    __db = None

    # 在这里配置自己的SQL服务器
    __config = {
        'host': "192.168.150.33",
        'port': 3306,
        'username': "root",
        'password': "test2o17",
        'database': "bidetect",
        'charset': "utf8"
    }

    def __init__(self):
        self.__connect()

    def __del__(self):
        if (self.__db is not None):
            self.__db.close()

    def __connect(self):
        if (self.__db == None):
            self.__db = pymysql.connect(
                host=self.__config['host'],
                port=self.__config['port'],
                user=self.__config['username'],
                passwd=self.__config['password'],
                db=self.__config['database'],
                charset=self.__config['charset']
            )
        return self.__db
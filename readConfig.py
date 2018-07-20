import os
# import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser(allow_no_value=True)
        self.cf.read(configPath, encoding='UTF-8')

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http_cp(self, url_cp):
        value = self.cf.get("HTTP", url_cp)
        return value

    def get_http_sp(self, url_sp):
        value = self.cf.get("HTTP", url_sp)
        return value

    def get_http_cu(self, url_cu):
        value = self.cf.get("HTTP", url_cu)
        return value

    def get_db_bi(self, database_bi):
        value = self.cf.get("DATABASE", database_bi)
        return value

    def get_db_bi1(self, database_bi1):
        value = self.cf.get("DATABASE150", database_bi1)
        return value

    def get_db_ps(self, database_ps):
        value = self.cf.get("DATABASE", database_ps)
        return value

    def get_db_ps1(self, database_ps1):
        value = self.cf.get("DATABASE150", database_ps1)
        return value

    def get_db_platform(self, database_platform):
        value = self.cf.get("DATABASE", database_platform)
        return value

    def get_db_platform1(self, database_platform1):
        value = self.cf.get("DATABASE150", database_platform1)
        return value

    def get_db_mall(self, database_mall):
        value = self.cf.get("DATABASE", database_mall)
        return value

    def get_db_mall1(self, database_mall1):
        value = self.cf.get("DATABASE150", database_mall1)
        return value

    def get_db_os(self, database_os):
        value = self.cf.get("DATABASE", database_os)
        return value

    def get_db_os1(self, database_os1):
        value = self.cf.get("DATABASE150", database_os1)
        return value

    def get_db_portal(self, database_portal):
        value = self.cf.get("DATABASE", database_portal)
        return value

    def get_db_portal1(self, database_portal1):
        value = self.cf.get("DATABASE150", database_portal1)
        return value





    def get_db_host(self, host):
        value = self.cf.get("DATABASE", host)
        return value

    def get_db_username(self, username):
        value = self.cf.get("DATABASE", username)
        return value


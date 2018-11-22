import os
# import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser(allow_no_value=True)
        self.cf.read(configPath, encoding='UTF-8')

    def get_email(self):
        value = self.cf.get("EMAIL", "name")
        return value

    def get_http_cp(self):
        value = self.cf.get("HTTP", "url_cp")
        return value

    def get_http_sp(self):
        value = self.cf.get("HTTP", "url_sp")
        return value

    def get_http_cu(self):
        value = self.cf.get("HTTP", "url_cu")
        return value

    def get_db_bi(self):
        value = self.cf.get("DATABASE150", "database_bi")
        return value

    def get_db_bi1(self):
        value = self.cf.get("DATABASE", "database_bi1")
        return value

    def get_db_ps(self):
        value = self.cf.get("DATABASE150", "database_ps")
        return value

    def get_db_ps1(self):
        value = self.cf.get("DATABASE", "database_ps1")
        return value

    def get_db_platform(self):
        value = self.cf.get("DATABASE150", "database_platform")
        return value

    def get_db_platform1(self):
        value = self.cf.get("DATABASE", "database_platform1")
        return value

    def get_db_mall(self):
        value = self.cf.get("DATABASE150", "database_mall")
        return value

    def get_db_mall1(self):
        value = self.cf.get("DATABASE", "database_mall1")
        return value

    def get_db_os(self):
        value = self.cf.get("DATABASE150", "database_os")
        return value

    def get_db_os1(self):
        value = self.cf.get("DATABASE", "database_os1")
        return value

    def get_db_portal(self):
        value = self.cf.get("DATABASE150", "database_portal")
        return value

    def get_db_portal1(self):
        value = self.cf.get("DATABASE", "database_portal1")
        return value

    def get_db_empos(self):
        value = self.cf.get("DATABASE150", "database_empos")
        return value

    def get_db_empos1(self):
        value = self.cf.get("DATABASE", "database_empos1")
        return value

    def get_db_host(self):
        value = self.cf.get("DATABASE", "host")
        return value

    def get_db_username(self):
        value = self.cf.get("DATABASE", "username")
        return value

    def get_db_order1(self):
        value = self.cf.get("DATABASE", "database_order1")
        return value

    def get_db_open_api(self):
        value = self.cf.get("DATABASE150", 'database_api')
        return value

    def get_db_open_api1(self):
        value = self.cf.get("DATABASE", 'database_api1')
        return value
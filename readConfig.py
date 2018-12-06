import os
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

    # ---------- 获取登录地址 ------------------
    def get_http_cp(self):
        value = self.cf.get("HTTP", "url_cp")
        return value

    def get_http_sp(self):
        value = self.cf.get("HTTP", "url_sp")
        return value

    def get_http_admin(self):
        value = self.cf.get("HTTP", "url_admin")
        return value

    def get_http_www(self):
        value = self.cf.get("HTTP", "url_www")
        return value

    def get_http_cu(self):
        value = self.cf.get("HTTP", "url_cu")
        return value

    def get_http_emp(self):
        value = self.cf.get("HTTP", "url_www")
        return value

    def get_http_user(self):
        value = self.cf.get("HTTP", "url_user")
        return value

    # -------- 获取登录用户 -----------------
    def read_admin_login(self):
        value = self.cf.get("username", 'admin_user')
        return value

    def read_sp_login(self):
        value = self.cf.get("username", 'sp_user')
        return value

    def read_cp_login(self):
        value = self.cf.get("username", 'cp_user')
        return value

    def read_cu_login(self):
        value = self.cf.get("username", 'cu_user')
        return value

    def read_www_login(self):
        value = self.cf.get("username", 'www_user')
        return value

    def read_emp_login(self):
        value = self.cf.get("username", 'emp_user')
        return value

    # ------------ 获取数据库用户登录信息 --------------
    def get_db_host(self):
        value = self.cf.get("DATA", "host")
        return value

    def get_db_username(self):
        value = self.cf.get("DATA", "username")
        return value

    def get_db_password(self):
        value = self.cf.get("DATA", "password")
        return value

    def get_db_port(self):
        value = self.cf.get("DATA", "port")
        return value

    # ------------ 获取数据库信息 --------------
    def get_db_bi(self):
        value = self.cf.get("DATA", "database_bi")
        return value

    def get_db_ps(self):
        value = self.cf.get("DATA", "database_ps")
        return value

    def get_db_platform(self):
        value = self.cf.get("DATA", "database_platform")
        return value

    def get_db_mall(self):
        value = self.cf.get("DATA", "database_mall")
        return value

    def get_db_os(self):
        value = self.cf.get("DATA", "database_os")
        return value

    def get_db_portal(self):
        value = self.cf.get("DATA", "database_portal")
        return value

    def get_db_empos(self):
        value = self.cf.get("DATA", "database_empos")
        return value

    def get_db_open_api(self):
        value = self.cf.get("DATA", 'database_api')
        return value

    def get_db_order(self):
        value = self.cf.get("DATA", "database_order")
        return value

    def get_db_content(self):
        value = self.cf.get("DATA", "database_content")
        return value

    # ------------ 获取环境变量  ----------
    # ------------ sp用户信息 -------------
    def read_sp_user(self):
        value = self.cf.get("branch", 'sp_createUser')
        return value

    def read_sp_com_id(self):
        value = self.cf.get("branch", 'spId')
        return value

    def read_sp_com_name(self):
        value = self.cf.get("branch", 'spComName')
        return value

    def read_sp_emp_id(self):
        value = self.cf.get("branch", 'spEmpId')
        return value

    def read_sp_emp_name(self):
        value = self.cf.get("branch", "spEmpName")
        return value

    # ------------ cu用户信息 ----------
    def read_cu_use(self):
        value = self.cf.get("branch", "cu_createUser")
        return value

    def read_cu_com_id(self):
        value = self.cf.get("branch", 'cuCompId')
        return value

    def read_cu_com_name(self):
        value = self.cf.get("branch", "cuComName")
        return value

    def read_cu_emp_id(self):
        value = self.cf.get("branch", 'cuEmpId')
        return value

    def read_cu_emp_name(self):
        value = self.cf.get("branch", "cuEmpName")
        return value

    # ------------ cp用户信息 ----------
    def read_cp_use(self):
        value = self.cf.get("branch", "cp_createUser")
        return value

    def read_cp_com_id(self):
        value = self.cf.get("branch", 'cpComId')
        return value

    def read_cp_com_name(self):
        value = self.cf.get("branch", "cpComName")
        return value

    def read_cp_emp_id(self):
        value = self.cf.get("branch", 'cpEmpId')
        return value

    def read_cp_emp_name(self):
        value = self.cf.get("branch", "cpEmpName")
        return value

    # ------------ admin用户信息 ----------
    def read_admin_emp_id(self):
        value = self.cf.get("branch", "adEmpId")
        return value


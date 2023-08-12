import configparser

config = configparser.RawConfigParser()

config.read("D:\\E\\IT\\Orangehrm Project DDT Framework\\Configuration\\config.ini")

class ReadValue:

    @staticmethod
    def getUrl():
        Url = config.get("login info",'url')
        return Url

    @staticmethod
    def getusername():
        username = config.get("login info", "username")
        return username


    @staticmethod
    def getpassword():
        password = config.get("login info", "password")
        return password


import configparser

config = configparser.RawConfigParser()

config.read("D:\\E\\IT\\Orangehrm Project\\Configuration\\config.ini")

class ReadValue:

    @staticmethod
    def getUrl():
        Url = config.get('login info', 'url')
        return Url


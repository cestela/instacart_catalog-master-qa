import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getSessionCookie():
        return config.get('common info', 'sessionCookie')

    @staticmethod
    def getStore():
        return config.get('basic info', 'store')

    @staticmethod
    def getIncorrectValue():
        return config.get('basic info', 'qa')

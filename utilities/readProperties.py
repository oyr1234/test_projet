import configparser

class ReadConfig:
    """Lecture du fichier config.ini"""
    
    @staticmethod
    def getApplicationURL():
        config = configparser.RawConfigParser()
        config.read("./Configurations/config.ini")
        return config.get('COMMON', 'baseURL')
    
    @staticmethod
    def getLoginURL():
        config = configparser.RawConfigParser()
        config.read("./Configurations/config.ini")
        return config.get('LOGIN', 'loginURL')
    
    @staticmethod
    def getUseremail():
        config = configparser.RawConfigParser()
        config.read("./Configurations/config.ini")
        return config.get('LOGIN', 'username')
    
    @staticmethod
    def getPassword():
        config = configparser.RawConfigParser()
        config.read("./Configurations/config.ini")
        return config.get('LOGIN', 'password')
    
    @staticmethod
    def getAPIBaseURL():
        config = configparser.RawConfigParser()
        config.read("./Configurations/config.ini")
        return config.get('API', 'apiBaseURL')

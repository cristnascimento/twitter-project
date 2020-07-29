import configparser

class Config:

    def __init__(self, fileName):
        self.config = configparser.ConfigParser()
        self.config.read(fileName)
        self.setAllAttributes()

    def setAllAttributes(self):
        self.api_key = self.config['default']['api_key']
        self.api_secret = self.config['default']['api_secret']
        self.token = self.config['default']['token']
        self.token_secret = self.config['default']['token_secret']

if __name__ == '__main__':
    config = Config('config.env')
    print('api_key:', config.api_key)

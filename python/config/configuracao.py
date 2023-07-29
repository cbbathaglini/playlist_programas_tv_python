class Configuracao:
    '''
    instance = {}
    def getInstance(self):
        if self.instance is None:
            self.instance = Configuracao()
        return self.instance
    '''
    def db_config(self):
        return ["localhost", "root", "","3306","playlists_withoutdocker"]
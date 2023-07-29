class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]

    @property
    def programas(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)


    def __str__(self):
        return f'nome: {self._nome}, programas:{self._programas}' # tamanho:{self.tamanho(self)}'        
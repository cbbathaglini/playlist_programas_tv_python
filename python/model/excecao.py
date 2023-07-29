
class Excecao(Exception):
    _array_validacoes = []
    _e = None

    def __construct__(self, texto = None, e = None):
      
        if (e is None):
            self.__construct__(texto, e.getCode(), e)
        elif texto is not None:
            self.__construct__(texto)
            
        self._array_validacoes = []

        if(e is not None):
            if(isinstance(e, Excecao)):
                self._e = e.get_excecao()
                self._array_validacoes = e.get_validacoes()
            else:
                self._e = e
                
        
    
    def adiciona_validacao(self, texto, tipoAlerta = None):
        self._array_validacoes.append([texto, tipoAlerta]) 

    def lancar_Validacoes(self):
        if self.possui_validacoes():
            raise self
    
    def possui_validacoes(self):
        return len(self._array_validacoes) > 0

    def get_excecao(self):
        return self._e
    
    def get_validacoes(self):
        return self._array_validacoes
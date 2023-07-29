from model.serie import Serie
from model.filme import Filme
from model.documentario import Documentario
from model.playlist import Playlist


vingadores = Filme("Vingadores - Guerra Infinita",2022,160)
#print(vingadores.nome)


friends = Serie("Friends",1999,12)
friends.nome = "friends"
friends.dar_like()
friends.dar_like()
#friends.imprime()

vida_selvagem = Documentario("Vida Selvagem",2021,120)
vida_selvagem.dar_like()

ted_lasso = Serie("Ted Lasso", 2019, 30)
ted_lasso.dar_like()
ted_lasso.dar_like()
ted_lasso.dar_like()

filmes_e_series = [vingadores,friends,vida_selvagem,ted_lasso]

'''
for programa in filmes_e_series:
    print(programa)
'''

playlist_1 = Playlist("Minha playlist", filmes_e_series)


''' se playlist for iterable
for programa in playlist_1:
    print(programa)

#contém série friends
print(f"friends in playlist_1? {friends in playlist_1}")
'''
print(f"friends in playlist_1? {friends in playlist_1}")
print(f"último item da playlist {playlist_1[-1]}")
for programa in playlist_1:
    print(programa)
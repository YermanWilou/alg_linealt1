import vec
#   python proyecto1.py


############################################## Parte A ##########################################
rating = [i.strip().split(",", 2) for i in list(open("ratings.csv", encoding = 'utf-8'))]
movies = [i.strip().split(",", 1) for i in list(open("movies.csv", encoding = 'utf-8'))]
rating.pop(0)
movies.pop(0)

#return Vec(u.D, {d: u[d] + v[d] for d in u.D})
dominio = {int(movies[i][0]) for i in range(len(movies))}

########################## Transformamos en int ###################################
for i in range(len(rating)):
    for j in range(len(rating[i])):
        rating[i][j] = int(rating[i][j])
for i in range(len(movies)):
    movies[i][0] = int(movies[i][0])

rating2 = []
num = rating[0][0]
lista = []
for i in range(len(rating)):  
    if i == 0:
        lista.append(rating[i])
    else:
        if rating[i][0] == rating[i-1][0]:
            lista.append(rating[i])
            if i == len(rating)-1:
                rating2.append(lista)
                lista = []
        else:
            rating2.append(lista)
            lista = []
            lista.append(rating[i])
####################### rating2[0] == Usuario 1 ######################
####################### por cada usuario "id_pelicula" : rating ####################

lista_vectores = list()
for user in rating2:
    funcion = {user[i][1]: user[i][2] for i in range(len(user))}
    vector = vec.Vec(dominio, funcion)
    lista_vectores.append([vector, user[0][0]])
######### Se crean los vectores de cada usuario #####################
######### users es diccionario user_id: vector  #####################
######### usuario[0] = vector y usuario[1] es el usuario ############
users = {usuario[1]:usuario[0] for usuario in lista_vectores} 
############################################## Parte B ##########################################
dominio_usuarios = {int(fila[0]) for fila in rating}
dict_movies = {int(fila[0]):dominio_usuarios for fila in movies}
for fila in rating:
    id_usuario = fila[0]
    id_pelicula = fila[1]
    rating_nada = fila[2]
    #aux = dict_movies[id_pelicula]
    #aux[id_usuario] = rating_nada
#print(dict_movies[1])

dom_aux = {int}

#print(dict_movies[1])

#movies[movie_id] = movies_vec(Vector de cada peli)
#cada pelicula con su vector rating

#Separamos el archivo de ratings por pelicula
def ordenador(lista):
    return lista[1]
rating_ordenado = sorted(rating, key=ordenador)


lista_peliculas = list()
lista = list()
for i in range(len(rating_ordenado)):
    if i == 0:
        lista.append(rating_ordenado[i])
    else:
        if rating_ordenado[i][1] == rating_ordenado[i-1][1]:
            lista.append(rating_ordenado[i])
            if i == len(rating_ordenado)-1:
                lista_peliculas.append(lista)
                lista = []              
        else:
            lista_peliculas.append(lista)
            lista = []
            lista.append(rating_ordenado[i])

print(len(lista_peliculas))

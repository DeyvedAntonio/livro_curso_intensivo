# Exercícios do capítulo 08

# 8.3
# def make_shirt(tamanho, texto):
#     print(f'A frase escolhida foi: {texto} e o tamanho é {tamanho}.')


# make_shirt('G', 'Atividades de ramificação')
# make_shirt(texto='Não tenha pressa, mas não perca tempo', tamanho='GG')

# # 8.4
# def make_shirt(texto='Eu amo Python', tamanho='G'):
#     print(f'A frase escolhida foi: {texto} e o tamanho é {tamanho}.')


# make_shirt()
# make_shirt(tamanho='M')
# make_shirt('I love Python', 'P')

# # 8.5
# def descibe_city(cidade, pais='Brasil'):
#     print(f'{cidade} está localizada no {pais}')


# descibe_city('Cariaica')
# descibe_city('Lisboa', 'Portugal')
# descibe_city('Recife')

# # 8.6
# def city_country(city, country):
#     return f'{city.title()}, {country.title()}'


# print(city_country('santiago', 'chile'))
# print(city_country('recife', 'brasil'))
# print(city_country('lisboa', 'portugal'))

# # 8.7
# def make_album(artist, title_album):
#     info = {'Artist': artist.title(), 'Title': title_album.title()}
#     return info


# album_0 = make_album('pitty', 'amanhã')
# album_1 = make_album('disturbed', 'atention')
# album_2 = make_album('system of down', 'system')

# print(album_0, '\n', album_1, '\n', album_2)

# # 8.8
# artistas = {}
# while True:
#     artista = input('Informe o nome do artista (caso queira sair digite "q" a qualquer momento): ')
#     if artista == 'q':
#         break
#     album = input('Informe o título do álbum: ')
#     if album == 'q':
#         break
#     artistas = make_album(artista, album)

# print(f'O dicionário criado é {artistas}')

# 8.9
# magicians = ['David', 'Fred', 'Sarah']

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)


# show_magicians(magicians)

# # 8.10
# def make_great(magicians):
#     for chave, magician in enumerate(magicians):
#         magicians[chave] = f'Grande {magician}'


# make_great(magicians)
# show_magicians(magicians)

# 8.11
# def make_great_copy(magicians):
#     for chave, magician in enumerate(magicians):
#         magicians[chave] = f'Grande {magician}'
    
#     return magicians


# new_magicians = make_great_copy(magicians[:])
# show_magicians(magicians)
# show_magicians(new_magicians)

# 8.12
# def itens_sanduba(*items):
#     print('O sanduíche é composto por:')
#     for item in items:
#         print(item)


# itens_sanduba('Bacon')
# itens_sanduba('Bacon', 'Queijo')
# itens_sanduba('Ovo', 'Tomate', 'Hamburguer', 'Alface')

# 8.13
# def build_profile(nome, sobrenome, **outros):
#     info = {}
#     print(f'First name: {nome}')
#     print(f'Last name: {sobrenome}')
#     for key, value in outros.items():
#         info[key] = value
#     print(f'informações: {info}')


# build_profile('Deyved', 'Silva', location='Brasil', cidade='Cariacica')

# 8.14
# def make_car(fabricante, modelo, **infos):
#     info_car = {'Fabricante': fabricante, 'Modelo': modelo, 'Informações': infos}
#     return info_car


# car = make_car('saburu', 'outback', color='blue', tow_package=True)
# print(car)

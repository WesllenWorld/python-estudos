def sum(a, b):
    return a + b

def say_my_name(name):
    return f'Hello, {name}'

def say_my_name(name="Captain Rex"):
    return f'Hello, {name}'

def returning_more_values(a, b):
    return a + b, a - b

def argument_passing(name, alignment, lightsaber_color):
    return f'Hello there. I am {name}, i am with the {alignment} side and my lightsaber color is {lightsaber_color}'

sum = sum(int(input()), int(input()))
print(sum)

print(say_my_name('Ahsoka Tano'))
print(say_my_name())

print(returning_more_values(10, 5))

print(argument_passing('Obi-Wan Kenobi', 'light', 'blue'))
print(argument_passing(lightsaber_color='green', alignment='light', name='Yoda'))
print(argument_passing(**{'name': 'Darth Vader', 'alignment': 'dark', 'lightsaber_color': 'red'}))


def cancao_do_exilio(titulo, *versos, **informacoes):
    texto = "\n".join(versos)
    meta_dados = "\n".join(f'{chave}: {valor}' for chave, valor in informacoes.items())
    mensagem = f'{titulo}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

cancao_do_exilio(
    'Cancao do Exilio',
    'Minha terra tem palmeiras',
    'Onde canta o sabiá',
    'As aves que aqui gorjeiam',
    'Não gorjeiam como lá',
    autor='Gonçalves Dias',
    pais='Brasil'
)

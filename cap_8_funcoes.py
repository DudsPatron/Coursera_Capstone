# definindo uma função

def greet_user():
    """Exibe uma saudação."""
    print("Hello!")
    
greet_user()    

# passando informações para uma função

def greet_user(username):
    """Exibe uma saudação."""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

# argumentos posicionais

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('dog', 'achilles')
describe_pet('hamster', 'toby')

# argumentos nomeados

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type='dog', pet_name='achilles')

# valores default

print("\n valores default")

def describe_pet(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('achilles')
describe_pet('harry', 'rato')

# devolvendo um valor simples - return

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimmy', 'page')
print(musician)

# argumento opcional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# devolvendo um dicionario

def build_person(first_name, last_name):
    """Devolve um dicionario com as informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    return person
    
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """Devolve um dicionario com as informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
    
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Usando uma função com um laço while
print("\nUsando uma função com laço while:")
#

def get_formatted_name(first_name, last_name):
    """blablablablabla"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
#while True:
#    print("\nPlease tell me your name:")
#    print("(enter 'q' at any time to quit)")
    
#    f_name = input("First name: ")
#    if f_name == 'q':
#        break
#    l_name = input("Last name: ")
#    if l_name == 'q':
#        break
    
#    formatted_name = get_formatted_name(f_name, l_name)
#    print("\nHello, " + formatted_name + "!")
    
# Passando uma lista para uma função
print("\nPassando uma lista para uma função:")
#

def greet_users(names):
    """exibe uma saudação simples pra cada usuario."""
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
        
# Modificando uma lista em uma função
print("\nModificando uma lista em uma função:")
#

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
#    
print("\nReorganizando o codigo:")
#
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\n----The following models have been printed:----")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
        
#    
print("\nEvitando que a funçao modifique a lista: uma copia da lista:")
#        
    
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\n----The following models have been printed:----")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)    

print(unprinted_designs)

# Passando um número arbitrário de argumentos
print("\nPassando um número arbitrário de argumentos:")
#    

def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Misturando argumentos posicionais e arbitrários
print("\n--Misturando argumentos posicionais e arbitrários:--")
#      

def make_pizza(size, *toppings):
    """fsfsfs"""
    print("\nMaking a " + str(size) + "-inch pizza with the toppings:")
    for topping in toppings:
        print("- " + topping)    

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')    

# Usando argumentos nomeados arbitrários
print("\n--Usando argumentos nomeados arbitrários:--")
# 

def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo q sabemos sobre um user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)
        
# Armazenando funções em modulos - importando um modulo
print("\n--Armazenando funções em modulos - importando um modulo:--")
# 

## primeiro criei um modulo chamado pizza.py

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'cheese')

# importando funções específicas
print("\n--importando funções específicas:--")
# 

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'cheese')

# usando a palavra reservada 'as' para atribuir um 'alias' a uma função
print("\n--usando a palavra reservada 'as' para atribuir um 'alias':--")
# 

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'cheese')

# usando a palavra reservada 'as' para atribuir um 'alias' a um modulo
print("\n--'as' para atribuir um 'alias' a um modulo:--")
# 

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'cheese')

# importando todas as funcoes de um modulo
print("\n--importando todas as funcoes de um modulo:--")
# 

from pizza import * 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'cheese')

## melhor é importar a função ou o modulo todo e usar a notação de ponto




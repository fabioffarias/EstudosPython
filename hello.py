import matematica
import texto

print(texto.reverso("fabio"))

print(texto.remove_espaco("teste de qualidade"))

print(texto.maiusculas_minusculas("FABIO"))

print(matematica.Fatorial(10))

print(matematica.Primo(19))

print(texto.remove_duplicados("catarata"))

x = "maca", "banana", "mamao"

y = 10

print(x)

for i in x:
    print (i)
    
name = input("Your Name: ")

print (texto.capitalizar(name))

primeiro_digito = ""
segundo_digito = ""

if len(name) >= 11:
    primeiro_digito = name[9]
    segundo_digito = name[10]

print(primeiro_digito)
print(segundo_digito)

print(str.isnumeric("f"))
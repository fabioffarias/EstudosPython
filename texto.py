def reverso(texto):
    
    texto_reverso = ""
    
    for i in texto:
        texto_reverso = i + texto_reverso
        
    return texto_reverso

def remove_espaco(texto):
    
    novo_texto = ""
    
    for i in texto:
        if i != " ":
            novo_texto = novo_texto + i
            
    return novo_texto

def maiusculas_minusculas(texto):
    
    novo_texto = ""
    contador = 0
    
    for i in texto:
        
        if contador % 2 == 0:
            novo_texto = novo_texto + str.upper(i)
        else:
            novo_texto = novo_texto + str.lower(i)
        
        contador = contador + 1
            
    return novo_texto

def remove_duplicados(texto):
    
    novo_texto = ""
    
    for i in texto:
        if novo_texto.find(i) < 0:
            
            novo_texto = novo_texto + i
            
    return novo_texto
    
def capitalizar(texto):
    
    novo_texto = ""
    maiuscula = True
    
    for i in texto:
        
        if maiuscula:
            novo_texto = novo_texto + str.upper(i)
        else:
            novo_texto = novo_texto + str.lower(i)
        
        if i == " ":
            maiuscula = True
        else:
            maiuscula = False
        
    return novo_texto
        
        
        
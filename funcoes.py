def incluir (vetor):
    
 pessoa={}
 pessoa["nome"]= input ("informe nome:")
 pessoa["email"]= input ("infome email")
 pessoa["telefone"]= input("infome o numero")

 vetor.append(pessoa)




def pesquisar (vetor,nomebusca):
    posicao=-1
    encontrado = False
    for elemento in vetor:
         if elemento ["nome"] .lower()== nomebusca.lower():
             encontrado = True
             break
    
         return posicao 

    if encontrado:
      
        return posicao

    else:
     
     return-1    
   



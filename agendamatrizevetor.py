agenda=[]

while True:
     
     print ("1-cadastro")
     print ("2 - pesquisa pelo nome")
     print ("3 - listar")
     print ("4 - alterar")
     print ("5- excluir")
     print ("9- saida")
     opcao= int(input("infome a opção"))

     if opcao ==1:
          
          pessoa={}
          pessoa["nome"]= input ("informe nome:")
          pessoa["email"]= input ("infome email")
          pessoa["telefone"]= input("infome o numero")

          agenda.append(pessoa)
     
     elif opcao ==2:
          
          nomebusca= input("infomer o nome para a busca:")
          
          for elemento in agenda:
            
            if elemento["nome"].lower()== nomebusca.lower(): 
                   
                   print(f"""{elemento["nome"]}\t {elemento["email"]}\t{elemento["telefone"]}""")
     elif opcao ==3:
          
          for elemento in agenda:
               
               print(f"""{elemento["nome"]}\t {elemento["email"]}\t{elemento["telefone"]}""")

     elif opcao ==4:

          nomebusca=input ("infomer o nome da busca")  

          posicao=-1
          
          for elemento in agenda :

               posicao= posicao+1

               if elemento ["nome"].lower == nomebusca.lower():
                 break     
          
          if posicao !=-1:
               
               agenda[posicao]["nome"]= input ("infome o nome:")

               agenda[posicao]["email"]= input("infome o email:")

               agenda[posicao]["telefone"]=input("infome o telefone")


     elif opcao ==5:
          
          nomebusca=input ("infomer o nome da busca")  

          posicao=-1
          
          for elemento in agenda :

               posicao= posicao+1

               if elemento ["nome"].lower == nomebusca.lower():
                 break    
                
     if posicao!=-1:
               agenda.pop(posicao)

     elif opcao ==9:
          break
     else:
          print("opção invalida.")
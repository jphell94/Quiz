print("Seja muito bem vindo ao quiz")
answer_user = input("Quer começar (s/n) ")

if answer_user != "s":
    quit()

score = 0    

print("Começamdo ...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (a) Rockstar Games \n (b) Epic Games \n (c) Ubisoft \n (d) activision \n (e) EA ") 
answer_1 = input("Resposta: ")

if answer_1 == "a":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual o nome do protagonista do Gta San Andreas (GTA SA)? \n (a) Carlos John \n (b) Carl Jonhson \n (c) Carl Jaqueline \n (d) Carlos Jonhson  \n (e) Cleitin ") 
answer_2 = input("Resposta: ")

if answer_2 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("O que são software e hardware respectivamente? \n (a) A parte fisica e a parte lógica do computador \n (b) A parte lógica e a parte física do computador \n (c) Setores de armazenamento de dados \n (d) Programas de analises de manutenção de micro \n (e) NDA ") 
answer_3 = input("Resposta: ")

if answer_3 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Para que serve a lixeira do computador ? \n (a) Reciclar arquivos temporários e fixos \n (b) Excluir temporariamente arquivo que serão reaproveitados pelo sistema \n (c) Armazenar temporariamente arquivos que depois serão excluidos definitivamente \n (d) Armazenar definitivamente arquivo do sistema operacional \n (e) NDA ") 
answer_4 = input("Resposta: ")

if answer_4 == "c":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")    

print("Serve para criar e editar slides: \n (a) Microsoft Word \n (b) Microsoft Power Point \n (c) Microsoft Outlook \n (d) Microsoft Excel \n (e) NDA ") 
answer_5 = input("Resposta: ")

if answer_5 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print(f"Quiz acabou ... Pontuação: {score}/5 ")     
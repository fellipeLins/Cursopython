# Classificador de Nivel de Heroi

nomeHeroi = input("Informe o nome do seu Heroi: ")

xp = float(input(f"Informe o nivel de experiencia de {nomeHeroi}:"))

if xp <= 1000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Ferro")
elif xp <=2000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Bronze")
elif xp <=5000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Prata")
elif xp <=7000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Ouro") 
elif xp <=8000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Platina")
elif xp <=9000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Ascedente")
elif xp <=10000:
    print(f"O Heroi de nome {nomeHeroi} está no nivel Imortal")
else:
    xp > 10000 
    print(f"O Heroi de nome {nomeHeroi} está no nivel Radiante")
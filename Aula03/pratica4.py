turma = {
    "Ana" : [8.0, 9.5],
    "Bruno" : [6.0, 5.5],
    "Carla" : [4.0, 3.5]
}

mediaTurma = []

for nome, nota in turma.items():

    media = (nota[0]+nota[1])/ 2
    mediaTurma.append(media)

    if media > 7:
        print(f"{nome} sua média é {media:.1f}, Aprovado")
    elif media > 5:
        print(f"{nome} sua média é {media:.1f}, Recuperação")
    else:
        print(f"{nome} sua média é {media:.1f}, Reprovado")

print(f"{(sum(mediaTurma)/len(mediaTurma)):.2f}")

mediaTurma.sort
print(f"A média da turma é {mediaTurma}")
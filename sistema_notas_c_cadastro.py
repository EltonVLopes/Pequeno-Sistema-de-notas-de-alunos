alunos = []

nota1 = float(input('insira a nota 1 '))
nota2 = float(input('insira a nota 2 '))
notaf = (nota1 + nota2) / 2 


nome = input('insira o nome do aluno ')
media = notaf

aluno = {
"nome" : nome,
"media" : media

}

alunos.append(aluno)

print(alunos)

if notaf >= 7:
    print(f'Aluno {nome} Aprovado!\n Media = {notaf:.1f}')
elif notaf >= 5 and notaf <= 6.9:
    print(f'Aluno {nome} Recuperação \n Media = {notaf:.1f}')
else:
    print(f'Reprovado \n Media = {notaf:.1f}')


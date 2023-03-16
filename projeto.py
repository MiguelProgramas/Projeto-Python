nascimento = 1997
nome = 'Caio'
salario = 666.66
salarioAnual = 0.0
anoAtual = 2023
nascimentojovem = 2006


def calculoIdade(nascimento, anoAtual):
    idade = anoAtual - nascimento
    return idade
idade = calculoIdade(nascimento, anoAtual)
idadejovem = calculoIdade(nascimentojovem, anoAtual)
print('Idade é '+str(idade))
print('Idade jovem é '+str(idadejovem))
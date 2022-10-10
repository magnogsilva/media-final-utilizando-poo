class media:

    p_alunos = 0

    def __init__(self,m):
        self.m = m
        media.p_alunos += 1

    def situacao(self,n2):
        self.m + n2 
        m_final = (self.m + n2) / 2
        if m_final >= 7:
            print('Com uma média final de {}'.format(m_final))
            print('A situação do {}º Aluno é: APROVADO'.format(media.p_alunos))
        else:
            print('Com uma média final de {}'.format(m_final))
            print('A situação do {}º Aluno é: REPROVADO'.format(media.p_alunos))

print('\n=== MÉDIA FINAL E SITUAÇÃO DOS ALUNOS ===\n')

aluno_1 = media(float(input('Informe a primeira nota: ')))
aluno_1.situacao(float(input('Informa a segunda nota: ')))
print('='*35)
print('')
aluno_2 = media(float(input('Informe a primeira nota: ')))
aluno_2.situacao(float(input('Informa a segunda nota: ')))
print('='*35)
print('')
aluno_3 = media(float(input('Informe a primeira nota: ')))
aluno_3.situacao(float(input('Informa a segunda nota: ')))

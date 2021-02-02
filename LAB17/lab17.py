class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

class Repositorio:
    def __init__(self):
        self.alunos = []

    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        import re
        regexsenha=re.compile(r'[A-Z][a-z]+[0-9]+[!@#$&*]..+')
        regexmail=re.compile(r'[\w\-\+\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}')
        for i in self.alunos:
            if aluno.ra == i.ra:
                raise RAInvalido
        if not regexsenha.match(aluno.senha):
            raise SenhaFraca
        elif not regexmail.match(aluno.email):
            raise EmailInvalido
        else:
            self.alunos.append(aluno)
    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        import re
        regexsenha=re.compile(r'[A-Z][a-z]+[0-9]+[!@#$&*]..+')
        regexmail=re.compile(r'[\w\-\+\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}')
        count=0
        for i in self.alunos:
            if aluno.ra == i.ra:
                break
            else:
                count+=1
        if count== len(self.alunos):
            raise RAInvalido
        elif not regexsenha.match(aluno.senha):
            raise SenhaFraca
        elif not regexmail.match(aluno.email):
            raise EmailInvalido
        else:
            for i in self.alunos:
                if i.ra==aluno.ra:
                    alunoIndex=self.alunos.index(i)
                    self.alunos[alunoIndex].ra= aluno.ra
                    self.alunos[alunoIndex].nome= aluno.nome
                    self.alunos[alunoIndex].email= aluno.email
                    self.alunos[alunoIndex].usuario= aluno.usuario
                    self.alunos[alunoIndex].senha= aluno.senha
                    break
    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        for i in self.alunos:
            if ra == i.ra:
                return i
            else:
                pass
        raise RAInvalido
    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        for i in self.alunos:
            if ra == i.ra:
                self.alunos.remove(i)
                return None
            else:
                pass
        raise RAInvalido

    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        self.alunos=[]

COLUNAS = {
    "nome": "Digite seu nome Completo",
    "email": "Informe um email para contato",
    "telefone": "Informe um número de contato",
    "data_nascimento": "Qual sua data de nascimento",
    "curso": "Qual foi o último curso feito ou cursando no Senac?",
    "instrutor": "Qual é o nome do instrutor que esteve ministrando as aula para você?",
    "cpf": "CPF"
}

# Constantes para facilitar acesso às colunas
COLUNA_NOME = "nome"
COLUNA_EMAIL = "email"
COLUNA_TELEFONE = "telefone"
COLUNA_DATA_NASCIMENTO = "data_nascimento"
COLUNA_CURSO = "curso"
COLUNA_INSTRUTOR = "instrutor"
COLUNA_CPF = "cpf"

# Mapeamento de colunas do Excel para o padrão esperado
MAPEAMENTO_COLUNAS = {
    "qual sua data de nascimento?": "data_nascimento",
    "qual foi o ultimo curso feito ou cursando no senac?": "curso",
    "qual e o nome do instrutor que esteve ministrando as aula para voce?": "instrutor",
    "digite seu nome completo": "nome",
    "informe um email para contato": "email",
    "informe um numero de contato": "telefone",
}

# Colunas que queremos manter no dataframe final
COLUNAS_FINAIS = ["nome", "email", "telefone", "data_nascimento", "curso", "instrutor", "cpf"]

# Mapeamento de cursos (normalizar variações do mesmo curso)
MAPEAMENTO_CURSOS = {
    "tecnico em informatica": "Técnico em Informática",
    "tecnico de informatica": "Técnico em Informática",
    "curso tecnico de informatica": "Técnico em Informática",
    "cursando tecnico de ti": "Técnico em Informática",
    "programador de sistemas": "Programador de Sistemas",
    "programador de sistemas em python": "Programador de Sistemas",
    "programacao de sistemas com aplicacaes financeiras": "Programador de Sistemas",
    "cursando programacao de sistemas com aplicacaes financeiras": "Programador de Sistemas",
    "programador full stack": "Programador Full Stack",
    "programador fullstack": "Programador Full Stack",
    "programacao full stack": "Programador Full Stack",
    "programacao full stack cursando": "Programador Full Stack",
    "desenvolvimento de sistema": "Desenvolvimento de Sistemas",
    "analise e desenvolvimento de sistemas": "Desenvolvimento de Sistemas",
    "desenvolvimento de jogos": "Desenvolvimento de Jogos",
    "desenvolvimento de games": "Desenvolvimento de Jogos",
    "tecnico em desenvolvimento de jogos digitais": "Desenvolvimento de Jogos",
    "tecnico em programacao de jogos digitais": "Desenvolvimento de Jogos",
    "cursando no senac desenvolvimento de games 2026": "Desenvolvimento de Jogos",
    "administrador de redes": "Administração de Redes",
    "adm de redes e introducao a cyberseguranca": "Administração de Redes e Cybersegurança",
}

# Mapeamento de instrutores (normalizar variações do mesmo nome)
MAPEAMENTO_INSTRUTORES = {
    "felipe monteiro": "Felipe Monteiro",
    "filipe monteiro": "Felipe Monteiro",
    "prof. felipe": "Felipe Monteiro",
    "prof felipe": "Felipe Monteiro",
    "felipe": "Felipe Monteiro",
    "filipe": "Felipe Monteiro",
    "diego anjos": "Diego Anjos",
    "diego dos anjos": "Diego Anjos",
    "diego": "Diego Anjos",
    "ivo barbosa": "Ivo Barbosa",
    "ivor barbosa": "Ivo Barbosa",
    "ivo": "Ivo Barbosa",
    "kassia modesto": "Kássia Modesto",
    "joana darc": "Joana Darc",
    "Simone Amaral": "Simone Amaral",
    "Simone": "Simone Amaral",
}

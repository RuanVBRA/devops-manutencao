# Sistema de Controle de Manutencao

## Descricao

Sistema desenvolvido como atividade pratica da disciplina de DevOps e Integracao Continua da UNINTER.

O projeto tem como objetivo demonstrar a aplicacao de praticas de DevOps no desenvolvimento de um sistema simples para cadastro e controle de veiculos, utilizando versionamento, testes automatizados, containerizacao e integracao continua.

## Objetivo

Desenvolver uma aplicacao web para auxiliar no controle e gerenciamento da manutencao de veiculos, demonstrando um fluxo de desenvolvimento organizado e automatizado.

## Tecnologias utilizadas

- Python 3.13
- Flask
- Pytest
- Git
- GitHub
- Docker
- GitHub Actions
- Visual Studio Code

## Funcionalidades

- Cadastro de veiculos
- Listagem de veiculos cadastrados
- Validacao de campos obrigatorios
- Validacao de placas duplicadas
- Testes automatizados
- Execucao da aplicacao em container Docker
- Integracao continua com GitHub Actions

## Estrutura do projeto

```text
devops-manutencao/
|-- app/
|   |-- app.py
|   |-- test_app.py
|-- .github/
|   |-- workflows/
|       |-- ci.yml
|-- .gitignore
|-- Dockerfile
|-- README.md
|-- requirements.txt
```

## Instalacao

### 1. Clonar o repositorio

```bash
git clone https://github.com/RuanVBRA/devops-manutencao.git
cd devops-manutencao
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual no Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependencias

```bash
pip install -r requirements.txt
```

## Execucao local

Para executar a aplicacao:

```bash
python app/app.py
```

Depois, acessar no navegador:

```text
http://127.0.0.1:5000
```

## Testes automatizados

Os testes foram desenvolvidos utilizando o framework Pytest.

Para executar os testes:

```bash
pytest app/test_app.py -v
```

O projeto possui quatro testes automatizados:

- Teste da pagina inicial
- Teste do cadastro de veiculo
- Teste de placa duplicada
- Teste de campos obrigatorios

## Docker

A aplicacao foi containerizada utilizando Docker.

Para criar a imagem:

```bash
docker build -t devops-manutencao .
```

Para executar o container:

```bash
docker run -d -p 5000:5000 --name manutencao-app devops-manutencao
```

A aplicacao pode ser acessada em:

```text
http://localhost:5000
```

A utilizacao do Docker permite padronizar o ambiente de execucao e facilitar a implantacao da aplicacao.

## Integracao Continua

O projeto utiliza GitHub Actions para automatizar a execucao dos testes.

A pipeline esta localizada em:

```text
.github/workflows/ci.yml
```

A cada atualizacao enviada ao repositorio, a pipeline configura o ambiente Python, instala as dependencias e executa os testes automatizados.

A execucao da pipeline apresentou sucesso com os quatro testes aprovados.

## Versionamento e colaboracao

O projeto utiliza Git e GitHub para controle de versao.

Branches utilizadas:

- main
- desenvolvimento
- feature/cadastro-veiculos

Durante o desenvolvimento foi realizado fluxo de integracao entre branches, incluindo Pull Request, merge e resolucao de conflito.

## GitHub

Foram utilizados recursos do GitHub para organizacao e acompanhamento do projeto:

- Issues
- Milestones
- Labels
- Projects
- Wiki
- Insights
- Pull Requests
- GitHub Actions

## Repositorio

O projeto esta disponivel no GitHub:

https://github.com/RuanVBRA/devops-manutencao

## Licenca

Projeto desenvolvido para fins academicos na disciplina de DevOps e Integracao Continua da UNINTER.
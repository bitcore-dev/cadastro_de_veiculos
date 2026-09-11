# 🚗 FleetCard

## Sistema de Gestão e Cadastro de Veículos

**Projeto Integrador — Programador Back-End Python**

**Unidade Curricular:** Desenvolvimento Web com Django

**Tecnologias principais:** Python, Django, SQLite, Bootstrap 5 e Django Admin

---

## 📌 Sobre o Projeto

O **FleetCard** é um sistema web desenvolvido em **Python e Django** com o objetivo de realizar o **cadastro, consulta e gerenciamento de veículos**.

O sistema foi planejado para trabalhar com veículos de diferentes categorias, permitindo o cadastro de:

* 🚗 Carros
* 🏍️ Motocicletas
* 🚚 Caminhões

A aplicação será desenvolvida utilizando uma estrutura organizada, responsiva e preparada para receber novas funcionalidades relacionadas ao gerenciamento de frotas.

---

# 1. Situação de Aprendizagem

O gerenciamento de veículos pode envolver uma grande quantidade de informações, como tipo, marca, modelo, placa, RENAVAM, ano, cor, combustível, quilometragem, situação e observações.

Quando essas informações são armazenadas de maneira manual ou desorganizada, podem ocorrer dificuldades para localizar dados, atualizar registros, controlar informações dos veículos e acompanhar a situação da frota.

Diante dessa necessidade, foi proposto o desenvolvimento de uma aplicação web capaz de centralizar essas informações em um único sistema.

O **FleetCard** será desenvolvido utilizando **Python, Django e SQLite**, disponibilizando uma interface web responsiva construída com **Bootstrap 5**.

A aplicação também utilizará o **Django Admin** para gerenciamento administrativo dos dados.

---

# 2. Desafio

Desenvolver um sistema web denominado **FleetCard**, permitindo realizar o **cadastro, consulta, atualização e exclusão de veículos** de forma organizada.

A aplicação deverá trabalhar com diferentes tipos de veículos, não ficando limitada somente a automóveis.

O sistema deverá possuir:

* Cadastro de veículos;
* Consulta de veículos;
* Listagem de veículos;
* Visualização dos detalhes;
* Edição;
* Exclusão;
* Classificação por tipo de veículo;
* Cadastros complementares;
* Relatórios;
* Django Admin;
* Interface responsiva utilizando Bootstrap 5.

---

# 3. Competências Desenvolvidas

Ao concluir o projeto, o estudante deverá demonstrar que é capaz de:

* Configurar um projeto Django;
* Criar aplicações utilizando Django;
* Modelar banco de dados utilizando ORM;
* Utilizar SQLite como banco de dados;
* Desenvolver operações CRUD;
* Utilizar Django Admin;
* Criar Templates reutilizáveis;
* Utilizar herança de Templates;
* Organizar URLs e Views;
* Criar formulários;
* Trabalhar com validação de dados;
* Utilizar Bootstrap para construção da interface;
* Desenvolver uma interface responsiva;
* Organizar arquivos estáticos;
* Trabalhar com Git e GitHub;
* Desenvolver aplicações organizadas seguindo boas práticas.

---

# 4. Recursos Disponíveis

Para o desenvolvimento do projeto serão utilizados:

* Python 3.x;
* Django 6.x;
* SQLite;
* Visual Studio Code;
* Bootstrap 5;
* Bootstrap Icons;
* Navegador Web;
* Git;
* GitHub.

---

# 5. Entregáveis

Ao final do desenvolvimento, o projeto deverá apresentar:

* Projeto Django funcionando;
* Código-fonte organizado;
* Banco de dados SQLite;
* Interface funcional e responsiva;
* Template base reutilizável;
* Menu lateral responsivo;
* Cadastro de veículos;
* Diferentes tipos de veículos;
* Lista de veículos;
* Página de detalhes;
* Edição de veículos;
* Exclusão de veículos;
* Django Admin;
* Cadastros complementares;
* Controle de manutenção;
* Controle de revisões;
* Controle de documentação;
* Relatórios.

### Quantidade de registros

Como adaptação ao projeto FleetCard, a etapa final poderá utilizar uma quantidade definida de veículos cadastrados para demonstração e validação do sistema.

---

# 6. Requisitos Funcionais

## RF01 — Criar o projeto Django

Criar um projeto Django chamado:

```text
FleetCard
```

O projeto deverá possuir a configuração necessária para execução da aplicação web.

---

## RF02 — Criar o aplicativo

Criar o aplicativo responsável pelas funcionalidades principais do sistema.

Aplicação inicialmente utilizada:

```text
FleetCard
```

O aplicativo será responsável por organizar as funcionalidades, Views, URLs, Models, Templates e demais componentes necessários.

---

## RF03 — Criar o modelo Veículo

Criar o modelo **Veículo** utilizando o Django ORM.

O modelo deverá armazenar as principais informações necessárias para identificar e controlar um veículo.

### Campos previstos

| Campo            | Tipo                        |
| ---------------- | --------------------------- |
| Tipo             | ChoiceField / CharField     |
| Marca            | CharField ou relacionamento |
| Modelo           | CharField                   |
| Placa            | CharField                   |
| Ano              | IntegerField                |
| Cor              | CharField ou relacionamento |
| Combustível      | ChoiceField / CharField     |
| Quilometragem    | IntegerField                |
| Observações      | TextField                   |
| Data de cadastro | DateTimeField               |

A definição final dos campos poderá ser ajustada durante a implementação do modelo.

---

## RF04 — Registrar o modelo no Django Admin

O modelo **Veículo** deverá ser registrado no Django Admin.

O painel administrativo deverá permitir:

* Visualizar veículos;
* Cadastrar veículos;
* Editar veículos;
* Excluir veículos;
* Pesquisar informações;

### Pesquisas previstas

* Placa;
* Modelo;
* Marca;

### Filtros previstos

* Tipo de veículo;
* Marca;

---

## RF05 — Criar as páginas

O sistema deverá possuir as seguintes páginas:

* Home / Dashboard;
* Lista de Veículos;
* Novo Veículo;
* Editar Veículo;
* Excluir Veículo;
* Detalhes do Veículo;
* Contatos;
* Sobre.

Também poderão ser criadas páginas específicas para as funcionalidades complementares.

---

## RF06 — Criar um Template Base

Criar um Template Base para centralizar a estrutura comum da aplicação.

Arquivo:

```text
base.html
```

Todas as páginas principais deverão utilizar herança de Templates.

Exemplo:

```django
{% extends 'base.html' %}
```

O Template Base deverá conter:

* Estrutura HTML;
* Bootstrap;
* Bootstrap Icons;
* CSS do projeto;
* Sidebar;
* Área de conteúdo;
* Footer.

---

## RF07 — Criar um menu de navegação

O sistema deverá possuir um **menu lateral (Sidebar)** utilizando o componente **Offcanvas do Bootstrap**.

O menu será acionado através de um botão de hambúrguer.

### Menu previsto

```text
☰ FleetCard

INÍCIO
└── Dashboard

VEÍCULOS
├── Cadastrar veículo
├── Lista de veículos
└── Consultar veículo

TIPOS DE VEÍCULOS
├── Carros
├── Motocicletas
├── Caminhões
├── Vans e Utilitários
├── Ônibus
└── Tratores e Máquinas

CADASTROS
├── Marcas
├── Categorias
├── Combustíveis
└── Cores

CONTROLE
├── Quilometragem
└── Documentação

RELATÓRIOS
└── Relatório de veículos

SISTEMA
├── Configurações
└── Administração
```

O menu deverá funcionar em:

* Computadores;
* Notebooks;
* Tablets;
* Smartphones.

---

## RF08 — Criar tela de listagem

A tela de listagem deverá apresentar os principais dados dos veículos.

### Informações previstas

| Informação    | Descrição             |
| ------------- | --------------------- |
| Tipo          | Tipo do veículo       |
| Marca         | Marca                 |
| Modelo        | Modelo                |
| Placa         | Placa                 |
| Ano           | Ano                   |
| Combustível   | Tipo de combustível   |
| Quilometragem | Quilometragem atual   |

---

## RF09 — Criar ações

As ações disponíveis para cada veículo deverão permitir:

* 👁️ Visualizar;
* ✏️ Editar;
* 🗑️ Excluir.

As ações deverão estar disponíveis na listagem dos veículos.

---

## RF10 — Criar página de detalhes

A página de detalhes deverá apresentar todas as informações cadastradas do veículo.

Exemplo:

```text
Tipo
Marca
Modelo
Placa
Ano
Cor
Combustível
Quilometragem
Observações
Data de cadastro
```

---

# 7. Tipos de Veículos

O FleetCard será desenvolvido para trabalhar com diferentes categorias de veículos.

## Tipos previstos

### 🚗 Carro

Veículos de passeio e automóveis.

### 🏍️ Motocicleta

Motocicletas e veículos de duas rodas.

### 🚚 Caminhão

Veículos destinados principalmente ao transporte de cargas.

---

# 8. Cadastro de Veículo

O cadastro será realizado através de um formulário único.

O usuário deverá selecionar o tipo do veículo.

Exemplo:

```text
Tipo de veículo
[ Carro ▼ ]

[ Adicionar imagem do veículo ]

Marca
[ __________________ ]

Modelo
[ __________________ ]

Placa
[ __________________ ]

Ano
[ __________________ ]

Cor
[ __________________ ]

Combustível
[ __________________ ]

Quilometragem
[ __________________ ]

Observações
[ __________________ ]

[ Cadastrar Veículo ]
```

O mesmo formulário poderá ser utilizado para:

* Carro;
* Moto;
* Caminhão.

---

# 9. Operações CRUD

O sistema deverá implementar as operações fundamentais de um CRUD.

## Create — Criar

Permitir cadastrar um novo veículo.

## Read — Ler

Permitir listar e visualizar veículos cadastrados.

## Update — Atualizar

Permitir alterar os dados de um veículo.

## Delete — Excluir

Permitir excluir um veículo cadastrado.

### Fluxo

```text
CADASTRAR
    ↓
BANCO DE DADOS
    ↓
LISTAR
    ↓
VISUALIZAR
    ↓
EDITAR
    ↓
EXCLUIR
```

---

# 10. Cadastros Complementares

Além dos veículos, o sistema será preparado para possuir cadastros que complementem as informações da frota.

## 10.1 Marcas

Permitir cadastrar e organizar as marcas dos veículos.

Exemplos:

* Fiat;
* Volkswagen;
* Chevrolet;
* Toyota;
* Honda;
* Ford.

## 10.2 Categorias

Permitir classificar os veículos conforme sua finalidade.

Exemplos:

* Passeio;
* Carga;
* Transporte;
* Utilitário;
* Comercial;
* Motocicleta.

## 10.3 Combustíveis

Tipos previstos:

* Gasolina;
* Etanol;
* Diesel;
* Flex;
* Elétrico;
* Híbrido.

## 10.4 Cores

Permitir organizar as cores utilizadas nos veículos.

---

# 11. Controle de Revisões

O sistema poderá registrar revisões realizadas e previstas.

Informações previstas:

* Veículo;
* Data;
* Quilometragem;
* Tipo de revisão;
* Observações.

---

# 13. Controle de Quilometragem

O sistema poderá manter informações relacionadas à quilometragem dos veículos.

O objetivo é auxiliar no acompanhamento de:

* Revisões;
* Manutenções;
* Uso do veículo;
* Histórico.

---

# 14. Controle de Documentação

O sistema poderá possuir uma área para acompanhamento da documentação dos veículos.

Exemplos:

* Documentação do veículo;
* Data de vencimento;
* Situação;
* Observações.

---

# 15. Relatórios

Como funcionalidade complementar, o FleetCard poderá disponibilizar relatórios.

### Relatórios previstos

* Relatório geral de veículos;
* Relatório por tipo;
* Relatório por marca;
* Relatório de manutenção;
* Relatório de revisões;
* Relatório de documentação.

---

# 16. Requisitos Técnicos

O projeto deverá utilizar obrigatoriamente:

* **Django**;
* **Django ORM**;
* **SQLite**;
* **Templates Django**;
* **Bootstrap 5**;
* **Bootstrap Icons**;
* **Django Admin**.

Também serão utilizados:

* Python;
* HTML5;
* CSS3;
* Git;
* GitHub.

---

# 17. Regras de Negócio

## RN01 — Tipo obrigatório

Todo veículo deverá possuir um tipo definido.

---

## RN02 — Identificação obrigatória

O veículo deverá possuir informações suficientes para sua identificação.

---

## RN03 — Placa

A placa deverá ser utilizada como identificador do veículo e não deverá ser duplicada no sistema.

---

## RN04 — Quilometragem

A quilometragem não poderá possuir valor negativo.

```text
Quilometragem >= 0
```

---

## RN05 — Ano

O ano deverá possuir um valor válido para o veículo cadastrado.

---

## RN06 — Campos obrigatórios

Os campos definidos como obrigatórios deverão ser preenchidos antes do cadastro.

---

## RN07 — Status do veículo

Todo veículo deverá possuir uma situação/status definida.

Exemplos:

* Ativo;
* Em manutenção;
* Inativo;
* Disponível;
* Indisponível.

---

## RN08 — Cadastro único

Cada veículo deverá possuir uma identificação própria dentro do sistema.

---

## RN09 — Exclusão

A exclusão de um veículo deverá possuir confirmação para evitar remoções acidentais.

---

## RN10 — Integridade dos dados

As informações deverão ser validadas antes de serem armazenadas no banco de dados.

---

# 18. Estrutura de Templates

O projeto utilizará Templates reutilizáveis.

Estrutura prevista:

```text
templates/
│
├── base.html
│
├── home.html
│
├── includes/
│   ├── navbar.html
│   └── footer.html
│
└── veiculos/
    ├── lista.html
    ├── cadastro.html
    ├── detalhes.html
    ├── editar.html
    └── excluir.html
```

---

# 19. Arquivos Estáticos

Os arquivos estáticos serão organizados separadamente dos Templates.

Estrutura:

```text
static/
│
├── css/
│   └── style.css
│
└── images/
```

O arquivo `style.css` será utilizado para complementar os componentes do Bootstrap.

---

# 20. Estrutura Geral do Projeto

A estrutura inicial do projeto será organizada aproximadamente da seguinte forma:

```text
FleetCard/
│
├── manage.py
│
├── FleetCard/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
│
└── README.md
```

A estrutura poderá crescer conforme novas aplicações e funcionalidades forem adicionadas.

---

# 21. Interface

A interface será desenvolvida utilizando **Bootstrap 5**, buscando manter uma aparência:

* Simples;
* Organizada;
* Moderna;
* Responsiva;
* Fácil de utilizar.

O sistema utilizará **Bootstrap Icons** para representar visualmente as funcionalidades.

---

# 22. Sidebar Responsivo

O menu lateral será desenvolvido utilizando o componente **Offcanvas do Bootstrap**.

### Funcionamento

```text
        ☰
        ↓
   Abre o menu
        ↓
┌─────────────────────────┐
│ 🚗 FleetCard         ×  │
├─────────────────────────┤
│ 🚗 VEÍCULOS             │
│    Cadastrar veículo    │
│    Lista de veículos    │
│    Consultar veículo    │
│                         │
│ 🏷️ CADASTROS           │
│    Marcas               │
│    Categorias           │
│    Combustíveis         │
│    Cores                │
│                         │
│                         │
│ 📞 Contatos             |
│                         │
│ ℹ️ Sobre                │
└─────────────────────────┘
```

O menu deverá permanecer funcional independentemente do tamanho da tela.

---

# 23. URLs e Views

O projeto deverá organizar as rotas utilizando o sistema de URLs do Django.

Exemplo inicial:

```python
urlpatterns = [
    path('', views.home, name='home'),
]
```

À medida que as funcionalidades forem implementadas, novas rotas serão adicionadas para:

* Cadastro;
* Listagem;
* Edição;
* Exclusão.

---

# 24. Banco de Dados

O projeto utilizará **SQLite** como banco de dados durante o desenvolvimento.

A comunicação com o banco será realizada através do **Django ORM**.

Fluxo:

```text
Model
  ↓
Django ORM
  ↓
Migration
  ↓
SQLite
```

As alterações nos modelos serão aplicadas através das migrations do Django.

Comandos principais:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# 25. Django Admin

O Django Admin será utilizado para gerenciamento administrativo.

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Acesso:

```text
/admin/
```

O Admin será utilizado para facilitar o gerenciamento dos registros durante o desenvolvimento e também como ferramenta administrativa do sistema.

---

# 26. Fluxo Principal do Sistema

```text

FLEETCARD
    │
    ↓
  HOME
    │
    ↓
  ☰ MENU
    │
    ┌─────────────┐
    ↓             ↓
VEÍCULOS      CADASTRAR
    │             │
    ↓             ↓
  Marcas       Cadastrar
Categorias     Listar
  Cores        Editar
    │          Excluir
    │          
    │
    ↓
BANCO DE DADOS
    │
    ↓
RELATÓRIOS

```

---

# 27. Desenvolvimento por Etapas

## Etapa 1 — Configuração inicial

* [x] Criar projeto Django;
* [x] Configurar aplicação;
* [x] Criar estrutura de Templates;
* [x] Criar `base.html`;
* [x] Criar `home.html`;
* [x] Criar `navbar.html`;
* [x] Criar `footer.html`;
* [ ] Criar `contatos.html`
* [ ] Criar `sobre.html`
* [x] Configurar Bootstrap;
* [x] Configurar Bootstrap Icons;
* [x] Criar `style.css`.

---

## Etapa 2 — Navegação

* [x] Implementar Sidebar;
* [x] Implementar botão hambúrguer;
* [ ] Organizar menu por categorias;
* [ ] Criar links para as funcionalidades;
* [x] Testar responsividade.

---

## Etapa 3 — Banco de dados

* [ ] Criar model Veículo;
* [ ] Definir campos;
* [ ] Definir tipos de veículos;
* [ ] Criar migrations;
* [ ] Aplicar migrations;
* [ ] Registrar modelo no Admin.

---

## Etapa 4 — Cadastro de veículos

* [ ] Criar formulário;
* [ ] Criar View de cadastro;
* [ ] Criar URL;
* [ ] Criar Template;
* [ ] Validar dados;
* [ ] Salvar no banco.

---

## Etapa 5 — Listagem

* [ ] Criar View de listagem;
* [ ] Criar Template;
* [ ] Exibir veículos;
* [ ] Criar ações;
* [ ] Criar consulta.

---

## Etapa 6 — CRUD

* [ ] Visualizar;
* [ ] Editar;
* [ ] Excluir;
* [ ] Confirmar exclusão.

---

## Etapa 7 — Cadastros complementares

* [ ] Marcas;
* [ ] Categorias;
* [ ] Combustíveis;
* [ ] Cores.

---

## Etapa 8 — Relatórios

* [ ] Relatório geral;
* [ ] Relatório por tipo;
* [ ] Relatório por marca;
* [ ] Relatório de manutenção;
* [ ] Relatório de documentação.

---

## Etapa 10 — Testes e finalização

* [ ] Testar cadastro;
* [ ] Testar edição;
* [ ] Testar exclusão;
* [ ] Testar consultas;
* [ ] Testar validações;
* [ ] Testar Django Admin;
* [ ] Testar responsividade;
* [ ] Organizar código;
* [ ] Atualizar documentação;
* [ ] Publicar código no GitHub.

---

# 28. Controle de Versão

O desenvolvimento será acompanhado através do **Git e GitHub**.

Estrutura de branches planejada:

```text
main
 │
 └── develop
       │
       ├── feature/sidebar
       ├── feature/veiculos
       ├── feature/crud-veiculos
       ├── feature/cadastros
       ├── feature/manutencao
       └── feature/relatorios
```

A branch `main` será utilizada para versões estáveis.

As funcionalidades poderão ser desenvolvidas em branches específicas antes de serem integradas.

---

# 29. Status do Projeto

## 🟢 Implementado

* Estrutura inicial do projeto Django;
* Aplicação inicial;
* Estrutura de Templates;
* `base.html`;
* `home.html`;
* Estrutura de includes;
* Navbar;
* Footer;
* Bootstrap;
* Bootstrap Icons;
* CSS estático;
* Configuração inicial de URLs e Views.

## 🟡 Em desenvolvimento

* Sidebar;
* Menu hambúrguer;
* Model Veículo;
* Banco de dados;
* Cadastro de veículos;
* Tipos de veículos;
* CRUD.

## 🔵 Planejado

* Marcas;
* Categorias;
* Combustíveis;
* Cores;
* Manutenção;
* Revisões;
* Quilometragem;
* Documentação;
* Relatórios;
* Melhorias no Dashboard.

---

# 30. Projeto Integrador

O **FleetCard** tem como finalidade aplicar, de forma prática, os conhecimentos desenvolvidos durante a formação em programação Back-End com Python e Django.

O projeto será desenvolvido de maneira incremental, partindo da estrutura inicial da aplicação e evoluindo para um sistema completo de gerenciamento de veículos.

A documentação acompanhará a evolução do projeto, registrando as funcionalidades desenvolvidas, tecnologias utilizadas, requisitos e regras de negócio.

---

# 31. Conclusão

O **FleetCard** propõe uma solução web para centralizar o cadastro e gerenciamento de veículos.

A utilização de **Python, Django, ORM, SQLite, Bootstrap e Django Admin** permitirá desenvolver uma aplicação estruturada e responsiva.

O sistema será preparado para trabalhar com diferentes tipos de veículos, possibilitando sua utilização em cenários que envolvam carros, motocicletas e caminhões.

A arquitetura também permitirá a evolução do projeto para funcionalidades de manutenção, revisões, documentação e relatórios.

> 🚗 **FleetCard — Organização, controle e gestão de veículos em um único sistema.**

---

## 👨‍💻 Projeto

**Projeto:** FleetCard
**Tipo:** Projeto Integrador
**Área:** Desenvolvimento Web
**Backend:** Python + Django
**Banco de Dados:** SQLite
**Frontend:** HTML5 + CSS3 + Bootstrap 5
**Administração:** Django Admin
**Controle de versão:** Git + GitHub

---


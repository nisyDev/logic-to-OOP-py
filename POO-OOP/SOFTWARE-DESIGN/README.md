# Software Design

## Injeção de Dependência

Uma classe se relacionando com a outra a partir de nosso método construtor

### Projetos Práticos

#### 1. DIP (Dependency Inversion Principle) completo
- injecao-de-dependencia/atividade_injecao_de_dependencia.py: simulação de um cenário real de infraestrutura, acesso de dados e regra de negócio

#### 2. Injeção de parâmetro
- injecao-de-dependencia/csv_handler.py: configuração externa simulada, sem injeção de dependência entre objetos.

#### 3. Regra de aplicação (Regra de Negócio)
- injecao-de-dependencia/injecao_de_dependencia.py: composição e injeção de dependência.



# SOLID

SOLID são princípios de Design de Software que podem tornar sua aplicação sólida, flexível e facilita a escalabilidade.


## S - Princípio de Responsabilidade Única

Este princípio sugere que devemos conter um responsável para cada ação. Em termos técnicos, temos que manter um módulo com um único modelo de negócio.

### Projeto Prático
- S\s_solid_single_responsability.py: exemplo de acúmulo de responsabilidades.


## 0 - Princípio de Open/Close

Classes devem permitir novos comportamentos por extensão, sem necessidade de modificação no código diretamente.

### Projeto Prático
- O\o_solid_openclosed: correção e extensão de comportamentos.


## L - Princípio de Substituição de Liskov

Criado por Barbara Liskov, este princípio diz que objetos de subclasses devem poder substituir objetos da classe base sem influenciar no comportamento da estrutura criada.

### Projetos Práticos
- l\l_solid_substituicao_de_liskov.py: classes mais específicas herdando de abstrações mais genéricas, mantendo o contrato definido pela classe base e utilizando exepction.

- l\l_solid2.py: exemplo num ambiente simulado de BD.

## I - Principio de Segregação das Interfaces

Classes que não devem ser forçadas a depender de uma interface que não a utiliza.

### Projetos Práticos
- i\i_solid_segregacao_das_interfaces.py: aplicação incorreta e forçada de classes, utilizando abstractmethod como método facilitador.

- i\i_solid2.py: correção utilizando classes específicas para cada implementação.


## D - Principio de Inversão de Dependência

Classes/Módulos devem depender de uma interface (abstração).

### Projeto Prático
- D\d_solid_inversao_de_dependencia\: Arquivo main.py contém uma classe onde controla e amarram todas as outras implementações necessárias. Contém DIP e injeção de dependência no construtor.
# Pilares da Programação Orientada a Objeto

Na programação, existem quatro pilares importantes para o desenvolvimento em orientação a objetos que tornam o programa modular e gerenciável.

- Abstração;
- Encapsulamento;
- Herança;
- Polimorfismo.


## Abstração

Cria-se elementos abstratos onde passarão determinados métodos e serão instanciados determinados objetos, conforme o elemento. Um caso mais comum desse conceito é o de **Interface**.

### Projetos Práticos

#### 1. Herança de Classe
- classe-abstrata\classe_abstrata.py: Herda da classe pai atributos e métodos para que haja o reaproveitamento na classe filha.

#### 2. Interface em Python
- interfaces\interfaces.py: Simula a implementação de interface (contrato de comportamento de classes concretas) a partir de classes e métodos abstratos.


## Encapsulamento

O que queremos manter privado e público dentro da classe (proteção de dados).

### Projetos Práticos

#### 1. Encapsulamento Protegido
- encapsulamento-protegido\encapsulamento.py: Encapsulamento com herança utilizando função super para executar métodos da classe pai.
- encapsulamento-protegido2\encapsulamento2.py: Encapsulamento com herança utilizando função super para executar métodos da classe pai, com exceção de métodos privados.

#### 2. Get Set
- getset\getset.py: acesso de métodos como se fosse atributo a partir do uso de @property.

#### 3. Metodo Privado
- dado-privado\private_method.py: operação interna da classe que "esconde" detalhes de implementação
- simulate-bd\encapsulamento.py: Encapsulamento sem restrição tratando dicionário como base de dados pública.


## Herança

Uma classe que herda características da outra.

### Projeto Prático

#### 1. Herança
- HERANCA\herancas.py: reutilização de atributos e métodos de classe pai para classe filha.


## Polimorfismo

Mesmo método/função se comportando de forma diferente. É uma flexibilização de comportamento.

### Projeto Prático

#### 1. Polimorfismo
- POLIMORFISMO\polimorfismo.py: objetos diferentes respondendo ao mesmo método com implementações diferentes.

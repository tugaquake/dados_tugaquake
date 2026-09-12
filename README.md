# Dados TugaQuake
Repositório que aloja as APIs e RSSs do TugaQuake.

## Estrutura dos Dados

### alertas.json

Contém os alertas emitidos pelo TugaQuake.

#### Formato:

[
  {
    "hora": "",
    "titulo": "",
    "mensagem": "",
    "zona": "",
    "canal": ""
  }
]

#### Feed: https://tugaquake.github.io/dados_tugaquake/alertas.json

### alertas.xml

Adaptação do ficheiro JSON para RSS.

#### Feed: https://tugaquake.github.io/dados_tugaquake/alertas.xml

#### Página associada: https://tugaquake0.wordpress.com/alertas/

## Utilização

Os dados podem ser utilizados por aplicações, websites, bots e outras ferramentas que pretendam consultar ou distribuir informação disponibilizada pelo TugaQuake.
A estrutura dos dados deve ser respeitada para garantir compatibilidade com os consumidores da API.

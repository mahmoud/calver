---
title: Controle de versão do calendário
entry_root: overview_pt_br
publish_date: July 1, 2019
orig_publish_date: March 25, 2016
---

*CalVer é uma convenção de versionamento baseada no lançamento do seu projeto conforme o calendário, em vez de números arbitrários.*

**O versionamento fica melhor com o tempo.**

Para mantenedores, o versionamento nos permite especificar dependências precisas dentro de um ecossistema em constante expansão. Para vendedores e promotores, a versão do projeto é uma parte dinâmica de uma marca. Para todos nós, o versionamento nos permite fazer referência ao passado enquanto atualizamos para o futuro.

Projetos diferentes usam sistemas diferentes para controle de versão, mas
práticas surgiram. Por exemplo, números separados por pontos (por exemplo,
*3.1.4*) são praticamente dados. Outro padrão de versionamento comum
incorpora um elemento baseado no tempo, geralmente parte da data de lançamento.

Essa abordagem baseada em data passou a ser chamada de Versionamento de Calendário, ou **CalVer** para abreviar.

[TOC]

# Esquema

Existem vários esquemas de versionamento de calendário, muito usados por projetos grandes e pequenos. Em vez de declarar um único esquema como CalVer, é importante reconhecer a praticidade de cada um e [projetar o esquema](http://sedimental.org/designing_a_version.html) (Inglês) para se adequar ao projeto. Primeiro, as partes da versão:

* **Major** - O primeiro número da versão. 2 e 3 são as famosas versões principais do Python. O segmento _major_ é o componente baseado em calendário mais comum.
* **Minor** - O Segundo número da versão. 7 é a versão secundária mais popular do Python.
* **Micro** - O terceiro e geralmente último número da versão. Às vezes
   referido como o segmento "patch".
* **Modifier** - Uma tag de texto opcional, como "dev", "alpha", "beta",
   "rc1" e assim por diante.

A grande maioria dos identificadores de versão modernos são compostos por dois ou três segmentos numéricos, mais o modificador opcional. A convenção
sugere que versões de quatro segmentos numéricos sejam desencorajadas.

[Projetando uma versão](http://sedimental.org/designing_a_version.html) (Inglês)

Como veremos nos Estudos de caso abaixo, projetos têm
encontrado mais de uma maneira útil de aproveitar as datas em suas
versões. Em vez de escolher um único esquema, o CalVer apresenta
terminologia padrão para desenvolvedores, além de versões "semânticas":

* **`YYYY`** - Ano completo - 2006, 2016, 2106
* **`YY`** - Ano curto - 6, 16, 106
* **`0Y`** - Ano preenchido com zeros - 06, 16, 106
* **`MM`** - Mês curto - 1, 2 ... 11, 12
* **`0M`** - Mês preenchido com zeros - 01, 02 ... 11, 12
* **`WW`** - Semana curta (desde o início do ano) - 1, 2, 33, 52
* **`0W`** - Semana preenchida com zeros - 01, 02, 33, 52
* **`DD`** - Dia curto - 1, 2 ... 30, 31
* **`0D`** - Dia preenchido com zeros - 01, 02 ... 30, 31

Note que os números de versão incrementados tradicionalmente são baseados em 0, enquanto os segmentos de data são baseados em 1 e os anos curtos e preenchidos com zeros são relativos ao ano 2000. Observe também que o uso de semanas é geralmente mutuamente exclusiva com meses/dias.

O [Calendário Gregoriano](https://pt.wikipedia.org/wiki/Calend%C3%A1rio_gregoriano) é assumido, assim como a convenção
de [UTC](https://pt.wikipedia.org/wiki/Tempo_Universal_Coordenado). Tecnicamente, qualquer calendário pode ser usado, desde que os projetos indique qual deles.

[gregorian]: https://pt.wikipedia.org/wiki/Calend%C3%A1rio_gregoriano
[utc]: https://pt.wikipedia.org/wiki/Tempo_Universal_Coordenado

# Estudos de caso

CalVer tem alguns usuários. Estes projetos foram selecionados por sua notabilidade e variadede de casos de uso.

## Ubuntu

<img src="https://img.shields.io/badge/calver-YY.0M.MICRO-22bfda.svg" />

**[Ubuntu](http://www.ubuntu.com/)**, um dos mais proeminentes sistemas operacionais baseados em Linux disponíveis, usa um esquema CalVer de três segmentos, com ano curto e mês preenchido com zeros. Tem feito isso
[desde o início](https://en.wikipedia.org/wiki/List_of_Ubuntu_releases), em Outubro de 2004, tornando 4.10 a primeira versão geral do Ubuntu.

Mesmo um sistema operacional simples envolve muitas, muitas partes, tornando difícil comunicar muito significado com um número arbitrário. Datando lançamentos do projeto, a versão baseada em calendário é muito mais do que um número arbitrário, comunicando informações úteis que são enraizadas em um dado simples.

O Ubuntu obtém benefícios adicionais de seu esquema CalVer, ao
integra-lo com seu cronograma de suporte. O Ubuntu atualmente tem
períodos de suporte de cinco anos para seus lançamentos de suporte de longo prazo (LTS), e apenas 9 meses para versões não LTS. Graças ao CalVer e matemática elementar, qualquer usuário pode facilmente determinar se sua a versão ainda é suportada. A versão atual do LTS no momento da escrita, 16.04, terá suporte até abril de 2021.

[ubuntu]: http://www.ubuntu.com/
[ubuntu_releases]: https://en.wikipedia.org/wiki/List_of_Ubuntu_releases

## Twisted

<img src="https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg" />

**[Twisted][twisted]**, o venerado framework Python execução assíncrona de rede, usa um esquema CalVer de três segmentos, com um ano curto na versão _major_, mês curto na versão _minor_ e _micro/patch_ na terceira e última posição.

Lançado pela primeira vez em 2002 e ainda desenvolvido ativamente hoje, Twisted é uma biblioteca [madura](https://en.wikipedia.org/wiki/Twisted_(software)) que cresceu para corresponder ao seu grande escopo. Ele apresenta tudo, desde um cliente IRC até um servidor HTTP e
uma série de utilitários para programação concorrente. Como um sistema operacional, o Twisted tem muitas peças, tornando o SemVer um encaixe inadequado devido as partes individuais depreciando e quebrando a compatibilidade individualmente.

As partes não obsoletas do Twisted são compatíveis com versões anteriores entre cada versão sucessiva, e as alterações significativas são feitas com base no tempo, onde um ano e dois lançamentos devem se passar entre o lançamento da descontinuação da funcionalidade e remoção dela.

Seu esquema de versionamento se espalhou para projetos relacionados, incluíndo, [Klein](https://github.com/twisted/klein), [Treq](https://github.com/twisted/treq), e até mesmo uma das dependências do Twisted, [PyOpenSSL](https://github.com/pyca/pyopenssl).

[twisted]: https://twistedmatrix.com
[twisted_wp]: https://en.wikipedia.org/wiki/Twisted_%28software%29
[klein]: https://github.com/twisted/klein
[treq]: https://github.com/twisted/treq
[pyopenssl]: https://github.com/pyca/pyopenssl

## youtube-dl

<img src="https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg" />

**[youtube-dl](https://youtube-dl.org/)**, o discreto aliado dos
arquivistas de mídia em todos os lugares da Internet, uses a usa um esquema CalVer de três segmentos, incluindo o ano inteiro, mês preenchido com zeros, e dia preenchido com zeros. A versão é quase totalmente orientada por calendário, exceto por um micro segmento que é adicionado em alguns contextos técnicos.

Apesar do nome, o escopo do youtube-dl é expansivo. Ele suporta extrair áudio e vídeo de uma lista longa e cada vez maior de sites. Considere o rápido ciclo de lançamento de serviços suportados, e fica claro por que o projeto adotou o CalVer com tanto grau de sucesso.

[youtube-dl]: https://youtube-dl.org/

## pytz

<img src="https://img.shields.io/badge/calver-YYYY.MINOR-22bfda.svg" />

**[pytz](https://pypi.python.org/pypi/pytz)** é a tradução Python do
[banco de dados de fuso horários do IANA/Olson](https://www.iana.org/time-zones), o banco de dados por trás da precisão de tempo para todo o mundo da informática. pytz usa um esquema CalVer de dois segmentos, incluindo ano completo e versão secundária.

Embora Python tenha um histórico de arquitetura "baterias inclusas", e
o módulo _datetime_ menciona frequentemente fusos horários, o _runtime core_ do Python não inclui informações de fuso horário. Isto é porque as atualizações de fuso horário não seguem um cronograma fixo e estão sujeitas a política e capricho legislativo. O CalVer oferece um retrato com data-estampada de um sistema caótico.

[pytz]: https://pypi.python.org/pypi/pytz
[iana_tz]: https://www.iana.org/time-zones

## Teradata

<img src="https://img.shields.io/badge/calver-YY.MM.MINOR.MICRO-22bfda.svg" />

O **[Teradata UDA client](https://pypi.python.org/pypi/teradata)** prove [acesso de próxima geração](https://developer.teradata.com/tools/reference/teradata-python-module) para tecnologias de armazenamento de dados para a [Teradata](http://www.teradata.com/)

O uso do Teradata é notável não pelo destaque da tecnologia
ou empresa, mas porque houve vários lançamentos em 2016
que foram versionados como `15.10`. Isso pode parecer complicado no início, mas o significado e a utilidade são claros.

Os mantenedores da biblioteca criaram um híbrido engenhoso de
[versionamento semântico](https://semver.org/lang/pt-BR/) e CalVer. A parte da versão **YY.MM** é usada como uma versão _major_ combinada do SemVer. Que
é, para novos lançamentos, a API da biblioteca permanece a mesma
deste que foi criada em outubro de 2015. O código dependente escrito desde então é seguro para atualizar.  Veremos os segmentos do ano e do mês atualizados na próxima vez que houver uma alteração significativa na API.

[teradata]: http://www.teradata.com/
[teradata_uda]: https://pypi.python.org/pypi/teradata
[uda_blog]: https://developer.teradata.com/tools/reference/teradata-python-module
[semver]: http://semver.org/

## Outros projetos notáveis

* [Unity](https://unity3d.com/unity/whats-new/) - **`YYYY.MINOR.MICRO`** - Engine de jogos multiplataforma.
* [pip](https://pip.pypa.io/en/stable/news/) - **`YY.MINOR.MICRO`** - Gerenciador de pacotes oficial do Python.
* [PyCharm](https://www.jetbrains.com/pycharm/download/) - **`YYYY.MINOR.MICRO`** - A IDE líder do Python.
* [OpenSCAD](http://www.openscad.org/) - **`YYYY.0M`** - O programa _open-source_ para  modelagem CAD 3D sólida.
* [fusefs-ntfs](http://www.freshports.org/sysutils/fusefs-ntfs) - **`YYYY.MM.DD_MICRO`** - Uma das mais antigas e mais multiplataforma camadas de acesso NTFS para Unix
  systems.
* [certifi](https://pypi.python.org/pypi/certifi) - **`YYYY.MM.DD`** - certifi é o empacotador ao redor do pacote autoridade certificadora da Mozilla, usada para comunicação segura da Internet. Similar ao [pytz](https://calver.org/#pytz), atualizações de certificados não seguem um cronograma fixo, mas temporal, atualizações datáveis são críticas para a segurança.
* [boltons](http://boltons.readthedocs.io/en/latest/) - **`YY.MINOR.MICRO`** - Uma ampla biblioteca de
   utilitários que complementam a biblioteca _standard_ do Python.

[unity]: https://unity3d.com/unity/whats-new/
[pycharm]: https://www.jetbrains.com/pycharm/download/
[fusefs-ntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[openscad]: http://www.openscad.org/
[certifi]: https://pypi.python.org/pypi/certifi
[boltons]: http://boltons.readthedocs.io/en/latest/
[pip]: https://pip.pypa.io/en/stable/news/


Veja a [Página de usuários](https://calver.org/users.html) para uma lista crescente de usuários CalVer.

[users]: /users.html

# Quando utilizar o CalVer

Se você e pessoas que você não conhece levam seu projeto a sério, então
use uma versão séria. Felizmente, a decisão de usar o CalVer para essa versão é mais fácil do que nunca:

* Seu projeto apresenta um escopo grande ou em constante mudança??
    * Grandes sistemas e _frameworks_, como [Ubuntu](#ubuntu) e [Twisted](#twisted).
    * Conjuntos de utilitários, como [Boltons](https://calver.org/#other_notable_projects).
* O seu projeto é sensível-ao-tempo de alguma forma? Outras mudanças externas impulsionam novos lançamentos do projeto?
    * Requisitos de negócio, como o foco do [Ubuntu](https://calver.org/#ubuntu) em cronogramas de suporte.
    * Atualizações de segurança, como a necessidade de atualização dos certificados do [certifi](https://calver.org/#other_notable_projects).
    * Mudanças políticas, como a manipulação de mudanças em fuso horário do [pytz](https://calver.org/#pytz).

Se você respondeu sim a alguma dessas perguntas, a semântica do CalVer torna ele uma forte escolha para o seu projeto.
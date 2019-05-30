## Birdie.


#### Ideia de Arquitetura.
https://drive.google.com/file/d/1DymhBkbRj5sEYyVQhTXworuzvgip0dd6/view?usp=sharing


### Instruções de Execução e instalação de componentes.


##### Dockers:
1 - Criação de tag de comunicação entre os os dockers `--net=ponte`
``` sh
$ sudo docker network create ponte
```
**Obs:** Você pode exibir a rede criada através **sudo docker network list**

2 - Docker Spark + Python 3+ (ele irá mapear seu diretório home em /work).
 ```sh 
$ sudo docker run --rm -p 10000:8888 --net=ponte --link elasticsearch:elasticsearch --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v "$PWD":/home/jovyan/work jupyter/all-spark-notebook
```
**Obs:** após startado acessar `http://127.0.0.1:10000/lab?`
Sera necessario informar o token de autenticação que será exibido no **terminal**

3 - Docker Elasticsearch.
```sh
$ sudo docker run --rm --name elasticsearch -p 9200:9200 -p 9300:9300 --net=ponte -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.2
```
4 - Docker Kibana.
```sh
$ sudo docker run --name kibana -p 5601:5601 --net=ponte --link elasticsearch:elasticsearch -e "ELASTICSEARCH_URL=http://elasticsearch:9200" docker.elastic.co/kibana/kibana:6.2.2
```
Obs: A criação da network se dá, para comunicação entre os containeres.

#### Pré-Processamento e Execução.

As bases utilizadas foram:

**1 -** Base core, com ID, titulos, textos e URL.
http://download.wikimedia.org/enwiki/20190520/enwiki-20190520-abstract.xml.gz

Arquivos json gerados através do código open source: http://medialab.di.unipi.it/wiki/Wikipedia_Extractor
Fonte: [AQUI!](https://drive.google.com/open?id=1WKDYDpFYMVpXSS-DudAnYqq40P2QeS4R)

O projeto compartilhado me auxiliou na geração do arquivos semi estruturados **json**, o arquivo original é zipado e encontrasse em **xml**.
O comando utilizado para extração foi:
```ssh
 $ WikiExtractor.py -b 10G --sections --json -o "/media/murillo-silva/Novo volume/files_xml/enwiki_latest_pages_articles_files" enwiki-latest-pages-articles.xml
```
O resultante desse processamento foi os dois arquivos **.json** encontrado na pasta [GDrive](https://drive.google.com/open?id=1CtaPHEBkNERNd15zrVFXH3A63EHCbIHB)(`wiki_00.json e wiki_01.json`)

**2 -** Base auxiliar de categorias.
http://download.wikimedia.org/enwiki/20190520/enwiki-20190520-category.sql.gz
O dump foi lido em docker mysql local, e posteriormente gerado arquivo **.csv**.
O resultante desse processamento encontrasse na pasta [Gdrive](https://drive.google.com/open?id=1izPzUjrwJIFmw9iUKjRhXD42bD4sz5v4)

**3 -** A partir do pré processamento dos dados gerados em **json** e **csv**, iniciei o trabalho de analise por amostragem, e depois todos os conteudos: etapas **1 - Articles dataset** e **2 - Category dataset** em `Processamento-Wiki.ipynb`

**4 -** Após trabalho de deduplicação e leitura dos dados, foi relacionado os dataset **base core(artigos)** e **category**, gerando um dataset unico em **json** que pode ser encontrado [AQUI](https://drive.google.com/open?id=1x5OTXJgNkyOsiMqAH45Bpt7105dlwpkJ).

**5 -** Em seguida foi realizado uma ingestão das informações geradas em json (diretório wiki_final) para o Elasticsearch, que pode ser verificado pelo notebook: etapa **ELSK** em `Processamento-Wiki.ipynb`

**6 -** Deixei tambem disponivel algumas formas de consultas via metodos do ELSK.


##### Considerações Finais.
Infelizmente não conclui todas as etapas do processo. Foi bem legal o desafio!!
Abraços.!

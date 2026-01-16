# OntoSite - Portal AirData Ontology

Site estatico que hospeda a documentacao publica da Ontologia AirData.

---

## Acesso

| Recurso | Link |
| :--- | :--- |
| Pagina Inicial | [ita-airdata.github.io/OntoSite](https://ita-airdata.github.io/OntoSite/) |
| Documentacao | [docs/index-pt.html](https://ita-airdata.github.io/OntoSite/docs/index-pt.html) |
| Grafo WebVOWL | [docs/webvowl/index.html](https://ita-airdata.github.io/OntoSite/docs/webvowl/index.html) |
| Changelog | [changelog.html](https://ita-airdata.github.io/OntoSite/changelog.html) |
| Estatisticas | [statistics.html](https://ita-airdata.github.io/OntoSite/statistics.html) |
| Versoes OWL | [versions.html](https://ita-airdata.github.io/OntoSite/versions.html) |

---

## Estrutura

```
OntoSite/
├── airdata-logo.png          # Logo do projeto
├── index.html                # Pagina inicial
├── development.html          # Guia de desenvolvimento
├── statistics.html           # Estatisticas da ontologia
├── statistics.json           # Dados de estatisticas
├── versions.html             # Catalogo de versoes
├── versions.json             # Dados de versoes
├── changelog.html            # Historico de mudancas
├── quality_report.html       # Relatorio de qualidade (ROBOT)
└── docs/                     # Documentacao gerada (WIDOCO)
    ├── index-pt.html         # Documentacao principal
    ├── ontology.owl          # Arquivo OWL para download
    ├── ontology.ttl          # Formato Turtle
    ├── ontology.jsonld       # Formato JSON-LD
    ├── provenance/           # Proveniencia da documentacao
    ├── resources/            # CSS/JS do WIDOCO
    └── webvowl/              # Visualizacao interativa
```

---

## Padronizacao Visual

O site utiliza cabecalho e rodape padronizados, injetados automaticamente pelo pipeline de deploy.

### Cabecalho

- Logo AirData com link para pagina inicial
- Menu de navegacao com dropdowns
- Cores institucionais do ITA (#003C7D)

### Rodape

- Nome da instituicao (ITA)
- Links para Portal AirData e GitHub
- Copyright 2026
- Barra azul inferior

---

## Geracao Automatica

Este site e gerado automaticamente pelo pipeline em `OntoDoc/`. Nao edite manualmente os arquivos HTML, pois serao sobrescritos no proximo deploy.

Para alterar o conteudo:

1. **Ontologia**: Edite o arquivo OWL em `OntoOwl/` e execute o pipeline
2. **Cabecalho/Rodape**: Edite os templates em `OntoDoc/normalize_header.py` e `normalize_footer.py`
3. **Paginas estaticas** (index, development): Podem ser editadas diretamente, mas o cabecalho/rodape serao normalizados

---

## Deploy

O deploy e feito via GitHub Pages, acionado automaticamente pelo script:

```bash
cd ../OntoDoc
./deploy_all.sh
```

---

**Instituto Tecnologico de Aeronautica (ITA)**
Projeto AirData - 2026

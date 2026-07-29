# Template — coleção «hedra edições»

Formato aparado 133 × 210 mm (`largepost`), mancha de **22 paicas**, corpo 11pt
Minion Pro, entrelinha 13,6pt (`\setSingleSpace{1.03}`), títulos em Formular,
autoria em FS Brabo Pro.

## Como usar

```sh
cp -R hedra_edicoes ../meu_livro && cd ../meu_livro
make          # gera edlab-git.sty, compila com lualatex e abre o PDF
make clean    # remove temporários
make hifens   # regera hyphenation.tex a partir do miolo (requer pyphen)
```

Depois: substitua `MUSSUMIPSUM.tex` pelo miolo, preencha `1-fronte.tex`,
`2-creditos.tex`, `3-rosto.tex` e `PRETAS.tex`, e ajuste a lista de arquivos no
alvo `hifens` do Makefile.

## Onde mexer

| arquivo | o quê |
| --- | --- |
| `LIVRO.tex` | preâmbulo: fontes, microtype, cabeços. **Não** mapeie os cortes do Minion à mão. |
| `INPUTS.tex` | ordem das partes do livro |
| `edlab-margins.sty` | formatos (`largepost` = esta coleção) |
| `edlab-penalties.sty` | penalidades, demerits, hifenação — calibrado para 22 paicas |
| `edlab-sections.sty` | estilos de parte/capítulo/seção e cabeços |
| `edlab-toc.sty` | sumário |
| `Y-publicidade.tex` + `publicidade/` | catálogo e logotipos das coleções |

Cabeço par usa `\parttitle` (definido pelo `\part`); cabeço ímpar usa
`\leftmark` (capítulo). Em livro sem `\part`, defina `\parttitle` à mão no
`LIVRO.tex`.

# Primeira diagramação

- [ ] Estruturação de níveis (Ex: Chapter)
- [ ] Tamanho e tipo da fonte
- [ ] Formato do livro
- [ ] Limpeza de arquivo (Ex: Sujeiras de conversão; negritos; etc)
- [ ] Padronização: Aspas
- [ ] Padronização: Itálicos
- [ ] Padronização: Travessão e meia risca
- [ ] Padronização: Versaletes
- [ ] Padronização: Epígrafes
- [ ] Padronização: Versos
- [ ] Padronização: Citações
- [ ] Padronização: Espaço fino
- [ ] Padronização: Pontuação das notas de rodapé (Ex: Antes ou depois da nota)
- [ ] Padronização: Reticências

# Fechamento

- [ ] Título
- [ ] Autor
- [ ] Título original
- [ ] Número da edição
- [ ] ISBN
- [ ] Ficha catalográfica
- [ ] Nomes do corpo editorial Reedições: Menção ao editorial antigo
- [ ] Nomes dos colaboradores
- [ ] Publicidade atualizada



# latex-edlab

Templates LaTeX (classe `memoir`, compilação com **LuaLaTeX**) para as coleções
da Hedra. Cada pasta é um projeto completo: copie a pasta da coleção, substitua
o miolo e rode `make`.

## Templates

| pasta | coleção | formato |
| --- | --- | --- |
| `hedra_edicoes/` | hedra edições | `largepost` — 133 × 210 mm, mancha 22 paicas, Minion Pro 11pt |
| `ayllon/` | Ayllon | `largepost` |
| `metabiblioteca/` | Metabiblioteca | `largepost` |
| `ecopolitica/` | Ecopolítica | `16x23` |
| `mundo_indigena/ensaio/` | Mundo Indígena (ensaio) | `16x23` |
| `mundo_indigena/literatura/` | Mundo Indígena (literatura) | `largepost`, Linux Libertine |
| `que_horas_sao/` | Que horas são? | `post`, SwiftNeueLTPro |
| `_outros/edlab-base-01/` | base genérica | `14x21` |
| `_outros/edlab-logos/` | logotipos de editoras parceiras | — |
| `misc/` | `edlab-boxes.sty` avulso | — |

## Uso

```sh
cp -R hedra_edicoes ../meu_livro && cd ../meu_livro
make          # gera edlab-git.sty, compila e abre o PDF
make clean    # remove temporários
```

Requer LuaLaTeX (TeX Live), `latexmk` e as fontes do projeto instaladas no
sistema (Minion Pro, Formular, FS Brabo Pro; `make fonts-update` atualiza o
cache). O alvo `hifens` (onde existir) precisa de `pip3 install pyphen`.

## Os pacotes `edlab-*`

Cada template carrega uma cópia própria dos `.sty` — não há instalação
compartilhada. Ao corrigir um deles, veja se a correção vale para as outras
coleções antes de propagar:

- `edlab-margins.sty` — formatos de papel/mancha, um `\DeclareOption` por
  formato. **Específico de coleção.**
- `edlab-sections.sty` — parte/capítulo/seção, cabeços e rodapés. Expõe
  `\parttitle` para o cabeço par. **Específico de coleção.**
- `edlab-toc.sty` — sumário. **Específico de coleção.**
- `edlab-penalties.sty` — penalidades, demerits, tolerância e hifenação.
  Tipográfico, não gráfico: em geral pode ser compartilhado entre coleções.
- `edlab-extra.sty` — epígrafe, `quote`, didascálias, `bibliohedra`.
- `edlab-footnotes.sty` — notas de rodapé (padrão Chicago) e notas de fim.
- `edlab-git.sty` — gerado pelo Makefile; carrega o hash do commit no colofão.

## Armadilhas conhecidas

- **Cortes da fonte**: use `\setmainfont[...]{Minion Pro}` e deixe o fontspec
  resolver. Mapear `UprightFont`/`ItalicFont`/… por nome legível faz o fontspec
  cair em silêncio no redondo — o livro sai inteiro sem itálico e sem negrito,
  sem nenhum aviso no log. Confira com `pdffonts LIVRO.pdf`: têm de aparecer
  `MinionPro-It`, `-Bold` e os cortes óticos.
- **`\clubpenalties` / `\widowpenalties`**: nos arrays do e-TeX o *último* valor
  se repete para todas as posições seguintes. Cada array precisa terminar em
  `0`, senão a penalidade da última posição vale para o parágrafo inteiro.
- **`\blankAteven`** só funciona depois de um `\clearpage`; sem ele o contador
  de página ainda não é o da página final.
- **`titlesec` com memoir**: a memoir avisa que não recomenda, mas `edlab-toc`
  depende de `\titleline` do titlesec. O aviso é esperado.

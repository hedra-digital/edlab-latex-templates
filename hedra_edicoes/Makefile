# A prova do livro. `make' compila, confere o log e só então abre o PDF.
#
# A conferência existe porque referência indefinida é *aviso*, não erro: o
# livro compila e sai com `??' impresso. Foi assim que dois `??' chegaram à 1ª
# edição do «Diário de um escritor» em 2015, e ninguém leu o log. Trazido do
# «Diário» ao template em 8/10/2026.

TOLERANCIA_OVERFULL = 0

# ⚠️ `-interaction=nonstopmode' não é gosto: sem ele, uma macro indefinida faz
# o lualatex PARAR e esperar resposta no terminal, e a compilação parece
# travada em vez de falhar. Foi o que aconteceu no «Diário», volume 3, em 21/9/2026, com
# um único \hl{} que a preparação trouxe e que não estava definido aqui.
all:
	git log -1 --date=short --format=format:'\newcommand{\RevisionInfo}{%h}' > edlab-git.sty
	latexmk -lualatex -interaction=nonstopmode LIVRO.tex
	$(MAKE) confere
	@if [ "`uname`" = Darwin ]; then open LIVRO.pdf; else evince LIVRO.pdf; fi

# Falha se houver referência ou citação indefinida, linha estourando a mancha
# além do tolerado, ou caractere que a fonte não tem --- este último porque
# acento escrito decomposto (o «ç» em dois pontos de código, em vez de um) cai
# no ar sem que nada falhe, e a palavra sai impressa sem acento. Relata, sem falhar, as marcas de trabalho que ainda
# esperam resposta --- no fechamento elas têm de dar zero.
confere:
	@erro=0; \
	n=`grep -c 'Reference .* undefined' LIVRO.log || true`; \
	if [ "$$n" -gt 0 ]; then echo "✗ $$n referência(s) indefinida(s) --- sai '??' impresso:"; \
	  grep 'Reference .* undefined' LIVRO.log | sed 's/^/    /'; erro=1; fi; \
	n=`grep -c 'Citation .* undefined' LIVRO.log || true`; \
	if [ "$$n" -gt 0 ]; then echo "✗ $$n citação(ões) indefinida(s)"; erro=1; fi; \
	n=`grep -c 'Overfull \\\\hbox' LIVRO.log || true`; \
	if [ "$$n" -gt $(TOLERANCIA_OVERFULL) ]; then \
	  echo "✗ $$n linha(s) estourando a mancha (tolerado: $(TOLERANCIA_OVERFULL))"; \
	  grep 'Overfull \\hbox' LIVRO.log | head -20 | sed 's/^/    /'; erro=1; fi; \
	n=`grep -c '^!' LIVRO.log || true`; \
	if [ "$$n" -gt 0 ]; then echo "✗ $$n erro(s) de compilação"; erro=1; fi; \
	n=`grep -c 'Missing character' LIVRO.log || true`; \
	if [ "$$n" -gt 0 ]; then echo "✗ $$n caractere(s) que a fonte não tem --- somem impressos:"; \
	  grep -o 'Missing character: There is no .\{0,12\}' LIVRO.log | sort -u | sed 's/^/    /'; erro=1; fi; \
	m=`sed 's/^[[:space:]]*%.*//' *.tex | grep -o '\\\\hl{' | wc -l | tr -d ' '`; \
	if [ "$$m" -gt 0 ]; then echo "· $$m marca(s) de trabalho \\hl{} à espera de resposta"; fi; \
	if [ "$$erro" -eq 0 ]; then echo "✓ log limpo"; else exit 1; fi

clean:
	-rm *aux *log *tui *toc *.4ct *.4tc *.html *.css *.dvi *.epub *.lg *.ncx *.xref *.tmp *.idv *.opf LIVRO.pdf *.fdb_latexmk *.fls
fonts-update:
	fc-cache -f -v

# Regera hyphenation.tex a partir do miolo (evita quebra de encontros
# vocálicos). Requer: pip3 install pyphen. Ajuste a lista de arquivos do miolo.
hifens:
	cat MUSSUMIPSUM.tex > .miolo-tmp.tex
	python3 hifens.py .miolo-tmp.tex
	-rm .miolo-tmp.tex

.PHONY: all confere clean fonts-update hifens

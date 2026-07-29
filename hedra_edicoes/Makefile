all:
	git log -1 --date=short --format=format:'\newcommand{\RevisionInfo}{%h}' > edlab-git.sty
	latexmk -lualatex LIVRO.tex   # compilador
#	evince LIVRO.pdf			  # linux: leitor de PDF
	open   LIVRO.pdf              # mac: leitor PDF
clean:
	-rm *aux *log *tui *toc *.4ct *.4tc *.html *.css *.dvi *.epub *.lg *.ncx *.xref *.tmp *.idv *.opf  LIVRO.pdf *.fdb_latexmk *.fls
fonts-update:
	fc-cache -f -v
# Regera hyphenation.tex a partir do miolo (evita quebra de encontros
# vocálicos). Requer: pip3 install pyphen. Ajuste a lista de arquivos do miolo.
hifens:
	cat MUSSUMIPSUM.tex > .miolo-tmp.tex
	python3 hifens.py .miolo-tmp.tex
	-rm .miolo-tmp.tex

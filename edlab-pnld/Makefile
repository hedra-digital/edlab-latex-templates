all:
	git log -1 --date=short --format=format:'\newcommand{\RevisionInfo}{%h}' > edlab-git.sty
	latexmk -lualatex LIVRO.tex   # compilador
	evince LIVRO.pdf	      # linux: leitor de PDF
	open   LIVRO.pdf              # mac: leitor PDF

html-lp:
	make4ht -x -d html-LP index-LP.tex
	thunar index-LP.html

html-le:
	make4ht -x -d html-LE index-LE.tex
	thunar index-LE.html

clean:
	-rm *aux *log *tui *toc *.4ct *.4tc *.html *.css *.dvi *.epub *.lg *.ncx *.xref *.tmp *.idv *.opf  LIVRO.pdf *.fdb_latexmk *.fls *.png *.html
fonts-update:
	fc-cache -f -v
pandoc:
	-pandoc -r markdown-auto_identifiers -w latex --top-level-division=part $(file).md -o $(file).tex

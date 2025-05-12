

# Estrutura dos arquivos

```sh
README.md  # Manual dos arquivos
LIVRO.tex  # Preâmbulos (classe, pacotes, comandos exporáticos; referência a outros arquivos)
	 |
	INPUTS.tex
		 |
		1.fronte.tex       		# [Frontistício]
		2-creditos.tex     		# [Créditos]
		3-rosto.tex     		# [folha de rosto]
		ARQUIVO_DE_TEXTO_A.tex		# Qualquer arquivo
		ARQUIVO_DE_TEXTO_B.tex
		ARQUIVO_DE_TEXTO_C.tex
		ARQUIVO_DE_TEXTO_D.tex
		[MUSSUMIPSUM.tex]		# Arquivo LIPSUM genérico 
		Y-Publicidade.tex	   	# [lista de livros publicados]
		Z-Colofon.tex   		# [colofon]

image.png		# imagem modelo
edlab-extra.sty 	# miscelânia de comandos e ajustes
edlab-footnotes.sty	# definições sobre notas
edlab-git.sty		# falso pacote .sty. arquivo temporário para guardar git ID
edlab-margins.sty	# dimensões do livro
edlab-penalties		# penalidades para ajustes da mancha de texto
edlab-sections.sty	# formatação de seções e cabeço
edlab-toc.sty		# formatação do sumário
Makefile 		# atalhos de comando. Ex: make; make clean
.gitignore 		# lista de arquivos ou tipos de arquivos que não vão subir para o github
gitrevisioninfo.sty 	# arquivo criado automaticamente com o número do git
```

# Vídeos

## Tópico: LaTeX: Formatações básicas (memoir)
```
Data: 30 abr. 2021 12:13 da tarde São Paulo

Gravação da reunião:
https://us02web.zoom.us/rec/share/m2gXTRsFztetm_gNDZxRDvDVBRzhwsfPY-gkaANlL_cItw_5oIVAvfuWOk50KzON.7J_RWMmOxC_KzXrP

Senha de acesso: !!!LaTeX!!13
```
**Resumo**: montei a estrutura de alguns tipos de poemas para explicar como fazer pesquisa e usar manuais.
* 0'-22' Poemas, verso livre, uso do texdoc (manual), ativando pacotes 

## Topic: LaTeX: Estruturando arquivos
```
Start Time : May 5, 2021 03:03 PM

Meeting Recording:
https://us02web.zoom.us/rec/share/XtPWr6SFd7RqY5HHb6G3j9UOm7aflMXc8gXEEWYYF7jEgM3grFpFI3rOpNQzHO4R.fqfsZGudCtkACdUN

Access Passcode: !!!LaTeX13!!
```

## Topic: LaTeX: Partes do livro; Entendendo arquivos
```
Date: May 7, 2021 12:28 PM Sao Paulo

Meeting Recording:
https://us02web.zoom.us/rec/share/N0OXQujQ2-Pso_AfLFK1pBkqPQcISqC1Pa7BMvD2OfKlS8sWKcyTmuCZOuLWCtM6.2aaCN4-f1xeHPQDX

Access Passcode: !!!LaTeT!!13
```

## Topic: LaTeX: Apresentação da Nova Classe EdLab
```
Date: May 10, 2021 12:47 PM Sao Paulo

Meeting Recording:
https://us02web.zoom.us/rec/share/CMw7woaCMesZXFTMoQtO4iCtPvs9VLvyo79kROFnSUnzz0agAJHx9DXNv3vcn1S8.yPsNtIJlTm3ssjFs

Access Passcode: !!!LaTeX!!13
```

----

## Tips

```sh
# Remove os links internos e fixa \part como a primeira categoria de seções
$ pandoc -r markdown-auto_identifiers -w latex --top-level-division=part A.md -o A.tex
```

----

## Etapas para diagramar um livro do zero a partir de um template (classe)

1. Ter em mãos o template
1. Vefiricar se o template está rodando na sua máquina
1. Copiar a pasta nova
1. Iniar o git (git init)
1. Criar um projeto no github
1. Comitar e dar push
1. Converter os originais para .md e editar com pandoc
1. Converter os mds (markdowns) para LaTeX com pandoc  (lembrar de coloar "--top-level-division=chapter")
1. Editar o arquivo INPUTS.tex para apontar o novo arquivo (lembre-se de tirar o MUSSUMIPSUM)
1. Rodar/Compilar o LaTeX
1. (Não está rodando?) Debugar (colocar apenas uma parte do texto e ver se funciona)
1. Comitar e dar push
1. Editar as primeiras e últimas páginas 

## Ferramentas e conhecimentos básicos básicos

```
Ferramentas utilizadas para edição em LaTeX
	LaTeX (Linguagem de markup. Ex: Markdown, CSS)
		Texlive (Linux; Mac)
		??? (Mac)
	Editor de texto 
		Sublime (Linux)
		Hyper (Mac)
	Instalador de software
		aptget (Linux) 
		brew (Mac)
	Versificador de código
		git (Linux; Mac)
		github (repositório na web)
		gitkraken (visualizador gráfico)
	Leitor de PDF
		Acrobat
		evince (Linux)
	Comparar versões
		meld (Linux; Mac) para código
		diffpdf (Linux) para pdf

Conhecimento básico
	Navegação em terminal de comando
		~   	\home
		cd  	change directory
		mkdir 	make directory
		cd ..	pula para o diretório anterior
		cd ~ 	pula para a home
		pwd 	onde estou?
		cp 		copiar arquivo cp A B (renomear) cp A ~/Desktop (mover)
		ls 		lista os arquivos que estão na pasta

	Git (versificador)
		comandos básicos
			git init 					começar a gravar as versões 
			git clone					clonar um projeto do github
			git add						colocar a versão no envelope
			git commit -m "mensagem"	colar uma etiqueta com o nome da revisão
			git push					enviar para o github o texto
			git pull					puxar o texto atualizado 
```

	

## Como enviar arquivos para revisão externa?

* Verificar se o arquivo está compilando
* Atualizar repositório  (`git add . & git commit -m "<mensagem>" & git push`)
* Converter arquivo para revisão em dois formatos
```
pandoc TEXTO.tex -o review/TEXTO.md
pandoc TEXTO.tex -o review/TEXTO.docx
```
* Atualizar repositório novamente (`git add . & git commit -m "preparando arquivos para revisão externa de <Fulano>" & git push`)

## Como receber arquivos de revisão externa?
* Gravar o arquivo .docx exatamente com o mesmo nome
* Converter de .docx para markdown 
* Atualizar repositório (`git add . & git commit -m "revisão externa recebida de <Fulano>" & git push`)
```
pandoc arquivoentreguepeloautor.docx -o original.md
```
* Comparar o .md enviado para o revisor com o .md que chegou pelo git diff ou diretamente no github 
* Se houver alguma modificação no .md, gravar e atualizar repositório
* Após aprovação, converter para ./review/TEXTO.tex e comaparar com a versão em diagramção (../TEXTO.tex)
```
meld TEXTO.tex ../TEXTO.tex
```
* Após comparação de arquivo, atualizar repositório (`git add . & git commit -m "revisão de <Fulano> incorporada" & git push`)
* Bater emendas no github.
import re
import sys
import pyphen
import os

def gerar_hifenizacao_definitiva(arquivo_entrada):
    # Dicionário do Pyphen
    dic = pyphen.Pyphen(lang='pt_BR')

    # Usamos apenas minúsculas aqui, pois o pyphen receberá tudo em minúsculo
    vogais = 'aeiouáàãâéêíóõôúü'
    regex_vogais = f'[{vogais}]'
    
    # Regex para detectar 2 ou mais vogais juntas
    regex_encontro = re.compile(f'{regex_vogais}{{2,}}') 
    
    # Regex para extrair as palavras (inclui acentos, ignora números/pontuação)
    regex_palavra = re.compile(r'\b[a-zA-ZÀ-ÖØ-öø-ÿ]+\b')

    # 1. Leitura do arquivo
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            texto = f.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
        sys.exit(1)

    # 2. Limpeza TeX Segura
    # Remove apenas as barras e nomes de comandos, mas MANTÉM o texto das chaves
    texto_limpo = re.sub(r'\\[a-zA-Z]+', ' ', texto)
    texto_limpo = texto_limpo.replace('{', ' ').replace('}', ' ')

    # 3. Extração das palavras preservando o Case original
    palavras_originais = set(regex_palavra.findall(texto_limpo))
    hifenizacoes_finais = set()

    for palavra in palavras_originais:
        palavra_lower = palavra.lower()
        
        # Filtra palavras com encontros vocálicos e tamanho maior que 3
        if regex_encontro.search(palavra_lower) and len(palavra) > 3:
            
            # Hifeniza usando a versão minúscula (onde o pyphen brilha)
            hifenizada_lower = dic.inserted(palavra_lower)

            # Remove hífen apenas se estiver entre duas vogais
            padrao_remover = f'(?<={regex_vogais})-(?={regex_vogais})'
            hifenizada_custom_lower = re.sub(padrao_remover, '', hifenizada_lower)

            # 4. RECONSTRUÇÃO DA CAPITALIZAÇÃO (A mágica do seu script)
            resultado_final = []
            idx_original = 0
            
            for char in hifenizada_custom_lower:
                if char == '-':
                    resultado_final.append('-')
                else:
                    if idx_original < len(palavra):
                        if palavra[idx_original].isupper():
                            resultado_final.append(char.upper())
                        else:
                            resultado_final.append(char)
                        idx_original += 1
                    else:
                        resultado_final.append(char)
            
            palavra_final = "".join(resultado_final)

            # 5. Adiciona à lista final se houve modificação útil
            if palavra_final != palavra:
                hifenizacoes_finais.add(palavra_final)
            elif '-' not in hifenizada_custom_lower and '-' in hifenizada_lower:
                # Caso a palavra seja pequena (ex: ideia) e tenha perdido todos os hifens
                # Adicionamos a palavra inteira para o LaTeX nunca quebrá-la
                hifenizacoes_finais.add(palavra)

    # 6. Geração do arquivo de saída
    nome_base, extensao = os.path.splitext(arquivo_entrada)
    arquivo_saida = f"hyphenation.tex"

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("% Lista definitiva para evitar quebra de encontros vocálicos\n")
        f.write("\\hyphenation{\n")
        for p in sorted(hifenizacoes_finais, key=str.lower):
            f.write(f"  {p}\n")
        f.write("}\n")

    print(f"Pronto! {len(hifenizacoes_finais)} palavras processadas.")
    print(f"Arquivo gerado: {arquivo_saida}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso correto: python script.py meu-arquivo.tex")
        sys.exit(1)

    arquivo = sys.argv[1]
    print(f"Analisando o arquivo: {arquivo}...")
    gerar_hifenizacao_definitiva(arquivo)
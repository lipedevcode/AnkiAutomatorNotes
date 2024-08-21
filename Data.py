print('=====================================================AnkiAutomator=====================================================')
texto_extraido = """"""

texto_extraido = texto_extraido.replace('\n', ' ').replace('●', '')
secoes_frases = texto_extraido.split('Frase')

frente = []
verso = []

for secao in secoes_frases[1:]:

    # Extrair a frase da frente e a frase do verso, identificando as linhas que contêm "Frente:" e "Verso:".
    frente_secao = secao.split("Frente:")[1].split("Verso:")[0].strip() if "Frente:" in secao else None
    verso_secao = secao.split("Verso:")[1].strip() if "Verso:" in secao else None
    # Remover os marcadores "Frente:" e "Verso:" e quaisquer espaços em branco extras das frases extraídas.
    if frente_secao:
      frente.append(frente_secao)
    if verso_secao:
      verso.append(verso_secao)

api = {}
for i in range(len(frente)):
    api[f'frase{i+1}'] = {'frente': frente[i], 'verso': verso[i]}
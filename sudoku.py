# Arquivo teste em python
# TODO adicionar a lógica para checar se o sudoku é válido ou não

def main():
    matrixNumber = int(input('Informe a quantidade de tabelas:'))
    
    if matrixNumber <= 0:
        print('-----------------------------------------------------')
        print('Quantidade de Matrizes inválida. Informe novamente...')
        print('-----------------------------------------------------')
        main()

    mensagem = ''
    for count in range(matrixNumber):
        aAux = []
        for countItemLine in range(9):
            itemsLine = input('')
            if itemsLine.strip() != '':
                splitItems = itemsLine.split(' ')
                aAux.append(splitItems)
            
        if checaListaSudoku(aAux) < 0:
            mensagem += 'Instância '+str(count + 1)+'\n'
            mensagem += 'NAO\n\n'
        else:
            mensagem += 'Instância '+str(count+1)+'\n'
            mensagem += 'SIM\n\n'
    
    print('\n\n'+mensagem)

# Função para checar se a matriz é um sudoku válido
def checaListaSudoku(lista):
    
    for posicao in range(9):
        #Verifica a validade da linha e coluna, respectivamente
        resultado_linha = valida_linha(posicao, lista)
        resultado_coluna = valida_coluna(posicao, lista)
    
        # Valores:
        #  Se resultado_linha ou resultado_coluna forem igual a zero tem valores repetidos
        #  Se resultado_linha ou resultado_coluna forem menores que zero existem valores menores que 0 e maiores que 9
        # Caso atenda uma dessas condições já lança o erro
        if (resultado_linha < 1 or resultado_coluna < 1):
            return -1
    
    resultado_quadrante = valida_quadrante(lista)
    if (resultado_quadrante < 1):
        return -1
    else:
        return 1

# Checa se a linha é válida
def valida_linha(posicao, lista):
    #seleciona a linha
    lista_temporaria = lista[posicao]
    
    #Remove todo item que estiver zerado
    lista_temporaria = list(filter(lambda a: a != 0, lista_temporaria))
 
    # Checa se existe valores menores que 0 e maiores que 9
    if any(int(i) < 0 and int(i) > 9 for i in lista_temporaria):
        print("Invalid value")
        return -1

    # Checa se existe valores respetidos
    elif len(lista_temporaria) != len(set(lista_temporaria)):
        return 0
    else:
        return 1


# Checa se a coluna é válida
def valida_coluna(posicao, lista): # Checa se a coluna é válida
    
    # Seleciona a coluna na matriz.
    lista_temporaria = [row[posicao] for row in lista]
  
    # Filtra todos os valores que são diferentes de 0
    lista_temporaria = list(filter(lambda a: a != 0, lista_temporaria))

    # Checa se tem valores menores que 0 e maiores que 9
    if any(int(i) < 0 or int(i) > 9 for i in lista_temporaria):
        print("Valor inválido. Verifique")
        return -1
    
    #Checa a existência de valores repetidos
    elif len(lista_temporaria) != len(set(lista_temporaria)):
        return 0
    else:
        return 1

#Verifica os quadrantes
def valida_quadrante(grid):
  for row in range(0, 9, 3):
      for col in range(0, 9, 3):
         lista_temporaria = []
         for linha in range(row, row+3):
            for coluna in range(col, col+3):
              if grid[linha][coluna] != 0:
                lista_temporaria.append(grid[linha][coluna])
         
         # Checa a existência de valores menores que 0 e maiores que 9 
         if any(int(i) < 0 and int(i) > 9 for i in lista_temporaria):
             print("Invalid value")
             return -1
         
         #Verifica a existência de valores repetidos
         elif len(lista_temporaria) != len(set(lista_temporaria)):
             return 0
  return 1

# Chama a função principal
if __name__ == "__main__":
    main()
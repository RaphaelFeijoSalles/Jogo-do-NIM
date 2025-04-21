def partida (): 
    n = int(input("Quantas peças? ")) 
    m = int (input("Limite de peças por jogada?" ))
    
    if n < m:
        print ("m não pode ser maior que n")
        while n < m:
            n = int(input("Quantas peças? ")) 
            m = int (input("Limite de peças por jogada?" ))
    
    Pc_ganhou = bool
    if n % (m+1) != 0:
        print ("Computador começa!")
        jogadaPc = True
        n = n - computador_escolhe_jogada(n, m)
        Pc_ganhou = True
    else:
        print("Voce começa!")
        jogadaPc = False
        n = n - usuario_escolhe_jogada(n, m)
        Pc_ganhou = False
    
    if n > 0:
        if jogadaPc == True:       
            while n > 0:
                n = n - usuario_escolhe_jogada(n, m)
                if n <= 0:
                    print ("Fim do jogo! Voce ganhou!")
                    Pc_ganhou = False
                if n > 0:
                    n = n - computador_escolhe_jogada(n, m)
                    if n <= 0:
                      print ("Fim do jogo! O computador ganhou!")      
                    Pc_ganhou = True
        
        if jogadaPc == False:
            while n > 0:
                n = n - computador_escolhe_jogada(n, m)
                if n <= 0:
                  print ("Fim do jogo! O computador ganhou!")
                  Pc_ganhou = True
                if n > 0:
                    n = n - usuario_escolhe_jogada(n, m)
                    if n <= 0:
                        print ("Fim do jogo! Voce ganhou!")
                        Pc_ganhou = False

                
    else:
        if jogadaPc == True:
            print ("Fim do jogo! O computador ganhou!")
            Pc_ganhou = True
        else:
            print ("Fim do jogo! Voce ganhou!")
            Pc_ganhou = False
    
    return Pc_ganhou
    

def usuario_escolhe_jogada (n, m):
    jogada = int (input("Quantas peças você vai tirar? "))
    if jogada > m or jogada <= 0:
        while jogada > m or jogada <= 0:
            print ("Oops! Jogada inválida! Tente de novo.")
            jogada = int (input("Quantas peças você vai tirar? "))
    
    if jogada == 1:
        print ("Voce tirou", jogada, "peça!")   
    else:
        print ("Voce tirou", jogada, "peças!")
    
    n = n - jogada
    
    if n == 1:
        print ("Agora resta", n, "peça no tabuleiro.")
    else:
        print ("Agora restam", n, "peças no tabuleiro.")
    
    return jogada
        

def computador_escolhe_jogada (n, m):
    if n == 1:
        print ('O computador tirou 1 peça.')
        print ("Agora restam 0 peças no tabuleiro.")
        jogada = 1
    
    aux = 1
    jogada = n
    n_Caso = n
    Caso = False
    if n % (m+1) == 0:
        n = n - 1
        while n % (m+1) != 0 and Caso == False:
            n = n - 1
            aux = aux + 1
            if aux > m:
                Caso = True
    
    else:
        while n % (m+1) != 0 and Caso == False:
            n = n - 1
            aux = aux + 1
            if aux > m:
                Caso = True
        
    
    if Caso == True:
        jogada = m
        n = n_Caso - jogada
    else:
        jogada = jogada - n
        n = n_Caso - jogada
        
    
    #Quando mesmo tirando M numeros o resto da divisão de N por M+1 ainda fica diferente de 0 fazemos N=N-M
    
        
    
    if jogada == 1:
        print ('O computador tirou', jogada , 'peça.')
    else:
        print ('O computador tirou', jogada , 'peças.')
    if n == 1:
        print ("Agora resta", n, "peça no tabuleiro")
    else:
        print ("Agora restam", n, "peças no tabuleiro.")
    return jogada

def campeonato():
    print ("")
    print ("Voce escolheu campeonato!")
    print ("")
    print ("**** Rodada 1 ****")
    aux = 1
    aux = partida()
    if aux == True:
        pontoPc = 1
        pontoUser = 0
    else:
        pontoUser = 1
        pontoPc = 0
    print ("")
    print ("**** Rodada 2 ****")
    print ("")
    aux = partida()
    if aux == True:
        pontoPc = pontoPc + 1
    else:
        pontoUser = pontoUser + 1
    print ("")
    print ("**** Rodada 3 ****")
    print ("")
    aux = partida()
    if aux == True:
        pontoPc = pontoPc + 1
    else:
        pontoUser = pontoUser + 1
    print ("")
    print ("**** Final do campeonato! ****")
    print ("")
    print ("Placar: Você ", pontoUser, " X ", pontoPc, " Computador")


def main ():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato")
    modo = int(input())
    while modo < 1 or modo > 2:
        modo = int(input("insira 1 para partida ou 2 para campeonato"))
    if modo == 1:
        print ("Voce escolheu uma partida!")
        partida()
    
    if modo == 2:
        campeonato()

main()

    
        






        
    
    
    
    
        
        
       
    
    
         
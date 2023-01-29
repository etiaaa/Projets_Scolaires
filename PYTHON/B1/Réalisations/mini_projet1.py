################################################################################


#Mini Projet Python:

#Nom: Sakoa
#Prenom: Etia-Anaelle


#################  On definit la fonction newBoard    ##########################


def newBoard(n):
    return [0 for i in range(n)]


#################  On definit la fonction display     ##########################


def display(board,n):

    ligne1 = ""
    ligne2 = ""

    for i in range(1,n+1):

        if i < 10: ligne2 = ligne2 + " "
        if board[i-1] < 10: ligne1 = ligne1 + " "
        ligne1 = ligne1 + "." + " "
        ligne2 = ligne2 + str(i) + " "

    print(ligne1)
    print(ligne2)


#################  On defnit la fonction set_player   ##########################


def set_player(player):
    if player == 1: player = "x"
    if player == 2: player = "o"


#################  On defnit la fonction possible   ############################


def possible(board, n, player, removed, i):
    set_player(player)
    return (board[i] == ".") and (i not in removed)


#################  On definit la fonction select    ############################


def select(board, n, player, removed):
     set_player(player)
     while True:
        i = int(input("saisir une position valide: " ))-1
        if possible(board, n, player, removed, i):
            return i


#################  On definit la fonction put       ############################


def put(board, n, player, removed, i):
    set_player(player)
    if 0 < i < n-1:
        board[i] = 1
        board[i-1] = -1
        board[i+1] = -1

    if i == 0:
        board[i]=1
        board[i+1]=-1

    if i==n-1:
        board[i]=1
        board[i-1]=-1
        return board


#################  On definit la fonction again     ############################


def again(board, n, player, removed):
    set_player(player)
    i = int(input("saisir une position valide: " ))-1
    return possible(board,n,player,removed,i)


#################  On definit la fonction win       ############################


def win(board,n):
    print("Vous avez perdu. Votre adversaire à gagner.")


#################  On definit la fonction Game      ############################


def game(board,n):
    player = 1
    while again(board,n,player,removed):
        display(board,n)
        i = select(board,n)
        put(board,n,player,removed,i)
        player = player % 2 + 1
    return win(tab,n)


#################  On definit la fonction Alak      ############################


def alak(n):
    board=newBoard
    game(board,n)


################ FIN DU JEU           #########################################
################ TESTER MES FONCTIONS #########################################

if __name__ == '__main__':

    print(newBoard(9))

    print(    )

    tab=newBoard(9)
    display(tab,9)


    print(    )


    print("Joueur 1")
    removed=[]
    print(game(tab,9))

    print(    )

#########   Je n'ai pas eu le temps de finir les tests  #######################
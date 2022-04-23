tablero=[[0,0,0],[0,0,0],[0,0,0]]
#esta el la funcion que imprime el tablero
def imprimeTablero():
    print('   0 1 2')
    print('  ------')
    for i in range(3):
        print(str(i)+'|',end=' ')
        for j in range(3):
            print(tablero[i][j],end=' ')
        print('')
    print('')
def primerLanzamiento():
    jugadorUno=input('J1 -> Escoje x/o: ')
    if jugadorUno=='x':
        print('Elejiste: x')
        return True
    elif jugadorUno=='o':
        print('Elejiste: O')
        return True
    else:
        print('No fue una opcion')
        return False
def leeCoordenadasJugador():
    try:
        x=int(input('J1 ----> Fila donde tiras: '))
        if x<3:
            print("") 
        else:
            print('existe?')
            return False
        y=int(input('J1 -> Columna donde tiras: '))
        if y<3:
            print('')
        else:
            print('existe?')
            return False    
     
    except:
        print('No es un numero')
                              
if __name__ == '__main__':
    print('Juego del gato')
    if primerLanzamiento():
        imprimeTablero()
        leeCoordenadasJugador()


from actividad2 import manejadorViajero

if __name__== '__main__':
    lista = manejadorViajero()
    lista.testViajero()
    k = input('Ingrese numero de viajero: ')
    n = lista.buscaViajero(k)
    opc = None
    if(n == None):
        print("El numero de viajero no existe.")
    else:
        while(opc != '0'):
            opc = input('''--Menu--
            1) Consultar cantidad de millas
            2) Acumular Millas
            3) Canjear millas
            0) Cerrar
            ''')
            if opc == '1':
                print("La cantidad de millas es: ",lista.getMillas(n))
            elif opc == '2':
                nuevas_millas = int(input('Ingrese la cantidad de millas nuevas: '))
                print("El total de millas es: ",lista.acumularMillas(nuevas_millas,n))
            elif opc == '3':
                cant = int(input('Ingrese cantidad de millas a canjear: '))
                lista.canjearMillas(cant,n)
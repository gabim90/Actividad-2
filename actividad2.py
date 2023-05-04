import csv
class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = None
    def __init__(self,num,dni,nom,ap,mill):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas_acum = mill
    def getNumViajero(self):
        return(self.__num_viajero)
    def getTotalMillas(self):
        return(self.__millas_acum)
    def acum_millas(self,nuevas_millas):
        self.__millas_acum=self.__millas_acum+nuevas_millas
        return(self.__millas_acum)
    def canjearMillas(self,cant):
        if(cant > self.__millas_acum):
            print("La cantidad de millas solicitas es menor a las que posee.")
        else:
            self.__millas_acum = self.__millas_acum - cant
            print("Sus millas han sido canjeadas y su total de millas acumulas es",self.__millas_acum)
        return()
    
class manejadorViajero:
    def __init__(self):
        self.__listaViajero= []
    def agregarViajero(self,unViajero):
        self.__listaViajero.append(unViajero)
    def testViajero(self):
        archivo = open('datosviajero.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            num = fila[0]
            dni = fila[1]
            nom = fila[2]
            ape = fila[3]
            mill = int(fila[4])
            unViajero = ViajeroFrecuente(num,dni,nom,ape,mill)
            self.agregarViajero(unViajero)
        archivo.close()
    def buscaViajero(self,num):
        i=0
        Retorno = None
        b = False
        while not b and i < len(self.__listaViajero):
            if self.__listaViajero[i].getNumViajero()==num:
                b =True
                Retorno=i
            else:
                i+=1
        return Retorno
    def getMillas(self,n):
        return(self.__listaViajero[n].getTotalMillas())
    def acumularMillas(self,nuevas_millas,n):
        m = self.__listaViajero[n].acumularMillas1(nuevas_millas)
        return m
    def canjearMillas(self,cant,n):
        self.__listaViajero[n].canjearMillas1(cant)
        return
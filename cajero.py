class Cajero:
    monto=0
    print('Ya has iniciado sesion como Jorge!')
    print('Hola Bienvenido a su cajero Chancholombia :)')
    def operaciones(self):
        self.opcion = int(input('''
        ------------------------------------------
        POR FAVOR INDIQUE QUE OPERACION DESEA REALIZAR.. 
        1. CONSULTAR SALDO DE CUENTA
        2. RECARGAR CUENTA
        3. ENVIAR DINERO
        4. RETIRO DE EFECTIVO
        5. RETIROS NEQUI
        6. DONACIONES
        7. SALIR'''))
        self.control=0
        while self.control==0:
            if self.opcion==1:
                self.consultasaldo()
            elif self.opcion==2:
                self.depositar()
            elif self.opcion==3:
                self.enviar()
            elif self.opcion==4:
                self.retirar()
            elif self.opcion==5:
                self.retirar_nequi()
            elif self.opcion==6:
                self.donar()
            elif self.opcion==7:
                self.control=1
                self.salir()
            else:
                print('UPS, LO SENTIMOS, ESA NO ES UNA OPCION VALIDA, RECUERDA QUE SOLO SE ADMITEN DIGITOS DEL 1 AL 7!, INTENTE DE NUEVO.. ')
                self.operaciones()

    def consultasaldo(self):
        print('SALDO DISPONIBLE: ', self.monto)
        print('QUIERE REALIZAR OTRA OPERACION?')
        self.operaciones()

    def depositar(self):
        self.deposito = int(input('INDIQUE LA CANTIDAD A RECARGAR A SU CUENTA '))
        self.monto=self.monto + self.deposito
        self.consultasaldo()

    def enviar(self):
        self.enviar = int(input('ESCRIBA EL NUMERO DE CUENTA A TRANSFERIR... '))
        self.enviar = int(input('INDIQUE LA CANTIDAD A ENVIAR.. '))
        self.control = 0
        while self.control==0:
            if self.enviar > self.monto:
                print('''UY! NO TIENES DINERO SUFICIENTE PARA CONTINUAR, POR FAVOR RECARGA TU CUENTA E INTENTALO DE NUEVO..
                --------------------------------------------------------------------------------------------------------''')
                self.enviar = int(input('INDIQUE DE NUEVO LA CANTIDAD A ENVIAR.. '))
            elif self.enviar<= self.monto:
                self.monto=self.monto-self.enviar
                self.control=1
                print('SU DINERO HA SIDO ENVIADO CON EXITO!: ', self.enviar)
                self.consultasaldo()
    def retirar(self):
        self.retiro = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
        self.control = 0
        while self.control==0:
            if self.retiro > self.monto:
                print('''LO SENTIMOS, NO TIENES DINERO SUFICIENTE PARA RETIRAR, RECARGA TU CUENTA E INTENTALO DE NUEVO..
                --------------------------------------------------------------------------------------------------------''')
                self.retiro = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
            elif self.retiro<= self.monto:
                self.monto=self.monto-self.retiro
                self.control=1
                print('DINERO RETIRADO SATISFACTORIAMENTE, HAS RETIRADO : ', self.retiro)
                self.consultasaldo()
    def retirar_nequi(self):
        self.retirar_nequi = int(input('ESCRIBA EL NUMERO DE TU TELEFONO '))
        self.retirar_nequi = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
        self.retirar_nequi = int(input('ESCRIBA EL CODIGO ENVIADO VIA SMS A SU TELEFONO PARA CONTINUAR.. '))
        self.control = 0
        while self.control==0:
            if self.retirar_nequi > self.monto:
                print('''UY! NO TIENES DINERO SUFICIENTE PARA CONTINUAR, POR FAVOR RECARGA TU CUENTA E INTENTALO DE NUEVO..
                --------------------------------------------------------------------------------------------------------''')
                self.retirar_nequi = int(input('INDIQUE DE NUEVO LA CANTIDAD A RETIRAR NEQUI.. '))
            elif self.retirar_nequi<= self.monto:
                self.monto=self.monto-self.retirar_nequi
                self.control=1
                print('SU DINERO HA SIDO RETIRADO CORRECTAMENTE!: ', self.retirar_nequi)
                self.consultasaldo()
    def donar(self):
        print('AYUDANOS CON NUESTRA CAUSA #SIALTRABAJO')
        self.donar = int(input('INDICA LA CANTIDAD A DONAR.. '))
        self.control = 0
        while self.control==0:
            if self.donar > self.monto:
                print('''UY! NO TIENES DINERO SUFICIENTE PARA CONTINUAR, POR FAVOR RECARGA TU CUENTA E INTENTALO DE NUEVO..
                --------------------------------------------------------------------------------------------------------''')
                self.donar = int(input('INDIQUE DE NUEVO LA CANTIDAD A DONAR.. '))
            elif self.donar<= self.monto:
                self.monto=self.monto-self.donar
                self.control=1
                print('MUCHAS GRACIAS POR TU DONACION Y BUEN CORAZON ', self.donar)
                self.consultasaldo()

    def salir(self):
        print('==========================================================================')
        print('MUCHAS GRACIAS POR USAR CHANCHOLOMBIA, ESPERAMOS QUE VUELVA PRONTO JORGE!')
        print(':)')
        print('==========================================================================')

ejecucion = Cajero()
ejecucion.operaciones()
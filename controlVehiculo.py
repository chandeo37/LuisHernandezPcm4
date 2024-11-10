import csv

class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, {self.velocidad} km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return  f"Marca {self.marca}, Modelo{self.modelo}, {self.num_ruedas} ruedas  {self.velocidad} km/h, {self.cilindrada} cc Puestos: {self.nro_puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc Carga: {self.peso_carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas Tipo: {self.tipo_bicicleta}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas Tipo: {self.tipo_bicicleta} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

#metodos para guardar y leer los datos en csv
def guardar_datos_csv(Vehiculo, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "a", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerow([str(Vehiculo.__class__), str(Vehiculo.__dict__)])
    except Exception as error:
        print(f"Error al guardar los datos: {error}")

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            vehiculos = {}
            for fila in archivo_csv:
                clase = fila[0]
                #convierte el string de diccionario a un diccionario real
                datos = eval(fila[1])
                if clase not in vehiculos:
                    vehiculos[clase] = []
                vehiculos[clase]. append(datos)
        return vehiculos
    except Exception as error:
        print(f"Error al leer los datos: {error}")
        return {}





def main():
    num_vehiculos = int(input("¿Cuántos vehículos desea insertar? "))
    automoviles = []

    for i in range(num_vehiculos):
        print(f"Datos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        num_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))

        automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
        automoviles.append(automovil)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, automovil in enumerate(automoviles):
        print(f"Datos del automóvil {i + 1} : {automovil.mostrar_info()}")

    particular = Particular("Ford","Fiesta",4,180,500,5)
    carga = Carga("Daft Trucks", "G 38", 10,120, 1000, 20000)
    bicicleta = Bicicleta("Shimano,", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s",2, "Deportiva", "2T", "Doble viga", 21)

    #imprimir vehiculos
    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

    # Verificar relaciones de la instancia motocicleta con las clases
    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    #guardar los vehiculos en el archivo csv
    guardar_datos_csv(particular)
    guardar_datos_csv(carga)
    guardar_datos_csv(bicicleta)
    guardar_datos_csv(motocicleta)

    #leer los vehiculos del archivo
    vehiculos_leidos = leer_datos_csv()
    #imprimir los vehiculos por categoria
    if vehiculos_leidos:
        for clase, vehiculos in vehiculos_leidos.items():
            print(f"Lista de vehiculos {clase.split('.')[-1]}:")
            for vehiculo in vehiculos:
                print(vehiculo)



if __name__ == "__main__":
    main()

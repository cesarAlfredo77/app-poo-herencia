class Vehiculo:

    def _init_(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def descripcion(self):
        return f"{self.marca}, {self.modelo}, {self.anio}"
    
    def tipo(self):
        return "Vehiculo Genérico"
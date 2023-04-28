class Cliente:
    def __init__(self,id_cliente,nombre,apellido,correo,fecha_registro ):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo=0

    def agregar_saldo(self,cantidad):
        self.__saldo+=cantidad
    
    def mostrar_saldo(self):
        return self.__saldo
        
class Producto:
    def __init__(self, SKU, nombre, categoria, proveedor, stock, valor_neto ):
        self.SKU=SKU
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
        self.__Impuesto = 1.19
 
        
class Vendedor:
    def __init__(self, RUN, nombre, apellido, seccion):
        self.RUN =RUN
        self.nombre =nombre 
        self.apellido =apellido
        self.seccion =seccion
        __comision = 0

#creación de instancias Cliente
cliente1=Cliente(1,"Goku","Gonzales","goku.g@gmail.com","01-02-2022")
cliente2=Cliente(2,"Don Ramon","Pizarro","d.ramon@gmail.com","05-04-2021")
cliente3=Cliente(3,"Pedro","perez","pe.perez@gmail.com","11-02-2020")
cliente4=Cliente(4,"Jason","Alvarez","j.alva@gmail.com","09-10-2019")
cliente5=Cliente(5,"Juan","Pinto","j.pintog@gmail.com","21-12-2020")

#creación de instancias Producto
producto1=Producto(1,"cocina","electrodomestico","Don_pepe",15,300000)
producto2=Producto(2,"celular","electrónica","Samnsung",10,120000)
producto3=Producto(3,"celular","electrónica","Lg",15,80000)
producto4=Producto(4,"papas","verdura","Don_pepe",15,800)
producto5=Producto(5,"platanos","fruta","Don_pepe",20,1200)

#creación de instancias Vendedor
vendedor1=Vendedor(1,"Pepito","Jefferson","Tech")
vendedor2=Vendedor(2,"Griffith","Eggling","Outdoor")
vendedor3=Vendedor(3,"Kike","Morande","Lenceria")
vendedor4=Vendedor(4,"Waton","Loyola","Vinos")
vendedor5=Vendedor(5,"Frank","Zappa","Guitarras")


cliente1.agregar_saldo(int(input("ingrese su saldo actual: ")))
print(f"el valor del {producto2.nombre} es de {producto2.valor_neto} ")

if producto2.valor_neto > cliente1.mostrar_saldo():
    print("no puede comprar el producto")
    print(f"necesita ${producto2.valor_neto} para  comprar este producto")
    
else:
    print (f"llamando al vendedor {vendedor4.nombre} {vendedor4.apellido}")


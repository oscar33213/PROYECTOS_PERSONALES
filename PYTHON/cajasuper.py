import tkinter as tk
from tkinter import messagebox, simpledialog
from decimal import Decimal, InvalidOperation


class Supermercado:
    def __init__(self):
        # Lista de trabajadores: {usuario: clave}
        self.trabajadores = {}
        # Diccionario de artículos: {nombre: precio}
        self.articulos = {}
        # Ventas de la sesión actual: [{articulo: precio}]
        self.ventas_sesion = []
        # Registro de todas las compras durante la sesión
        self.registro_compras = []
        # Variable que almacena el dinero actual en caja
        self.dinero_caja = Decimal("0.0")
        # Límite de dinero en caja para retirar
        self.limite_dinero = Decimal("1000.0")

    # Función para registrar un nuevo trabajador
    def crear_trabajador(self):
        usuario = simpledialog.askstring("Nuevo trabajador", "Cree un número de usuario:")
        while True:
            clave = simpledialog.askstring("Nueva clave", "Cree una clave de 4 dígitos (numérica):", show="*")
            if clave and len(clave) == 4 and clave.isdigit():
                break
            else:
                messagebox.showerror("Error", "La clave debe ser de 4 dígitos numéricos. Intente nuevamente.")
        self.trabajadores[usuario] = clave
        messagebox.showinfo("Éxito", f"Trabajador {usuario} registrado exitosamente.")
        return usuario

    # Función para iniciar sesión de trabajador y establecer el dinero en caja a 200€
    def iniciar_sesion(self, usuario):
        while True:
            clave = simpledialog.askstring("Iniciar sesión", f"Ingrese la clave para el usuario {usuario}:", show="*")
            if self.trabajadores[usuario] == clave:
                self.dinero_caja = Decimal("200.0")  # Inicializar la caja con 200€
                messagebox.showinfo("Bienvenido", f"Bienvenido, {usuario}. Dinero inicial en caja: 200.00 €.")
                return True
            else:
                messagebox.showerror("Error", "Clave incorrecta. Intente nuevamente.")

    # Función para realizar el cobro de una compra
    def realizar_cobro(self):
        total = Decimal("0.0")
        compra_actual = {}

        # Ingresar artículos para la compra
        while True:
            articulo = simpledialog.askstring("Artículos", "Ingrese el nombre del artículo (o 'salir' para terminar la compra):")
            if articulo is None or articulo.lower() == 'salir':
                if len(compra_actual) > 0:
                    # Preguntar si desea eliminar un artículo antes de finalizar la compra
                    if messagebox.askyesno("Eliminar artículos", "¿Desea eliminar un artículo de la compra?"):
                        self.eliminar_articulo(compra_actual)
                    # Preguntar si desea cancelar la compra entera antes de proceder al pago
                    if messagebox.askyesno("Cancelar compra", "¿Desea cancelar la compra completa?"):
                        self.cancelar_compra(compra_actual)
                        return  # Salir de la función si se cancela toda la compra
                break

            while True:
                try:
                    precio = Decimal(simpledialog.askstring("Precio", f"Ingrese el precio de {articulo}:"))
                    if precio <= 0:
                        messagebox.showerror("Error", "El precio debe ser mayor que cero. Intente nuevamente.")
                    else:
                        self.articulos[articulo] = precio
                        break
                except (ValueError, InvalidOperation):
                    messagebox.showerror("Error", "Precio inválido. Intente nuevamente.")

            while True:
                try:
                    cantidad = Decimal(simpledialog.askstring("Cantidad", f"Ingrese la cantidad de {articulo}:"))
                    if cantidad <= 0:
                        messagebox.showerror("Error", "La cantidad debe ser mayor que cero. Intente nuevamente.")
                    else:
                        compra_actual[articulo] = cantidad
                        break
                except (ValueError, InvalidOperation):
                    messagebox.showerror("Error", "Cantidad inválida. Intente nuevamente.")

        # Calcular el total de la compra
        for articulo, cantidad in compra_actual.items():
            precio_articulo = self.articulos[articulo] * cantidad
            total += precio_articulo
            self.ventas_sesion.append({articulo: precio_articulo})

        # Verificar si se cancela la compra completa
        if total > 0:
            self.confirmar_compra(compra_actual, total)

        # Verificar si el dinero en caja ha superado el límite
        self.verificar_dinero_caja()

    # Función para confirmar la compra antes del cobro
    def confirmar_compra(self, compra_actual, total):
        if messagebox.askyesno("Confirmar compra", f"Total a pagar: {total:.2f} €. ¿Desea continuar con el cobro?"):
            self.procesar_pago(total)
            self.registro_compras.append(compra_actual)  # Registrar la compra actual
        else:
            if messagebox.askyesno("Cancelar compra", "¿Desea cancelar la compra completa?"):
                self.ventas_sesion.pop()  # Elimina la última venta si se cancela la compra
                messagebox.showinfo("Compra cancelada", "La compra ha sido cancelada.")

    # Función para procesar el pago de la compra
    def procesar_pago(self, total):
        while True:
            try:
                pago = Decimal(simpledialog.askstring("Pago", "Ingrese el monto recibido:"))
                if pago >= total:
                    cambio = pago - total
                    self.dinero_caja += total
                    messagebox.showinfo("Pago realizado", f"Su cambio es {cambio:.2f} €.")
                    break
                else:
                    messagebox.showerror("Error", "El pago es insuficiente.")
            except (ValueError, InvalidOperation):
                messagebox.showerror("Error", "Monto inválido. Intente nuevamente.")

    # Función para verificar si se debe sacar dinero de la caja
    def verificar_dinero_caja(self):
        if self.dinero_caja >= self.limite_dinero:
            messagebox.showwarning("Advertencia", f"Dinero en caja supera los {self.limite_dinero:.2f} €. Es obligatorio retirar 150 €.")
            self.extraer_dinero_automatico(Decimal("150.00"))

    # Función para extraer dinero automáticamente
    def extraer_dinero_automatico(self, monto):
        self.dinero_caja -= monto
        # Registrar como gasto en el resumen final
        self.ventas_sesion.append({"Retiro automático": monto})
        messagebox.showinfo("Retiro realizado", f"Se han retirado {monto:.2f} €. Dinero restante en caja: {self.dinero_caja:.2f} €.")

    # Función para eliminar un artículo de la compra actual
    def eliminar_articulo(self, compra_actual):
        articulo = simpledialog.askstring("Eliminar artículo", "Ingrese el nombre del artículo que desea eliminar:")
        if articulo in compra_actual:
            del compra_actual[articulo]
            messagebox.showinfo("Eliminado", f"El artículo {articulo} ha sido eliminado de la compra.")
        else:
            messagebox.showerror("Error", f"El artículo {articulo} no se encuentra en la compra actual.")

    # Función para cancelar una compra completa antes de realizar el pago
    def cancelar_compra(self, compra_actual):
        compra_actual.clear()
        messagebox.showinfo("Compra cancelada", "Se ha cancelado la compra completa.")

    # Función para cerrar la sesión y mostrar las ventas realizadas
    def cerrar_sesion(self, usuario):
        clave = simpledialog.askstring("Cerrar sesión", "Ingrese su clave para cerrar sesión:", show="*")
        if self.trabajadores[usuario] == clave:
            resumen_ventas = f"Sesión cerrada para {usuario}. Resumen de ventas:\n"
            for compra in self.registro_compras:
                for articulo, precio in compra.items():
                    resumen_ventas += f"Artículo vendido: {articulo}, Precio: {precio:.2f} €\n"
            resumen_ventas += f"Dinero en caja al cerrar sesión: {self.dinero_caja:.2f} €"  # Mostrar dinero en caja
            messagebox.showinfo("Resumen de ventas", resumen_ventas)
            # Reiniciar ventas de la sesión
            self.ventas_sesion = []
            self.registro_compras = []
            # Aquí se destruye el programa al cerrar sesión
            app.destroy()
        else:
            messagebox.showerror("Error", "Clave incorrecta. No se pudo cerrar la sesión.")


# Clase para la interfaz gráfica
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caja del Supermercado")
        
        # Establecer tamaño de la ventana a 25% de la pantalla
        self_width = int(self.winfo_screenwidth() * 0.25)
        self_height = int(self.winfo_screenheight() * 0.25)
        self.geometry(f"{self_width}x{self_height}")

        self.supermercado = Supermercado()

        self.boton_registrar = tk.Button(self, text="Registrar Trabajador", command=self.registrar_trabajador)
        self.boton_registrar.pack(pady=5)

        self.boton_iniciar_sesion = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=5)

        self.boton_cerrar_sesion = tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.pack(pady=5)
        self.boton_cerrar_sesion.config(state="disabled")

        self.boton_realizar_cobro = tk.Button(self, text="Realizar Cobro", command=self.realizar_cobro)
        self.boton_realizar_cobro.pack(pady=5)
        self.boton_realizar_cobro.config(state="disabled")

    def registrar_trabajador(self):
        self.supermercado.crear_trabajador()

    def iniciar_sesion(self):
        usuario = simpledialog.askstring("Iniciar sesión", "Ingrese su número de usuario:")
        if usuario in self.supermercado.trabajadores:
            if self.supermercado.iniciar_sesion(usuario):
                self.boton_realizar_cobro.config(state="normal")
                self.boton_cerrar_sesion.config(state="normal")
        else:
            messagebox.showerror("Error", "Usuario no registrado.")

    def cerrar_sesion(self):
        usuario = simpledialog.askstring("Cerrar sesión", "Ingrese su número de usuario para cerrar sesión:")
        if usuario in self.supermercado.trabajadores:
            self.supermercado.cerrar_sesion(usuario)

    def realizar_cobro(self):
        self.supermercado.realizar_cobro()


if __name__ == "__main__":
    app = App()
    app.mainloop()

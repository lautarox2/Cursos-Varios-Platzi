def mayus(func):
    def envol(texto):
        return func(texto).upper()
    return envol

@mayus
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"

print(mensaje("Cesar"))
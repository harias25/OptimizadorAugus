from datetime import datetime

class Optimizacion():
    def __init__(self,regla,antes,despues,linea):
        self.regla = regla
        self.antes = antes
        self.despues = despues
        self.linea = str(linea)
        
class OptmizacionResultado():
    def __init__(self):
        self.codigo = ""
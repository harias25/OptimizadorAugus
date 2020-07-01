from Optimizador.OptimizadorAST.Instruccion import Instruccion

class Etiqueta(Instruccion):
    def __init__(self,  id, instrucciones, linea, columna):
        self.id = id
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def optmimizarCodigo(self):
        pass

    def generarAugus(self):
        pass
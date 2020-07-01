import Optimizador.grammarOptimizacion as g
import Optimizador.OptimizadorAST.Instruccion as Instruccion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion 
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion

class Optimizador():
    def __init__(self):
        self.codigoOptimizado = ""
        self.codigoAnterior = ""
        self.instrucciones = []

    def optimizar(self, ventana):
        self.codigoAnterior = ventana.editor.text()
        self.codigoOptimizado = ""
        ventana.consola.clear()
        ReporteOptimizacion.func(None, True)
        g.textoEntrada = ventana.editor.text()
        g.func(0, None)
        instrucciones = g.parse(ventana.editor.text())
        self.instrucciones = instrucciones

        bandera = False
        if(instrucciones != None):
            for func in instrucciones:
                self.codigoOptimizado += func.id+":\n"

                for ins in func.instrucciones:
                    # try:
                    self.codigoOptimizado += "    "+ins.optmimizarCodigo().codigo
                    # except:
                    #    pass

        ventana.consola.append(self.codigoOptimizado)

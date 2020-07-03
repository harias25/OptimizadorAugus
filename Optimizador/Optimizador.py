import Optimizador.grammarOptimizacion as g
import Optimizador.OptimizadorAST.Instruccion as Instruccion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion 
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion
from Optimizador.OptimizadorAST.AST import AST

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
        ast = AST(self.instrucciones)
        #PRIMERA PASADA PARA GUARDAR TODAS LAS ETIQUETAS
        if(instrucciones != None):
            for ins in instrucciones:
                try:
                    print(ins.id)
                    ast.agregarEtiqueta(ins)
                except:
                    pass

        if(instrucciones != None):
            for func in instrucciones:
                self.codigoOptimizado +=func.optmimizarCodigo(ast)
    
        ventana.consola.append(self.codigoOptimizado)

    def reporte(self):
        reporte = ReporteOptimizacion.ReporteOptimizacion()
        reporte.ReporteOptimizacion()
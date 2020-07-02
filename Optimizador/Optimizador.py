import Optimizador.grammarOptimizacion as g
import Optimizador.OptimizadorAST.Instruccion as Instruccion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion 
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion
from Optimizador.OptimizadorAST.AST import AST
from Optimizador.OptimizadorAST.GoTo import GoTo

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
                self.codigoOptimizado += func.id+":\n"
                contador = 0
                for ins in func.instrucciones:
                    # try:
                    self.codigoOptimizado += "    "+ins.optmimizarCodigo().codigo
                    
                    #Regla 2 Mirilla
                    if(isinstance(ins,GoTo)):
                        if(ast.existeEtiqueta(ins.id)):
                            if(len(func.instrucciones[contador+1:]) == 0): continue
                            optimizacion = Optimizacion()
                            optimizacion.linea = str(ins.linea)
                            codigoOptimizar="<div>"
                            for i in func.instrucciones[contador+1:]:
                                codigoOptimizar+="<p>"+i.optmimizarCodigo().codigo+"</p>"
                            codigoOptimizar+="</div>"
                            optimizacion.antes = codigoOptimizar
                            optimizacion.despues = ins.id+":"
                            optimizacion.regla = "regla 2"
                            optimizacion.tipo = "Mirilla - Eliminación de Código Inalcanzable"
                            ReporteOptimizacion.func(optimizacion)
                            break
                    contador = contador + 1
                    # except:
                    #    pass

        ventana.consola.append(self.codigoOptimizado)

    def reporte(self):
        reporte = ReporteOptimizacion.ReporteOptimizacion()
        reporte.ReporteOptimizacion()
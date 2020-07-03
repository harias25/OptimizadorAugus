import Optimizador.grammarOptimizacion as g
import Optimizador.OptimizadorAST.Instruccion as Instruccion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion 
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion
from Optimizador.OptimizadorAST.AST import AST
from Optimizador.OptimizadorAST.GoTo import GoTo
from Optimizador.OptimizadorCondicionales.If import If
from Optimizador.OptimizadorValorImplicito.Asignacion import Asignacion

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
                instruccionAnterior = None
                asignacionPrevia = None
                codigoAnterior = ""
                for ins in func.instrucciones:
                    # try:
                        if(isinstance(ins,Asignacion)):
                            ins.instruccionPrevia = asignacionPrevia
                            asignacionPrevia = ins
                        elif(isinstance(ins,If)):
                            ins.ast = ast
                            ins.instrucciones = func.instrucciones[contador+1:]
                            
                        optimizado = ins.optmimizarCodigo().codigo
                        #Regla 2 Mirilla
                        if(isinstance(ins,GoTo)):
                            if(codigoAnterior.startswith('goto')):
                                if(isinstance(instruccionAnterior,If)):
                                    codigoAnterior = ""
                                    continue
                                else:
                                    optimizacion = Optimizacion() #si hay optimización
                                    optimizacion.linea = str(ins.linea)
                                    optimizacion.antes = codigoOptimizar
                                    optimizacion.despues = ins.id+":"
                                    optimizacion.regla = "Regla 20"
                                    optimizacion.tipo = "Bloques - Eliminación de Código Muerto"
                                    ReporteOptimizacion.func(optimizacion)
                                    codigoAnterior = ''
                            elif(ast.existeEtiqueta(ins.id)):
                                if(optimizado!=""):
                                    self.codigoOptimizado += "    "+optimizado
                                    codigoAnterior = optimizado
                                if(len(func.instrucciones[contador+1:]) == 0): continue  #si no existen mas instrucciones no hay optimización
                                optimizacion = Optimizacion() #si hay optimización
                                optimizacion.linea = str(ins.linea)
                                codigoOptimizar="<div>"
                                for i in func.instrucciones[contador+1:]:
                                    codigoOptimizar+="<p>"+i.optmimizarCodigo().codigo+"</p>"
                                codigoOptimizar+="</div>"
                                optimizacion.antes = codigoOptimizar
                                optimizacion.despues = ins.id+":"
                                optimizacion.regla = "Regla 2"
                                optimizacion.tipo = "Mirilla - Eliminación de Código Inalcanzable"
                                ReporteOptimizacion.func(optimizacion)
                                codigoAnterior = ''
                                break
                            else:
                                if(optimizado!=""):
                                    self.codigoOptimizado += "    "+optimizado
                                    codigoAnterior = optimizado
                        else:
                            if(optimizado!=""):
                                self.codigoOptimizado += "    "+optimizado
                                codigoAnterior = optimizado

                        instruccionAnterior = ins
                        contador = contador + 1
                    # except:
                    #    pass
    
        ventana.consola.append(self.codigoOptimizado)

    def reporte(self):
        reporte = ReporteOptimizacion.ReporteOptimizacion()
        reporte.ReporteOptimizacion()
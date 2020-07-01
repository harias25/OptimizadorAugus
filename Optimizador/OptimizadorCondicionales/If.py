from Optimizador.OptimizadorAST.Instruccion import Instruccion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion , OptmizacionResultado
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion

class If(Instruccion) :
    def __init__(self,  condicion, etiqueta,linea,columna) :
        self.condicion = condicion
        self.etiqueta = etiqueta
        self.linea = linea
        self.columna = columna

    def optmimizarCodigo(self):
        antes = self.generarAugus()
        resultado = OptmizacionResultado()
        resultado.codigo = antes;
        return resultado

    def generarAugus(self):
        codigoAugus = "if( "+self.condicion.generarAugus()+" ) goto "+self.etiqueta+";\n"
        return codigoAugus
        
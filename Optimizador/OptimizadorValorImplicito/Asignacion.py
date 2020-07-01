from Optimizador.OptimizadorAST.Instruccion import Instruccion
from Optimizador.OptimizadorAST.Simbolo import TIPO_DATO as Tipo
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion , OptmizacionResultado
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion

class Asignacion(Instruccion):
    def __init__(self,id,valor,linea,columna,parametro):
        self.linea = linea
        self.columna = columna
        self.id = id
        self.valor = valor
        self.parametro = parametro

    def optmimizarCodigo(self):
        antes = self.generarAugus()
        resultado = OptmizacionResultado()
        resultado.codigo = antes;
        return resultado

    def generarAugus(self):
        if(self.parametro):
            codigoAugus = self.id+" = &"+self.valor.generarAugus()+";\n"
        else:
            codigoAugus = self.id+" = "+self.valor.generarAugus()+";\n"
        return codigoAugus
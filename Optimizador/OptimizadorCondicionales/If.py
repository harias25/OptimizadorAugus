from Optimizador.OptimizadorAST.Instruccion import Instruccion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion , OptmizacionResultado
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion
from Optimizador.OptimizadorValorImplicito.Operacion import TIPO_OPERACION
from Optimizador.OptimizadorAST.GoTo import GoTo

class If(Instruccion) :
    def __init__(self,  condicion, etiqueta,linea,columna) :
        self.condicion = condicion
        self.etiqueta = etiqueta
        self.linea = linea
        self.columna = columna
        self.instrucciones = []
        self.ast = None

    def optmimizarCodigo(self):
        antes = self.generarAugus()
        resultado = OptmizacionResultado()
        resultado.codigo = antes
        return resultado

    def generarAugus(self):
        codigoAugus = "if( "+self.condicion.generarAugus()+" ) goto "+self.etiqueta+";\n"
        optimizacion = Optimizacion()
        optimizacion.linea = str(self.linea)
        optimizacion.antes = codigoAugus
        optimizacion.tipo = "Mirilla - Eliminación de Codigo Inalcanzable"


        
        if(self.condicion.tipo == TIPO_OPERACION.IGUAL_IGUAL):
            if(self.condicion.validarRegla4()):
                optimizacion.regla = "Regla 4"
                optimizacion.despues = "goto "+self.etiqueta+";"
                ReporteOptimizacion.func(optimizacion)
                codigoAugus = "goto "+self.etiqueta+";\n"
            elif(self.condicion.validarRegla5()):
                optimizacion.regla = "Regla 5"
                optimizacion.despues = ""
                ReporteOptimizacion.func(optimizacion)
                return ""


        #validacion de regla 6 o 7 Mirilla
        optimizacion = Optimizacion()
        optimizacion.linea = str(self.linea)
        optimizacion.antes = codigoAugus
        optimizacion.tipo = "Mirilla - Optimizaciones de flujo de control"
        if(codigoAugus.startswith('goto')):
            optimizacion.regla = "Regla 6"
        else:
            optimizacion.regla = "Regla 7"
        try:
            etiqueta = self.ast.obtenerEtiqueta(self.etiqueta)
            if isinstance(etiqueta.instrucciones[0],GoTo):
                if(codigoAugus.startswith('goto')):
                    codigoAugus = "goto "+etiqueta.instrucciones[0].id+";\n"
                else:
                    codigoAugus = "if( "+self.condicion.generarAugus()+" ) goto "+etiqueta.instrucciones[0].id+";\n"
                optimizacion.despues = codigoAugus
                ReporteOptimizacion.func(optimizacion)
        except:
            pass
        
        return codigoAugus
        
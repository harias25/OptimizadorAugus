def func(opt,param=False):
    #Declaración e inicilizacion de la variable "estática"
    if not hasattr(func,"listado"):
        func.listado = []

    if(param):
        func.listado = []
    else:
        if(opt!=None):
            func.listado.append(opt)
        else:
            return func.listado
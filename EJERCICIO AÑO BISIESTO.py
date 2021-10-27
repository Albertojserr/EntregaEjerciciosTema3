def esBisiesto(año):
    esBisiesto=True
    if(año%4==0):
        if(año%100==0):
            if(año%400==0):
                esBisiesto=True
            else:
                esBisiesto=False
        else:
            esBisiesto=True
    else:
        esBisiesto=False
    return esBisiesto
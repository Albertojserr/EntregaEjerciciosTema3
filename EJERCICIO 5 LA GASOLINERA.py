def precio(galones,precioporlitro):
    galonesAlitros=3.78541
    litros=galones*galonesAlitros
    precioACobrar=litros*precioporlitro
    print("Tiene que pagar ", precioACobrar,"euros")

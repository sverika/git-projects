@get("/temperatura/{Marabá}")
def temperatura(cidade):
    return{"temperatura": get_temperatura(cidade)}
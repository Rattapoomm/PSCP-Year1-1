'''Meteorite'''
def shot(weight, per, den):
    '''sol'''
    meteo = 1
    shoot = 0
    while weight >= den:
        shoot += meteo
        meteo = per * meteo
        weight /= per
    print(shoot)

shot(float(input()), int(input()), float(input()))

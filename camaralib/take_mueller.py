import take_mueller_stokes
from tools.stokeslib import  calcular_mueller_inv, normalizar_mueller

#Calcula la matriz de Mueller. Sincroniza con los motores, toma las fotos, 
# carga la Sin invertida y entrega la matriz de mueller observada.

def take_mueller(S_in_stat_inv, exposure_time, N, thetas_list):

    #Captura Stokes en los tres ángulos
    S_out_stat = take_mueller_stokes(exposure_time, N, thetas_list)

    #Calcula Mueller
    print('Calculando Matriz de Mueller...')
    M = calcular_mueller_inv(S_in_stat_inv, S_out_stat)

    # Normaliza la matriz de Mueller
    M_norm = normalizar_mueller(M)

    # Imagen de intensidad
    m00 = M[:,:,:,0,0]
    
    return m00, M_norm

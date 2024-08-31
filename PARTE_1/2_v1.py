def tiempo_adicional(tiempo):
    # Convertir la entrada de MM:SS a horas y minutos que el microondas toma
    minutos = int(tiempo[:2])
    segundos = int(tiempo[3:])
    
    # Calcular la cantidad de tiempo que el microondas realmente toma
    horas_reales = minutos // 60
    minutos_reales = minutos % 60
    
    # Convertir la entrada a tiempo esperado en segundos
    tiempo_esperado_seg = minutos * 60 + segundos
    
    # Convertir el tiempo real en segundos
    tiempo_real_seg = (horas_reales * 60 + minutos_reales) * 60
    
    # Calcular la diferencia en segundos
    diferencia_seg = tiempo_real_seg - tiempo_esperado_seg
    
    # Convertir la diferencia en horas, minutos y segundos
    horas = diferencia_seg // 3600
    minutos = (diferencia_seg % 3600) // 60
    segundos = diferencia_seg % 60
    
    # Formatear el resultado a HH:MM:SS
    return f"{horas:02}:{minutos:02}:{segundos:02}"

# Leer la cantidad de casos de prueba
t = int(input())

# Procesar cada caso de prueba
for _ in range(t):
    tiempo = input().strip()
    resultado = tiempo_adicional(tiempo)
    print(resultado)

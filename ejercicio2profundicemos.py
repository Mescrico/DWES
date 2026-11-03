grupos = {
    
    "chirigotas": {
            
        "Los Yesterday": {
                    
            "preliminares": [9.1, 9.3, 9.0, 9.2],
                        
            "cuartos": [9.4, 9.2, 9.1, 9.3],
                        
            "semifinal": [9.6, 9.5, 9.4, 9.5],
                        
            "final": [9.7, 9.6, 9.8, 9.7]
            
        },
            
        "Er Chele Vara": {
                        
            "preliminares": [8.5, 8.6, 8.7, 8.9],
                        
            "cuartos": [8.9, 8.8, 8.6, 8.7]
            
         }
        
    },
        
    "comparsas": {
            
        "Los Ángeles Caídos": {
                    
            "preliminares": [9.5, 9.6, 9.7, 9.8],
                        
            "cuartos": [9.7, 9.6, 9.8, 9.9],
                        
            "semifinal": [9.8, 9.9, 9.8, 9.9],
                        
            "final": [9.9, 9.9, 9.8, 9.8]
                
        },
                
        "Los Millonarios": {
                    
            "preliminares": [9.3, 9.4, 9.5, 9.6],
                        
            "cuartos": [9.6, 9.5, 9.7, 9.8],
                        
            "semifinal": [9.7, 9.6, 9.7, 9.8]
                
        }
        
    },
        
    "coros": {
            
        "La Trinidad": {
                        
            "preliminares": [9.0, 9.1, 9.2, 9.3],
                        
            "cuartos": [9.3, 9.4, 9.5, 9.6],
                        
            "semifinal": [9.5, 9.6, 9.7, 9.8],
                        
            "final": [9.7, 9.8, 9.9, 9.8]
                
        },
                
        "El Batallón Fletilla": {
                    
            "preliminares": [8.8, 8.9, 9.0, 9.1],
                        
            "cuartos": [9.0, 9.1, 9.2, 9.3],
                        
            "semifinal": [9.2, 9.3, 9.4, 9.5]
                    
        }
            
    },
        
    "cuartetos": {
                
        "Tres notas Musicales": {
                    
            "preliminares": [9.2, 9.3, 9.1, 9.4],
                        
            "cuartos": [9.4, 9.5, 9.3, 9.6],
                        
            "semifinal": [9.5, 9.6, 9.7, 9.6],
                        
            "final": [9.7, 9.8, 9.6, 9.7]
                    
        },
                
        "Ser o no Ser": {
                    
            "preliminares": [8.7, 8.8, 8.9, 8.6],
                        
            "cuartos": [8.9, 9.0, 8.8, 8.9]
                
        }
        
    }
}

def calcula_media_puntuaciones(grupos, *puntuaciones_extra, ag=None, fase=None):
    """
    Calcula las medias de las puntuaciones de las agrupaciones del concurso.
    
    Parámetros:
    - grupos (dict): Diccionario con modalidades, agrupaciones y sus fases.
    - *puntuaciones_extra: Puntuaciones adicionales a sumar en el cálculo.
    - ag (str, opcional): Nombre exacto de la agrupación.
    - fase (str, opcional): Nombre exacto de la fase.
    
    Retorna:
    - dict: Diccionario de dos niveles (modalidad y agrupación) con la media calculada.
    """
    resultado = {}

    if ag is None and fase is None:
        for grupo, contenido in grupos.items():
            agrupaciones = {}
            for banda, valor in contenido.items():
                sumaFase = 0
                contadorFase = 0

                for titulo, notas in valor.items():
                    notas_redondeadas = list(map(round, notas, [2] * len(notas)))
                    if notas_redondeadas:
                        mediaFase = sum(notas_redondeadas) / len(notas_redondeadas)
                        sumaFase += mediaFase
                        contadorFase += 1
                if puntuaciones_extra:
                    notas_extra_redondeadas = list(map(round, puntuaciones_extra, [2] * len(puntuaciones_extra)))
                    if notas_extra_redondeadas:
                        suma_medias_fases += sum(notas_extra_redondeadas) / len(notas_extra_redondeadas)
                        contadorFase += 1

                if contadorFase > 0:
                    media_general = suma_medias_fases / contadorFase
                    agrupaciones[banda] = round(media_general, 2)
            
            if agrupaciones:
                resultado[grupo] = agrupaciones

    elif fase is None:
        banda_buscada = ag
        for grupo, contenido in grupos.items():
            agrupaciones_dict = {}
            for banda, valor in contenido.items():
                if banda == banda_buscada:
                    suma_medias_fases = 0
                    contador_fases = 0

                    for titulo, notas in valor.items():
                        notas_redondeadas = list(map(round, notas, [2] * len(notas)))
                        if notas_redondeadas:
                            media_fase = sum(notas_redondeadas) / len(notas_redondeadas)
                            suma_medias_fases += media_fase
                            contador_fases += 1                    
                    if puntuaciones_extra:
                        notas_extra_redondeadas = list(map(round, puntuaciones_extra, [2] * len(puntuaciones_extra)))
                        if notas_extra_redondeadas:
                            suma_medias_fases += sum(notas_extra_redondeadas) / len(notas_extra_redondeadas)
                            contador_fases += 1

                    if contador_fases > 0:
                        media_general = suma_medias_fases / contador_fases
                        agrupaciones_dict[banda] = round(media_general, 2)
            
            if agrupaciones_dict:
                resultado[grupo] = agrupaciones_dict
                break

    else:
        banda_buscada = ag
        fase_buscada = fase
        for grupo, contenido in grupos.items():
            agrupaciones_dict = {}
            for banda, valor in contenido.items():
                if banda == banda_buscada:
                    if fase_buscada in valor:
                        notas_totales = list(valor[fase_buscada]) + list(puntuaciones_extra)
                        
                        notas_redondeadas = list(map(round, notas_totales, [2] * len(notas_totales)))
                        
                        if notas_redondeadas:
                            media_fase = sum(notas_redondeadas) / len(notas_redondeadas)
                            agrupaciones_dict[banda] = round(media_fase, 2)
            
            if agrupaciones_dict:
                resultado[grupo] = agrupaciones_dict
                break

    return resultado
    

print(calcula_media_puntuaciones(grupos, 2.876, 1.944, ag="Los Yesterday", fase="final"))

# calcula_media_puntuaciones(grupos, ag="Los Yesterday", fase="final")
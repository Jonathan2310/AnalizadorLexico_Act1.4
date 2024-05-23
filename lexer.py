import re

# Diccionario de sinónimos (con 50 palabras)
sinonimos = {
    'facil': 'sencillo',
    'morir': 'fallecer',
    'grande': 'enorme',
    'rapido': 'veloz',
    'feliz': 'contento',
    'triste': 'afligido',
    'inteligente': 'listo',
    'bonito': 'hermoso',
    'feo': 'horrendo',
    'bueno': 'excelente',
    'malo': 'pésimo',
    'nuevo': 'reciente',
    'viejo': 'antiguo',
    'amigo': 'compañero',
    'enemigo': 'adversario',
    'amor': 'cariño',
    'odio': 'rencor',
    'fuerte': 'robusto',
    'debil': 'fragil',
    'alto': 'elevado',
    'bajo': 'pequeño',
    'caliente': 'ardiente',
    'frio': 'helado',
    'cerca': 'proximo',
    'lejos': 'distante',
    'claro': 'lucido',
    'oscuro': 'sombrio',
    'rapido': 'preciso',
    'lento': 'pausado',
    'grande': 'enorme',
    'pequeño': 'minusculo',
    'rico': 'adinerado',
    'pobre': 'necesitado',
    'feliz': 'contento',
    'triste': 'deprimido',
    'amable': 'cortes',
    'grosero': 'maleducado',
    'limpio': 'aseado',
    'sucio': 'desordenado',
    'sabio': 'erudito',
    'tonto': 'necio',
    'rápido': 'preciso',
    'lento': 'pausado',
    'joven': 'mozo',
    'viejo': 'anciano',
    'fuerte': 'vigoroso',
    'debil': 'endeble',
    'hermoso': 'bello',
    'feo': 'desagradable',
    'libro': 'tomo',
    'casa': 'hogar'
}

def analizar_texto(entrada):
    lineas = entrada.split("\n")
    resultados = []

    for i, linea in enumerate(lineas, start=1):
        linea_analizada = []
        palabras = linea.split()
        
        # Diccionario de sinónimos en minúsculas para coincidencias sin importar el caso
        sinonimos_lower = {k.lower(): v for k, v in sinonimos.items()}

        for palabra in palabras:
            palabra_sin_acento = ''.join(c for c in palabra if c.isalnum())
            palabra_sin_acento_lower = palabra_sin_acento.lower()
            
            if palabra_sin_acento_lower in sinonimos_lower:
                sinonimo = sinonimos_lower[palabra_sin_acento_lower]
                linea_analizada.append(('Palabra cambiada', palabra, sinonimo))
            elif palabra.isdigit():
                linea_analizada.append(('Número', palabra))
            elif re.match(r'^\W+$', palabra):
                linea_analizada.append(('Símbolo', palabra))
            else:
                linea_analizada.append(('Palabra', palabra))
        
        resultados.append((i, linea, linea_analizada))

    return resultados

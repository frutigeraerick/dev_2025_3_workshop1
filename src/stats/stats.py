class Stats:
    def promedio(self, numeros):
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        numeros = sorted(numeros)
        n = len(numeros)
        if n % 2 == 1:
            return numeros[n // 2]
        else:
            return (numeros[n // 2 - 1] + numeros[n // 2]) / 2
    
    def moda(self, numeros):
        from collections import Counter
        frecuencia = Counter(numeros)
        return frecuencia.most_common(1)[0][0]
    
    def desviacion_estandar(self, numeros):
        import math
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return math.sqrt(varianza)
    
    def varianza(self, numeros):
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        return max(numeros) - min(numeros)
class Strings:
    def es_palindromo(self, texto):
        texto = ''.join(e for e in texto if e.isalnum()).lower()
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)
    
    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for char in texto if char in consonantes)
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        return ' '.join([palabra.capitalize() for palabra in texto.split()])
    
    def eliminar_espacios_duplicados(self, texto):
        return ' '.join(texto.split())
    
    def es_numero_entero(self, texto):
        if texto.startswith('-'):
            texto = texto[1:]
        return texto.isdigit() and len(texto) > 0
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = []
        for char in texto:
            if char.isalpha():
                desplazamiento_real = desplazamiento % 26
                base = ord('a') if char.islower() else ord('A')
                resultado.append(chr((ord(char) - base + desplazamiento_real) % 26 + base))
            else:
                resultado.append(char)
        return ''.join(resultado)
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        i = 0
        while i < len(texto):
            i = texto.find(subcadena, i)
            if i == -1:
                break
            posiciones.append(i)
            i += 1
        return posiciones
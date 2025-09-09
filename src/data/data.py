class Data:
    
    def invertir_lista(self, lista):
        inversa = []
        for elemento in lista:
            inversa.insert(0, elemento)
        return inversa
    
    def buscar_elemento(self, lista, elemento):
        for i, elem in enumerate(lista):
            if elem == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        resultado = []
        for elemento in lista:
            if elemento not in resultado:
                resultado.append(elemento)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        k = k % len(lista)  # Para manejar k mayor que el tamaño de la lista
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        pila = {
            'stack': [],
            'push': lambda x: pila['stack'].append(x),
            'pop': lambda: pila['stack'].pop() if pila['stack'] else None,
            'peek': lambda: pila['stack'][-1] if pila['stack'] else None,
            'is_empty': lambda: len(pila['stack']) == 0
        }
        return pila
    
    def implementar_cola(self):
        cola = {
            'queue': [],
            'enqueue': lambda x: cola['queue'].append(x),
            'dequeue': lambda: cola['queue'].pop(0) if cola['queue'] else None,
            'peek': lambda: cola['queue'][0] if cola['queue'] else None,
            'is_empty': lambda: len(cola['queue']) == 0
        }
        return cola
    
    def matriz_transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        transpuesta = []
        for j in range(columnas):
            fila = []
            for i in range(filas):
                fila.append(matriz[i][j])
            transpuesta.append(fila)
        return transpuesta
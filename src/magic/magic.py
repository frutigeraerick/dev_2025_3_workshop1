class Magic:
    def fibonacci(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])
        return seq[:n]
    
    def es_primo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        divisores = [i for i in range(1, n) if n % i == 0]
        return sum(divisores) == n
    
    def triangulo_pascal(self, filas):
        tri = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(tri[i-1][j-1] + tri[i-1][j])
            fila.append(1)
            tri.append(fila)
        return tri
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(digit) for digit in str(n))
    
    def es_numero_armstrong(self, n):
        num_str = str(n)
        power = len(num_str)
        return n == sum(int(digit)**power for digit in num_str)
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_fila = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_fila:
                return False
        
        for col in range(n):
            if sum(matriz[i][col] for i in range(n)) != suma_fila:
                return False
        
        if sum(matriz[i][i] for i in range(n)) != suma_fila:
            return False
        
        if sum(matriz[i][n-i-1] for i in range(n)) != suma_fila:
            return False
        
        return True
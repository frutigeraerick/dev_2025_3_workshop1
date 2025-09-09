import random

class Games:
    
    def piedra_papel_tijera(self, jugador1, jugador2):
        reglas = {
            ("piedra", "tijera"): "jugador1",
            ("tijera", "piedra"): "jugador2",
            ("tijera", "papel"): "jugador1",
            ("papel", "tijera"): "jugador2",
            ("papel", "piedra"): "jugador1",
            ("piedra", "papel"): "jugador2"
        }
        
        if jugador1 == jugador2:
            return "empate"
        
        return reglas.get((jugador1, jugador2), "empate")
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento < numero_secreto:
            return "muy bajo"
        elif intento > numero_secreto:
            return "muy alto"
        return "correcto"
    
    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]
        
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        
        for fila in tablero:
            if " " in fila:
                return "continua"
        
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False 
        
        if desde_fila == hasta_fila: 
            rango = range(min(desde_col, hasta_col) + 1, max(desde_col, hasta_col))
            for col in rango:
                if tablero[desde_fila][col] != " ":
                    return False
        elif desde_col == hasta_col:  
            rango = range(min(desde_fila, hasta_fila) + 1, max(desde_fila, hasta_fila))
            for fila in rango:
                if tablero[fila][desde_col] != " ":
                    return False
        
        return True
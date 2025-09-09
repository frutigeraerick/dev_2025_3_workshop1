class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def fahrenheit_a_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
    def metros_a_pies(self, metros):
        pies = metros * 3.28084
        return pies
    
    def pies_a_metros(self, pies):
        metros = pies / 3.28084
        return metros
    
    def decimal_a_binario(self, decimal):
        binario = bin(decimal)[2:]
        return binario
    
    def binario_a_decimal(self, binario):
        decimal = int(binario, 2)
        return decimal
    
    def decimal_a_romano(self, numero):
        if numero < 1 or numero > 3999:
            return "El número debe estar entre 1 y 3999"
        
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        romano = ""
        for valor, simbolo in valores:
            while numero >= valor:
                romano += simbolo
                numero -= valor
        return romano

    def romano_a_decimal(self, romano):
        valores = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        i = 0
        while i < len(romano):
            if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
                total += valores[romano[i + 1]] - valores[romano[i]]
                i += 2
            else:
                total += valores[romano[i]]
                i += 1
        return total

    def texto_a_morse(self, texto):
        morse_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }
        texto = texto.upper()
        morse = " ".join(morse_dict[c] for c in texto if c in morse_dict)
        return morse

    def morse_a_texto(self, morse):
        morse_dict = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
            ".": "E", "..-.": "F", "--.": "G", "....": "H",
            "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
            "--": "M", "-.": "N", "---": "O", ".--.": "P",
            "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
            "-.--": "Y", "--..": "Z",
            "-----": "0", ".----": "1", "..---": "2", "...--": "3",
            "....-": "4", ".....": "5", "-....": "6", "--...": "7",
            "---..": "8", "----.": "9"
        }
        inv_morse_dict = {v: k for k, v in morse_dict.items()}
        texto = "".join(inv_morse_dict[c] for c in morse.split() if c in inv_morse_dict)
        return texto

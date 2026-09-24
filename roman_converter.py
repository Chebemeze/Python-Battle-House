def to_roman(number):
    if 1<=number<= 3999:
        decision_roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50,"XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        roman_string = ""
        for key, value in decision_roman.items():
            count = number // value
            print(number//value)
            number %= value
            roman_string += key*count
        return roman_string

print(to_roman(9))
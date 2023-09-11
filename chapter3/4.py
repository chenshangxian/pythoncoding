num = int(input("please enter a number within the range of 1 through 10: "))

roman_numerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}

if num >= 1 and num <= 10:
    roman_numeral = roman_numerals[num]
    print(f" the Roman numeral version of the number: {roman_numeral}")
else:
    print("an error message")
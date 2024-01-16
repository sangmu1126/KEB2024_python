dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec, octal, hexadecimal, binary)
print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
print(bin(dec), bin(octal), bin(hexadecimal), bin(binary))
print(ord('B'), ord('Z'), ord('a'), ord('2'))  # 66, 90, 97, 50

# (100°F − 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F

menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")

if menu == '1':
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
elif menu == '2':
    celsius = float(input('Input Celcius : '))
    print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')

letter = input('Input alphabet letter : ')
#vowels = {'a', 'e', 'i', 'o', 'u'}  # set
vowels = "aeiuo"  # str
print(type(vowels))
if letter in vowels:  # in
    print(f'{letter} is a vowel~')
else:
    print(f'{letter} is a consonant!')

l = [1, 3, 3, 2, 4]  # list
s = {1, 3, 3, 2, 4}  # set
print(l, s)  # [1, 3, 3, 2, 4] {1, 2, 3, 4}


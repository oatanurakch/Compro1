#### Slide หน้าที่ 5
'''
เขียนโปรแกรมเพื่อรับเลขจำนวนเต็มเก็บไว้ที่ตัวแปร n แล้วแสดงออกเป็น
เลขฐานสอง ฐานแปด และ ฐานสิบหก ดังตัวอย่างการรันโปรแกรม
'''

# Coding 
number = int(input('Enter a number: '))
print('Type of n = %s' %(type(number)))
print('Decimal number %d = Binary number %s' %(number, bin(number)))
print('Decimal number %d = Octal number %s' %(number, oct(number)))
print('Decimal number %d = Hexadecimal number %s' %(number, hex(number)))

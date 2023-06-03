### Slide หน้า 9
"""
เขียนโปรแกรมในการรับเลขจำนวนเต็ม 3 จำนวนเก็บไว้ที่ตัวแปร a, b และ c
แล้วแสดงผลลัพธ์ในการเปรียบเทียบค่าของตัวแปรทั้ง 3
"""

# Coding
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('a = %d, b = %d and c = %d' %(a, b, c))
print('%d > %d ==> %s' %(a, b, a > b))
print('%d is an odd number ==> %s' %(c, c % 2 == 1))
print('%d > %d and %d is an even number == > %s' %(a, b, a, a > b and a % 2 == 0))
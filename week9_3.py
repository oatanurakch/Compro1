### Slide หน้า 12
"""
เขียนโปรแกรมในการรับเลขจำนวนเต็ม 1 จำนวนมีค่าตั้งแต่ 100 ถึง 999 แล้วประมวลผลหาเลขที่มากที่สุด
โดยใช้ if elif else แล้วแสดงออกที่จอภาพ
้"""

# Coding
number = int(input("Enter number (100-999): "))
n1 = number // 100
n2 = (number // 10) % 10
n3 = number % 10
if n1 > n2 and n1 > n3:
    bignumber = n1
elif n2 > n1 and n2 > n3:
    bignumber = n2
else:
    bignumber = n3
print('The biggest number is %d.' %(bignumber))
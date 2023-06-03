### Slide หน้า 6
"""
เขียนโปรแกรมในการรับเลขจำนวนเต็ม 1 จำนวนมีค่าตั้งแต่ 100 - 999
แล้วทำการแยกหลักพร้อมกับหาผลบวกของหลักต่าง ๆ แล้วแสดงออกที่จอภาพ
"""

# Coding
number = int(input("Enter number (100-999): "))
n1 = number // 100
n2 = (number // 10) % 10
n3 = number % 10
print('%d is separated to %d, %d and %d' %(number, n1, n2, n3))
print('Sum of %d, %d and %d is %d.' %(n1, n2, n3, n1+n2+n3))
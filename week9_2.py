### Slide หน้า 9
"""
เขียนโปรแกรมในการรับเลขจำนวนเต็ม 1 จำนวน ถ้าเป็นเลขคู่ให้แสดงคำว่า "It is even number." ออกที่จอภาพ
แต่ถ้าเป็นเลขคี่ให้แสดงคำว่า "It is odd number." ออกที่จอภาพ
"""

# Coding
number = int(input("Enter a number: "))
if number % 2 == 0:
    print('It is even number.')
else:
    print('It is odd number.')
print('End Program !!!')
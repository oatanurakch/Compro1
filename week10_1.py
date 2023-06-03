### Slide หน้า 8
"""
เขียนโปรแกรมโดยใช้ for ในการพิมพ์เลขจำนวนเต็มจาก 1 ถึง 9 ออกที่จอภาพ
้"""

# Coding
print('Printing 1 to 9 using for loop')
for i in range(1, 10):
    if i == 8:
        print(i, end = ' and ')
    elif i == 9:
        print(i, '.', sep = '')
    else:
        print(i, end = ', ')
print('End Program !!!')
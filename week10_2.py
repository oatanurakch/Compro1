### Slide หน้า 12
"""
เขียนโปรแกรมโดยใช้ for ในการวนลูปรับเลขจำนวนเต็ม 1 ถึง 10 เท่านั้น ถ้าไม่อยู่ในพิสัยให้วนลูปรับข้อมูลใหม่
จนกว่าจะได้ข้อมูลที่ต้องการ หลังจากนั้น ให้ใช้ลูป while เพื่อพิมพ์เลขจำนวนนั้นมาจนถึง 1 โดยพิมพ์เฉพาะเลขคี่เท่านั้น
พร้อมกับบอกผลรวมของเลขเหล่านั้นออกที่จอภาพ
้"""

# Coding
print('Using while loop ...')
while True:
    number = int(input('Enter number (1-10): '))
    if number >= 1 and number <= 10:
        break
i = number
sumodd = 0
while i >= 1:
    if i % 2 == 1:
        print(i, end = ' ')
        sumodd += i
    i -= 1
print()
print('Sum = %d' %(sumodd))
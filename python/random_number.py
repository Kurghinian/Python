import random
number = random.randint(1,50)
yor_num = int(input("Enter Number "))
while number != yor_num:
    if number > yor_num:
         print("dzer nermucac tivy poqr e sharjveq araj")
         yor_num = int(input("Enter Number "))
    elif number < yor_num:
        print("dzer nermucac tivy mec e sharjveq depi nerqev")
        yor_num = int(input("Enter Number "))

print("Shnorhavorum enq haxteciq")
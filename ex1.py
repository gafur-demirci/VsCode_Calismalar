num = int(input("Kaç sayı girmek istiyorsunuz ? "))
total_sum = 0

for n in range(num):
    numbers = float(input("Sayı giriniz : "))
    total_sum += numbers

avg = total_sum / num
print("Average is : ",avg)
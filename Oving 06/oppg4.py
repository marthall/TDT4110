teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114,
    109, 11, 2, 21, 45, 2, 26, 81, 54, 14,
    118, 108, 117, 27, 115, 43, 70, 58, 107]
sum_twenty = 0
sum_ten = 0
sum_five = 0
sum_one = 0
sum_fifty = 0

def money(i):
    global teeth
    teeth[i] *= 0.5
    twenty = teeth[i] // 20
    teeth[i] -= twenty*20
    ten = teeth[i] // 10
    teeth[i] -= ten*10
    five = teeth[i] // 5
    teeth[i] -= five*5
    one = teeth[i] // 1
    teeth[i] -= one*1
    fifty = teeth[i] // 0.5
    return twenty, ten, five, one, fifty

for i in range(len(teeth)):
    twenty, ten, five, one, fifty = money(i)
    sum_twenty += twenty
    sum_ten += ten
    sum_five += five
    sum_one += one
    sum_fifty += fifty

print("  20: %i" % sum_twenty)
print("  10: %i" % sum_ten)
print("   5: %i" % sum_five)
print("   1: %i" % sum_one)
print("0.50: %i" % sum_fifty)

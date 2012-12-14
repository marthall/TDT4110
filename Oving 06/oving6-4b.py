teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]
number_coins, temp_num_coin, coins, temp_teeth = [0, 0, 0, 0, 0,], [0, 0, 0, 0, 0,], [20, 10, 5,1, 0.5], [(0.5*i) for i in teeth]
print("-------------------------------------------")
print("Gram:  20kr -- 10kr -- 5kr -- 1kr -- 50ører")
for i in range(len(teeth)):
	for j in range(len(coins)):
		temp_num_coin[j] = (temp_teeth[i] // coins[j])
		number_coins[j] += temp_num_coin[j]
		temp_teeth[i] -= (temp_num_coin[j]*coins[j])
	print("%3i\t" % teeth[i] + "%i\t%i\t%i\t%i\t%i" % tuple(temp_num_coin[0:5]))
print("Tot:\t%i\t%i\t%i\t%i\t%i" % tuple(number_coins[0:5]))
print("--------------------------------------------")
teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97,
    114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14,
    118, 108, 117, 27, 115, 43, 70, 58, 107]
coins = [20, 10, 5,1, 0.5]
tot_coins = 5*[0]
tooth_coins = 5*[0]     # Coins for current tooth

print("-------------------------------------------")
print("Gram:  20kr -- 10kr -- 5kr -- 1kr -- 50orer")

for i in teeth:
    toot_value = 0.5 * i                                        # Value of current tooth
    for coin_index, coin_value in enumerate(coins):
        tooth_coins[coin_index] = toot_value // coin_value      # Floor division with coin_value
        tot_coins[coin_index] += tooth_coins[coin_index]        # Adds number of coins for this tooth to the total
        toot_value -= tooth_coins[coin_index]*coin_value        # The remaining value of the tooth
    print("%3i\t" % i + "%i\t%i\t%i\t%i\t%i" % tuple(tooth_coins[0:5]))     # Prints out the information for every tooth

print("Tot:\t%i\t%i\t%i\t%i\t%i" % tuple(tot_coins[0:5]))                   # Prints out the total
print("--------------------------------------------")
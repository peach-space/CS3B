#################################################
# Lab 7
# Student Name: Cen Li
#################################################

orders = [[34587, "Learning Python, Mark Lutz", 4, 40.95],
          [98762, "Programming Python, Mark Lutz", 5, 56.80],
          [77226, "Head First Python, Paul Barry", 3, 32.95],
          [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]]


order_prices = list(map(lambda x: (x[0], round(x[2] * x[3] + 10 if x[2] * x[3] < 100 else x[2] * x[3], 2)), orders))
print(order_prices)

# order_prices = []
# for order in orders:
#     price = order[2] * order[3]
#     if price < 100:
#         price = price + 10
#     order_prices.append((order[0], price))




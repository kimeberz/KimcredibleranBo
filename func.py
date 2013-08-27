def powsub(a, b):
  return pyth(a, b) * pyth(b, a)

def pyth(a, b):
  return (powsub(a, b) ** 2 + b ** 2) ** .5


print pyth(2, 3)
# print powsub(3, 4)


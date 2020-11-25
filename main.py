def p_price(gross_price, extension):
  return int(gross_price) + extension

print(p_price(3.50, 0.95))
print(p_price(3.25, .75))


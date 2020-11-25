####Build a Pretty Price Method in Python

def pretty_price(gross_price, extension):
  return int(gross_price) + extension

print(pretty_price(3.50, 0.95))


def p_price(gross, ext):
  return int(gross.sum(ext))

print(p_price(2.25, .50))
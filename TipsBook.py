def apply_discount(product, discount):
  price = int(product['price'] * (1.0 - discount)) 
  assert 0 <= price <= product['price']
  return price

#adder factiory
def make_adder(n): 
  def add(x):
    return x + n 
  return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

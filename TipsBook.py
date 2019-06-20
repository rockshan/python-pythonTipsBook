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

#Lambdas are in line function 
(lambda x, y: x + y)(5, 3)

#each function have a name which can accessed by self.__name

def yell(5):
  return 5

del yell
bark = yell
print(bark.__name) # This will print yell only


sorted(range(-5, 6), key=abs)#sort by absolute value
sorted(range(-5, 6), key=lambda x: x*x)# same result


#What’s a lexical closure? It’s just a fancy name for a function that remembers the 
#values from the enclosing lexical scope even when the program flow is no longer in 
#that scope. Here’s a (fairly academic) example to illustrate the idea:
def make_adder(n):
  return lambda x: x + n

plus_3 = make_adder(3)
 plus_3(4)
output: 7  

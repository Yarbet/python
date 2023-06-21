items = [
  {
    'producto' : 'camisa',
    'price' : 100
  },
  {
    'producto': 'pantalones',
    'price' : 300
  },
  {
    'producto': 'zapatos',
    'price' : 500
  }
]

prices = list(map(lambda item: item['price'], items))
products = list(map(lambda item: item['producto'], items))
print(prices)
print(products)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)

def LinearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
        indices.append(index)

  return indices


#Exmpla usage:
products = ["shoes", "boot", "Loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result =  LinearSearchProduct(products, target)
print(result)
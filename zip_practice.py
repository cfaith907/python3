list1 = [1,2,3,4,5,6]
list2 = ['one', 'two', 'three', 'four', 'five','']

zipped = list(zip(list1, list2))

# print(zipped)

unzipped = list(zip(*zipped))

# print(unzipped)

item = ['Apple', 'Banana', 'Orange']
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]

sentances = []
for (item, count, price) in zip(item, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentance = 'I bought ' + count + ' ' + item + 's at ' + price + ' cents each.'
    sentances.append(sentance)
print(sentances)
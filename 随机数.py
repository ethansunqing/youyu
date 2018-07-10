import random

r = random.random()
print(r)

a = random.uniform(0, 0.2)
print(a)

ids = [{
    'id': 8869,
    'price': 2662.0
}, {
    'id': 8861,
    'price': 2662.0
}, {
    'id': 8864,
    'price': 2662.0
}, {
    'id': 8864,
    'price': 2662.0
}, {
    'id': 8865,
    'price': 2662.0
}, {
    'id': 8869,
    'price': 2662.0
}]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)
print(news_ids)

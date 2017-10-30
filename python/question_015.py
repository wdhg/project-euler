SIZE = 20 

def pascal():
    layer = []
    while True:
        if len(layer) < 2:
            layer += [1]
        else:
            layer = [1] + [layer[i] + layer[i + 1] for i in range(len(layer) - 1)] + [1]
        yield layer

x = pascal()
for _ in range(SIZE * 2 + 1):
    layer = next(x)

print(layer[int(len(layer) / 2)])

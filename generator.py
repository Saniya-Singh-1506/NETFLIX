def my_gen():
    yield 1
    yield 2
    yield 3

for num in my_gen():
    print(num)

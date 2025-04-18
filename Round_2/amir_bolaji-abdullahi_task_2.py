def fizzbuzz(n): 
    for i in range(1,n): 
        if i % 15 == 0 : 
            print("FooBar", end="")
        elif i % 3 == 0: 
            print("Foo",end="",)
        elif i % 5 == 0: 
            print("Bar",end="")
        else: 
            print(i,end="")

print(fizzbuzz(10))

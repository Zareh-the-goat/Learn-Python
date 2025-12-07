hello = {
    "Hello" : "Chicken",
    "Chicken" : "eat",
    "Me" : 2013
}
x = hello.get("Chicken")
print(x)

x = hello.keys()
print(x)

x = hello.values()
print(x)

x = hello.items()
print(x)

if "Chicken" in hello:
    print("Yes")


hello["Color"] = "red"
hello["Yummy"] = "Chicken"
hello["Chicken"] = "Yummy"

print(hello)

hello.update({"Hello ": 2026})

hello.pop("Yummy")
hello.popitem()
print(hello)

del hello["Color"]
print(hello)
hello.clear()
print(hello)

del hello
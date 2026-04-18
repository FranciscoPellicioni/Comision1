edad = int(input())

if edad < 4:
    print(" $ 0.0")
elif 4 <= edad < 12:
    print("$ 50.0")
elif 12 <= edad < 18:
    print("$ 75.0")
elif 18 <= edad < 60:
    print("$ 150.0")
elif edad >=60:
    print("$ 75.0")
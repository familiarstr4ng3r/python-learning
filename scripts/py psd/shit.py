def get_user_input(text):
    user = input(text)
    try:
        value = float(user)
    except ValueError:
        return None
    else:
        return value
    
x = None
y = None

while (not x or not y):
    if not x:
        x = get_user_input("X: ")

    if not y:
        y = get_user_input("Y: ")

print(x, y)
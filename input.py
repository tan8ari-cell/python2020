def weather_con(temp):
    if temp > 7:
        return "hangat"
    else:
        return "dingin"


user_input = int(input("masukan input :"))

print(type(user_input), user_input)

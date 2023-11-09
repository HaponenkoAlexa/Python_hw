#Варіант 1
def say_hi(name, age):
    say_hi_message = f"Hi. My name is {name} and I'm {age} years old"
    print(say_hi_message)
    return say_hi_message

user_name = input("Введіть ім'я: ")
user_age = int(input("Введіть ваш вік: "))

assert say_hi(user_name, user_age) == f"Hi. My name is {user_name} and I'm {user_age} years old", 'Test1'
print('ОК')


#Варіант2
def say_hi(name, age):
    say_hi_message = f"Hi. My name is {name} and I'm {age} years old"
    return say_hi_message

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

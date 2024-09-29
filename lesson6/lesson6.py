# res = 5/0
#
# print("Hello World")
# print(res)
# print("End code")

print("=========== Base Exception ============")

print(f"nameError = {type(NameError)} - {issubclass(NameError, BaseException)}")

print("========================")
try:
    print(hello)
except NameError:
    print("NameError")

print("========================")


try:
    print(int(input("enter first num = ")) / int(input("enter second num = ")))
except ZeroDivisionError:
    print("ZeroDivisionError - wat aru doing MAN? why do you from?")
except ValueError as e:
    print("ValueError - enter only numbers!!!", end=" ")
    print(e)

print("========================")

try:
    list_color = ["red", "green", "blue"]
    print(list_color[10])
except (IndexError, NameError) as error:
    print("something went wrong", end=" ")
    print(error)



print("========================")

try:
    print("Hello World")
except:
    print("Something went wrong")
finally:
    print("No problem")

print("========================")


try:
    print("Hello World")
    print(hello)
except NameError as error:
    print(error)
else:
    print("Else no problem")
finally:
    print("Finally code")



print("========================")
print("End code")

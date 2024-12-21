#FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

#KeyError

#IndexError

# try:
#     file = open("a_file.py")
#     a_dic = {"key": "value"}
#     print(a_dic["key"])
# except FileNotFoundError:
#     # print(f"error_message: {error_message}")
#     file = open("a_file.py", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up")
    # file.close()
    # print("file closed")
# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

# try:
#     a_dic = {"key": "value"}
#     print(a_dic["not_exist_key"])
# except KeyError as error_message:
#     print(error_message)


height = float(input("Height: "))
weight = float(input("Weight: "))

if height < 3:
    raise ValueError("Please input a normal human height")

bmi = weight / height ** 2
print(bmi)
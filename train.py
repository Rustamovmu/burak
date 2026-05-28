# TASK M

# Array ichidagi har bir raqam uchun raqamning o'zi va
# uning kvadratidan tashkil topgan object hosil qilib qaytarsin.

# Masalan: getSquareNumbers([1, 2, 3]) return [{number: 1, square: 1}, ...]
# def getSquareNumbers(arr):
#     result = []
#     for num in arr:
#         obj = {
#             "number": num,
#             "square": num ** 2
#         }
#     result.append(obj)
#     return result


# print(getSquareNumbers([1, 2, 3]))

# TASK L

# So'zlarni ketma-ketligini buzmasdan har bir so'zni alohida teskarisiga o'girib beradigan function tuzing.

# Masalan: reverseSentence("we like coding!") return "ew ekil !gnidoc"


# def reverseSentence(sentence):
#     words = sentence.split()
#     reverse_words = []

#     for word in words:
#         reverse_words.append(word[::-1])

#     return " ".join(reverse_words)


# print(reverseSentence("we like coding!"))


# script.jsEditor
# Console
# Build a Celsius to Fahrenheit Converter
# In this lab, you will write a function that converts the temperature from Celsius to Fahrenheit. The formula to convert from Celsius to Fahrenheit is:

# Example Code
# fahrenheit = celsius * (9/5) + 32
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should create a function named convertCtoF.
# convertCtoF should take a single numeric argument, which is the temperature in Celsius.
# convertCtoF should return a number.
# Tests:
# Waiting:1. You should create a function named convertCtoF.
# Waiting:2. convertCtoF should take a single parameter.
# Waiting:3. convertCtoF(0) should return a number.


# def convertCtoF(celsius):
#     fahrenheit = celsius * (9/5) + 32
#     return fahrenheit


# print(convertCtoF(0))

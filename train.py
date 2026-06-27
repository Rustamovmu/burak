# TASK Y

# Ikkala arrayda ham ishtirok etgan bir xil qiymatlarni qaytarsin.

# Masalan: findIntersection([1, 2, 3], [3, 2, 0]) return [2, 3]

def findIntersection(arr1, arr2):
    result = []
    for num in arr1:
        if num in arr2:
            result.append(num)
    
    return result

print(findIntersection([1, 2, 3], [3, 2, 0]))
# TASK X

# Object tarkibida (nested bo'lsa ham) berilgan kalit necha marta takrorlanganini sanang.

# Masalan: countOccurrences({model: "A", s: {model: "B"}}, "model") return 2

# def countOccurrences(obj, key):
#     count = 0

#     for k, v in obj.items():
#         if k == key:
#             count += 1

#         if isinstance(v, dict):
#             count += countOccurrences(v, key)

#     return count


# print(countOccurrences(
#     {"model": "A", "s": {"model": "B"}},
#     "model"
# ))

# TASK W

# Arrayni berilgan uzunlikda bo'laklarga ajratib qaytarsin.

# Masalan: chunkArray([1, 2, 3, 4, 5], 2) return [[1, 2], [3, 4], [5]]


# def chunkArray(arr, size):
#     result = []

#     for i in range(0, len(arr), size):
#         result.append(arr[i:i + size])

#     return result


# print(chunkArray([1, 2, 3, 4, 5], 2))



# TASK V

# Stringdagi har bir harf necha marta takrorlanganini object sifatida qaytarsin.

# Masalan: countChars("hello") return {h: 1, e: 1, l: 2, o: 1}

# def countChars(text):
#     result = {}

#     for letter in text:
#         if letter in result:
#             result[letter] += 1
#         else:
#             result[letter] = 1

#     return result

# print(countChars("hello"))




# TASK T

# Ikkita arrayni qabul qilib, ularni birlashtirib tartiblangan holda qaytarsin.

# Masalan: mergeSortedArrays([0, 3, 4], [4, 6]) return [0, 3, 4, 4, 6]

# def mergeSortedArrays(a, b):
#     return sorted(a + b)


# print(mergeSortedArrays([0, 3, 4], [4, 6]))


# TASK S

# Array ichidagi tushib qolgan sonni topib qaytarsin.

# Masalan: missingNumber([3, 0, 1]) return 2
# def missingNumber(num):
#     n = len(num)
#     kutilgan_yigindi = n * (n + 1) // 2
#     yigindi = sum(num)
#     return kutilgan_yigindi - yigindi


# print(missingNumber([3, 0, 1]))


# TASK R

# "1 + 2" ko'rinishidagi stringni hisoblab number qaytarsin.

# Masalan: calculate("1 + 3") return 4
# def calculate(srt):
#     return eval(srt)


# print(calculate("4 - 3"))

# TASK Q

# Objectda berilgan string propertysi borligini tekshirsin.

# Masalan: hasProperty({name: "BMW"}, "name") return true.     in python

# def hasProperty(obj, p):
#     return p in obj


# # Test
# print(hasProperty({"name": "Porshe"}, "name"))
# print(hasProperty({"name": "BMW"}, "age"))


# TASK P

# Objectni nested array sifatida convert qilib qaytarsin.

# Masalan: objectToArray({a: 10, b: 20}) return [["a", 10], ["b", 20]]

# def objectToArray(obj):
#     return [[key, value] for key, value in obj.items()]


# print(objectToArray({"a": 10, "b": 20}))

# TASK O

# Array ichidagi har xil qiymatlardan faqat sonlar yig'indisini hisoblab qaytarsin.

# Masalan: calculateSumOfNumbers([10, "10", {son: 10}, true, 35]) return 45

# def calculate_sum_of_numbers(arr):
#     return sum(
#         item for item in arr
#         if isinstance(item, (int, float)) and not isinstance(item, bool)
#     )


# print(calculate_sum_of_numbers([10, "10", 11, {"son": 10}, True, 35]))  # 45


# project Standarts:
#  - Logging standarts:
#  - Naming standarts:
#     functiona, methods, variables => camelCase
#     classes => PascalCase
#     folders => kebab-case
#     css => snake-case
#  =Error handling standarts:


# TASK N

# Stringni palindrom ekanligini aniqlab true yoki false qaytarsin.

# Masalan: palindromCheck("dad") return true
# def palindromCheck(str):
#     str = str.lower()

#     return str == str[::-1]


# print(palindromCheck("dad"))


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

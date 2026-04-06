'''

🐍 DATA TYPES IN PYTHON
🎯 What is a Data Type?

👉 It tells what kind of value a variable holds

📦 MAIN DATA TYPES (You NEED these)
🔢 1. Integer (int)
x = 10

✔ Whole numbers (positive / negative)

🔢 2. Float (float)
pi = 3.14

✔ Decimal numbers

🔤 3. String (str)
name = "Rohith"

✔ Text (inside quotes)

✅ 4. Boolean (bool)
is_valid = True

✔ Only two values:

True
False

👉 Used in conditions (VERY important)

🧠 Check Data Type
x = 10
print(type(x))

Output:

<class 'int'>
🔄 TYPE CONVERSION (VERY IMPORTANT)
👉 Convert String → Int
x = "10"
y = int(x)
👉 Convert Int → Float
a = 5
b = float(a)
👉 Convert Number → String
num = 100
text = str(num)
⚠️ VERY IMPORTANT (COMMON ERROR)
age = input("Enter age: ")
print(type(age))

👉 Output:

str

⚠️ Input is ALWAYS string

✔ Correct:

age = int(input("Enter age: "))






Python groups data types into categories 👇

🔤 1. TEXT TYPE
👉 str (String)
name = "Rohith"

✔ Used for text
✔ Supports indexing & slicing

🔢 2. NUMERIC TYPES
👉 int, float, complex
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex

✔ complex is rarely used in DSA/ML

📦 3. SEQUENCE TYPES

👉 Ordered collection of items

🟢 List (MOST IMPORTANT for DSA)
arr = [1, 2, 3]

✔ Mutable (can change)
✔ Indexing allowed

🟢 Tuple
t = (1, 2, 3)

✔ Immutable (cannot change)

🟢 Range
r = range(5)

✔ Used in loops:

for i in range(5):
    print(i)
🗺️ 4. MAPPING TYPE
👉 Dictionary (dict)
student = {
    "name": "Rohith",
    "age": 20
}

✔ Key-value pairs
✔ Very important for hashing in DSA

🔗 5. SET TYPES
👉 set
s = {1, 2, 3}

✔ No duplicates
✔ Unordered

👉 frozenset
fs = frozenset([1, 2, 3])

✔ Immutable version of set
✔ Rarely used

✅ 6. BOOLEAN TYPE
👉 bool
is_valid = True

✔ Used in:

Conditions
Loops
Comparisons
💾 7. BINARY TYPES

👉 Used for raw data (advanced, not needed now)

🟢 bytes
b = b"hello"
🟢 bytearray
ba = bytearray(5)
🟢 memoryview
mv = memoryview(b"abc")

👉 ❗ Not needed for DSA/ML now

🚫 8. NONE TYPE
👉 NoneType
x = None

✔ Represents no value / empty

🧠 Example:
def func():
    pass

print(func())   # None


⚡ FULL SUMMARY 
Text	      str
Numeric	      int, float, complex
Sequence	  list, tuple, range
Mapping	      dict
Set	          set, frozenset
Boolean	      bool
Binary	      bytes, bytearray, memoryview
None	      NoneType

'''
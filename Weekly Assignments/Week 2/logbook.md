Notes

- Variables store values; name should be meaningful (e.g., age, score). Cannot start with digit or use special chars like &.

- Assignment uses =, e.g., x = 10, name = "Alice".

- Variables are dynamic: can change data types over time, e.g., x = 10 (int), then x = "hello" (str).

- Common data types: int, float, bool, str.

- e.g., x = 5 (int), price = 19.99 (float), is_valid = True (bool), name = "John" (str).

- Strings use quotes: 'single', "double", '''triple quotes'''.

- String operations:

- Concatenate: "Hello " + "World" → "Hello World".

- Repeat: "ha" * 3 → "hahaha".

- Lists group multiple values:

- e.g., numbers = [1, 2, 3].

- Lists are mutable: numbers[0] = 10.

- len() gives list/string length, e.g., len(name).

Examples

age = 20
age = age + 1  # updates age to 21
name = "Alice"
greeting = "Hi " + name  # concatenation
numbers = [1, 2, 3]
numbers.append(4)  # adds 4 at the end
length = len(numbers)  # returns 4
data_types = {
  'Python': ["Integer", "String", "Float", "Boolean"],
  'C++': ["Integer", "Float", "Char", "Bool", "Double"],
  'Java': ["Byte", "Short", "Int", "Long", "Float", "Double", "Boolean", "Char"]
}

data_type_descriptions = {
  'Python': {
      "Integer": "Integer (int): Represents whole numbers without a fractional component, e.g., -20, 0, 42.",
      "Float": "Floating Point (float): Represents real numbers with a fractional part, e.g., -0.1, 0.0, 3.14.",
      "String": "String (str): A sequence of Unicode characters, e.g., 'hello', '123'.",
      "Boolean": "Boolean (bool): A truth value, either True or False."
  },
  'C++': {
      "Integer": "Integer (int): Represents whole numbers without a fractional component, typically 32-bit, e.g., -42, 0, 42.",
      "Float": "Floating Point (float): Represents single-precision floating-point numbers, e.g., 3.14f.",
      "Char": "Character (char): Represents a single character stored as a small integer, e.g., 'a', '4'.",
      "Bool": "Boolean (bool): A truth value, either true or false.",
      "Double": "Double Precision Floating Point (double): Represents double-precision floating-point numbers, e.g., 3.1415926535."
  },
  'Java': {
      "Byte": "Byte: An 8-bit signed two's complement integer, e.g., -128, 0, 127.",
      "Short": "Short: A 16-bit signed two's complement integer, e.g., -32768, 0, 32767.",
      "Int": "Integer (int): A 32-bit signed two's complement integer, e.g., -2^31, 0, 2^31-1.",
      "Long": "Long: A 64-bit signed two's complement integer, e.g., -2^63, 0, 2^63-1.",
      "Float": "Floating Point (float): Represents single-precision 32-bit IEEE 754 floating-point numbers, e.g., 3.14f.",
      "Double": "Double Precision Floating Point (double): Represents double-precision 64-bit IEEE 754 floating-point numbers, e.g., 3.141592653589793.",
      "Boolean": "Boolean: Represents a truth value, either true or false.",
      "Char": "Character (char): Represents a single 16-bit Unicode character, e.g., 'A', '4'."
  }
}

quiz_questions = {
  'Python': {
      "Integer": [
          {
              "question": "In Python, which data type represents whole numbers like 42 and -99?",
              "options": ["int", "str", "float", "bool"],
              "answer": "int",
              "correct_detail": "Correct! Integers (int) are used in Python to represent whole numbers without any fractional part.",
              "incorrect_detail": "Incorrect! The correct answer is 'int'. Integers like 42 and -99 are whole numbers without decimal points."
          },
          {
              "question": "If a number has no fractional part in Python, what data type is it likely to be?",
              "options": ["Boolean", "String", "Integer", "Float"],
              "answer": "Integer",
              "correct_detail": "Correct! Numbers without fractional parts are typically integers in Python.",
              "incorrect_detail": "Incorrect! A number without a fractional part is best represented as an 'Integer', not a Float or any other type."
          },
          {
              "question": "Which of the following is an integer in Python: '3.14', 'True', '-20'?",
              "options": ["'3.14'", "'True'", "'-20'"],
              "answer": "'-20'",
              "correct_detail": "Correct! '-20' is an integer as it represents a whole number without a decimal.",
              "incorrect_detail": "Incorrect! The only integer here is '-20'. '3.14' is a float and 'True' is a boolean."
          },
          {
              "question": "What will be the data type of result in Python after this operation: 5 + 3?",
              "options": ["int", "str", "list", "tuple"],
              "answer": "int",
              "correct_detail": "Correct! The result of adding two integers (5 and 3) is an integer.",
              "incorrect_detail": "Incorrect! When you add two integers like 5 and 3, the result is also an integer."
          }
      ],
      "String": [
          {
              "question": "What type of data does the String (str) in Python represent?",
              "options": ["Unicode characters", "Whole numbers", "Boolean values", "Floating-point numbers"],
              "answer": "Unicode characters",
              "correct_detail": "Correct! A String (str) in Python represents a sequence of Unicode characters.",
              "incorrect_detail": "Incorrect! A String represents Unicode characters, not numbers or Boolean values."
          },
          {
              "question": "Which Python data type is represented by a sequence of characters like 'hello'?",
              "options": ["list", "str", "int", "dict"],
              "answer": "str",
              "correct_detail": "Correct! The 'str' type is used for sequences of characters like 'hello'.",
              "incorrect_detail": "Incorrect! Text like 'hello' is represented by the 'str' (string) data type."
          },
          {
              "question": "If you want to store the text '123' in Python, which data type do you use?",
              "options": ["int", "str", "bool", "float"],
              "answer": "str",
              "correct_detail": "Correct! Even though '123' looks like a number, if it's in quotes it's considered a string.",
              "incorrect_detail": "Incorrect! Text enclosed in quotes is treated as a string, so '123' should be stored as a 'str'."
          },
          {
              "question": "What is the result of type('Python') in Python?",
              "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
              "answer": "<class 'str'>",
              "correct_detail": "Correct! The type of 'Python' is a string since it's a sequence of characters in quotes.",
              "incorrect_detail": "Incorrect! The type('Python') function returns <class 'str'>, indicating it's a string."
          }
      ],
      "Float": [
          {
              "question": "Which Python data type is used to represent real numbers with a fractional part?",
              "options": ["int", "complex", "float", "decimal"],
              "answer": "float",
              "correct_detail": "Correct! A float in Python is used to represent real numbers that include a decimal point.",
              "incorrect_detail": "Incorrect! The correct answer is 'float', which is used for numbers with fractional parts."
          },
          {
              "question": "In Python, what is the data type of the number 3.14?",
              "options": ["Integer", "Float", "String", "Char"],
              "answer": "Float",
              "correct_detail": "Correct! The number 3.14 is a floating-point number, hence it is represented as a float.",
              "incorrect_detail": "Incorrect! The number 3.14, having a decimal, is a float, not an integer or string."
          },
          {
              "question": "Which of the following is a floating-point number in Python: 0, '3.14', 3?",
              "options": ["0", "'3.14'", "3"],
              "answer": "'3.14'",
              "correct_detail": "Correct! '3.14' is a string representation of a floating-point number.",
              "incorrect_detail": "Incorrect! While '3.14' is a string, it represents a float when not in quotes."
          },
          {
              "question": "What will be the data type of result in Python after this operation: 7 / 1?",
              "options": ["int", "str", "float", "complex"],
              "answer": "float",
              "correct_detail": "Correct! Division in Python always results in a float, even if both numbers are integers.",
              "incorrect_detail": "Incorrect! The division of two integers in Python results in a float, not an integer."
          }
      ],
      "Boolean": [
          {
              "question": "In Python, what is the Boolean (bool) data type used to represent?",
              "options": ["Text", "Whole numbers", "Truth values", "Fractional numbers"],
              "answer": "Truth values",
              "correct_detail": "Correct! The Boolean data type in Python is used to represent truth values (True or False).",
              "incorrect_detail": "Incorrect! Booleans represent truth values like True or False, not numeric or text data."
          },
          {
              "question": "Which Python data type represents the truth value of an expression?",
              "options": ["str", "bool", "int", "float"],
              "answer": "bool",
              "correct_detail": "Correct! A 'bool' represents the truth value, which can be either True or False.",
              "incorrect_detail": "Incorrect! The truth value of an expression is represented by 'bool', not other data types."
          },
          {
              "question": "In Python, what would be the data type of True?",
              "options": ["String", "Boolean", "Integer", "List"],
              "answer": "Boolean",
              "correct_detail": "Correct! 'True' is a Boolean value in Python, representing a truth value.",
              "incorrect_detail": "Incorrect! 'True' is specifically a Boolean value, not any other type."
          },
          {
              "question": "What will be the data type of the result in Python after evaluating: 5 == 5?",
              "options": ["int", "bool", "float", "NoneType"],
              "answer": "bool",
              "correct_detail": "Correct! The expression '5 == 5' evaluates to True, which is a Boolean value.",
              "incorrect_detail": "Incorrect! Comparisons in Python result in Boolean values, not integers or floats."
          }
      ],
      "String": [
          {
              "question": "What type of data does the String (str) in Python represent?",
              "options": ["Unicode characters", "Whole numbers", "Boolean values", "Floating-point numbers"],
              "answer": "Unicode characters",
              "correct_detail": "Correct! A String (str) in Python represents a sequence of Unicode characters.",
              "incorrect_detail": "Incorrect! A String represents Unicode characters, not numbers or Boolean values."
          },
          {
              "question": "Which Python data type is represented by a sequence of characters like 'hello'?",
              "options": ["list", "str", "int", "dict"],
              "answer": "str",
              "correct_detail": "Correct! The 'str' type is used for sequences of characters like 'hello'.",
              "incorrect_detail": "Incorrect! Text like 'hello' is represented by the 'str' (string) data type."
          },
          {
              "question": "If you want to store the text '123' in Python, which data type do you use?",
              "options": ["int", "str", "bool", "float"],
              "answer": "str",
              "correct_detail": "Correct! Even though '123' looks like a number, if it's in quotes it's considered a string.",
              "incorrect_detail": "Incorrect! Text enclosed in quotes is treated as a string, so '123' should be stored as a 'str'."
          },
          {
              "question": "What is the result of type('Python') in Python?",
              "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
              "answer": "<class 'str'>",
              "correct_detail": "Correct! The type of 'Python' is a string since it's a sequence of characters in quotes.",
              "incorrect_detail": "Incorrect! The type('Python') function returns <class 'str'>, indicating it's a string."
          }
      ],
      "Float": [
          {
              "question": "Which Python data type is used to represent real numbers with a fractional part?",
              "options": ["int", "complex", "float", "decimal"],
              "answer": "float",
              "correct_detail": "Correct! A float in Python is used to represent real numbers that include a decimal point.",
              "incorrect_detail": "Incorrect! The correct answer is 'float', which is used for numbers with fractional parts."
          },
          {
              "question": "In Python, what is the data type of the number 3.14?",
              "options": ["Integer", "Float", "String", "Char"],
              "answer": "Float",
              "correct_detail": "Correct! The number 3.14 is a floating-point number, hence it is represented as a float.",
              "incorrect_detail": "Incorrect! The number 3.14, having a decimal, is a float, not an integer or string."
          },
          {
              "question": "Which of the following is a floating-point number in Python: 0, '3.14', 3?",
              "options": ["0", "'3.14'", "3"],
              "answer": "'3.14'",
              "correct_detail": "Correct! '3.14' is a string representation of a floating-point number.",
              "incorrect_detail": "Incorrect! While '3.14' is a string, it represents a float when not in quotes."
          },
          {
              "question": "What will be the data type of result in Python after this operation: 7 / 1?",
              "options": ["int", "str", "float", "complex"],
              "answer": "float",
              "correct_detail": "Correct! Division in Python always results in a float, even if both numbers are integers.",
              "incorrect_detail": "Incorrect! The division of two integers in Python results in a float, not an integer."
          }
      ],

  "Boolean": [
          {
              "question": "In Python, what is the Boolean (bool) data type used to represent?",
              "options": ["Text", "Whole numbers", "Truth values", "Fractional numbers"],
              "answer": "Truth values",
              "correct_detail": "Correct! The Boolean data type in Python is used to represent truth values (True or False).",
              "incorrect_detail": "Incorrect! Booleans represent truth values like True or False, not numeric or text data."
          },
          {
              "question": "Which Python data type represents the truth value of an expression?",
              "options": ["str", "bool", "int", "float"],
              "answer": "bool",
              "correct_detail": "Correct! A 'bool' represents the truth value, which can be either True or False.",
              "incorrect_detail": "Incorrect! The truth value of an expression is represented by 'bool', not other data types."
          },
          {
              "question": "In Python, what would be the data type of True?",
              "options": ["String", "Boolean", "Integer", "List"],
              "answer": "Boolean",
              "correct_detail": "Correct! 'True' is a Boolean value in Python, representing a truth value.",
              "incorrect_detail": "Incorrect! 'True' is specifically a Boolean value, not any other type."
          },
          {
              "question": "What will be the data type of the result in Python after evaluating: 5 == 5?",
              "options": ["int", "bool", "float", "NoneType"],
              "answer": "bool",
              "correct_detail": "Correct! The expression '5 == 5' evaluates to True, which is a Boolean value.",
              "incorrect_detail": "Incorrect! Comparisons in Python result in Boolean values, not integers or floats."
          }
      ]

  },

  'C++': {
      "Integer": [
          {
              "question": "Which C++ data type is typically used to represent whole numbers without a fractional part?",
              "options": ["float", "char", "int", "bool"],
              "answer": "int",
              "correct_detail": "Correct! The 'int' data type in C++ is used to represent whole numbers without fractional components.",
              "incorrect_detail": "Incorrect! The correct answer is 'int'. It's used for whole numbers, unlike float or char."
          },
          {
              "question": "In C++, what data type is a 32-bit whole number?",
              "options": ["double", "char", "int", "long"],
              "answer": "int",
              "correct_detail": "Correct! An 'int' in C++ is typically a 32-bit whole number on most systems.",
              "incorrect_detail": "Incorrect! A 32-bit whole number is an 'int', not a double or a char."
          },
          {
              "question": "Which of the following is a correct representation of an integer in C++?",
              "options": ["42.0", "'A'", "true", "42"],
              "answer": "42",
              "correct_detail": "Correct! '42' is an integer, while '42.0' is a float, and 'A' is a char.",
              "incorrect_detail": "Incorrect! '42' is the only correct representation of an integer here."
          },
          {
              "question": "What is the result of the following C++ code: sizeof(int)? (Assuming 32-bit int)",
              "options": ["8", "4", "2", "1"],
              "answer": "4",
              "correct_detail": "Correct! The size of an 'int' is typically 4 bytes on a system with 32-bit integers.",
              "incorrect_detail": "Incorrect! The sizeof(int) is 4 bytes, not 8, 2, or 1 byte."
          }
      ],
  "Float": [
          {
              "question": "What precision does the 'float' data type provide in C++?",
              "options": ["Single", "Double", "Triple", "Quadruple"],
              "answer": "Single",
              "correct_detail": "Correct! A 'float' in C++ provides single precision for floating-point numbers.",
              "incorrect_detail": "Incorrect! The 'float' data type provides single, not double or higher, precision."
          },
          {
              "question": "Which of the following literals is a float type in C++?",
              "options": ["3.14f", "3", "3.14", "'3.14'"],
              "answer": "3.14f",
              "correct_detail": "Correct! The literal '3.14f' specifically denotes a float in C++.",
              "incorrect_detail": "Incorrect! '3.14f' is the notation used in C++ to specify a floating-point number as a float."
          },
          {
              "question": "In C++, which data type is used to store floating-point numbers with less memory?",
              "options": ["int", "double", "float", "long"],
              "answer": "float",
              "correct_detail": "Correct! The 'float' type uses less memory compared to 'double', which offers higher precision.",
              "incorrect_detail": "Incorrect! For less memory usage among floating-point types, use 'float', not 'double'."
          },
          {
              "question": "What is the size of a 'float' in C++ on most systems?",
              "options": ["8 bytes", "4 bytes", "2 bytes", "1 byte"],
              "answer": "4 bytes",
              "correct_detail": "Correct! A 'float' typically occupies 4 bytes of memory on most systems.",
              "incorrect_detail": "Incorrect! The size of a float is commonly 4 bytes, not 8, 2, or 1 byte."
          }
      ],
  "Char": [
          {
              "question": "In C++, the 'char' data type is used to store:",
              "options": ["Strings", "Single characters", "Integers", "Booleans"],
              "answer": "Single characters",
              "correct_detail": "Correct! 'Char' in C++ is specifically for storing single characters.",
              "incorrect_detail": "Incorrect! 'Char' stores single characters, not strings or integers."
          },
          {
              "question": "Which of the following represents a char in C++?",
              "options": ["'1'", "1", "\"1\"", "bool(1)"],
              "answer": "'1'",
              "correct_detail": "Correct! The character '1' is represented as '1' in C++ using single quotes.",
              "incorrect_detail": "Incorrect! A char is represented by single quotes, such as '1'."
          },
          {
              "question": "How much memory does a 'char' typically use in C++?",
              "options": ["4 bytes", "2 bytes", "1 byte", "8 bytes"],
              "answer": "1 byte",
              "correct_detail": "Correct! A 'char' typically occupies 1 byte of memory in C++.",
              "incorrect_detail": "Incorrect! The size of a char is 1 byte, not 2, 4, or 8 bytes."
          },
          {
              "question": "In C++, a 'char' is actually stored as:",
              "options": ["A string", "A boolean", "A small integer", "A floating-point number"],
              "answer": "A small integer",
              "correct_detail": "Correct! Internally, a 'char' is stored as a small integer representing Unicode or ASCII values.",
              "incorrect_detail": "Incorrect! A 'char' is stored as a small integer, not as a string or boolean."
          }
      ],
  "Bool": [
          {
              "question": "What are the possible values of the 'bool' data type in C++?",
              "options": ["Any integer", "0 and 1", "true and false", "Yes and No"],
              "answer": "true and false",
              "correct_detail": "Correct! The 'bool' data type in C++ can only be 'true' or 'false'.",
              "incorrect_detail": "Incorrect! The correct values for a 'bool' are 'true' and 'false', not numeric values."
          },
          {
              "question": "What is the size of a 'bool' data type in C++?",
              "options": ["1 bit", "8 bits", "16 bits", "Depends on the compiler"],
              "answer": "Depends on the compiler",
              "correct_detail": "Correct! The size of a 'bool' in C++ can depend on the compiler and the target architecture.",
              "incorrect_detail": "Incorrect! The size of a 'bool' is not fixed and can depend on the compiler settings."
          },
          {
              "question": "Which C++ operator can you use to get a boolean result?",
              "options": ["=", "+", "==", "%"],
              "answer": "==",
              "correct_detail": "Correct! The '==' operator compares two values and returns a boolean result.",
              "incorrect_detail": "Incorrect! The '==' operator is used for comparisons and returns a boolean, not '=' or '+'."
          },
          {
              "question": "In C++, what is the result type of the expression (7 > 3)?",
              "options": ["int", "float", "bool", "char"],
              "answer": "bool",
              "correct_detail": "Correct! The expression '7 > 3' evaluates to a boolean value 'true'.",
              "incorrect_detail": "Incorrect! Comparisons like '7 > 3' return a boolean value, indicating whether the statement is true or false."
          }
      ],
  "Double": [
          {
          "question": "What is the primary use of the 'double' data type in C++?",
          "options": ["To store large integers", "Manages boolean value", "Precise float numbers", "To handle characters"],
          "answer": "Precise float numbers",
          "correct_detail": "Correct! The 'double' data type is used for high-precision floating-point numbers, allowing for more significant digits than 'float'.",
          "incorrect_detail": "Incorrect! The 'double' data type is specifically used for high-precision floating-point numbers, not integers or characters."
          },
          {
          "question": "How much memory does a 'double' data type typically use on a 64-bit system?",
          "options": ["8 bytes", "4 bytes", "16 bytes", "2 bytes"],
          "answer": "8 bytes",
          "correct_detail": "Correct! On most 64-bit systems, a 'double' occupies 8 bytes of memory.",
          "incorrect_detail": "Incorrect! A 'double' typically uses 8 bytes of memory on a 64-bit system, not 4, 16, or 2 bytes."
          },
          {
          "question": "Which of the following literals is correctly defined as a double in C++?",
          "options": ["3.14f", "3.14", "314e-2", "'3.14'"],
          "answer": "3.14",
          "correct_detail": "Correct! '3.14' without an 'f' suffix is treated as a double in C++.",
          "incorrect_detail": "Incorrect! '3.14' without the 'f' suffix is recognized as a double, not as a float or string."
          },
          {
          "question": "What is the main difference in precision between a 'float' and a 'double' in C++?",
          "options": ["Floats are more precise", "Doubles are more precise", "Has same precision", "System decides Precision"],
          "answer": "Doubles are more precise",
          "correct_detail": "Correct! A 'double' provides more precision than a 'float' due to its larger size.",
          "incorrect_detail": "Incorrect! The 'double' data type offers more precision than a 'float' because it uses more memory."
          }
      ]
  },

  'Java':{


  "Byte": [
          {
              "question": "What is the range of a byte data type in Java?",
              "options": ["-128 to 127", "-32768 to 32767", "-2147483648 to 2147483647", "-9223372036854775808 to 9223372036854775807"],
              "answer": "-128 to 127",
              "correct_detail": "Correct! A byte in Java has a range of -128 to 127, making it suitable for very small integer values.",
              "incorrect_detail": "Incorrect! The correct range of a byte is -128 to 127, not the other listed ranges."
          },
          {
              "question": "How many bits are used to represent a byte in Java?",
              "options": ["8 bits", "16 bits", "32 bits", "64 bits"],
              "answer": "8 bits",
              "correct_detail": "Correct! A byte in Java is represented using 8 bits.",
              "incorrect_detail": "Incorrect! A byte in Java uses 8 bits, not 16, 32, or 64 bits."
          },
          {
              "question": "Which of the following Java data types has the smallest range?",
              "options": ["byte", "short", "int", "long"],
              "answer": "byte",
              "correct_detail": "Correct! The byte data type has the smallest range among the options, suitable for very small integers.",
              "incorrect_detail": "Incorrect! The smallest range among these types is the byte, not short, int, or long."
          },
          {
              "question": "In Java, which keyword would you use to define a variable that holds an 8-bit signed integer?",
              "options": ["int", "short", "byte", "long"],
              "answer": "byte",
              "correct_detail": "Correct! The 'byte' keyword is used for declaring an 8-bit signed integer in Java.",
              "incorrect_detail": "Incorrect! To define an 8-bit signed integer, the 'byte' keyword is used, not int, short, or long."
          }
      ],
  "Short": [
          {
              "question": "In Java, which data type would you choose to save memory in large arrays of numbers with a wider range than byte?",
              "options": ["int", "short", "byte", "long"],
              "answer": "short",
              "correct_detail": "Correct! The 'short' data type uses less memory than an 'int' and has a wider range than a 'byte'.",
              "incorrect_detail": "Incorrect! To save memory while needing a range wider than byte, 'short' is more suitable than int or long."
          },
          {
              "question": "What is the bit length of a short data type in Java?",
              "options": ["8", "16", "32", "64"],
              "answer": "16",
              "correct_detail": "Correct! A 'short' in Java is a 16-bit signed two's complement integer.",
              "incorrect_detail": "Incorrect! The 'short' data type is 16 bits, not 8, 32, or 64 bits."
          },
          {
              "question": "Which Java data type is a 16-bit signed two's complement integer?",
              "options": ["byte", "short", "int", "long"],
              "answer": "short",
              "correct_detail": "Correct! The 'short' data type is a 16-bit integer, making it larger than a byte but smaller than an int.",
              "incorrect_detail": "Incorrect! The 'short' data type is defined as a 16-bit integer, not byte, int, or long."
          },
          {
              "question": "If a Java integer variable does not require the full range of an int, what is the next smallest data type you could use?",
              "options": ["byte", "short", "float", "char"],
              "answer": "short",
              "correct_detail": "Correct! If the full range of an int is not needed, using a 'short' can save memory space.",
              "incorrect_detail": "Incorrect! The next smallest type after an int for integers is 'short', not byte or float."
          }
      ],

  "Int": [
      {
          "question": "Which Java data type is a 32-bit signed two's complement integer?",
          "options": ["byte", "short", "int", "long"],
          "answer": "int",
          "correct_detail": "Correct! In Java, an 'int' is a 32-bit signed two's complement integer, used for numerical data that doesn't require the larger size of a 'long'.",
          "incorrect_detail": "Incorrect! The 'int' type is specifically a 32-bit signed integer, not byte, short, or long."
      },
      {
          "question": "What is the default data type of the numbers 123 in Java?",
          "options": ["byte", "short", "int", "long"],
          "answer": "int",
          "correct_detail": "Correct! The number 123 is treated as an 'int' by default in Java, as are all integer literals without a specific type designation.",
          "incorrect_detail": "Incorrect! By default, integer numbers without any suffix are considered 'int' in Java."
      },
      {
          "question": "What is the size in bits of an int data type in Java?",
          "options": ["8", "16", "32", "64"],
          "answer": "32",
          "correct_detail": "Correct! An 'int' in Java occupies 32 bits, which is standard for storing medium-sized integers.",
          "incorrect_detail": "Incorrect! An 'int' uses 32 bits, not 8, 16, or 64 bits."
      },
      {
          "question": "What would be the result of this Java operation: Math.min(Integer.MIN_VALUE, 0)?",
          "options": ["0", "Integer.MAX_VALUE", "Integer.MIN_VALUE", "An error"],
          "answer": "Integer.MIN_VALUE",
          "correct_detail": "Correct! The Math.min function returns the smaller of the two arguments, and Integer.MIN_VALUE (-2^31) is less than 0.",
          "incorrect_detail": "Incorrect! Integer.MIN_VALUE is smaller than 0, hence it is the minimum in this context, not Integer.MAX_VALUE or an error."
      }
  ],

  "Long": [
      {
          "question": "What is the range of a long data type in Java?",
          "options": ["-9223372036854775808 to 9223372036854775807", "-2147483648 to 2147483647", "-32768 to 32767", "-128 to 127"],
          "answer": "-9223372036854775808 to 9223372036854775807",
          "correct_detail": "Correct! A 'long' in Java is a 64-bit signed integer, allowing for a large range of values from about -9.22 quintillion to 9.22 quintillion.",
          "incorrect_detail": "Incorrect! The range for a 'long' is much wider than for types like int or short, covering -9.22 quintillion to 9.22 quintillion."
      },
      {
          "question": "How would you define a long literal with the value 100 in Java?",
          "options": ["100", "100L", "100l", "100.0"],
          "answer": "100L",
          "correct_detail": "Correct! Long literals in Java are suffixed with 'L' or 'l', with '100L' being a common convention to specify the literal as a long.",
          "incorrect_detail": "Incorrect! To explicitly declare a numeric literal as a long, use the suffix 'L', making '100L' the correct form."
      },
      {
          "question": "Which Java data type is the best choice for an identifier for a bank account balance?",
          "options": ["int", "float", "double", "long"],
          "answer": "long",
          "correct_detail": "Correct! A 'long' is suitable for a bank account balance, as it can handle large integers securely without the risk of overflow, unlike 'int'.",
          "incorrect_detail": "Incorrect! For large integers such as a bank account balance, 'long' is preferable over 'int' or floating-point types like 'float' or 'double'."
      },
      {
          "question": "In Java, which keyword would you use for a variable that holds a 64-bit integer?",
          "options": ["int", "short", "byte", "long"],
          "answer": "long",
          "correct_detail": "Correct! The 'long' keyword is used in Java to declare variables that need to store 64-bit integers.",
          "incorrect_detail": "Incorrect! For storing 64-bit integers, the correct keyword is 'long', not 'int', 'short', or 'byte'."
      }
  ],
  "Float": [
      {
          "question": "In Java, which data type is used for precision up to 6-7 decimal places?",
          "options": ["float", "double", "BigDecimal", "int"],
          "answer": "float",
          "correct_detail": "Correct! A 'float' in Java provides precision up to 6-7 decimal places and is useful for saving memory when high precision is not required.",
          "incorrect_detail": "Incorrect! While 'double' provides higher precision, a 'float' is sufficient for up to 6-7 decimal places."
      },
      {
          "question": "Which of the following literals is a float type in Java?",
          "options": ["3.14", "3.14f", "3.14d", "3.14F"],
          "answer": "3.14f",
          "correct_detail": "Correct! In Java, floating-point literals are double by default. The 'f' or 'F' suffix explicitly makes them float.",
          "incorrect_detail": "Incorrect! The suffix 'f' or 'F' is required to denote a floating-point literal as a 'float' explicitly."
      },
      {
          "question": "What is the size of a float in Java?",
          "options": ["32 bits", "64 bits", "16 bits", "8 bits"],
          "answer": "32 bits",
          "correct_detail": "Correct! A 'float' in Java uses 32 bits, which is sufficient for storing floating-point numbers with moderate precision.",
          "incorrect_detail": "Incorrect! A 'float' is a 32-bit IEEE 754 floating-point. It is not 64, 16, or 8 bits."
      },
      {
          "question": "Which Java data type is less precise than a double but uses less memory?",
          "options": ["int", "long", "short", "float"],
          "answer": "float",
          "correct_detail": "Correct! A 'float' uses less memory and is less precise than a 'double', making it a good choice for less critical applications.",
          "incorrect_detail": "Incorrect! Among the given options, 'float' is less precise than 'double' and also uses less memory."
      }
  ],

  "Double": [
      {
          "question": "In Java, which data type is used for precision up to 15-16 decimal places?",
          "options": ["float", "double", "BigDecimal", "int"],
          "answer": "double",
          "correct_detail": "Correct! The 'double' data type provides precision up to 15-16 decimal places, suitable for most scientific calculations.",
          "incorrect_detail": "Incorrect! For precision up to 15-16 decimal places, 'double' is the appropriate choice, not 'float' or 'BigDecimal'."
      },
      {
          "question": "What is the default type for a floating-point number in Java?",
          "options": ["float", "double", "BigDecimal", "int"],
          "answer": "double",
          "correct_detail": "Correct! By default, floating-point numbers without a suffix in Java are treated as 'double'.",
          "incorrect_detail": "Incorrect! Without any suffix, floating-point literals are considered 'double' in Java, not 'float' or 'BigDecimal'."
      },
      {
          "question": "How much memory does a 'double' consume in Java?",
          "options": ["64 bits", "32 bits", "16 bits", "128 bits"],
          "answer": "64 bits",
          "correct_detail": "Correct! A 'double' in Java occupies 64 bits, allowing for high precision and large range values.",
          "incorrect_detail": "Incorrect! A 'double' consumes 64 bits of memory, not 32, 16, or 128 bits."
      },
      {
          "question": "Which data type would you use in Java to store the value of pi with great precision?",
          "options": ["int", "long", "float", "double"],
          "answer": "double",
          "correct_detail": "Correct! For high precision, such as storing the value of pi accurately, 'double' is the best choice in Java.",
          "incorrect_detail": "Incorrect! 'double' is the most suitable for high precision values like pi, not 'float', 'int', or 'long'."
      }
  ],

  "Boolean": [
      {
          "question": "In Java, which data type represents one bit of information?",
          "options": ["int", "char", "byte", "boolean"],
          "answer": "boolean",
          "correct_detail": "Correct! The 'boolean' data type in Java is used to represent one bit of information, indicating true or false.",
          "incorrect_detail": "Incorrect! The 'boolean' type is used for representing one bit of truth value information, not 'int', 'char', or 'byte'."
      },
      {
          "question": "Which Java data type is used to represent true/false values?",
          "options": ["bit", "bool", "boolean", "binary"],
          "answer": "boolean",
          "correct_detail": "Correct! The 'boolean' data type is specifically used for true/false values in Java.",
          "incorrect_detail": "Incorrect! The correct data type for representing true/false values in Java is 'boolean'."
      },
      {
          "question": "What will the following Java expression return: 10 > 9?",
          "options": ["true", "false", "1", "0"],
          "answer": "true",
          "correct_detail": "Correct! The expression '10 > 9' evaluates to true because 10 is greater than 9.",
          "incorrect_detail": "Incorrect! The expression '10 > 9' evaluates to 'true', not 'false', '1', or '0'."
      },
      {
          "question": "Which of the following is a valid Boolean literal in Java?",
          "options": ["True", "0", "None", "false"],
          "answer": "false",
          "correct_detail": "Correct! 'false' is a valid Boolean literal in Java. Note that Boolean literals in Java are always in lowercase.",
          "incorrect_detail": "Incorrect! The correct Boolean literals in Java are 'true' and 'false', both in lowercase."
      }
  ],

  "Char": [
      {
          "question": "What does the char data type in Java represent?",
          "options": ["A character", "A number", "A boolean", "A string"],
          "answer": "A character",
          "correct_detail": "Correct! The 'char' data type in Java is used to store a single 16-bit Unicode character.",
          "incorrect_detail": "Incorrect! The 'char' type represents a single character, not a number, boolean, or string."
      },
      {
          "question": "How is the char data type stored in Java?",
          "options": ["As a 16-bit Unicode character", "As an 8-bit ASCII value", "As a 32-bit integer", "As a single bit"],
          "answer": "As a 16-bit Unicode character",
          "correct_detail": "Correct! In Java, 'char' is a 16-bit data type used to store Unicode characters.",
          "incorrect_detail": "Incorrect! The 'char' in Java is stored as a 16-bit Unicode character, not as an 8-bit ASCII value, a 32-bit integer, or a single bit."
      },
      {
          "question": "What is the output of this Java code: (char) 65?",
          "options": ["65", "'A'", "Error", "True"],
          "answer": "'A'",
          "correct_detail": "Correct! Casting the integer 65 to 'char' in Java will output 'A', which is the ASCII and Unicode representation of 65.",
          "incorrect_detail": "Incorrect! The expression '(char) 65' converts the integer 65 to the character 'A', not '65', 'Error', or 'True'."
      },
      {
          "question": "Which Java data type is suitable for storing letters and digits as characters?",
          "options": ["byte", "int", "char", "string"],
          "answer": "char",
          "correct_detail": "Correct! The 'char' data type is specifically designed to store individual characters, including letters and digits.",
          "incorrect_detail": "Incorrect! To store single characters, such as letters and digits, use 'char', not 'byte', 'int', or 'string'."
      }
  ]
}
}
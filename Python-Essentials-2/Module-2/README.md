Let us look at some of the built-in exceptions :

1. ArithmeticError
    - Location: BaseException ← Exception ← ArithmeticError
    - Description: an abstract exception including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain

2. AssertionError
    - Location: BaseException ← Exception ← AssertionError
    - Description: a concrete exception raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string

3. BaseException
    - Location: BaseException
    - Description: the most general (abstract) of all Python exceptions – all other exceptions are included in this one; it can be said that the following two except branches are equivalent: except: and except BaseException:.

4. IndexError
    - Location: BaseException ← Exception ← LookupError ← IndexError
    - Description: a concrete exception raised when you try to access a non-existent sequence's element (e.g., a list's element)

5. KeyboardInterrupt
    - Location: BaseException ← KeyboardInterrupt
    - Description: a concrete exception raised when the user uses a keyboard shortcut designed to terminate a program's execution (Ctrl-C in most OSs); if handling this exception doesn't lead to program termination, the program continues its execution.
    - Note: this exception is not derived from the Exception class. Run the program in IDLE.

6. LookupError
    - Location: BaseException ← Exception ← LookupError
    - Description: an abstract exception including all exceptions caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)

7. MemoryError
    - Location: BaseException ← Exception ← MemoryError
    - Description: a concrete exception raised when an operation cannot be completed due to a lack of free memory.

8. OverflowError
    - Location: BaseException ← Exception ← ArithmeticError ← OverflowError
    - Description: a concrete exception raised when an operation produces a number too big to be successfully stored

9. ImportError
    - Location: BaseException ← Exception ← StandardError ← ImportError
    - Description: a concrete exception raised when an import operation fails

10. KeyError
    - Location: BaseException ← Exception ← LookupError ← KeyError
    - Description: a concrete exception raised when you try to access a non-existent element in a collection (e.g., a dictionary's element)
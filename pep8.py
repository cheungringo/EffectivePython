# pep8 = Python Enhancement Proposal 8 (PEP 8)
# allows you to share code with other Python developers
# and everyone will be using the same style
# kind of like speaking a popular dialect of Chinese
# or American English
# https://www.python.org/dev/peps/pep-0008/

# 1. Use 4 spaces instead of tabs per indentation level
# 2. Lines should be 79 characters long or les
# 3. Two blank lines should be used to separate functions and classes
# 4. Continuations of long expressions onto additional lines should be
#     indented by 4 spaces from the previous line
# 5. In a class, methods should be separated by a single blank line
# 6. Don't put spaces around list indexes, function calls, or keyword argument
#     assignments
# 7. Put one and only one space before and after assignment operators

# Naming
# 1. Functions, variables, and attributes should be in lowercase_underscore
#     format
# 2. Protected instance attributes should be in _leading_underscore format
# 3. Private instance attributes should be in __double_leading_underscore
#     format
# 4. Classes and exceptions should be in CapitalizedWord format
# 5. Module-level constants should be in ALL_CAPS format
# 6. Instance methods in classes should use self as the name of the first
#     parameter
# 7. Class methods should use cls as the name of the first parameter

# Expressions and Statements
# 1. Use inline negation (if a is not b) instead of negation of positive
#     expressions (if not a is b)
# 2. Don't check for empty values (like [] or '') by checking the length
#     (if len(somelist) == 0) use if not somelist and assume empty values
#     will evaluate to False
# 3. The same thing goes for non-empty values (like [1] or 'hi').
#     The statement if somelist is implicitly True for non-empty values.
# 5. Avoid single-line if statements, for and while loops, and except compound
#     statements. Spread these over multiple lines for clarity.
# 6. Always put import statements at the top of a file.
# 7. Always use absolute names for modules when importing them, not
#     relative names.
# 8. If you must do relative imports, use the explicit syntax from . import foo
# 9. Imports should bein sections in the following order:
#     1. standard library imports
#     2. related third party imports
#     3. local application/library specific imports
#     Each subsection should have imports in alphabetical order.

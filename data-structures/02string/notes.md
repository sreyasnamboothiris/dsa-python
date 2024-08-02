# String
A string is a sequence of characters, typically used to represent text. It allows for the manipulation and processing of textual data in computer programs.

## Operations on String:
- **Concatenation:** Joining two strings together.
- **Comparison:** Comparing two strings lexicographically.
- **Substring extraction:** Extracting a substring from a string.
- **Search:** Searching for a substring within a string.
- **Modification:** Changing or replacing characters within a string.

## Applications of String:
- Text processing.
- Pattern matching.
- Data validation.
- Database management.

## Time Complexity:
- **Access:** O(1) (for indexing, assuming immutable string in some languages)
- **Search:** O(n)
- **Concatenation:** O(n + m) (for concatenating two strings of length n and m)
- **Substring:** O(k) (for creating a substring of length k)
- **Insertion:** O(n + m) (for inserting a string of length m into another string of length n)
- **Deletion:** O(n) (for deleting part of a string)

## Space Complexity:
- **Space Complexity:** O(n) (for storing n characters)
- **Auxiliary Space:** O(1) (if in-place operations are possible), O(n) (for creating new strings)
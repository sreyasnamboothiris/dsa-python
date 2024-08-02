# Hash Table

A hash table is a data structure that uses hash functions to map keys to values. It provides efficient insertion, deletion, and lookup operations.

## Characteristics of Hash Table:
- **Hash Function:** Computes an index into an array of buckets or slots.
- **Dynamic Size:** Can resize as needed to handle more elements.
- **Collision Handling:** Mechanisms to handle cases where different keys map to the same index (e.g., chaining, open addressing).

## Operations on Hash Table:
- **Insert:** Adding a key-value pair to the table.
- **Delete:** Removing a key-value pair from the table.
- **Search:** Finding the value associated with a key.
- **Update:** Modifying the value associated with a key.

## Applications of Hash Table:
- Implementing associative arrays (dictionaries).
- Database indexing.
- Caching (e.g., memoization).
- Implementing sets with fast membership testing.

## Operations on Hash Table:
- **Insert:** Adding a key-value pair to the table.
  - Average Time Complexity: O(1)
  - Worst Time Complexity: O(n) (due to collisions)
- **Delete:** Removing a key-value pair from the table.
  - Average Time Complexity: O(1)
  - Worst Time Complexity: O(n) (due to collisions)
- **Search:** Finding the value associated with a key.
  - Average Time Complexity: O(1)
  - Worst Time Complexity: O(n) (due to collisions)
- **Update:** Modifying the value associated with a key.
  - Average Time Complexity: O(1)
  - Worst Time Complexity: O(n) (due to collisions)
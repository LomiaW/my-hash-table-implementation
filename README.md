# Hash Table Implementation in Python

## What is a Hash Table?

A table is an unordered collection of records.
A hash table is a data structure that maps the keys of records to the locations in it.

## Load Factor

$\lambda = \frac{\text{Number of Records}}{\text{Number of Locations}}\$

## Hash Function

A hash function is a function that maps keys to locations in a hash table.

## Collision

When two keys have the same hash index in a hash table, it is called a collision.

## Collision Resolution

### Close Addressing

In close addressing, all the records with the same hash index are stored in the same location using a linked list. This method is also called $chaining$.

### Open Addressing

In open addressing, all the records with the same hash index are stored in different locations. This method is also called $probing$.

 - Simple Probing
 - Tombstone Probing
   - Quadratic Probing
   - Double Hashing
   
Probing Sequence: $h(k, i) = (h'(k) + f(i)) \mod m$
or {hash(k), (hash(k)+1)%m, (hash(k)+2)%m, ...}

Quadratic Probing: $f(i) = i^2$
{hash(k), (hash(k)+1)%m, (hash(k)+4)%m, (hash(k)+9)%m, ...}

Double Hashing: $f(i) = i \times hash_2(k)$
{hash(k), (hash(k)+hash_2(k))%m, (hash(k)+2*hash_2(k))%m, ...}

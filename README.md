### Tortoise & Hare

This is a quick implementation of the tortoise & hare cycle detection algorithm for linked lists.

## How it works.

We create two pointers to the head node, one a tortoise and the other a hare.

Each time we iterate, the tortoise will move one node further in the list. The hare will move two nodes.

Since our tortoise is always moving faster than the hare, the only way for them to be pointing at the same thing is if a cycle exists.
# Logi
Version 1.0
## Description
Logi is a language to describe logic gate circurts.
## How to use?
**[instructions]**
```
new # To add a logic gate or a node
mod # To modify a logic gate or a node
```
Examples:
```
# To make a Half Adder
new node a 1 # Add a node names a, truth value is True
new node b 0 # Add a node names b, truth value is False
new xor X a, b # Add a xor gate, input lines is a and b
new and S a, b # Add an and gate, input lines is a and b
mod node b 1 # Modify b turn to True
```
Gates Components:
```
Gate
    - Gate Type: AND, OR, NOT, XOR
    - Gate Name: convinent to modify it and it is the node which outputs
    - Input Lines: except NOT is 1 input line, at least 2 input lines
    - Output Line: a node, you can connect it to other gates

Node
    - Node Name: convinent to modify it
    - Node Truth Value: (You can use these standard in the code)
        - True: True / T / 1
        - False: False / F / 0
```

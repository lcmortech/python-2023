# What is a node?
# The value and the pointer together make up the node, which itself is a dictonary in code

# EX:
# {
#   "value": 4,
#   "next": None
#  }

# A full linked list in code
head: {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": {
                    # tail node
                    "value": 4,
                    next: None
                }
            }
        }
    }
}

print([head]["next"]["next"]["value"])

# This will only run with a Linked List
# print(my_linked_list.head.next.next.value)
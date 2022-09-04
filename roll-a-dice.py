import random

response = "y"

while response == "y":
    r = random.randint(1,6)
    if r == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif r == 2:
        print("[    0]")
        print("[     ]")
        print("[0    ]")
    elif r == 3:
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")
    elif r == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    elif r == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    elif r == 6:
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
    response = input("Roll again?:")

    
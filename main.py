import sys
import random
from typing import Any

from Application import Application
from SetupFunctions import SetupFunctions

def println(a: Any):
    print(str(a))

def init():
    d1 = {"name": "Ryan", "age": 26, "isDeveloper": True}
    d2 = {"name": "James", "Age": 21, "isDeveloper": False}
    d3 = {"name": "Paul", "Age": 22, "isDeveloper": True}

    names = {"1": d1, "2": d2, "3": d3}

    listName = random.choice(list(names))

    name = names[listName]

    if name.get("isDeveloper"):

        for k, v in name.items():
            names_list_created = SetupFunctions.NamePicked(v)
            print(f"{k} | {names_list_created.get()}")

        println("Successfully Got Value from Dictionary")
        sys.exit(0)
    else:
        println("Error Getting Values from Dictionary")
        sys.exit(1)

def main():

    app = Application(init())
    app.get()


if __name__ == "__main__":
    main()
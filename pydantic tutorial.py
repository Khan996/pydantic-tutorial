
"""Why Pydnatic is required?"""

# def insert_data(name, age):
#     print(name)
#     print(age)
#     print("Data inserted into database")



# insert_data("Babar", "thirty-three")

# def insert_data(name: str, age: int) -> None:
#     print(name)
#     print(age)
#     print("Data inserted into database")

# insert_data("Babar", 45)
# insert_data("Babar", "45")

def insert_data(name:  str, age: int) -> None:

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative")

        else:
            print(name)
            print(age)
            print("Data inserted into database")
    else:
        raise TypeError("Typing mistake")

insert_data("Babar", 56)
insert_data("Babar", -44)
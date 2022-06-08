from Bank import Bank

class Owner():
    def __init__(self):
        pass

    @classmethod
    def find_owner(cls, id_number):
        owners_dict = {}
        with open("/Users/evangarcia/code-platoon/week3/day2/oop-bank-accounts/support/owners.csv") as owners:
            for row in owners.readlines():
                owner = row.strip().split(",")
                owners_dict[owner[0]] = owner[1:]

        return owners_dict[id_number]


# test = Owner()

# print(test.owners_dict['14'])


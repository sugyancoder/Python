# ex 1

def add(*nums):
   total = 0
   for num in nums:
       total += num
   return total

print(add(1, 2, 3, 4))

# ex 2

def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Dr.", "Mifam", "Dorje", "Lama", "I")

# Kwargs
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

print_address(street="luzernerst.27",
              pobox="P.O Box 777",
              city="Luzern",
              zip="4806")

# Exercise
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Sugyan", "Lama",
               street="123 Fake St.",
               city="Detroit",
               state="MI",
               zip="54321")
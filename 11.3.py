def is_even(number: int) -> bool:
    """Перевірка на парність.
    """
    return (number & 1) == 0

print(is_even(2494563894038**2))# == True, 'Test1'
print(is_even(1056897**2))# == False, 'Test2'
print(is_even(24945638940387**3))# == False, 'Test3'
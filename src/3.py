def get_random_code():
    import random
    letters = ['a', 'b', 'c', 'd', 'e']
    numbers = [1, 2, 3, 4, 5]
    return f'{random.choice(letters)}{random.randint(0,9)}{random.choice(letters)}{random.randint(0,9)}'

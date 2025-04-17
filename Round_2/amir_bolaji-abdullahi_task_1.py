def pattern_gen(n): 
    num_of_stars = 1
    num_of_spaces =  n
    for _ in range(n): 
        print(" " * num_of_spaces, "*" * num_of_stars)
        num_of_stars += 2
        num_of_spaces -= 1

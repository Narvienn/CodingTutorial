"""A flight company has a library of films to show its customers on long flights. Design a system that would select
exactly two films per flight based on the duration of the flight - the running time of both films needs to be
equal to the flight duration."""
# target = flight times
# def solution(library of films, target)
# aim for a solution of n*n solution or better (e.g. for x for y


flight_time = 180 # just one flight - once there is a function, we can run it on however many flight time instances
films = [40, 60, 80, 90, 100, 110, 115] # a list of film lengths in minutes

# 30, 30 - 60 --> that means film1 == film2, which we need to avoid


def solution(films, target):
    for index1, f1 in enumerate(films): # enumerate: built-in function that returns value of item and counter in list
        for index2, f2 in enumerate(films): # O(n*n)
            if f1 + f2 == target and not (index1 is index2):
                return f1, f2
    return [] # Q: What are we returning here if return f1, f2 is already defined?


def solution2(films, target):
    flights = { } # a hash map / dictionary - reduced space complexity as there is one variable less to save/read
    for f1 in films: # O(n)
        if f1 not in flights:
            flights[f1] = target - f1
        else:
            return f1, target - f1
    return []
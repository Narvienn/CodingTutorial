"""A flight company has a library of films to show its customers on long flights. Design a system that would select
exactly two films per flight based on the duration of the flight - the running time of both films needs to be shorter
or equal to the flight duration."""
# target = flight times
# def function(library of films, target) <-- WHY this function + these arguments?
# aim for a solution of n*n solution or better (e.g. for x for y)


import random

flight_times = [180, 240, 280, 360, 440, 550] # a list of flight lengths in minutes
films = [40, 60, 85, 90, 100, 110, 115] # a list of film lengths in minutes

film = random.choice(films)
film2 = []


# film1 != film2
# Q2: Where + How to insert this condition? try/except? while?

for flight in flight_times:
    for film in films:
        # iterate over films to find a film2 value so that film + film2 <= flight
        #Q: Unacceptable because that makes it O(n*3) complexity

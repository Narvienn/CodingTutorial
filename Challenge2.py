"""A flight company has a library of films to show its customers on long flights. Design a system that would select
exactly two films per flight based on the duration of the flight - the running time of both films needs to be shorter
or equal to the flight duration."""
# target = flight times
# def function(library of films, target):
# aim for a solution of n*n solution or better (e.g. for x for y)

import random

flight_times = [120, 180, 240, 280, 360, 440, 550] # a list of flight lengths in minutes
films = [40, 60, 85, 90, 100, 110, 115] # a list of film lengths in minutes

# for an item from flight_times - iterate over films to find item1 + item2 =< flight_time


film1 = random.choice(films) # randomly selects the first film to display


for flight in flight_times:
    if film1 >= flight:
        # randomly select another film
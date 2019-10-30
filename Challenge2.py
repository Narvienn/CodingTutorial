"""A flight company has a library of films to show its customers on long flights. Design a system that would select
exactly two films per flight based on the duration of the flight - the running time of both films needs to be shorter
or equal to the flight duration."""
# target = flight times
# def function(library of films, target):
# aim for a solution of n*n solution or better (e.g. for x for y)

import random

flight_times = [180, 240, 280, 360, 440, 550] # a list of flight lengths in minutes
films = [40, 60, 85, 90, 100, 110, 115] # a list of film lengths in minutes

film1 = random.choice(films) # randomly selects the first film to display
film2 = int # placeholder for 'an unspecified item from films'

while film1 == film2:
    # randomly select another film here

# or: try / except syntax?


def suggest_films(flight_times, films):
    for flight in flight_times:
        for film in films:
            """ if film1 + film2 =< flight
                return film1, film2"""



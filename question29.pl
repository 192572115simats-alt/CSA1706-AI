planet(mercury, 1, 0).
planet(venus, 2, 0).
planet(earth, 3, 1).
planet(mars, 4, 2).
planet(jupiter, 5, 95).
planet(saturn, 6, 146).
planet(uranus, 7, 28).
planet(neptune, 8, 16).

planet_position(Name, Position) :-
    planet(Name, Position, _).

planet_moons(Name, Moons) :-
    planet(Name, _, Moons).
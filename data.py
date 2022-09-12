from re import I


class DataStructures:
        escort = [  'Circuit Royal', 
                    'Dorado', 
                    'Havana', 
                    'Junkertown', 
                    'Rialto', 
                    'Route 66',
                    'Gothenburg']

        hybrid = [  'Blizzard World', 
                    'Eichenwalde', 
                    'Hollywood', 
                    'King\'s Row', 
                    'Midtown', 
                    'Numbani', 
                    'Paraiso']

        control = [ 'Busan', 
                    'Ilios', 
                    'Lijiang Tower', 
                    'Nepal', 
                    'Oasis']

        push = [    'Colosseo', 
                    'New Queen Street', 
                    'Portugal']

        tank = [    'D.Va', 
                    'Doomfist',
                    'Junker Queen', 
                    'Orisa', 
                    'Reinhardt', 
                    'Roadhog', 
                    'Sigma', 
                    'Winston', 
                    'Wrecking Ball', 
                    'Zarya'] 

        dps = [     'Ashe', 
                    'Bastion', 
                    'Cassidy', 
                    'Echo', 
                    'Genji', 
                    'Hanzo', 
                    'Junkrat', 
                    'Mei', 
                    'Phara', 
                    'Reaper', 
                    'Soldier: 76', 
                    'Sojourn', 
                    'Sombra', 
                    'Symmetra', 
                    'Torbjorn', 
                    'Tracer', 
                    'Widowmaker'] 

        support = [ 'Ana', 
                    'Baptiste', 
                    'Brigitte', 
                    'Lucio', 
                    'Mercy', 
                    'Moira', 
                    'Zenyatta']

        maps = {'Escort': escort, 'Hybrid': hybrid, 'Control': control, 'Push': push}
        heroes = {'Tank': tank, 'DPS': dps, 'Support': support} 
        results = ['Victory', 'Defeat', 'Draw']
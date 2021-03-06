from collections import OrderedDict

tableformat = '{:<31}|{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'

def tally(rows):

    scoreboard = {
    "Allegoric Alaskans" : {
        "MP" : 0,
        "W" : 0,
        "D" : 0,
        "L" : 0,
        "P" : 0
    },
    "Courageous Californians" : {
        "MP" : 0,
        "W" : 0,
        "D" : 0,
        "L" : 0,
        "P" : 0
    },
    "Blithering Badgers" : {
        "MP" : 0,
        "W" : 0,
        "D" : 0,
        "L" : 0,
        "P" : 0
    },
    "Devastating Donkeys" : {
        "MP" : 0,
        "W" : 0,
        "D" : 0,
        "L" : 0,
        "P" : 0
    },
    }

    for i in rows:
        elements = i.split(';')
        home = elements[0]
        away = elements[1]
        result = elements[2]

        if result == 'win':
            scoreboard[home]['MP'] = scoreboard[home]['MP']+1
            scoreboard[away]['MP'] = scoreboard[away]['MP']+1
            scoreboard[home]['W'] = scoreboard[home]['W']+1
            scoreboard[away]['L'] = scoreboard[away]['L']+1
            scoreboard[home]['P'] = scoreboard[home]['P']+3
            #print('The home was '+home+' the away was '+away+' and the result was '+result)
        elif result == 'draw':
            scoreboard[home]['MP'] = scoreboard[home]['MP']+1
            scoreboard[away]['MP'] = scoreboard[away]['MP']+1
            scoreboard[home]['D'] = scoreboard[home]['D']+1
            scoreboard[away]['D'] = scoreboard[away]['D']+1
            scoreboard[home]['P'] = scoreboard[home]['P']+1
            scoreboard[away]['P'] = scoreboard[away]['P']+1
        elif result == 'loss':
            scoreboard[home]['MP'] = scoreboard[home]['MP']+1
            scoreboard[away]['MP'] = scoreboard[away]['MP']+1
            scoreboard[home]['L'] = scoreboard[home]['L']+1
            scoreboard[away]['W'] = scoreboard[away]['W']+1
            scoreboard[away]['P'] = scoreboard[away]['P']+3

    ordered = OrderedDict(sorted(scoreboard.items(), key=lambda i: i[1]['P'], reverse=True))

    header = [tableformat.format('Team', 'MP', 'W', 'D', 'L', 'P',)]
    table = [tableformat.format(field,
                                v['MP'],
                                v['W'],
                                v['D'],
                                v['L'],
                                v['P'],) for field, v in ordered.items() if v['MP'] > 0]

    return header + table
    pass

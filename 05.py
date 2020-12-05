def load(path):
    with open(path, 'r') as raw:
        return [line.strip() for line in raw.readlines()]

def iterate(seatcode, rows):
    for char in seatcode:
        if char == "F" or char == "L":
            rows = rows[:len(rows) // 2]
        else:
            rows = rows[len(rows) // 2:]
    return rows[0]

def recurse(seatcode, rows):
    if len(seatcode) == 0:
        return rows[0]
    else:
        char = seatcode[0]
        if char == "F" or char == "L":
            return recurse(seatcode[1:], rows[:len(rows) // 2])
        else:
            return recurse(seatcode[1:], rows[len(rows) // 2:])

def execute(seatcode, function=recurse):
    row = function(seatcode[:7], list(range(128)))
    column = function(seatcode[-3:], list(range(8)))
    seat_id = row * 8 + column
    return row, column, seat_id

def part1(path):
    seatcodes = load(path)
    return max([execute(code)[2] for code in seatcodes])

def part2(path):
    seatcodes = load(path)
    occupied_seats = set([execute(code)[2] for code in seatcodes])
    all_seats = set(range(min(occupied_seats), max(occupied_seats)))
    your_seat = all_seats - occupied_seats
    return your_seat.pop()


TICKET_LENGTH = 10
NUMBER_LENGTHS = [1, 2]
MAX_NUMBER = 80


def helper(idx, numbers, ticket, repeated, solutions):
    """Return all possible ticket numbers that can be generated using an specific set of digits.

    Args:
        idx (int): Index of the current digit we're analyzing.
        numbers (str): Set of digits that can be used to form ticket number.
        ticket (List[int]): List of numbers considered for the current ticket.
        repeated (set): Set of numbers that have been added to the current ticket.
        solutions: (List[str]): A list of all the valid tickets.

    Returns:
        List[str]: List of all the valid tickets.
    """
    if len(ticket) > TICKET_LENGTH:
        return solutions

    if idx >= len(numbers):
        if len(ticket) < TICKET_LENGTH:
            return solutions
        else:
            solutions.append('-'.join(ticket))
            return solutions
    
    for length in NUMBER_LENGTHS:
        new_number = numbers[idx : idx + length] if idx + length <= len(numbers) else None

        if new_number and new_number not in repeated and 0 < int(new_number) < MAX_NUMBER:
            new_ticket = ticket + [new_number]
            
            repeated.add(new_number)
            solutions = helper(idx + length, numbers, new_ticket, repeated, solutions)
            repeated.remove(new_number)

    return solutions


if __name__ == '__main__':
    with open('./numbers.txt') as f:
        line = f.readline()
        numbers = line.split(', ')

        combinations = []
        for n in numbers:
            sol = helper(0, n, [], set(), [])
            combinations += sol
        
        print(combinations)

        with open('./solutions.txt', 'a') as f2:
            f2.write(', '.join(combinations))

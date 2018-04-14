from pathlib import Path
from typing import List, Tuple, Iterator


def read_ints(lines: Iterator[str]) -> List[int]:
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def get_director_item(lines: Iterator[str]) -> int:
    """Returns worst item id picked by director."""
    k, = read_ints(lines)
    for i in range(k):
        next(lines)
    director_item, = read_ints(lines)
    return director_item


def get_employee_item(votes: List[int], director_item: int) -> int:
    """Returns worst item id by given employee votes."""
    worst = min(votes)
    if votes.count(worst) > 1:
        return director_item
    else:
        return votes.index(worst) + 1


def get_worst_item(worst_votes: List[int], director_item: int) -> int:
    """Returns worst item from given list of votes for each item."""
    worst_item = worst_votes.index(max(worst_votes)) + 1
    best_votes = worst_votes[:]
    worst_vote = best_votes.pop(worst_item - 1)
    if worst_vote > sum(best_votes):
        return worst_item
    else:
        return director_item


def count_votes(lines: Iterator[str], director_item: int, n_items: int=3) -> Tuple[List[int], int]:
    # First line from input stream tells us how many units we have.
    k, = read_ints(lines)

    # Initialize results.
    worst_votes = [0] * n_items

    # Read unit votes data and calculate totals.
    for i in range(k):
        employee_item = get_employee_item(read_ints(lines), director_item)
        worst_votes[employee_item - 1] += 1

    return worst_votes, get_worst_item(worst_votes, director_item)


def main(path: Path) -> None:
    # Read and process input data.
    with open(path / 'U1.txt') as f:
        # Since worst item picked by directer is in last line, we have to read
        # whole file to get it.
        director_item = get_director_item(f)

        # Now we reset file pointer to the beginning of file and count votes.
        f.seek(0)
        worst_votes, worst_item = count_votes(f, director_item)

    # Write results to output file.
    with open(path / 'U1rez.txt', 'w') as f:
        print(*worst_votes, file=f)
        print(worst_item, file=f)


if __name__ == '__main__':
    main(Path())

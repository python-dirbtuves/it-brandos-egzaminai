from pathlib import Path
from typing import List, Tuple, Iterator


def read_ints(lines: Iterator[str]) -> List[int]:
    return list(map(int, next(lines).split()))


def update_totals(totals: List[int], update: List[int]) -> List[int]:
    return [a + b for a, b in zip(totals, update)]


def add_director_points(total_points: List[int], director_points: List[int], max_point: int) -> List[int]:
    return [
        director_points[i] if point == max_point else point
        for i, point in enumerate(total_points)
    ]


def get_unit_points(points_map: Tuple[int, ...], votes: List[int]) -> List[int]:
    max_vote = max(votes)
    max_vote_count = votes.count(max_vote)
    return [
        points_map[max_vote_count - 1] if vote == max_vote else 0
        for vote in votes
    ]


def get_final_points(total_points: List[int], director_points: List[int]) -> List[int]:
    max_point = max(total_points)
    max_point_count = total_points.count(max_point)
    if max_point_count > 1:
        return add_director_points(total_points, director_points, max_point)
    else:
        return total_points


def get_winner_item(points: List[int]) -> int:
    # Since our points list is 0-based, we have to add 1, to make it 1-based.
    return points.index(max(points)) + 1


def count_votes(
        lines: Iterator[str],
        points_map: Tuple[int, ...]=(4, 2, 0),
        n_items: int=3) -> Tuple[List[int], List[int], int]:
    assert len(points_map) == n_items

    # First line from input stream tells us how many units we have.
    k, = read_ints(lines)

    # Initialize totals.
    total_votes = [0] * n_items
    total_points = [0] * n_items

    # Read unit votes data and calculate totals.
    for i in range(k):
        votes = read_ints(lines)
        points = get_unit_points(points_map, votes)
        total_votes = update_totals(total_votes, votes)
        total_points = update_totals(total_points, points)

    # Read director points and decide the winner item.
    director_points = read_ints(lines)
    final_points = get_final_points(total_points, director_points)
    winner_item = get_winner_item(final_points)

    return total_votes, final_points, winner_item


def format_results(votes: List[int], points: List[int], winner: int) -> Iterator[str]:
    yield ' '.join(map(str, votes))
    yield ' '.join(map(str, points))
    yield str(winner)


def main(path: Path) -> None:
    # Read and process input data.
    with open(path / 'U1.txt') as f:
        results = count_votes(f)

    # Write results to output file.
    with open(path / 'U1rez.txt', 'w') as f:
        for line in format_results(*results):
            print(line, file=f)

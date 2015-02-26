#!/usr/bin/env python3

def parse_votes_line(line, n_items):
    votes = list(map(int, line.split()))
    assert len(votes) == n_items
    return votes


def update_totals(totals, update):
    """Update totals in places by adding numbers from update list."""
    for i, number in enumerate(update):
        totals[i] += number


def add_director_points(total_points, director_points, max_point):
    return [
        director_points[i] if point == max_point else point
        for i, point in enumerate(total_points)
    ]


def count_unit_points(points_map, votes):
    max_vote = max(votes)
    max_vote_count = votes.count(max_vote)
    for vote in votes:
        if vote == max_vote:
            yield points_map[max_vote_count]
        else:
            yield 0


def get_final_points(total_points, director_points):
    max_point = max(total_points)
    max_point_count = total_points.count(max_point)
    if max_point_count > 1:
        return add_director_points(total_points, director_points, max_point)
    else:
        return total_points


def get_winner_item(total_points):
    return total_points.index(max(total_points)) + 1


def count_votes(input_stream, points_map, n_items):
    # First line from input stream tells us how many units we have.
    k = int(next(input_stream))

    # Initialize totals and director points.
    total_votes = [0] * n_items
    total_points = [0] * n_items
    director_points = [0] * n_items

    for i, line in enumerate(input_stream):
        votes = parse_votes_line(line, n_items)

        # Count votes and points of each unit using k as number of units.
        if i < k:
            points = count_unit_points(points_map, votes)
            update_totals(total_votes, votes)
            update_totals(total_points, points)

        # Last line in file is director points.
        else:
            director_points = votes
            break

    final_points = get_final_points(total_points, director_points)
    winner_item = get_winner_item(final_points)

    return total_votes, final_points, winner_item


def format_results(results):
    votes, points, winner = results
    yield ' '.join(map(str, votes))
    yield ' '.join(map(str, points))
    yield str(winner)


def main():
    # Number of items to vote for.
    n_items = 3

    # Map of max vote count to points.
    # Number of items in this dict should be equal to n_items.
    points_map = {
        1: 4,
        2: 2,
        3: 0
    }

    # Read and process input data.
    with open('U1.txt') as f:
        results = count_votes(f, points_map, n_items)

    # Write results to output file.
    with open('U1rez.txt', 'w') as f:
        f.write('\n'.join(format_results(results)))


if __name__ == '__main__':
    main()

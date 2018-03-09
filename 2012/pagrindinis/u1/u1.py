#!/usr/bin/env python3

from typing import List, Tuple, Iterator, Optional


class Player:
    def __init__(self, k: int, times: List[int]) -> None:
        self.no = k
        self.playing = sum([t for t in times if t > 0])
        self.sitting = sum([abs(t) for t in times if t < 0])
        self.came_first = times[0] > 0

    def get_better_player_by(self, other: Optional['Player'], prop: str) -> 'Player':
        """Compare current palyer with the other by given property."""
        if other is None:
            return self
        elif getattr(self, prop) == getattr(other, prop):
            return self if self.no < other.no else other
        else:
            return self if getattr(self, prop) > getattr(other, prop) else other


def read_ints(lines: Iterator[str]) -> List[int]:
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_data(lines: Iterator[str]) -> Tuple[List[int], Optional[Player], Optional[Player]]:
    came_first = []
    most_playing = most_sitting = None
    n, = read_ints(lines)
    for i in range(n):
        k, t, *times = read_ints(lines)
        player = Player(k, times[:t])
        if player.came_first:
            came_first.append(player.no)
        most_playing = player.get_better_player_by(most_playing, 'playing')
        most_sitting = player.get_better_player_by(most_sitting, 'sitting')
    return came_first, most_playing, most_sitting


def main() -> None:
    with open('U1.txt') as f:
        came_first, most_playing, most_sitting = read_data(f)

    with open('U1rez.txt', 'w') as f:
        print(*sorted(came_first), file=f)
        print(most_playing.no, most_playing.playing, file=f)
        print(most_sitting.no, most_sitting.sitting, file=f)


if __name__ == '__main__':
    main()

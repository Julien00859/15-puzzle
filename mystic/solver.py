"""
A* implementation

The game is captured in a graph, each stable game stable is captured in
the Branch() class. Each discovered branch is placed in a priority
queue sorted by "how good" the branch is (better branches first). The
quality of each branch is determined by the following heuristic :

    branch.step + branch.invalid

where "step" is the depth of the branch in the game graph and "invalid"
is how many nodes are incorrectly placed in the mystic square.

This heuristic ensure we find a somewhat short solution (step) with a
byass that favor moving piece an ordered way (invalid).
"""

from mystic.heapq import heappush, heappop

class Branch:
    def __init__(self, parent, value, invert, step, invalid):
        self.parent = parent    # the parent branch
        self.value = value      # the mystic square internal array
        self.invert = invert    # the direction from this branch to its parent
        self.step = step        # this branch depth in the tree (used in heuristic)
        self.invalid = invalid  # how many tiles are invalid in the mystic square (used in heuristic)

    def __repr__(self):
        return f"<Branch value={self.value}, step={self.step}, invalid={self.invalid}>"

steps = []
def play(square):
    if steps:
        return steps.pop()

    real = square.numbers

    ns = tuple(square.numbers)
    root = Branch(
        parent=None,
        value=ns,
        invert=None,
        step=0,
        invalid=9 - square.count_valid(),
    )
    leafs = [root]
    seens = {ns}

    while True:
        best = heappop(leafs, key=lambda b: b.step + b.invalid)
        square.numbers = list(best.value)
        if square.is_won():
            break

        for dir_ in square.valid_directions():
            getattr(square, dir_)()
            ns = tuple(square.numbers)
            if ns not in seens:
                seens.add(ns)
                leaf = Branch(
                    parent=best,
                    value=ns,
                    invert=dir_,
                    step=best.step + 1,
                    invalid=9 - square.count_valid()
                )
                heappush(leafs, leaf, key=lambda b: b.step + b.invalid)
            square.numbers = list(best.value)

    square.numbers = real

    print(f"AI found a solution using {len(seens)} nodes")

    dirs = {'left': 'h', 'down': 'j', 'up': 'k', 'right': 'l'}
    while best.parent:
        steps.append(dirs[best.invert])
        best = best.parent

    return steps.pop()

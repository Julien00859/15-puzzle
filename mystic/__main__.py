import sys
from mystic import solver
from mystic.square import Square

import pdb; pdb.set_trace()

# argparse ? never heard of that :P
if len(sys.argv) == 1:
    sys.exit(f"usage: {sys.executable} -m mystic --difficulty n [--ai]")
DIFFICULTY = int(sys.argv[sys.argv.index('--difficulty') + 1])
USE_AI = '--ai' in sys.argv

def main():
    s = Square(DIFFICULTY)
    step = 0
    dirs = {'h': s.left, 'j': s.down, 'k': s.up, 'l': s.right}

    print("Generated puzzle:")
    while True:
        ns = [str(n) for n in s.numbers]
        ns[s.numbers.index(0)] = " "
        for i in range(4):
            print("[%s]" % ", ".join(ns[i * 4:(i + 1) * 4]))

        if s.is_won():
            break

        if USE_AI:
            d = solver.play(s)
            print('?', d)
        else:
            d = input('? ')

        dirs.get(d, lambda: None)()
        step += 1

    print(f'Won in {step} steps')

main()

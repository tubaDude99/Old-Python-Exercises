
# [ ] The following program generates a staircase character art
# The `size` variable controls the number of steps
# The `base_shape` defines the characters used to generate the art
# Modify the program so the `size` is set as a positional command line argument, and base_shape as an optional 
# command line argument with a default value of `[]`
import argparse
p = argparse.ArgumentParser()
p.add_argument('size', type = int, help = 'Number of steps')
p.add_argument('-b', '--base_shape', type = str, default = '[]', help = 'Base shape used in generation')
args = p.parse_args()
def gen_stairs(steps, base_shape):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()

# Generate a staircase with 6 steps using '[]` as a base shape
gen_stairs(args.size, args.base_shape)
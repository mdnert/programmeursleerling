import os
import random
import subprocess

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# configuration settings
settings = f'''
tab name: Tests
python input without prompt: true
block count: multi
input block size: 2
output block size: ends with
comparison: exact match
line order sensitive: false
'''

# generate test data
cases = [(48, 52)]
while len(cases) < 50:
    lower = random.randint(1, 1000)
    upper = lower + random.randint(0, 20)
    if (lower, upper) not in cases:
        cases.append((lower, upper))

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8')

# generate unit tests
for index, stdin in enumerate(cases):

    # add input to input file
    stdin = '\n'.join(str(line) for line in stdin)
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.en.py')
    process= subprocess.run(
        ['python', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True, shell=True, check=True
    )
    stdout = process.stdout

    # add stdout to output file
    if index:
        print(file=outfile)
    print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 60 + settings, file=outfile)

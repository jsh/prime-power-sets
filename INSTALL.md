# Getting This to Run


## Requirements
This was developed with Python 3.13.3 and uv 0.7.3, both of which are public and easy to download.

If it also happens to work with earlier versions of either, let me know.

I wrote this on my Mac M2. As I find other machines it works on, I'll add them to the list.

### Machines
Macbook Air M2 (2022), 8G memory

## The code

The program is a single, Python file.
There's really nothing hard or tricky.

Unit tests are in `tests/`


The `README.md` file has more information.
The easiest way to read it, or any other Markdown (`.md`) file that may be added (like this one),
is to brows to (https://github.com/jsh/<repo-name>)[the GitHub repo] and click on the file.

## Running the code

```
git clone https://github.com/jsh/<repo-name> # you already did this
cd <repo-name>                  # go into the folder
uv sync                         # install Python packages
source .venv/bin/activate       # enter virtual environment
python <program-name>.py --help # how to run the search program
```

### Example
To look in S={3^k} for non-intersecting subsets with identical means

`python <program-name> --exponent_limit 10 --prime 3`


## Testing the code.

If you want to improve the code, there's a test suite of 76 tests
that you can use to make sure you don't break anything.

```
pytest              # run the unit tests
pytest --cov        # find untested lines in the source
mutmut              # run mutation tests
```

Right now, the progam passes all 76.

The second of these, coverage testing, runs the test suite,
watches every line of your code to see which lines are executed,
and reports all lines that the test suites fail to pass through.

Currently, the suite uses 100% of the executable lines in the program.

The third of these, mutation testing, can be a little tricky to wrap your head around. I'll try to explain.

### Mutation testing

Unit tests test a particular version of the code.
Even though the tests exercise every line of the source,
it's possible to change the code and still pass the tests.

Some changes are invisible to unit tests.

Changing the comment on this line:
```
if x > 1  # an unimportant possibility
```
to this:
```
if x > 1 # an important possibility
```

will not change program behavior. No unit test can detect such misteaks.

In contrast, this typo
```
if x >= 1 # an unimportant possibility
```

would change the program behavior. But would your tests tell you?

If your tests check that the program behaves differently for `x = 0` and `x = 2`,
both the original and the typo would pass.
Your tests are testing this code, but they won't detect this subtle change.
Here's where mutation testing helps you.

`mutmut` methodically creates an array of mutatnts of your code, runs each one against your test suite, and reports any mutant that still passes.

For this program, mutmut tries 101 mutants.
All of them run to completion.
Nevertheless, I've enhanced the test suite so that each mutant fails some test in the test suite.


# Getting This to Run

## Requirements
This requires Python >=3.11 and uv >=0.5.10, both of which are public and easy to download.

I'm currently using newer versions of both. If it also happens to work with earlier versions of either, let me know.

I wrote this on my Mac M2. As I find other machines it works on, I'll add them to the list.

### Machines this is known to run on
Macbook Air M2 (2022), 8G memory, macOS
Acer Chromebook Plus 514, AMD Ryzen 3 chip, 8G memory. Container, with 8G memory, runs Penguin Linux 6.6.72, x86_64, Debian 12.10 (bookworm)
Google Cloud Shell, Container with about 1.7G memory, runs Linux 6.6.72, x86_64, Debian 13 (trixie/sid)


## The code

The program is a single, Python file. There's really nothing hard or clever in the code.

Unit tests are in `tests/`

The `README.md` file has more information.
The easiest way to read it, or any other Markdown (`.md`) file that may be added (like this one),
is to brows to (https://github.com/jsh/<repo-name>)[the GitHub repo] and click on the file.

## Running the code

### A turnkey script
So long as `uv` and `python` are installed, you can run the program on your Linux or Mac with
`./<program_name>.py` .

The first time you run it, it will take a few seconds to install all the dependencies.
After that, it'll see the dependencies are installed and launch immediately.

The magic behind turnkey operation *is* clever,
and is stuffed into a comment block at the top of the code.
It takes a little patient explaining, but I put a link to the explanation in that block.
If you don't want to comb through the PPA spec, or read PEP 723, and want me to explain it instead,
just ask.

### A development environment
If you want to do improve the app,
here's the no-magic-required, easier-to-understand, way to play with it.

```
git clone https://github.com/jsh/<repo-name> # you already did this
cd <repo-name>                  # go into the folder
uv sync                         # install Python packages and create virtual environment
source .venv/bin/activate       # enter virtual environment
python <program-name>.py --help # how to run the search program
```

### Example
To look in S={3^k} for non-intersecting subsets with identical means

`python <program-name> --exponent_limit 10 --prime 3`


## Testing the code.

If you decide to improve the code, there's a test suite of 76 tests,
which you can use to make sure you don't break anything as you tinker.

```
pytest              # run the unit tests
pytest --cov        # find untested lines in the source
mutmut run          # create and run mutation tests
```

Right now, the first command runs and passes all 76.

The second of these commands, coverage testing.
It runs the test suite, watches every line of your code to see which lines are executed,
and reports all lines that the test suites don't exercise.

Currently, the suite exercises 100% of the executable lines in the program.

The third command, `mutmut`, does mutation testing, which can be a little tricky to wrap your head around. I'll try to explain.

### Mutation testing

Unit tests test a particular version of the code.
Even though the tests exercise every line of the source,
it's possible to break the code and still pass the tests.

Some changes are invisible to unit tests.

Changing a comment, like this
```
if x > 1  # an unimportant possibility
```
to this:
```
if x > 1 # an important possibility
```

does not change program behavior. No unit test can detect such misteaks.

In contrast, this typo
```
if x >= 1 # an unimportant possibility
```

does change program behavior. But would your tests tell you?

If you test by checking that the program behaves differently for `x = 0` and `x = 2`,
both the original and the typo would pass.
Your tests are testing this code, but they won't detect this subtle change.

Your tests aren't good enough.
Here's where mutation testing helps you.

`mutmut` methodically creates an array of mutatnts of your code, and runs each one against your current test suite. If any mutant still passes,
your test suite isn't good enough.

For this program, mutmut creates 101 mutants.
Each mutant runs to completion, yet all fail the test suite somewhere.
This gives me a lot more confidence that my tests are solid.

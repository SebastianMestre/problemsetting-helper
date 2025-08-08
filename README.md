
## Usage

- Put your test cases in the `tests` directory.
- Put your solutions in the `solutions` directory. (the correct solution should be `ac.cpp`)
- Run `run-system.sh`

This will run all the solutions against all the test cases in parallel. It will
also cache results "as much as possible" (i.e. only re-run solution/test-cases
if they have been changed).

It achieves this by expressing all the data dependencies in a makefile.

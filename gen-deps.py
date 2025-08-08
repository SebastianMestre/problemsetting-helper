#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict

class Item:
	def __init__(self, path, deps, command):
		self.path = path
		self.deps = deps
		self.command = command

	def show(self):
		if not self.deps:
			return

		print(f"{self.path}: {' '.join(str(dep.path) for dep in self.deps)}")

		if self.command != "":
			print('\t' + '\n\t'.join(self.command.split('\n')))

test_dir = Path('tests')
tests = []
for path in test_dir.rglob("*.in"):
	tests.append(Item(path, [], ""))

solution_dir = Path('solutions')
solution_sources = []
for path in list(solution_dir.rglob("*.cpp")):
	solution_sources.append(Item(path, [], ""))

solution_binaries = []
for source in solution_sources:
	path = Path(f"bin/{source.path.stem}")
	command = f"g++ -o {path} {source.path}"
	command = ""
	solution_binaries.append(Item(path, [source], command))

# Generate answer & veredict files
ac_solution = None
for solution in solution_binaries:
	if solution.path.stem == 'ac':
		ac_solution = solution
		break
if ac_solution is None:
	print("Did not detect accepted solution", file=sys.stderr)
	exit(1)

answer_files = []
veredict_files = []

solution_veredict_deps = defaultdict(lambda: [])

for test in tests:
	path = Path(f"out/{test.path.stem}.ans")
	command = f"{ac_solution.path} < {test.path} > {path}"
	answer = Item(path, [ac_solution, test], command)
	answer_files.append(answer)

	for solution in solution_binaries:
		path = Path(f"out/test.{solution.path.stem}.{test.path.stem}.veredict")
		command = f"./check.sh {solution.path} {test.path} {answer.path} > {path}"
		test_veredict = Item(path, [solution, test, answer], command)
		veredict_files.append(test_veredict)

		solution_veredict_deps[solution.path].append(test_veredict)

solution_veredicts = []
for solution_path, deps in solution_veredict_deps.items():
	path = Path(f"out/solution.{solution_path.stem}.veredict")
	command = f"./combine_veredict.py {solution_path.stem} {' '.join(str(dep.path) for dep in deps)} > {path}"
	solution_veredict = Item(path, deps, command)
	veredict_files.append(solution_veredict)
	solution_veredicts.append(solution_veredict)

path = Path(f"out/overall.veredict")
command = f"cat {' '.join(str(dep.path) for dep in solution_veredicts)} > {path}"
overall_veredict = Item(path, solution_veredicts, command)
veredict_files.append(overall_veredict)

all_items = []
all_items += tests
all_items += solution_sources
all_items += solution_binaries
all_items += answer_files
all_items += veredict_files

for item in all_items:
	item.show()

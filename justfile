_default:
  just --list

# run linting and typecheking over the solutions
@lint:
  ruff check --quiet
  ruff format --check --quiet
  pyright

# run every solution for a given year
@validate year:
	for i in $(seq 1 25); do ./advent $i --slow --year {{year}}; echo; done;

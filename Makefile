install:
	uv sync

build:
	uv build

package-install:
	uv tool install /mnt/c/Users/Chalo\ Nov/dist/hexlet_code-0.1.0-py3-none-any.whl

package-install:
	uv tool install dist/*.whl

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games

clean:
	rm -rf dist *.egg-info .venv

brain-even:
	/mnt/c/Users/Chalo\ Nov/.venv/bin/python -m brain_games.scripts.brain_even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	/mnt/c/Users/Chalo\ Nov/.venv/bin/python -m brain_games.scripts.brain_progression

brain-prime:
	/mnt/c/Users/Chalo\ Nov/.venv/bin/python -m brain_games.scripts.brain_prime
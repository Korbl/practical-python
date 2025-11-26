import json
from pathlib import Path
from pprint import pprint

FILE = Path("/Users/sitschner/SBP/training/practical-python/Work", "test.json")


content = json.load(FILE.read_text())

print(f"TYPE {type(content)}")
pprint(content)

from ..src.utils.load_data import load_data
from src.settings import EXAMPLE_FILE

data = load_data(EXAMPLE_FILE)
print(data)
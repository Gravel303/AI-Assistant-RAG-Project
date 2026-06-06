
from utils.storage_manager import (save_chunks, load_chunks)

chunks = ["TCP", "UDP"]

save_chunks(chunks)

loaded = load_chunks()

print(loaded)
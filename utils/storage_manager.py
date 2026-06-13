import pickle
import faiss
import os

def save_chunks(
    chunks,
    filepath="data/chunks.pkl"
):
    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )

    with open(
        filepath,
        "wb"
    ) as file:

        pickle.dump(
            chunks,
            file
        )

def load_chunks(
    filepath="data/chunks.pkl"
):

    with open(
        filepath,
        "rb"
    ) as file:

        return pickle.load(
            file
        )

def save_index(
    index,
    filepath="data/faiss.index"
):
    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )
    
    faiss.write_index(
        index,
        filepath
    )

def load_index(
    filepath="data/faiss.index"
):

    return faiss.read_index(
        filepath
    )

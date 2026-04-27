from config.settings import model

def embed_chunks(chunks):
    return model.encode(chunks)
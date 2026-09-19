from .normalizer import normalize
from .tokenizer import tokenize


from .vocabulary import Vocabulary
from .embedding import Embedding


class NLProcessing:
    def __init__(self):
        self.vocab = Vocabulary(load=True, save=False)

        vocab_size = self.vocab.token_count
        dimension = 5
        self.embedding = Embedding(vocab_size, dimension, load=True)

    def manage(self, entries):
        """Recebe as entradas e faz o tratamento"""

        normalized = normalize(entries)
        tokens = tokenize(normalized)

        print(self.embedding.weights)
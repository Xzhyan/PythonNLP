import numpy as np

# core
from core.config import EMBEDDING_FILE


class Embedding:
    def __init__(self, vocab_size, dimension, load=False):
        # tamanho e dimensão da matriz do vocabulary
        self.vocab_size = vocab_size
        self.dimension = dimension

        self.weights = np.ndarray # matriz

        # se o load estiver ativo a matriz persistente do embedding.json é carregada
        if load:
            self.load_matriz(EMBEDDING_FILE)

    def save_matriz(self, path):
        """Salva a matriz no embedding.json"""

        try:
            np.save(EMBEDDING_FILE, self.weights)

        except Exception as e:
            print(str(e))

    def generate_weights(self, save=False):
        """Gera a matriz de pesos com base no tamanho do vocab e na dimensão"""

        self.weights = np.random.randn(
            self.vocab_size,
            self.dimension
        )

        # se o save estiver ativo a matriz vai ser salva no embedding.npy
        if save:
            self.save_matriz(EMBEDDING_FILE)

    def load_matriz(self, path):
        """Carrega a matriz do embedding.json"""

        try:
            self.weights = np.load(EMBEDDING_FILE)

        except Exception as e:
            print(str(e))

    def get_vector(self, token_id):
        """Pega o vector do token"""

        return self.weights[token_id]





# import numpy as np


# # core
# from core.config import EMBEDDING_FILE


# class Embedding:
#     def __init__(self, vocab_size, embedding_dim):
#         """Configurações inicias de tamanho e dimensão do embedding"""

#         self.vocab_size = vocab_size
#         self.embedding_dim = embedding_dim

#         self.weights = np.random.randn(
#             self.vocab_size,
#             self.embedding_dim
#         )


#     def save_matriz(self):
#         try:
#             np.save(EMBEDDING_FILE, self.weights)

#         except Exception as e:
#             print(str(e))


#     def load_matriz(self):
#         try:
#             self.weights = np.load(EMBEDDING_FILE)

#         except Exception as e:
#             print(str(e))


#     def get_vector(self, token_id):
#         """Pega o vector do token_id"""

#         return self.weights[token_id]


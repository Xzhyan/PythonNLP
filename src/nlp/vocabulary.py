

# core
from core.config import VOCAB_JSON

# utils
from utils.functions import write_json, read_json


class Vocabulary:
    def __init__(self, load=False, save=False):
        self.token_to_id = {}
        self.id_to_token = {}

        self.token_count = 0 # contagem de tokens do vocabulary

        self.updated = False # status de atualização do vocabulary

        self.save = save # controle de salvamento do vocabulary.json

        # Se a instancia tiver load=True ele já carrega o vocabulary.json
        if load:
            self.load_vocab()

    def add_token_id(self, token):
        """Verifica se o token possuí ID, se não, adiciona"""

        if not token in self.token_to_id:
            token_id = len(self.token_to_id)

            # adiciona o token/id na lista
            self.token_to_id[token] = token_id
            self.id_to_token[token_id] = token

            self.updated = True

    def add_tokens(self, tokens):
        """Separa token por token para adicionar ao vocabulary"""

        for token in tokens:
            self.add_token_id(token)

        # verifica se tokens novos foram adicionados e atualiza o vocabulary
        if self.updated and self.save:
            self.save_vocab()

    def save_vocab(self):
        """Salva os dados no vocabulary.json"""

        write_json(VOCAB_JSON, self.token_to_id)

    def load_vocab(self):
        """Carrega os dados do vocabulary.json"""

        data = read_json(VOCAB_JSON)

        for token, token_id in data.items():

            self.token_to_id[token] = token_id
            self.id_to_token[token_id] = token

        self.token_count = len(self.token_to_id)



# utils
from utils.console import entry, clear

# nlp
from nlp import NLProcessing


class Main:
    def __init__(self):
        self.running = True

        self.nlp = NLProcessing()

    def startup(self):
        while self.running:
            try:
                entries = entry()

                if 'clear' in entries:
                    clear()

                self.nlp.manage(entries)

            except ValueError as e:
                print(str(e))

            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    try:
        app = Main()
        app.startup()

    except KeyboardInterrupt:
        print("\nFinalizando...")

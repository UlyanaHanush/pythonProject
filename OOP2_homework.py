import string


class Alfabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(f'буквы алфавита: {self.letters}')

    def letters_num(self):
        print(f'количество букв алфавите {len(self.letters)}')


class EngAlfabet(Alfabet):

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    __letters_num = len(string.ascii_lowercase)

    def is_en_letter(self, a):
        if len(a) == 1 and a in self.letters:
            print('эта буква английского алфавита')
        else:
            print('эта НЕ буква английского алфавита')

    def letters_num(self):
        return EngAlfabet.__letters_num

    @staticmethod
    def example():
        return 'Ex.: hellow world'
        # lang = input('введите язык: ')
        # letters = input('введите буквы алфавита: ')


yes = EngAlfabet()
yes.print()
print(yes.letters_num())
yes.is_en_letter('F')
yes.is_en_letter('Щ')
print(yes.example())

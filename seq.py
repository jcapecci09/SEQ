class Seq:

    def __init__(self, sequence: str):
        self.__seq = sequence

    
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, index: int):
        pass

    def __eq__(self, other):
        pass

    def count(self, sub: str):
        """Returns number of times a subsequence occurs in the sequence

        :param sub: subsequence to look for
        :return: Number of occurences 
        """

        # Intialize a counter and find the length of the subsequence
        counter = 0
        length = len(sub)

        # Number of times to loop through the sequence
        loop = len(self.__seq - length + 1)

        # loop through sequence and add to counter if subsequence is found
        for index in range(loop):
            if self.__seq[index:index+length] == sub:
                counter += 1
        return counter

    def complement(self):
        pass

    def reverse_complement(self):
        pass

    def transcribe(self):
        pass

    def back_transcribe(self):
        pass

    def translate(self):
        pass

    def gc_content(self):
        pass


def main():
    
    my_seq = Seq('ATGAGACGATGAG')
    print(my_seq.count('A'))

if __name__ == '__main__':
    main()
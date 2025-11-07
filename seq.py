class Seq:

    def __init__(self, sequence: str):
        self.__seq = sequence

    
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        
        return len(self.__seq)

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
        loop = len(self.__seq) - length + 1

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

    def gc_content(self) -> float:
        """Finds the gc content (percentage) of the given sequence

        :return: percent gc
        """
        
        # Intialize counter
        counter = 0

        # For each base find out if it is either C or G and add to the counter
        for base in self.__seq:
            if base in ['C', 'G']:
                counter += 1
        
        # Divide number of g or c bases by length of the sequence
        return counter / len(self.__seq)


def main():
    
    my_seq = Seq('ATGAGACGATGAG')
    print(my_seq.count('A'))
    print(len(my_seq))
    print(my_seq.gc_content())

if __name__ == '__main__':
    main()
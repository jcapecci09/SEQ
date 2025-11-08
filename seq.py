from __future__ import annotations

class Seq:

    def __init__(self, sequence: str):
        self.__seq = sequence
        self.__complements = {'A':'T', 'T':'A', 'C':'G', 'G':"C"}

    def __str__(self) -> str:
        """Returns sequence as a string"""
        
        return str(self.__seq)

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

    def complement(self) -> Seq:
        """Finds the complement of the sequence

        Returns:
            Seq: Complement as Seq object
        """
        
        # Build string using the complements dictionary 
        new_sequence = ''
        for base in self.__seq:
            new_sequence += self.__complements[base]
        
        return Seq(new_sequence)
            

    def reverse_complement(self) -> Seq:
        """Reverse complement of sequence

        Returns:
            Seq: Reverse complement as a Seq object
        """

        # Similar to .complement() but builds string in reverse
        new_sequence = ''
        for base in self.__seq:
            
            new_sequence = self.__complements[base] + new_sequence
        
        return Seq(new_sequence)

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
    print(my_seq.complement())
    print(my_seq.reverse_complement())

if __name__ == '__main__':
    main()
"""Consideration: I want the object to be able to handle DNA, RNA, and Amino acids
Right now it only handles DNA

TODO: Finish making this as just a DnaSeq object, but I need to start over and rethink how I'm gonna
have a sequence object handle eveyrthing. 

"""

from __future__ import annotations

class DnaSeq:

    def __init__(self, sequence: str):
        self.__seq = sequence
        self.__complements = {'A':'T', 'T':'A', 'C':'G', 'G':"C"}

    def __str__(self) -> str:
        """Returns sequence as a string"""
        
        return str(self.__seq)

    def __repr__(self):
        pass

    def __len__(self) -> int:
        """Return length of sequence

        Returns:
            int: Number of letters in sequence
        """
        
        return len(self.__seq)

    def __getitem__(self, index: int):
        pass

    def __eq__(self, other):
        pass

    def reverse(self) -> DnaSeq:
        """Reverse the sequences

        Returns:
            DnaSeq: Reverse DNA sequence
        """

        # Builds string in reverse
        new_sequence = ''
        for letter in self.__seq:
            new_sequence = letter + new_sequence
        
        return DnaSeq(new_sequence)

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

    def complement(self) -> DnaSeq:
        """Finds the complement of the sequence

        Returns:
            Seq: Complement as Seq object
        """
        
        # Build string using the complements dictionary 
        new_sequence = ''
        for base in self.__seq:
            new_sequence += self.__complements[base]
        
        return DnaSeq(new_sequence)
            
    def reverse_complement(self) -> DnaSeq:
        """Reverse complement of sequence

        Returns:
            Seq: Reverse complement as a Seq object
        """

        # Find the complement
        complement = self.complement()

        # then reverse it
        reverse = complement.reverse()

        return reverse
       
    def transcribe(self) -> DnaSeq:
        """Turns sequence into mRNA transcript. Assumes coding strand is 
        entered. 

        TODO Return RNASEQ

        Returns:
            Seq: mRNA transcript as a Sequence
        """

        # Could just use .replace('T', 'U') but I wanted to build my own
        # Uses string concantenation to replace t's with u's
        new_seq = ''
        for base in self.__seq:
            if base == 'T':
                new_seq += 'U'
            else:
                new_seq += base
        
        return DnaSeq(new_seq)

    def reverse_transcribe(self) -> DnaSeq:
        """Reverse transcribed version of sequence

        Returns:
            DnaSeq: Sequence as a DnaSeq
        """
        
        # transcribe sequence then reverse it
        transcribe = self.transcribe()
        reverse = transcribe.reverse()

        return reverse

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
    orginal = 'ATGAGACGATGAG'
    my_seq = DnaSeq(orginal)
    print(f'orginal: {orginal}')
    print(f'Number of A: {my_seq.count('A')}')
    print(f'Sequence length: {len(my_seq)}')
    print(f'Percent gc {my_seq.gc_content()}')
    print(f'Complement: {my_seq.complement()}')
    print(f'reverse complement: {my_seq.reverse_complement()}')
    print(f'Transcribed: {my_seq.transcribe()}')
    print(f'Reverse Transcribed: {my_seq.reverse_transcribe()}')

if __name__ == '__main__':
    main()
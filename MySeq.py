
class SeqError(Exception):
    pass

class Seq:

    def __init__(self, sequence: str, __seq_id = None):
        """Sequence object containing a biological sequence

        :param sequence: Sequence to be added
        :param __seq_id: The type of sequence (protein, dna, rna), defaults to None
        :raises SeqError: If non-biological sequence is entered raise an error
        """

        # Intialize the sequence
        self.seq = sequence

        # For finding the sequence_id there are 4 options
        # DNA, RNA, Protein, errorneous sequences
        if __seq_id is None:
            
            # Intialize sets displaying all possible letters in each sequence
            amino_acids = {"A", "R", "N", "D", "C", "E", "Q", 
                       "G", "H", "I", "L", "K", "M", "F", 
                       "P", "S", "T", "W", "Y", "V"}
            dna = {'G', 'A', 'T', "C"}
            rna = {'G', 'A', 'U', 'C'}

            # Find unique values in provided sequence
            uniques = set(self.seq)

            # This will be the basis for how we check for the type of sequence 
            # We are checking for the difference between the sets
            # If unique contains anything expect bases find in DNA then it's not DNA 
            isit_dna = uniques - dna

            # Check the length for each set difference
            if len(isit_dna) == 0:
                self.id = 'DNA'
            elif len(uniques - rna) == 0:
                self.id = 'RNA'
            elif len(uniques - amino_acids) == 0:
                self.id  = 'PROTEIN'
            
            # Raise error if biological sequence is not found
            else:
                raise SeqError('Provided Sequence is not a biological sequence')
        
        # If ID is already provided bypass previous steps
        else:
            self.id = __seq_id
        
        print(self.id)
    
    def __len__(self):

        return len(self.seq)
    
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


def main():
    Seq('AGCUx')

if __name__ == '__main__':
    main()



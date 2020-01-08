# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    #sequence='ab'
    
    def permutator(list_of_chars):
        char=list_of_chars.pop()
        if len(list_of_chars)==0:
            return [[char]]
        else:
            permutations=[]
            for i in permutator(list_of_chars):
                for j in range(len(i)+1):
                    lol=i.copy()
                    lol.insert(j,char)
                    permutations.append(lol)
            return permutations
            
    def joinlist(sequence,glue):
        if len(sequence) == 1:
            conjoined=sequence[0]
        else:
            conjoined=sequence[0]+glue
            conjoined+=joinlist(sequence[1:],glue)    
        return conjoined           
    
    sequence_list=[]
    for i in sequence:
        sequence_list.append(i)
    
    list_form=permutator(sequence_list)
    
    string_form=[]
    
    for i in list_form:
        string_form.append(joinlist(i,''))
        
    return string_form
    
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here


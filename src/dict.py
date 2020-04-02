## @file dict.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Custom dictionary ADT
#  @date Mar 17, 2020


## @brief Generic Dict ADT
#  @details A generic dictionary ADT module which had add, remove, and to_seq methods
class Dict():
    
    ## @brief Dict constructor
    def __init__(self):
        self.d = {}
        self.c = 0

    ## @brief Adds a new entry
    #  @param e New entry to be added to the Dict
    def add(self, e):
        self.d[self.c] = e
        self.c += 1

    ## @brief Adds an entry
    #  @param id Key of entry to update
    #  @param e New value of entry
    def update(self, id, e):
        self.d[id] = e

    ## @brief Remove an entry with key id 
    #  @param id Key of the entry
    #  @throws KeyError If ID does not exist
    def remove(self, id):
        if id in self.d:
            del self.d[id]
        else:
            raise KeyError
    
    ## @brief Returns a dictionary with keys in sorted order
    def to_seq(self):
        seq = []
        for key in sorted(self.d):
            seq.append([key, self.d[key]])
        return seq
    
    def get_count(self):
        return self.c - 1


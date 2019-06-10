# ref) https://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python
import pickle

# Saving the objects:
def save_variables(list_of_variables, filename = 'backup_variables.pkl'):
    with open(filename, 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(list_of_variables, f) # list_of_variables = [var1, var2, var3, ...]

# Getting back the objects:
def load_variables(filename = 'backup_variables.pkl'):
    with open(filename, 'rb') as f:  # Python 3: open(..., 'rb')
        list_of_variables = pickle.load(f)  # list_of_variables = [var1, var2, var3, ...]
    return list_of_variables
 
### Getting Started #####################
a0 = 'hello world'
b0 = ['a','b','c']
c0 = [1,2,3,4,5]

save_variables([a0,b0,c0]) # Saving the objects

#-----------------------------------------
[a1,b1,c1] = load_variables() # Getting back the objects
a1

# Script to loop over a large number of Chimera data files

# import required module
import os
import subprocess

# assign directory of models
directory = 'snowglobes/fluxes'
print('Directory',directory)

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('**************')
        print('Flux filename = ',filename)

        # using negative indexing
        filename = filename[:-4]
        print('Flux = ',filename)

        # python -m snowglobes filename argon ar40kt
        subprocess.run(["python","-m","snowglobes",filename,"argon","ar40kt"])

        print(filename,' finished')


print('SG iteration over Chimera files is finished')


import sys
import traceback
import numpy as np

def cutPizza(pizza, ingr_ps, max_cells, rows, columns):

    mushrooms = ingr_ps
    tomatoes = ingr_ps

    slice_counter = 0

    i = 0
    j = 0
    if pizza[i,j] == 'T':
        if pizza[i + 1, j] == 'M':

        elif pizza[i, j + 1] == 'T':



    elif pizza[i,j] == 'M':


    else:
        if i < rows:
            i += 1
        elif j < columns:
            j += 1
        else:
            print "no more slices possible"
            break
    # for i in range(rows):
    #     j = 0
    #     while tomatoes > 0 and mushrooms > 0:
    #         if pizza[i, j] == 'T':
    #             tomatoes -= 1
    #         elif pizza[i, j] == 'M':
    #             mushrooms -= 1
    #         if tomatoes > 0 and mushrooms > 0:
    #             j += 1
    #
    #                 # for a in range(max_cells):
    #                 #     for b in range(max_cells):
    #                 #         if pizza[a,b] == 'T':
    #                 #             tomatoes -= 1
    #                 #         elif pizza[a,b] == 'M':
    #                 #             mushrooms -= 1

# ensure propper usage
if (len(sys.argv) != 2):
    print "improper usage. USAGE: pizza.py inputfile"
else:
    try:

        # try and get the proper parameters from command line argument
        infile = sys.argv[1]

        f = open(infile)
        rowamount = 0
        for row in f:

            # for the first row get the parameters from the infile
            if row[0].isdigit():
                numbers = row.split()
                rows = int(numbers[0])
                columns = int(numbers[1])
                ingr_ps = int(numbers[2])
                max_cells = int(numbers[3])

                # make a 2d array to represent the pizza
                pizza = np.zeros(shape=(rows, columns), dtype=object)

            # fill the pizza with the given ingredients
            elif row[0] == 'T' or row[0] == 'M':
                columnamount = 0
                for char in row:
                    if char.isalpha():
                        pizza[rowamount, columnamount] = char
                        columnamount += 1
                rowamount += 1

        print pizza
        cutPizza(pizza, ingr_ps, max_cells, rows, columns)

    except ValueError:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print ''.join(line for line in lines)
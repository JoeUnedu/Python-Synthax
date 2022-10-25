from traceback import print_list


def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # we start counting from 5 and stop at 7

    if (start <= stop):
     counter = start
    while (counter <= stop):
        print(counter)
        counter += 1
    else:
        print(f"an error has occured stop at {stop} and start at {start}")




count_up(5, 7)        

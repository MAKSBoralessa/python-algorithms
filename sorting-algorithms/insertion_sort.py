

def insertion_sort(a_list):

    #Traverse through 1 to len(a_list)
    for i in range(1, len(a_list)):

        key = a_list[i]

        #Move elements of a_list[0,...,i-1], that are
        #greater than the key, to one position ahead
        #of their current position
        j = i -1
        while j >= 0 and key < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = key

    return a_list

a_list = [2, 4, 5, 3, 1]
print(a_list)
print(insertion_sort(a_list))

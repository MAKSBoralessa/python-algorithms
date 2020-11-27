

def bubble_sort(a_list):
    n = len(a_list)

    #Traverse through all array elements
    for i in range(n-1):

        #Last i elements are already in place
        for j in range(0, n-i-1):

            #Traverse the array from 0 to n-i-1
            #Swap if the element found is greater
            #than the next element
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

#Testing the bubble_sort function
a_list = [2, 5, 3, 4, 1]
print(a_list)
print(bubble_sort(a_list))

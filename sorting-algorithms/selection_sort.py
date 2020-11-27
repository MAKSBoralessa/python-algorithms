a_list = [3, 2, 1, 5, 4]

print(a_list)

for i in range(len(a_list)):
    #Find the minimum element in the unsorted part of the array
    min_ = i
    for j in range(i+1, len(a_list)):
        if a_list[min_] > a_list[j]:
            min_ = j

    #Swap the found minimum element with first element
    a_list[i], a_list[min_] = a_list[min_], a_list[i]

print(a_list)

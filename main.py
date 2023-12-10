from collections import Counter

def nth_most_rare(lst, n):
    # Use Counter to get the frequency of each element
    frequency_counter = Counter(lst)

    # Sort the elements based on frequency and then by value
    sorted_items = sorted(frequency_counter.items(), key=lambda x: (x[1], x[0]))

    # Extract the nth-rarest item from the sorted list
    if n <= len(sorted_items):
        return sorted_items[n - 1][0]
    else:
        return None  # Return None if n is out of range

# Example 
my_list = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n_value = 2
result = nth_most_rare(my_list, n_value)
print(result)

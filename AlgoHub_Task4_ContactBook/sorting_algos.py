# Week 4: Sorting algorithms implementation (using Python built-in and custom logic)[span_0](start_span)[span_0](end_span)

def bubble_sort_contacts(contacts_list):
    """
    Sorting contacts alphabetically by name using basic sorting algorithm logic.[span_1](start_span)[span_1](end_span)
    """
    n = len(contacts_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contacts_list[j]['name'].lower() > contacts_list[j + 1]['name'].lower():
                # Swap elements
                contacts_list[j], contacts_list[j + 1] = contacts_list[j + 1], contacts_list[j]
    return contacts_list

def optimized_sort(contacts_list):
    """
    Using Python's built-in efficient sorting (Timsort - O(N log N)) 
    as mentioned in Week 4 models/tools (sorted()).[span_2](start_span)[span_2](end_span)
    """
    return sorted(contacts_list, key=lambda x: x['name'].lower())
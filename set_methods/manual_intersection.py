def manual_intersection(main_set, *sub_sets):
    result = set()

    for main_item in main_set:
        found = any(main_item in sub_set for sub_set in sub_sets)
        if found:
            result.add(main_item)
    
    return result
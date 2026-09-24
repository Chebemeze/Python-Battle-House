def unmatched_skus(warehouse_a, warehouse_b):
    # TODO: compute the symmetric difference using union/intersection/difference,
    # without using ^ or .symmetric_difference()
    warehouse_a_difference = warehouse_a.difference(warehouse_b)
    warehouse_b_difference = warehouse_b.difference(warehouse_a)
    return warehouse_a_difference | warehouse_b_difference

print(unmatched_skus({"X"}, set()))

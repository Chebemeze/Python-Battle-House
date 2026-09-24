def fulfill_orders(stock, orders):
    # TODO: process orders in sequence against a working copy of stock.
    # Fulfill only orders where every item is fully available; deduct nothing
    # for rejected orders. Do not modify the `stock` argument.

    #1 form a copy of stock - done
    #2 check if order exist in the copy. if it exit go further to check agaist the available quantity. - done
    #forms a temp dictionary that will be appended to the actual remaining stock if one order is performed -done. if successful it appends the deducted to remaining stock and adds the id to fulfilled. if rejected it adds the id to rejected - done.
    #orders is a list of dictionary, each dictionary is an order
    #if it exist and quantity ordered is lower.

    stock_copy = {key: value for key, value in stock.items()}
    stock_status = {"fulfilled": [], "rejected": [], "remaining_stock": stock_copy}

    for order in orders:
        temp_dict = {}
        #tracking state variable for orders
        is_order_acceptable = True
        for product, quantity in order["items"].items():
            if product in stock_copy:
                if quantity <= stock_copy[product]:
                    temp_dict[product] = stock_copy[product] - quantity
                else:
                    is_order_acceptable = False
                    break
            else:
                is_order_acceptable = False
                break
        if is_order_acceptable:
            stock_status["remaining_stock"].update(temp_dict)
            stock_status["fulfilled"].append(order["id"])
        else:
            stock_status["rejected"].append(order["id"])
    return stock_status

print(fulfill_orders({"a": 5, "b": 1}, [{"id": "o1", "items": {"a": 2, "b": 5}}]))
print(fulfill_orders({"apple": 5}, [{"id": "o1", "items": {"apple": 2}}, {"id": "o2", "items": {"apple": 4}}]))
print(fulfill_orders({"apple": 5}, []))

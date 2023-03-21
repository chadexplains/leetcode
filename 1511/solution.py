def getCustomerWithOrders(orders: List[List[str]]) -> List[int]:
    orders.sort(key=lambda x: (x[0], x[1]))
    customer_orders = {}
    result = []
    for order in orders:
        customer_id, order_time, _ = order
        if customer_id not in customer_orders:
            customer_orders[customer_id] = []
        if customer_orders[customer_id] and order_time - customer_orders[customer_id][-1] <= timedelta(hours=1):
            result.append(customer_id)
        customer_orders[customer_id].append(order_time)
    return list(set(result))
"""Logic from Assignment_1.ipynb, Part II, copied unchanged for the Streamlit app."""
from starter import delivery_times


def calculate_late_cost(costs):
    # Direct refund cost for a late order
    refund_cost = costs["refund"]

    # Churn cost: future lost orders multiplied by profit margin per order
    churn_cost = costs["churn_orders"] * costs["margin"]

    # Total cost per late order
    total_cost = refund_cost + churn_cost
    return total_cost


def find_best_promise(zone, time_block, promise_list, costs, seed=1):
    # Calculate total cost per late order using our previous logic
    cost_per_late = calculate_late_cost(costs)

    best_promise = None
    max_net_profit = -999999.0

    for p in promise_list:
        # Simulate delivery times for this specific promise
        times = delivery_times(zone, time_block, promise=p, seed=1)
        n_orders = len(times)

        if n_orders == 0:
            net_profit = 0.0
        else:
            # Count how many orders arrived after the promised time (late)
            n_late = sum(1 for t in times if t > p)

            # Gross profit collected from all orders
            gross_profit = n_orders * costs["margin"]

            # Total late costs incurred
            total_late_cost = n_late * cost_per_late

            # Net profit = Gross profit minus late costs
            net_profit = gross_profit - total_late_cost

        # Track the promise that yields the highest net profit
        if net_profit > max_net_profit:
            max_net_profit = net_profit
            best_promise = p

    return best_promise, max_net_profit

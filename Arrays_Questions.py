# Array Questions

def even_odd(A):
    #   An array boot camp. Input an array of integers and reorder its entries 
    # so that the even entris appear first.
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

#   q1: If we can define a function to switch element of array, that might
# increase time complexity, since the array itself has index searching.


# buy stock question - given list, buy once and return max profit method.
def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit




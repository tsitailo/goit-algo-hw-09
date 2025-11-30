import time

def find_coins_greedy(amount):
    """
    Знаходить решту використовуючи жадібний алгоритм.
    Завжди вибирає найбільший можливий номінал монети.
    """
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    
    for coin in coins:
        count = amount // coin
        if count > 0:
            change[coin] = count
            amount -= coin * count
    
    return change

def find_min_coins(amount):
    """
    Знаходить мінімальну кількість монет для решти використовуючи динамічне програмування.
    Гарантує знаходження глобального оптимуму (мінімальної кількості монет).
    """
    coins = [50, 25, 10, 5, 2, 1]
    # min_coins[i] зберігає мінімальну кількість монет для суми i
    # Ініціалізуємо нескінченністю, крім 0 (для суми 0 потрібно 0 монет)
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    # coin_used[i] зберігає останню монету, додану для досягнення суми i
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin
    
    # Відновлення результату (які саме монети були використані)
    change = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        current_amount -= coin
        
    return change

if __name__ == "__main__":
    test_amount = 113
    
    print(f"Сума: {test_amount}")
    print("Жадібний алгоритм:", find_coins_greedy(test_amount))
    print("Динамічне програмування:", find_min_coins(test_amount))
    
    # Невеликий тест продуктивності
    large_amount = 5248
    
    start_time = time.time()
    find_coins_greedy(large_amount)
    print(f"\nЖадібний (сума {large_amount}): {time.time() - start_time:.6f} сек")
    
    start_time = time.time()
    find_min_coins(large_amount)
    print(f"Динамічний (сума {large_amount}): {time.time() - start_time:.6f} сек")

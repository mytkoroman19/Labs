def get_max(piles):
    """Ручна реалізація пошуку максимуму в списку"""
    if not piles:
        return 0
    max_val = piles[0]
    for x in piles:
        if x > max_val:
            max_val = x
    return max_val

def manual_ceil(n, d):
    """Ручна реалізація округлення вгору при діленні n на d"""
    
    if n % d == 0:
        return n // d
    else:
        return (n // d) + 1

def min_eating_speed(piles, H):
    low = 1
   
    high = get_max(piles)
    result = high

    while low <= high:
        k = (low + high) // 2
        total_time = 0
        
       
        for count in piles:
            total_time += manual_ceil(count, k)
        
        if total_time <= H:
            result = k
            high = k - 1
        else:
            low = k + 1
            
    return result

def main():
    print(" Програма для розрахунку швидкості Джекі ")
    try:
        raw_input = input("Введіть кількість бананів у кошиках через пробіл: ")
        piles = [int(x) for x in raw_input.split()]
        H = int(input("Введіть кількість годин (H): "))

        if H < len(piles):
            print("Помилка: годин менше ніж кошиків!")
            return

        k = min_eating_speed(piles, H)
        print(f"Мінімальна швидкість: {k} банан(ів)/год")
    except ValueError:
        print("Вводьте лише цифри!")

if __name__ == "__main__":
    main()
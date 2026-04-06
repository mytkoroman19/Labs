def find_kth_lightest(weights, k):
    if not (1 <= k <= len(weights)):
        raise ValueError(f"Помилка: k повинно бути від 1 до {len(weights)}.")
  
    indexed_weights = list(enumerate(weights))

   
    indexed_weights.sort(key=lambda x: x[1])

 
    original_index, weight = indexed_weights[k - 1]
    return weight, original_index

def main():
    print(" Програма для аналізу маси вантажів ")
    
    try:
   
        raw_input = input("Впишіть масу вантажів (через пробіл або кому): ")
        
     
        weights = [float(w) for w in raw_input.replace(',', ' ').split()]
        
        if not weights:
            print("Ви не ввели жодного числа.")
            return

    
        k_value = int(input(f"Який за рахунком вантаж знайти (від 1 до {len(weights)}): "))

    
        weight, position = find_kth_lightest(weights, k_value)

        print(" Результат аналізу")
        print(f"Відсортовані маси: {sorted(weights)}")
        print(f"{k_value}-й за масою вантаж: {weight}")
        print(f"Його позиція в оригінальному списку (індекс): {position}")

    except ValueError as e:
        print(f"Помилка введення: Переконайтеся, що вводите лише числа. {e}")

if __name__ == "__main__":
    main()
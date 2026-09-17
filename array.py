import random
 
def generate_array(length, min_v, max_v):
    return [random.randint(min_v, max_v) for _ in range(length)]
 
def count_sum_even_in_range(arr, from_i, to_i):
    evens = [x for x in arr[from_i:to_i + 1] if x % 2 == 0]
    return len(evens), sum(evens)
 
def average_and_count_above(arr):
    avg = sum(arr) / len(arr)
    count = sum(1 for x in arr if x > avg)
    return avg, count
 
def pairwise_sum(a, b):
    return [x + y for x, y in zip(a, b)]
 
def concat(a, b):
    return a + b
 
def swap_max_min(arr):
    max_i = arr.index(max(arr))
    min_i = arr.index(min(arr))
    arr[max_i], arr[min_i] = arr[min_i], arr[max_i]
    return arr
 
def split_positive_negative(arr):
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    return pos, neg
 
def remove_max_min_duplicates(arr):
    mx, mn = max(arr), min(arr)
    result = []
    max_used = min_used = False
    for x in arr:
        if x == mx:
            if max_used:
                continue
            max_used = True
        elif x == mn:
            if min_used:
                continue
            min_used = True
        result.append(x)
    return result
 
def between_averages(a, b):
    avg_a, avg_b = sum(a) / len(a), sum(b) / len(b)
    low, high = min(avg_a, avg_b), max(avg_a, avg_b)
    return [x for x in a + b if low <= x <= high]
 
if __name__ == "__main__":
    arr = generate_array(10, -20, 20)
    print("Масив:", arr)
 
    count, s = count_sum_even_in_range(arr, 2, 7)
    print(f"1) Парних у [2..7]: кількість={count}, сума={s}")
 
    avg, cnt = average_and_count_above(arr)
    print(f"2) Середнє={avg:.2f}, більших за середнє={cnt}")
 
    a = generate_array(5, 1, 10)
    b = generate_array(5, 1, 10)
    print("3) a =", a, " b =", b)
    print("   Попарна сума:", pairwise_sum(a, b))
 
    c = generate_array(7, 1, 10)
    print("4) Конкатенація a+c:", concat(a, c))
 
    arr5 = generate_array(8, -10, 10)
    print("5) До:", arr5)
    swap_max_min(arr5)
    print("   Після:", arr5)
 
    pos, neg = split_positive_negative(arr)
    print("6) Додатні:", pos, " Від'ємні:", neg)
 
    arr7 = [1, 5, 3, 5, 2, 1, 5]
    print("7) До:", arr7, " Після:", remove_max_min_duplicates(arr7))
 
    print("8) Між середніми a і c:", between_averages(a, c))
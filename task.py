# 1. Хөөсөн эрэмбэлэлт (Bubble Sort)
def bubble_sort(arr):
    """
    Bubble Sort алгоритм ашиглан массивыг эрэмбэлэх.
    """
    pass

# 2. Сонгох эрэмбэлэлт (Selection Sort)
def selection_sort(arr):
    """
    Selection Sort алгоритм ашиглан массивыг эрэмбэлэх.
    """
    pass

def run_tests():
    # Тест хийх өгөгдөл
    test_array = [64, 34, 25, 12, 22, 11, 90]
    expected_result = sorted(test_array)

    test_cases = [
        (bubble_sort, "Хөөсөн эрэмбэлэлт (Bubble Sort)"),
        (selection_sort, "Сонгох эрэмбэлэлт (Selection Sort)"),
    ]

    attempted = 0
    correct = 0

    print("Эрэмбэлэх алгоритмын тестүүд")

    for func, name in test_cases:
        try:
            # Массивыг хуулбарлаж авна (эх утгыг өөрчлөхгүйн тулд)
            data = test_array.copy()
            
            # Функцийг дуудах
            # Хэрэв функц утга буцаахгүй (None) бол массивыг шууд өөрчилсөн гэж үзнэ.
            result = func(data)
            actual_output = result if result is not None else data

            # Хэрэв массив анхны байснаараа байвал оролдоогүй гэж үзнэ
            if actual_output == test_array:
                print(f"{name}: ОРОЛДООГҮЙ (Массив хэвээрээ байна)")
                continue

            attempted += 1

            if actual_output == expected_result:
                print(f"{name}: ЗӨВ")
                correct += 1
            else:
                print(f"{name}: БУРУУ (Үр дүн: {actual_output})")

        except Exception as e:
            print(f"{name}: АЛДАА ГАРЛАА ({e})")

    print("\n" + "="*35)
    print(f"Оролдсон: {attempted}/{len(test_cases)}")
    print(f"Зөв: {correct}/{len(test_cases)}")
    print("="*35)

if __name__ == "__main__":
    run_tests()
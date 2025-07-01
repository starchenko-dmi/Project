def total_numbers(arg: list[int], arg_2: list[int]) -> list[int]:
    """Функция принимает два списка чисел, и возвращает список пересекающихся числ"""
    total_number = set(arg).intersection(set(arg_2))
    return list(total_number)


print(total_numbers([1, 2, 3, 4], [3, 4, 5, 6]))


def is_palindrome(arg: list[int]) -> list[int]:
    """Функция принимает список чисел и возвращает список чисел являющихся полиндромами"""
    numbers_palindrome = []
    for num in arg:
        if str(num) == str(num)[::-1]:
            numbers_palindrome.append(num)
    return numbers_palindrome


print(is_palindrome([121, 123, 131, 34543]))


def different_numbers(arg: list[int], arg_2: list[int]) -> list[int]:
    """Функция принимает два списка чисел и возвращает список, содержащий не повторяющиеся числа"""
    different_number = set(arg).difference(set(arg_2))
    different_number_1 = set(arg_2).difference(set(arg))
    return list(different_number.union(different_number_1))


print(different_numbers([1, 2, 3, 4], [3, 4, 5, 6]))


def area_of_circle(r: float) -> float:
    """Функция принимает радиус круга и возвращает его площадь"""
    PI = 3.14
    circle_area = PI * r**2
    return circle_area


def format_description(r: float, area: float) -> str:
    """Функция принимает значение радиуса круга и его площади и возвращает информацию в текстовом фопмате,
    площадь круга округляется до 2 знаков после запятой"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float) -> None:
    """Функция принимает значение радиуса круга, использут фунции area_of_circle и format_description
    и печатает результат работы функции format_description в консоль"""
    area = area_of_circle(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)

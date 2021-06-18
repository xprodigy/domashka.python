print('Lesson 2_1')

list_any_elements = [543, -0, 2342, 0xfff, False, 'False', (-0.1 - 0.2j), None, [1, 2], [1, 2.0], (1, 2.0),
                     ZeroDivisionError, {"1": 500, 2: 400, "key3": True, 4: None}, frozenset('weqweq')]

for i, element in enumerate(list_any_elements):
    print(f"Element {i:02}: {element} - {type(element)}")

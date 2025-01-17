# 1. https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# 2. https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)

# 3. https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# 4. https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    pos = []
    neg = 0
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg += i
            
    return [len(pos),neg]

# 5. https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
def check(seq, elem):
    if elem in seq:
        if type(elem) == str or type(elem) == int:
            return True
    else:
        return False
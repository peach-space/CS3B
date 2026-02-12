#################################################
# CS03B - Winter 2026
# Assignment 2
# Student Name: Cen Li
# SID: 20713344
#################################################
def run():
    """ from Question 1 to Question 4 """
    # Question 1-A
    color_names = ["Black", "Red", "Maroon", "Yellow"]
    color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    output = zip(color_names, color_codes)
    color_list = []
    for color, code in output:
        color_list.append({"color_name":color, "color_code": code})
    print(color_list)

    # Question 1-B
    keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
    values = [1, 2, 2, 3]

    result = {}
    for k,v in zip(keys, values):
        result.setdefault(k, set()).add(v)
    print(result)

    #Question 2-A
    x = {'key1': 1, 'key2': 3, 'key3': 2}
    y = {'key1': 1, 'key2': 2}
    match = {}
    for k,v in x.items():
        for i,j in y.items():
            if v == j and k == i:
                match[k] = v
    for k,v in match.items():
        print(f"{k}: {v} is present in both x and y")

    #Question 2-B
    x = {'Math':81, 'Physics':83, 'Chemistry':87}
    output_2 = []
    for k,v in x.items():
        output_2.append((k,v))
    output_2.sort(key=lambda item: item[1], reverse=True)
    print(output_2)

    #Question 3
    sentences = "Let's take LeetCode contest"
    result_3 = sentences.split()
    temp_list = []
    for word in result_3:
        temp_list.append(word[::-1])
        reversed_sentences = " ".join(temp_list)
    print(reversed_sentences)

    # Question 4
def k_grammar(N,K):
    row = "0"
    for i in range(N-1):
        next_row = ""
        for num in row:
            if num == "0":
                next_row += "01"
            else:
                next_row += "10"
        row = next_row

    return row[K-1]


if __name__ == '__main__':
    run()
    result = k_grammar(4,5)
    print(result)


# if __name__ == "__main__":
#     # This allows students to run this specific file
#     # individually for testing (e.g., `python q1.py`)
#     run()
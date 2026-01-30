#################################################
# Lab 4
# Student Name: Cen Li
#################################################
def num_analysis():
    nums = []
    print("Please enter 20 numbers")
    for i in range(20):
        while True:
            try:
                num = float(input(f"Enter number: "))
                nums.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    results = {
        "min": min(nums),
        "max": max(nums),
        "sum": sum(nums),
        "avg": sum(nums) / len(nums)
    }

    return results


def initials():
    full_name = input("Enter a first, middle, and last name: ")
    name_parts = full_name.split()
    initials_list = []
    for name in name_parts:
        initials_list.append(f"{name[0].upper()}.")

    result = "".join(initials_list)
    return result


def main():
    print("Welcome to the Number Analysis Program!")
    data = num_analysis()
    print("\n--------------------------")
    print("      Final Analysis")
    print("--------------------------")
    print(f"Lowest:  {data['min']}")
    print(f"Highest: {data['max']}")
    print(f"Total:   {data['sum']}")
    print(f"Average: {data['avg']:.2f}")

    print("--- Name Initials Generator ---")
    try:
        final_initials = initials()
        print(f"The initials are: {final_initials}")
    except IndexError:
        print("Error: You didn't enter any names.")

if __name__ == "__main__":
    main()
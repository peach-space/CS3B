#################################################
# Lab 5
# Student Name: Cen Li
#################################################

def power(x,n):
    if n < 1:
        return 1
    else:
        return x*power(x,n-1)

def main():
    result = power(2,3)
    print(result)

if __name__ == "__main__":
    main()
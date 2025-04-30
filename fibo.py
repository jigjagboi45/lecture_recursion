
def recursive_nth_fibo(num):
    # <= misto == je pojistka pred nekonecnou rekurzi
    if num <= 0:
        return 0
    if num == 1:
        return 1
    else:
        return recursive_nth_fibo(num - 1) + recursive_nth_fibo(num - 2)


def main():
    ntc = int(input("Zadejte cislo "))
    print(f"{ntc}. prvek posloupnosti je {recursive_nth_fibo(ntc)}")

if __name__ == "__main__":
    main()

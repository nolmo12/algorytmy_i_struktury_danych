#zad 1
def number(n:int):
    if(n<0):
        return

    print(n)
    number(n-1)

number(10)
#zad 2
def fib(n:int)->int:
    if(n<=2):
        return 1
    return fib(n-1)+fib(n-2)

print(fib(5))
#zad 3
def power(number:int, n:int)->int:
    if(n==0):
        return 1
    if(n==1):
        return number
    return number*power(number, n-1)

print(power(2,4))
#zadanie 4
def reverse(txt:str)->str:
    if len(txt)==0:
        return txt
    else:
        return reverse(txt[1:])+txt[0]

str="Tata"
print(reverse(str))
#zadanie 5
def factorial(n:int)->int:
    if(n<2):
        return 1
    if(n==2):
        return n
    return n*factorial(n-1)

print(factorial(6))
#zadanie 6
def prime(n:int, i:int=2)->bool:
    if (n <= 2):
        return True if (n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return prime(n, i + 1)

a=5
print(prime(a))
#zadanie 7
def n_sums(n: int, licz: int, lista=[])->list[int]:
    if licz > (10 ** n):
        return lista
    temp = [int(x) for x in str(licz)]
    if sum(temp[::2]) == sum(temp[1::2]):
        lista.append(licz)
    return n_sums(n, licz + 1, lista)
#zadanie 8

#zadanie 9
def remove_duplicates(txt: str) -> str:
    if len(txt) == 1:
        return txt[0]
    if txt[0] != txt[1]:
        return txt[0] + remove_duplicates(txt[1:])
    else:
        return remove_duplicates(txt[1:])
#zadanie 10
def printParenthesis(str, n):
    if (n > 0):
        _printParenthesis(str, 0,
                          n, 0, 0)
    return


def _printParenthesis(str, pos, n,
                      open, close):
    if (close == n):
        for i in str:
            print(i, end="")
        print()
        return
    else:
        if (open > close):
            str[pos] = '}'
            _printParenthesis(str, pos + 1, n,
                              open, close + 1)
        if (open < n):
            str[pos] = '{'
            _printParenthesis(str, pos + 1, n,
                              open + 1, close)


# Driver Code
n = 2
str = [""] * 2 * n
printParenthesis(str, n)

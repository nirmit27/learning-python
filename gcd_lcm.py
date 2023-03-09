# Euclidean GCD Algorithm

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd((b % a), a)


def lcm(a, b):
    return (a*b)//gcd(a, b)


if __name__ == "__main__":
    n = list(input("\n Enter two integers : ").split(' '))
    print(
        f"\n GCD of {n[0]} and {n[1]} is {gcd(int(n[0]),int(n[1]))}\n LCM of {n[0]} and {n[1]} is {lcm(int(n[0]),int(n[1]))}\n")

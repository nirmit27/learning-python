# Tower of Hanoi

def toh(n, src, dest, aux):
    if n == 1:
        print(f" Move disk 1 from {src} to {dest}.")
        return
    else:
        toh((n-1), src, aux, dest)
        print(f" Move disk {n} from {src} to {dest}.")
        toh((n-1), aux, dest, src)


if __name__ == "__main__":
    n = int(input("\n Enter the number of disks: "))
    print(f"\n Solution to the Tower of Hanoi problem for {n} disks :-\n")
    toh(n, 'A', 'B', 'C')

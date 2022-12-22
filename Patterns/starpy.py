# Star Patterns

menu = "STAR PATTERN PROGRAM"
print(f"\n{menu.center(32)}")
print("-------------------------------")
opt = 1

while opt:
  opt = list(input(" Enter the rows and type : ").split(' '))
  row = int(opt[0])
  ch = int(opt[1])

  print("\n Here's your pattern ...\n")

  if ch == 1:
    #           *
    #         * *
    #       * * *
    #     * * * *
    #   * * * * *
    for i in range(row):
      sp = row
      j = 0
      print("\t\t", end='')
      while (1):
        if sp > i:
          print("  ", end='')  # 2 spaces
          sp -= 1
          continue
        elif j <= i:
          print("* ", end='')
          j += 1
          continue
        else:
          break
      print()

  elif ch == 2:
    #   *
    #   * *
    #   * * *
    #   * * * *
    #   * * * * *
    for i in range(row):
      j = 0
      print("\t\t", end='')
      while (1):
        if j <= i:
          print("* ", end='')
          j += 1
          continue
        else:
          break
      print()

  elif ch == 3:
    #       *
    #      * *
    #     * * *
    #    * * * *
    #   * * * * *
    for i in range(row):
      sp = row
      j = 0
      print("\t\t", end='')
      while (1):
        if sp > i:
          print(" ", end='')  # 1 space
          sp -= 1
          continue
        elif j <= i:
          print("* ", end='')
          j += 1
          continue
        else:
          break
      print()

  elif ch == 4:
    #   * * * * *
    #    * * * *
    #     * * *
    #      * *
    #       *
    for i in range(row, 0, -1):
      sp = row - i
      j = 0
      print("\t\t", end='')
      while (1):
        if sp > 0:
          print(" ", end='')  # 1 space
          sp -= 1
          continue
        elif j < i:
          print("* ", end='')
          j += 1
          continue
        else:
          print()
          break
  
  opt = int(input("\n Want more? (0/1)\t"))
  print("-------------------------------")
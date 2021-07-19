cisla = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]

suda = licha = rozdil = 0
while cisla:
  cislo = cisla.pop(0)
  if (cislo % 2) == 0:
    suda += cislo
  else:
    licha += cislo

rozdil = abs(suda - licha)
print("soucet suda cisla: ", suda)
print("soucet licha cisla: ", licha)
print("rozdil je: ", rozdil)

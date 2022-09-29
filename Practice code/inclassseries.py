n = int(input("Enter the number of terms in the series: "))
series_num = 0
for k in range(n):
    series_num += 1/(2**k)
    print(k)
print(series_num)

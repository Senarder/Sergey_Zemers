def count_digits(number):
    if len(str(number)) == 1:
        return number

    else:
        number_sum = 0

        for i in range(len(str(number))-1):
            number_sum += int(str(number)[i])
            print(str(number)[i], end=" + "),

        number_sum += int(str(number)[-1])
        print(str(number)[-1], end=" "),

        print("= " + str(number_sum))

        if len(str(number_sum)) != 1:
            return count_digits(number_sum)
        else:
            return number_sum


print(count_digits(155), end="\n\n")
print(count_digits(5), end="\n\n")
print(count_digits(7456132), end="\n\n")

def main():
    months = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
    }

    months["Apr2"] = "April2"

    months.update({"Mon": "Monday", "Tue": "Tuesday"})

    print(len(months))
    print(months)

    for month in months:
        print(month + ": " + months[month])


    for (sh_month, l_month) in months.items():
        print(sh_month + ": " + l_month)

    for month in months.values():
        print(month)

main()
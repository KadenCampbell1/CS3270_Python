import calendar


def main():
    with open(f'gas_prices.txt') as IN_FILE:
        data = IN_FILE.read().strip().split()
        date_price = []

        for i in data:
            v = i.split(":")
            date = v[0].split("-")
            date = (date[0], date[-1])
            date_price.append((date, v[-1]))

    with open("gas_report.txt", "w") as OUT_FILE:
        year = 1994
        month = 1
        month_list = []
        year_avg_list = []
        month_avg_list = []
        low_price = 100
        high_price = -1
        text = []

        while year <= int(date_price[-1][0][-1]):
            for time, price in date_price:
                if int(time[-1]) == year:
                    year_avg_list.append(float(price))
                    if int(time[0]) == month:
                        month_avg_list.append(float(price))
                        month_list.append((time, price))

            for i in month_list:
                if float(i[-1]) < low_price:
                    low_price = float(i[-1])
                elif float(i[-1]) > high_price:
                    high_price = float(i[-1])

            text.append((calendar.month_name[month], sum(month_avg_list) / len(month_avg_list)))
            month_list.clear()
            month_avg_list.clear()
            month += 1

            if month > 12:
                year_avg = sum(year_avg_list) / len(year_avg_list)
                OUT_FILE.write(f"{year}:\n")
                OUT_FILE.write(f"\tLow: ${low_price:.2f}, Avg: ${year_avg:.2f}, High: ${high_price:.2f}\n")
                for i, v in text:
                    OUT_FILE.write(f"\t{i:10} ${v:.2f}\n")
                text.clear()
                low_price = 100
                high_price = -1
                year += 1
                month = 1


if __name__ == "__main__":
    main()

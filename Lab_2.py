filename = "C:/Lab2/GOOG.csv"

def get_data(file_name):
    """ Read the data from the file_name and save them into a 2-D list or any other data structure for processing

    :param file_name:  <str> - the file's name you saved for the stock's prices
    :return: a list of lists <list> (2-D list), or any other data structure you think more efficient
    """
    with open(filename, "r") as f:
        next(f)
        data = []
        for row in f:
            row = row.strip("\n")
            row = row.split(",")
            data.append(row)
        return data

def get_averages_by_month(list, month):
    """

       :param data_list:  <list> - the list that you will process
       :param month: <int> - from which month you want the statistics
       :return: a float which is the average price of that month
       """
    sale = 0.00
    volume = 0.00
    for rows in list:
        date = rows[0].split("/")
        if int(date[0]) == month:  # date sub zero will give me the very first element of every date
            sale += float(rows[5]) * float(rows[6])
            volume += float(rows[6])
    avg = sale/volume
    return avg

def get_highest_by_month(list, month):
    """

        :param data_list: <list> - the list that you will process
        :param month: <int> - from which month you want the statistics
        :return: a float which is the highest price of that month
        """
    max = 0
    for rows in list:
        date = rows[0].split("/")
        if int(date[0]) == month:
            if max < float(rows[5]):
                max = float(rows[5])
    return max

data_list = get_data(filename)
print(data_list)
#print("This is the data from the csv file: Goog.csv")

#avg_aug = get_averages_by_month(data_list, 8)
#avg_jun = get_averages_by_month(data_list, 6)
#print(avg_aug)
#print("June's Average Stock price")
#print(avg_jun)
#print("August's Average Stock price")

#jun_highest = get_highest_by_month(data_list, 6)
#print(jun_highest)
#print("June's Highest Closing Price")
from datetime import date, timedelta

from Item import *


def createItems():
    items = list()
    names = ("Banana", "Bread", "Sprite", "Cans", "Milk")
    releaseDates = (date.today(), date(2021, 12, 31), date(2022, 2, 15), date(2021, 6, 26), date(2022, 2, 14))
    expiryDates = (
    date.today() + timedelta(days=10), date(2022, 1, 7), date(2022, 9, 15), date(2077, 2, 28), date(2022, 2, 18))
    prices = (7.5, 14.88, 22.8, 69, 27)
    for i in range(5):
        items.append(Item(names[i], releaseDates[i], expiryDates[i], prices[i], expiryDates[i] - releaseDates[i]))
    return items


def fillFile(path, items):
    with open(path, "wb") as writer:
        for i in range(len(items)):
            itemInfo = f"{items[i].name:<8}  {str(items[i].releaseDate):<12}  {str(items[i].expiryDate):<12} {str(items[i].price):<4}\n"
            writer.write(str.encode(itemInfo))

def printItems(items):
    print("\nItems: ")
    for i in range(len(items)):
        itemInfo = f"{items[i].name:<8}  {str(items[i].releaseDate):<12}  {str(items[i].expiryDate):<12} {str(items[i].price):<4} "
        print(itemInfo)

def editPrices(items):
    for item in items:
        if item.lifeDuration.days <= 14:
            item.price = round(item.price * 0.95, 2)
        elif item.lifeDuration.days > 365:
            item.price = round(item.price * 1.03, 2)
    return items

def copyToNewFile(items, path):
    print()
    with open(path, "wb") as writer:
        todayDate = date.today()
        for item in items:
            if item.releaseDate < date(todayDate.year, todayDate.month, 1):
                itemInfo = f"{item.name:<8}  {str(item.releaseDate):<12}  {str(item.expiryDate):<12} {str(item.price):<4}\n"
                print(itemInfo, end="")
                writer.write(str.encode(itemInfo))

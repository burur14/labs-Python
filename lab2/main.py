import funcs

if __name__ == "__main__":
    items = funcs.createItems()
    path = input("Enter file's name: ") + ".bin"

    funcs.fillFile(path, items)
    funcs.printItems(items)

    items = funcs.editPrices(items)
    funcs.fillFile(path, items)
    print("Prices have been edited!")
    funcs.printItems(items)

    newPath = input("\nEnter new file's name:") + ".bin"
    funcs.copyToNewFile(items, newPath)

from tkinter import*
root = Tk()
root.title("SORTED")
root.geometry("400x270")
frame = Frame(root)
root.config(bg="#45c9b1")
myList = [42, 12, 13, 89, 63, 11]
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

mergeSort(myList)
label = Label(root, text=myList)
label.place(x=100, y=115)
label.config(bg="#45c9b1", font="Consolas 15 bold")

root.mainloop()

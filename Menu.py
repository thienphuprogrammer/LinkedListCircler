from CircleLinkedList import CircleLinkedList

def Menu():
    print("+----------------------+")
    print("| 1.Insert first       |")
    print("| 2.Insert last        |")
    print("| 3.Insert after       |")
    print("| 4.display            |")
    print("| 5.delete first       |")
    print("| 6.delete last        |")
    print("| 7.delete after       |")
    print("| 8.get size           |")
    print("+----------------------+")

    while True:
        choice = int(input('Nhập lựa chọn của ní:'))

        if choice == 1:
            data = input()
            CircleLinkedList.insertfirst(data)
        elif choice == 2:
            data = input()
            CircleLinkedList.insertlast(data)
        elif choice == 3:
            data = input()
            CircleLinkedList.insertafter(data)
        elif choice == 4:
            data = input()
            CircleLinkedList.display()
        elif choice == 5:
            print('coming soon')
        elif choice == 6:
            print('coming soon')
        elif choice == 7:
            print('coming soon')
        elif choice == 8:
            print('coming soon')
        else:
            print('lựa chọn chỉ trong khoản từ 1 - 8')

Menu()

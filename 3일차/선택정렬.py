array=[40, 90, 10, 50, 20];

#입력된 자료 출력
print("SELECTION Sort");
for k in range(0, len(array)):
    print(array[k],end=" ");
print();

#선택 정렬과 출력(과정)
for i in range(0, len(array)-1):
    min=i;
    for j in range(i+1, len(array)):
        if(array[j]<array[min]):
            min=j;
    temp=array[i];
    array[i]=array[min];
    array[min]=temp;

    for k in range(0, len(array)):
        print(array[k],end=" ");
    print();


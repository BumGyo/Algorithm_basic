array=[40, 90, 10, 50, 20];

#�Էµ� �ڷ� ���
print("SELECTION Sort");
for k in range(0, len(array)):
    print(array[k],end=" ");
print();

#���� ���İ� ���(����)
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


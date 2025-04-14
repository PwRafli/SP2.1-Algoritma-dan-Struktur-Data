from queue import LifoQueue

setak =  LifoQueue(maxsize = 6);
print(setak.qsize());

setak.put('A');
setak.put('B');
setak.put('C');
setak.put('D');
setak.put('E');
setak.put('F');

print('full :', setak.full());
print('size :', setak.qsize());

print('\nElement dikeluarkan dari stack');
print(setak.get());
print(setak.get());
print(setak.get());
print(setak.get());
print(setak.get());
print(setak.get());

print('\nEmpty: ', setak.empty());
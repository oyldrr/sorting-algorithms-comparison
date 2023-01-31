# Qucik Sort algoritmasının python programı olarak uygulanması

import random # Random kütüphanesinin dahil edilmesi

#Sıralama işlemlerinin uygulanacağı fonksiyonlar
def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)

		quickSort(array, low, pi - 1)

		quickSort(array, pi + 1, high)

data = list(range(10000000)) # 0'dan başlayarak içine girilen değere kadar
						 # artan düzende dizi oluşturma

random.shuffle(data) # Oluşturulan sıralı diziyi rastgele şekilde karıştırma

size = len(data) # Dizinin uzunluğunu bir değişkene atama

print("Unsorted Array : ", data) # Karıştırılan diziyi ekrana yazdırma
print("-"*100) # Çizgi çekmek için kullanılan kod (Gerekli değil)
quickSort(data, 0, size - 1) # Sıralama işlemi için fonksiyonu çağırma
print('Sorted Array : ', data) # Sıralanmış diziyi ekrana yazdırma


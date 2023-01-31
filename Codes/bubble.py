# Bubble Sort algoritmasının python programı olarak uygulanması

import random # Random kütüphanesinin dahil edilmesi

# Sıralama işleminin uygulanacağı fonksiyon
def bubbleSort(arr): 
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = list(range(1000)) # 0'dan başlayarak içine girilen değere kadar
						# artan düzende dizi oluşturma

random.shuffle(arr)	# Oluşturulan sıralı diziyi rastgele şekilde karıştırma

print("Unsorted array : ", arr) # Karıştırılan diziyi ekrana yazdırma
print("-"*100) # Çizgi çekmek için kullanılan kod (Gerekli değil)
bubbleSort(arr) # Sıralama işlemi için fonksiyonu çağırma

print("Sorted array :", arr) # Sıralanmış diziyi ekrana yazdırma


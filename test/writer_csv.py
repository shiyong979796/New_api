import csv

from my_path import product_goods_path

aa = [{'goodsId': 1035594, 'catId': 2, 'goodsName': 'Azazie Heaton BG', 'colorId': 11620, 'sizeId': 9564},
      {'goodsId': 1051778, 'catId': 2, 'goodsName': 'Azazie Dysis BG', 'colorId': 11629, 'sizeId': 6769},
      {'goodsId': 1035604, 'catId': 2, 'goodsName': 'Azazie Delaina BG', 'colorId': 11630, 'sizeId': 6767},
      {'goodsId': 1006581, 'catId': 2, 'goodsName': 'Azazie Lorenza BG', 'colorId': 12173, 'sizeId': 6767},
      {'goodsId': 1006564, 'catId': 2, 'goodsName': 'Azazie Cindy BG', 'colorId': 11620, 'sizeId': 9568},
      {'goodsId': 1035612, 'catId': 2, 'goodsName': 'Azazie Fawn BG', 'colorId': 11620, 'sizeId': 6769},
      {'goodsId': 1003075, 'catId': 2, 'goodsName': 'Azazie Xena BG', 'colorId': 11620, 'sizeId': 9567},
      {'goodsId': 1035602, 'catId': 2, 'goodsName': 'Azazie Rhodes BG', 'colorId': 11630, 'sizeId': 6771},
      {'goodsId': 1006552, 'catId': 2, 'goodsName': 'Azazie Josephine BG', 'colorId': 11630, 'sizeId': 9564},
      {'goodsId': 1006623, 'catId': 2, 'goodsName': 'Azazie Devi BG', 'colorId': 11629, 'sizeId': 9561},
      {'goodsId': 1004153, 'catId': 2, 'goodsName': 'Azazie Saffron BG', 'colorId': 11620, 'sizeId': 9561},
      {'goodsId': 1051737, 'catId': 2, 'goodsName': 'Azazie Fahren BG', 'colorId': 11620, 'sizeId': 9568},
      {'goodsId': 1003089, 'catId': 2, 'goodsName': 'Azazie Melrose BG', 'colorId': 11630, 'sizeId': 6771},
      {'goodsId': 1051829, 'catId': 2, 'goodsName': 'Azazie Leonie BG', 'colorId': 11630, 'sizeId': 9566},
      {'goodsId': 1035621, 'catId': 2, 'goodsName': 'Azazie Alemia BG', 'colorId': 11629, 'sizeId': 6770},
      {'goodsId': 1051775, 'catId': 2, 'goodsName': 'Azazie Gala BG', 'colorId': 11630, 'sizeId': 9564},
      {'goodsId': 1051760, 'catId': 2, 'goodsName': 'Azazie Starlow BG', 'colorId': 11620, 'sizeId': 9565},
      {'goodsId': 1003003, 'catId': 2, 'goodsName': 'Azazie Lafayette BG', 'colorId': 11620, 'sizeId': 9562},
      {'goodsId': 1001512, 'catId': 2, 'goodsName': 'Azazie Judith BG', 'colorId': 11630, 'sizeId': 9566},
      {'goodsId': 1006625, 'catId': 2, 'goodsName': 'Azazie Sorella BG', 'colorId': 11620, 'sizeId': 6771},
      {'goodsId': 1051769, 'catId': 2, 'goodsName': 'Azazie Vivienne BG', 'colorId': 11630, 'sizeId': 6765},
      {'goodsId': 1051771, 'catId': 2, 'goodsName': 'Azazie Mistie BG', 'colorId': 11620, 'sizeId': 9562},
      {'goodsId': 1051850, 'catId': 2, 'goodsName': 'Azazie Calliana BG', 'colorId': 11620, 'sizeId': 9562},
      {'goodsId': 1006628, 'catId': 2, 'goodsName': 'Azazie Trixie BG', 'colorId': 11620, 'sizeId': 6769},
      {'goodsId': 1051772, 'catId': 2, 'goodsName': 'Azazie Empiria BG', 'colorId': 11630, 'sizeId': 9565},
      {'goodsId': 1051833, 'catId': 2, 'goodsName': 'Azazie Diora BG', 'colorId': 307026, 'sizeId': 6767},
      {'goodsId': 1003085, 'catId': 2, 'goodsName': 'Azazie Rowe BG', 'colorId': 11629, 'sizeId': 6767},
      {'goodsId': 1035566, 'catId': 2, 'goodsName': 'Azazie Devonna BG', 'colorId': 11630, 'sizeId': 9567},
      {'goodsId': 1006553, 'catId': 2, 'goodsName': 'Azazie Bella BG', 'colorId': 11629, 'sizeId': 9566},
      {'goodsId': 1035574, 'catId': 2, 'goodsName': 'Azazie July BG', 'colorId': 11629, 'sizeId': 6769},
      {'goodsId': 1035586, 'catId': 2, 'goodsName': 'Azazie Bellisima BG', 'colorId': 11629, 'sizeId': 6772},
      {'goodsId': 1003032, 'catId': 2, 'goodsName': 'Azazie Roux BG', 'colorId': 11620, 'sizeId': 6770},
      {'goodsId': 1051819, 'catId': 2, 'goodsName': 'Azazie James BG', 'colorId': 11629, 'sizeId': 9564},
      {'goodsId': 1001992, 'catId': 2, 'goodsName': 'Azazie Saskia BG', 'colorId': 11630, 'sizeId': 6770},
      {'goodsId': 1001024, 'catId': 2, 'goodsName': 'Azazie Nicola BG', 'colorId': 9478, 'sizeId': 6771},
      {'goodsId': 1006559, 'catId': 2, 'goodsName': 'Azazie Florine BG', 'colorId': 11621, 'sizeId': 9565},
      {'goodsId': 1035606, 'catId': 2, 'goodsName': 'Azazie Irelynn BG', 'colorId': 11630, 'sizeId': 6770},
      {'goodsId': 1051751, 'catId': 2, 'goodsName': 'Azazie Rosalia BG', 'colorId': 11620, 'sizeId': 6769},
      {'goodsId': 1035605, 'catId': 2, 'goodsName': 'Azazie Daira BG', 'colorId': 11620, 'sizeId': 6771},
      {'goodsId': 1051848, 'catId': 2, 'goodsName': 'Azazie Nyx BG', 'colorId': 11629, 'sizeId': 6768},
      {'goodsId': 1000990, 'catId': 2, 'goodsName': 'Azazie Dolores BG', 'colorId': 3, 'sizeId': 6770},
      {'goodsId': 1002001, 'catId': 2, 'goodsName': 'Azazie Bess BG', 'colorId': 11630, 'sizeId': 6770},
      {'goodsId': 1006541, 'catId': 2, 'goodsName': 'Azazie Poppy BG', 'colorId': 11630, 'sizeId': 6765},
      {'goodsId': 1051764, 'catId': 2, 'goodsName': 'Azazie Konstantin BG', 'colorId': 11620, 'sizeId': 6766},
      {'goodsId': 1006551, 'catId': 2, 'goodsName': 'Azazie Mira BG', 'colorId': 11630, 'sizeId': 6768},
      {'goodsId': 1051765, 'catId': 2, 'goodsName': 'Azazie Camari BG', 'colorId': 11630, 'sizeId': 9563},
      {'goodsId': 1051836, 'catId': 2, 'goodsName': 'Azazie Florian BG', 'colorId': 11630, 'sizeId': 6765},
      {'goodsId': 1051841, 'catId': 2, 'goodsName': 'Azazie Cerelia BG', 'colorId': 11620, 'sizeId': 6766},
      {'goodsId': 1006587, 'catId': 2, 'goodsName': 'Azazie Elias BG', 'colorId': 11620, 'sizeId': 9564},
      {'goodsId': 1051845, 'catId': 2, 'goodsName': 'Azazie Amaryllis BG', 'colorId': 11629, 'sizeId': 9564},
      {'goodsId': 1051762, 'catId': 2, 'goodsName': 'Azazie Maylie BG', 'colorId': 11620, 'sizeId': 6766},
      {'goodsId': 1002067, 'catId': 2, 'goodsName': 'Azazie Stevie BG', 'colorId': 12110, 'sizeId': 9564},
      {'goodsId': 1051846, 'catId': 2, 'goodsName': 'Azazie Aurelie BG', 'colorId': 11620, 'sizeId': 9563},
      {'goodsId': 1003048, 'catId': 2, 'goodsName': 'Azazie Ramona BG', 'colorId': 11621, 'sizeId': 6767},
      {'goodsId': 1002050, 'catId': 2, 'goodsName': 'Azazie Marlin BG', 'colorId': 11621, 'sizeId': 6766},
      {'goodsId': 1002069, 'catId': 2, 'goodsName': 'Azazie Indie BG', 'colorId': 11621, 'sizeId': 6766},
      {'goodsId': 1003072, 'catId': 2, 'goodsName': 'Azazie Sydney BG', 'colorId': 11629, 'sizeId': 9567},
      {'goodsId': 1001525, 'catId': 2, 'goodsName': 'Azazie Angelique BG', 'colorId': 11620, 'sizeId': 6768}]

for i in range(10):
    list1 = ['test' + str(i) for i in range(10)]
    print(list1)
    headers = ['goodsId', 'catId', 'goodsName', 'colorId', 'sizeId', 'stock_num']
    with open(product_goods_path + '\/data.csv', mode='w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writerows(aa)

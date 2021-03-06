from graph import Graph

wegmans=Graph.Graph()
wegmans.add_values("01A", "02A", "03A", "04A", "05A", "06A", "07A", "08A", "09A", "10A", "Card Shop", "Card Shop",
                   "13A", "Bulk Foods", "Bulk Foods", "16A", "17A", "18A", "19A", "20A", "21A", "22A", "23A", "24A")
wegmans.add_values("Cor01A", "Cor02A", "Cor03A", "Cor04A", "Cor05A", "Cor06A", "Cor07A", "Cor08A", "Cor09A", "Cor10A",
                   "Cor11A", "Cor12A", "Cor13A", "Cor14A", "Cor15A", "Cor16A", "Cor17A", "Cor18A", "Cor19A", "Cor20A",
                   "Cor21A", "Cor22A", "Cor23A", "Cor24A")
wegmans.add_values("01B", "02B", "03B", "04B", "05B", "06B", "07B", "08B", "09B", "10B", "11B", "12B", "13B", "14B",
                   "15B", "16B", "17B", "18B", "19B", "20B", "21B", "22B", "23B", "24B")
wegmans.add_values("Cor01B", "Cor02B", "Cor03B", "Cor04B", "Cor05B", "Cor06B", "Cor07B", "Cor08B", "Cor09B", "Cor10B",
                   "Cor11B", "Cor12B", "Cor13B", "Cor14B", "Cor15B", "Cor16B", "Cor17B", "Cor18B", "Cor19B", "Cor20B",
                   "Cor21B", "Cor22B", "Cor23B", "Cor24B")
wegmans.add_values("01C", "02C", "03C", "04C", "05C", "06C", "07C", "08C", "09C", "10C", "11C", "12C", "13C", "14C",
                   "15C", "16C", "17C", "18C", "19C", "20C")
wegmans.add_values("Cor01C", "Cor02C", "Cor03C", "Cor04C", "Cor05C", "Cor06C", "Cor07C", "Cor08C", "Cor09C", "Cor10C",
                   "Cor11C", "Cor12C", "Cor13C", "Cor14C", "Cor15C", "Cor16C", "Cor17C", "Cor18C", "Cor19C", "Cor20C")
wegmans.add_values("Beer Shop", "Frozen", "Diary", "Meat Case", "Produce", "Fresh Bakery", "Deli", "Prepared Food",
                   "Pharmacy", "Floral", "Checkout")


wegmans.connect_undirected("Frozen", "Cor24A", "Cor23A", "Cor22A", "Cor21A", "Cor20A", "Cor19A", "Cor18A", "Cor17A",
                           "Cor16A", "Cor15A")
wegmans.connect_undirected("Cor24A", "Cor23A", "24A", "Frozen")
wegmans.connect_undirected("Cor23A", "Cor24A", "Cor22A", "23A", "Frozen")
wegmans.connect_undirected("Cor22A", "Cor23A", "Cor21A", "22A", "Frozen")
wegmans.connect_undirected("Cor21A", "Cor22A", "Cor20A", "21A", "Frozen")
wegmans.connect_undirected("Cor20A", "Cor21A", "Cor19A", "20A", "Frozen")
wegmans.connect_undirected("Cor19A", "Cor20A", "Cor18A", "19A", "Frozen")
wegmans.connect_undirected("Cor18A", "Cor19A", "Cor17A", "18A", "Frozen")
wegmans.connect_undirected("Cor17A", "Cor18A", "Cor16A", "17A", "Frozen")
wegmans.connect_undirected("Cor16A", "Cor17A", "Cor15A", "16A", "Frozen")
wegmans.connect_undirected("Cor15A", "Cor16A", "Cor14A", "Bulk Foods", "Frozen")
wegmans.connect_undirected("Cor14A", "Cor15A", "Cor13A", "Bulk Foods")
wegmans.connect_undirected("Cor13A", "Cor14A", "Cor12A", "13A", "Checkout")
wegmans.connect_undirected("Cor12A", "Cor13A", "Cor11A", "Card Shop", "Checkout")
wegmans.connect_undirected("Cor11A", "Cor12A", "Cor10A", "Card Shop", "Checkout")
wegmans.connect_undirected("Cor10A", "Cor11A", "Cor09A", "10A", "Checkout")
wegmans.connect_undirected("Cor09A", "Cor10A", "Cor08A", "09A", "Checkout")
wegmans.connect_undirected("Cor08A", "Cor09A", "Cor07A", "08A", "Checkout")
wegmans.connect_undirected("Cor07A", "Cor08A", "Cor06A", "07A", "Checkout")
wegmans.connect_undirected("Cor06A", "Cor07A", "Cor05A", "06A", "Checkout")
wegmans.connect_undirected("Cor05A", "Cor06A", "Cor04A", "05A", "Checkout")
wegmans.connect_undirected("Cor04A", "Cor05A", "Cor03A", "04A", "Checkout")
wegmans.connect_undirected("Cor03A", "Cor04A", "Cor02A", "03A", "Checkout", "Floral")
wegmans.connect_undirected("Cor02A", "Cor03A", "Cor01A", "02A", "Floral")
wegmans.connect_undirected("Cor01A", "Cor02A", "Pharmacy", "01A", "Floral")
wegmans.connect_undirected("Pharmacy", "Floral", "Prepared Food", "Cor01A", "01A")
wegmans.connect_undirected("Prepared Food", "Floral", "Pharmacy", "Deli", "Fresh Bakery")
wegmans.connect_undirected("Checkout", "Cor13A", "Cor12A", "Cor11A", "Cor10A", "Cor09A", "Cor08A", "Cor07A", "Cor06A",
                           "Cor05A", "Cor04A", "Cor03A", "Floral")
wegmans.connect_undirected("Floral", "Checkout", "Cor03A", "Cor02A", "Cor01A", "Pharmacy", "Prepared Food")



wegmans.connect_undirected("24A", "Cor24A", "Cor24B")
wegmans.connect_undirected("23A", "Cor23A", "Cor23B")
wegmans.connect_undirected("22A", "Cor22A", "Cor22B")
wegmans.connect_undirected("21A", "Cor21A", "Cor21B")
wegmans.connect_undirected("20A", "Cor20A", "Cor20B")
wegmans.connect_undirected("19A", "Cor19A", "Cor19B")
wegmans.connect_undirected("18A", "Cor18A", "Cor18B")
wegmans.connect_undirected("17A", "Cor17A", "Cor17B")
wegmans.connect_undirected("16A", "Cor16A", "Cor16B")
wegmans.connect_undirected("Bulk Foods", "Cor15A", "Cor15B")
wegmans.connect_undirected("Bulk Foods", "Cor14A", "Cor14B")
wegmans.connect_undirected("13A", "Cor13A", "Cor13B")
wegmans.connect_undirected("Card Shop", "Cor12A", "Cor12B")
wegmans.connect_undirected("Card Shop", "Cor11A", "Cor11B")
wegmans.connect_undirected("10A", "Cor10A", "Cor10B")
wegmans.connect_undirected("09A", "Cor09A", "Cor09B")
wegmans.connect_undirected("08A", "Cor08A", "Cor08B")
wegmans.connect_undirected("07A", "Cor07A", "Cor07B")
wegmans.connect_undirected("06A", "Cor06A", "Cor06B")
wegmans.connect_undirected("05A", "Cor05A", "Cor05B")
wegmans.connect_undirected("04A", "Cor04A", "Cor04B")
wegmans.connect_undirected("03A", "Cor03A", "Cor03B")
wegmans.connect_undirected("02A", "Cor02A", "Cor02B")
wegmans.connect_undirected("01A", "Cor01A", "Cor01B", "Pharmacy")



wegmans.connect_undirected("Cor24B", "Cor23B", "24A", "Beer Shop")
wegmans.connect_undirected("Cor23B", "Cor24B", "Cor22B", "23A", "Beer Shop")
wegmans.connect_undirected("Cor22B", "Cor23B", "Cor21B", "22A", "Beer Shop")
wegmans.connect_undirected("Cor21B", "Cor22B", "Cor20B", "21A", "Beer Shop")
wegmans.connect_undirected("Cor20B", "Cor21B", "Cor19B", "20B", "20A")
wegmans.connect_undirected("Cor19B", "Cor20B", "Cor18B", "19B", "19A")
wegmans.connect_undirected("Cor18B", "Cor19B", "Cor17B", "18B", "18A")
wegmans.connect_undirected("Cor17B", "Cor18B", "Cor16B", "17B", "17A")
wegmans.connect_undirected("Cor16B", "Cor17B", "Cor15B", "16B", "16A")
wegmans.connect_undirected("Cor15B", "Cor16B", "Cor14B", "15B", "Bulk Foods")
wegmans.connect_undirected("Cor14B", "Cor15B", "Cor13B", "14B", "Bulk Foods")
wegmans.connect_undirected("Cor13B", "Cor14B", "Cor12B", "13B", "13A")
wegmans.connect_undirected("Cor12B", "Cor13B", "Cor11B", "12B", "Card Shop")
wegmans.connect_undirected("Cor11B", "Cor12B", "Cor10B", "11B", "Card Shop")
wegmans.connect_undirected("Cor10B", "Cor11B", "Cor09B", "10B", "10A")
wegmans.connect_undirected("Cor09B", "Cor10B", "Cor08B", "09B", "09A")
wegmans.connect_undirected("Cor08B", "Cor09B", "Cor07B", "08B", "08A")
wegmans.connect_undirected("Cor07B", "Cor08B", "Cor06B", "07B", "07A")
wegmans.connect_undirected("Cor06B", "Cor07B", "Cor05B", "06B", "06A")
wegmans.connect_undirected("Cor05B", "Cor06B", "Cor04B", "05B", "05A")
wegmans.connect_undirected("Cor04B", "Cor05B", "Cor03B", "04B", "04A")
wegmans.connect_undirected("Cor03B", "Cor04B", "Cor02B", "03B", "03A")
wegmans.connect_undirected("Cor02B", "Cor03B", "Cor01B", "02B", "02A")
wegmans.connect_undirected("Cor01B", "Cor02B", "01A", "01B")
wegmans.connect_undirected("Beer Shop", "Cor24B", "Cor23B", "Cor22B", "Cor21B", "20B", "Diary")


wegmans.connect_undirected("Deli", "Fresh Bakery", "Prepared Food")
wegmans.connect_undirected("Fresh Bakery", "Produce", "Deli", "Prepared Food")

wegmans.connect_undirected("20B", "Cor20C", "Cor20B", "Beer Shop")
wegmans.connect_undirected("19B", "Cor19C", "Cor19B")
wegmans.connect_undirected("18B", "Cor18C", "Cor18B")
wegmans.connect_undirected("17B", "Cor17C", "Cor17B")
wegmans.connect_undirected("16B", "Cor16C", "Cor16B")
wegmans.connect_undirected("15B", "Cor15C", "Cor15B")
wegmans.connect_undirected("14B", "Cor14C", "Cor14B")
wegmans.connect_undirected("13B", "Cor13C", "Cor13B")
wegmans.connect_undirected("12B", "Cor12C", "Cor12B")
wegmans.connect_undirected("11B", "Cor11C", "Cor11B")
wegmans.connect_undirected("10B", "Cor10C", "Cor10B")
wegmans.connect_undirected("09B", "Cor09C", "Cor09B")
wegmans.connect_undirected("08B", "Cor08C", "Cor08B")
wegmans.connect_undirected("07B", "Cor07C", "Cor07B")
wegmans.connect_undirected("06B", "Cor06C", "Cor06B")
wegmans.connect_undirected("05B", "Cor05C", "Cor05B")
wegmans.connect_undirected("04B", "Cor04C", "Cor04B")
wegmans.connect_undirected("03B", "Cor03C", "Cor03B")
wegmans.connect_undirected("02B", "Cor02C", "Cor02B")
wegmans.connect_undirected("01B", "Cor01C", "Cor01B")


wegmans.connect_undirected("Diary", "Beer Shop", "Cor20C")


wegmans.connect_undirected("Cor20C", "Cor19C", "20B", "Diary")
wegmans.connect_undirected("Cor19C", "Cor20C", "Cor18C", "19B")
wegmans.connect_undirected("Cor18C", "Cor19C", "Cor17C", "18B")
wegmans.connect_undirected("Cor17C", "Cor18C", "Cor16C", "17B")
wegmans.connect_undirected("Cor16C", "Cor17C", "Cor15C", "16B")
wegmans.connect_undirected("Cor15C", "Cor16C", "Cor14C", "15B")
wegmans.connect_undirected("Cor14C", "Cor15C", "Cor13C", "14B")
wegmans.connect_undirected("Cor13C", "Cor14C", "Cor12C", "13B")
wegmans.connect_undirected("Cor12C", "Cor13C", "Cor11C", "12B")
wegmans.connect_undirected("Cor11C", "Cor12C", "Cor10C", "11B")
wegmans.connect_undirected("Cor10C", "Cor11C", "Cor09C", "10B")
wegmans.connect_undirected("Cor09C", "Cor10C", "Cor08C", "09B", "Meat Case")
wegmans.connect_undirected("Cor08C", "Cor09C", "Cor07C", "08B", "Meat Case")
wegmans.connect_undirected("Cor07C", "Cor08C", "Cor06C", "07B", "Meat Case")
wegmans.connect_undirected("Cor06C", "Cor07C", "Cor05C", "06B", "Meat Case")
wegmans.connect_undirected("Cor05C", "Cor06C", "Cor04C", "05B")
wegmans.connect_undirected("Cor04C", "Cor05C", "Cor03C", "04B")
wegmans.connect_undirected("Cor03C", "Cor04C", "Cor02C", "03B")
wegmans.connect_undirected("Cor02C", "Cor03C", "Cor01C", "02B")
wegmans.connect_undirected("Cor01C", "Cor02C", "Produce", "01B")


wegmans.connect_undirected("Meat Case", "Cor09C", "Cor08C", "Cor07C", "Cor06C")
wegmans.connect_undirected("Produce", "Fresh Bakery", "Cor01C")

test=wegmans.store_path("Floral", ["Diary", "Fresh Bakery", "21A", "09B", "13A", "Checkout"])
print(test)
test2=set()
test2.update(test)
print(test2)
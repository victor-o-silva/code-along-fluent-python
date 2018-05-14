invoice = """
|....|.................................|.........|........|........|
1909  Pimoroni PiBrella                    $17.50 3           $52.50
1489  6mm Tactile Switch x20                $4.95 2            $9.90
1510  Panavise Jr. - PV-201                $28.00 1           $28.00
""".strip()

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 50)
QUANTITY = slice(50, 59)
ITEM_TOTAL = slice(59, None)

first = invoice.split('n')[0]
print(first[SKU])
print(first[DESCRIPTION])
print(first[UNIT_PRICE])
print(first[QUANTITY])
print(first[ITEM_TOTAL])

line_items = invoice.split('\n')[1:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

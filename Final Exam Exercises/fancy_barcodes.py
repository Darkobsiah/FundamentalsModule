import re


def parse_barcode(bar: str) -> bool:
    """"
    This function check if a single barcode
    is valid or not
    """
    regex = r'@#+[A-Z][A-Za-z0-9]+[A-Z]@#+'
    result = re.fullmatch(regex, bar)
    if result:
        return True
    print('Invalid barcode')   # else
    return False


num = int(input())
barcodes = [input() for _ in range(num)]
for barcode in barcodes:
    match = parse_barcode(barcode)
    if match:
        print(barcode)
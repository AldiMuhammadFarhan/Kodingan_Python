# input
uang = input()
# ubah
idr = int(uang)
# perhitungan
usd = idr * 0.000070
cny = idr / 2208.69
# output
print("{:,.2f}".format(usd),'usd')
print("{:,.2f}".format(cny),'cny')
import psd_tools
from psd_tools import PSDImage

psd = PSDImage.open('Cop.psb')

image = psd.composite()
#print(type(image))
#image.save('cop.png')

print('done')

import psd_tools
from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer
from psd_tools.api.layers import Group

psd = PSDImage.open('image.psd')

## size = (width, height) tuple.
## bbox = (left, top, right, bottom) tuple.

def handle_layers():

    groups = []

    for i, layer in enumerate(psd):
        print(type(layer))
        print(f'{layer.name} = {layer.size} = {layer.bbox} : {get_center(layer)}')
        
        if type(layer) == Group: ## good
        #if layer.is_group: ## shit
            print(f'{layer.name} is Group! Index: {i}')
            groups.append(layer)
            #if layer.has_clip_layers():
            #print(len(layer.clip_layers))
            #for _, sub_layer in enumerate(layer):
            #    print(f'={sub_layer.name}')
        
        print('#'*10)
    
    print('Iterating groups')
    for g in groups:
        print(len(g))
        #for layer in g:
        #    print(layer.name)

    '''
    group = psd[-1]
    print(type(group))

    for l in group:
        print(l.name)
    '''
    
    '''
    red_layer = psd[2]
    green_layer = psd[3]

    red_layer.left = green_layer.left
    red_layer.top = green_layer.top
    #red_layer.offset = tuple(int(x) * 2 for x in red_layer.offset)
    #red_layer.left = red_layer.left * 2
    #red_layer.top = red_layer.top * 2
    psd.save('image_modified.psd')
    '''
    

def get_center(layer):
    size = layer.size
    box = layer.bbox
    x = box[0] + size[0] * 0.5
    y = box[1] + size[1] * 0.5
    return x, y

def set_center(layer):
    #x, y = get_center(layer)
    #box = layer.bbox
    #layer.left = x + box[0]
    #layer.top = y + box[1]
    pass

def main():
    handle_layers()

if __name__ == "__main__":
    main()
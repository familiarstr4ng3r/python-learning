import argparse
import math

# positional arguments
# python arg_parser.py 2 4

# optional agruments could be in any order:
# python arg_parser.py -R 2 -H 4
# python arg_parser.py --height 4 --radius 2

#python arg_parser.py -R 2 -H 4 -q
#python arg_parser.py -R 2 -H 4 -v
#python arg_parser.py -R 2 -H 4

def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    volume = round(volume, 2)
    return volume

def main():
    parser = argparse.ArgumentParser(description = 'Calculate volume of cylinder')
    
    # optional agruments
    parser.add_argument('-R', '--radius', type = int, metavar = '', required = True, help = 'Radius of cylinder')
    parser.add_argument('-H', '--height', type = int, metavar = '', required = True, help = 'Height of cylinder')

    # argument could be only one at time
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action = 'store_true', help = 'print quiet')
    group.add_argument('-v', '--verbose', action = 'store_true', help = 'print verbose')
    
    args = parser.parse_args()
    volume = cylinder_volume(args.radius, args.height)
    
    if args.quiet:
        print(volume)
    elif args.verbose:
        verbose_text = 'Volume of a Cylinder with radius %s and height %s is %s'
        print(verbose_text % (args.radius, args.height, volume))
    else:
        print(f'Volume is {volume}')

if __name__ == '__main__':
    main()

# https://assetstore.unity.com/packages/audio/sound-fx/ultimate-sound-fx-bundle-151756

def main1():
    price = 0

    with open("price.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()[-4:]
            value = float(line)
            price += value

    print(price)

def main():
    with open("price.txt") as f:
        lines = f.readlines()
        lines = [line.strip()[-4:] for line in lines]
        lines = [float(line) for line in lines]
        price = sum(lines)
        print(price)

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt

def flood_fill(pic, x : int, y : int):

    x_size = len(pic[0])
    y_size = len(pic)
    # Chytani pixelu mimo obraz
    if x < 0 or x >= x_size or y < 0 or y >= y_size:
        return pic

    pixel = pic[y][x]
    # Ignorovani jiz prebarvenych pixelu a pixelu pozadi
    if pixel == 0 or pixel == 2:
        return pic

    elif pixel == 1:
        pic[y][x] = 2

        pic = flood_fill(pic, x, y - 1) # Dolu
        pic = flood_fill(pic, x, y + 1) # Nahoru
        pic = flood_fill(pic, x - 1, y) # Levo
        pic = flood_fill(pic, x + 1, y) # Pravo

    return pic

def main():

    #img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    #img = plt.imread("files/img2.png")[:, :, 0]
    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(10)
    plt.clf()


if __name__ == "__main__":
    main()

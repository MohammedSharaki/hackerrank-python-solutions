if __name__ == '__main__':
    X = int (input())
    Y = int (input())
    Z = int (input())
    n = int (input())
    X += 1
    Y += 1
    Z += 1
    temp_list = [[x, y, z]for x in range(X) for y in range(Y) for z in range(Z) if z +x +y !=n]
    print(temp_list)
 
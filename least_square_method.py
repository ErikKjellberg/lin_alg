import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import random

def least_square(a,y):
    at_a = np.dot(np.transpose(a),a)
    v = np.dot(la.inv(at_a),np.dot(np.transpose(a),y))
    return v

def main():
    #polynomials
    while 1:
        print("Enter all x in a row, use space between them")
        try:
            xs = input("> ")
            x_list = np.array([int(x) for x in xs.split(" ")])
        except ValueError:
            print("Please enter real numbers with spaces between them, and make sure the amounts of x:s and y:s are the same.")
        break
    while 1:
        print("Enter all y in a row, use space between them")
        try:
            ys = input("> ")
            y_list = np.array([int(y) for y in ys.split(" ")])
        except ValueError:
            print("Please enter real numbers with spaces between them, and make sure the amounts of x:s and y:s are the same.")
        break
    while 1:
        try:
            degree = int(input("How many degrees do you want the polynomial to be in?"))+1
        except ValueError:
            print("Please enter an integer >:(")
        else:
            break

    a = np.array([[x**i for i in range(degree)] for x in x_list])
    v = least_square(a,y_list)

    plt.scatter(x_list, y_list, s=5, c="black")
    x2 = np.linspace(min(x_list),max(x_list),(max(x_list)-min(x_list))*10)
    print(max(x_list))
    plt.plot(x2, sum(v[i]*x2**i for i in range(len(v))))
    plt.show()

main()

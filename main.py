import sympy as sym
import numpy as np
import math as m
import matplotlib.pyplot as plt

x = sym.Symbol('x')

# # hasil = sym.integrate(fungsi, (x, batas_bawah, batas_atas))
# hasil = sym.integrate(x**2 * sym.cos(x**2), (x, 1.5, 2.5), method = 'riemannc')
# print(hasil)

# fungsi = x**2 * sym.cos(x**2)
# fungsi = sym.simplify(fungsi)


def kiri(f, b, i, d):
    f = sym.sympify(f)
    akum = 0
    batas = b
    for z in range(i):
        try:
        
            fx = float(f.subs(x, batas))

            batas += d

            luas = fx * d

            akum += luas

            if z == i-1:
                print(akum)

        except(ZeroDivisionError, ValueError):
            print("Terjadi kesalahan dalam perhitungan. Pastikan fungsi valid")

def kanan(f, a, i, d):
    f = sym.sympify(f)
    akum = 0
    batas = a
    for z in range(i):
        try:
        
            fx = float(f.subs(x, batas))

            batas -= d

            luas = fx * d

            akum += luas

            if z == i-1:
                print(akum)

        except(ZeroDivisionError, ValueError):
            print("Terjadi kesalahan dalam perhitungan. Pastikan fungsi valid")

def tengah(f, b, i, d):
    f = sym.sympify(f)
    cx = 0
    akum = 0
    b1 = b
    b2 = 0
    for z in range(i):
        try:
            b2 = b1 + d

            cx = (b1+b2)/2

            fx = float(f.subs(x, cx))

            luas = fx * d

            akum += luas

            print(f"b1 = {b1} dan b2 = {b2}")

            b1 = b2

            if z == i-1:
                print(akum)

        except(ZeroDivisionError, ValueError):
            print("Terjadi kesalahan dalam perhitungan. Pastikan fungsi valid")

def plot_riemann(f, a, b, n, method='left'):
    f = sym.sympify(f)
    x_vals = np.linspace(a, b, 1000)  # Points for plotting the function
    y_vals = [float(f.subs(x, x_val)) for x_val in x_vals]
    
    # Membuat plot
    plt.figure(figsize=(12, 6))
    
    # Plot fungsi asli
    plt.plot(x_vals, y_vals, 'b-', label='f(x)')
    
    # Menghitung titik-titik Riemann
    dx = (b - a) / n
    x_riemann = np.linspace(a, b, n+1)
    
    for i in range(n):
        if method == 'left':
            x_point = x_riemann[i]
        else:  # right
            x_point = x_riemann[i+1]
            
        y_point = float(f.subs(x, x_point))
        
        # Plot persegi panjang
        plt.fill([x_riemann[i], x_riemann[i], x_riemann[i+1], x_riemann[i+1]],
                [0, y_point, y_point, 0],
                alpha=0.3)  # alpha untuk transparansi
        
        # Plot titik evaluasi
        plt.plot(x_point, y_point, 'ro', markersize=4)

    plt.grid(True)
    plt.title(f'Riemann Sum ({method}) dengan n={n} subinterval')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def plot_riemann_center(f, a, b, n):
    f = sym.sympify(f)
    x_vals = np.linspace(a, b, 1000)  # Points for plotting the function
    y_vals = [float(f.subs(x, x_val)) for x_val in x_vals]
    
    # Membuat plot
    plt.figure(figsize=(12, 6))
    
    # Plot fungsi asli
    plt.plot(x_vals, y_vals, 'b-', label='f(x)')
    
    # Menghitung titik-titik Riemann
    dx = (b - a) / n
    x_riemann = np.linspace(a, b, n+1)
    
    for i in range(n):
        # Hitung titik tengah
        x_mid = (x_riemann[i] + x_riemann[i+1]) / 2
        y_mid = float(f.subs(x, x_mid))
        
        # Plot persegi panjang
        plt.fill([x_riemann[i], x_riemann[i], x_riemann[i+1], x_riemann[i+1]],
                [0, y_mid, y_mid, 0],
                'g', alpha=0.3)  # alpha untuk transparansi, warna hijau
        
        # Plot titik evaluasi di tengah
        plt.plot(x_mid, y_mid, 'ro', markersize=4)

    plt.grid(True)
    plt.title(f'Riemann Sum (Center) dengan n={n} subinterval')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def Main():
    print("Metode yang Tersedia: ")
    print("1. Riemann Left")
    print("2. Riemann Right")
    print("3. Riemann Center")
    print("4. Exit")

    user = input("Metode yang ingin digunakan: ")

    if user == '1':
        fungsi = input(f"Masukkan Fungsi: ")
        fungsi = sym.simplify(fungsi)
        batas_bawah = float(input(f"Masukkan batas bawah: "))
        batas_atas = float(input(f"Masukkan batas atas: "))
        iterasi = int(input(f"Masukkan batas iterasi: "))
        delta_x = (abs(batas_atas - batas_bawah))/iterasi

        kiri(fungsi, batas_bawah, iterasi, delta_x)

        plot_riemann(fungsi, batas_bawah, batas_atas, iterasi, 'left')

        Main()


    elif user == '2':
        fungsi = input(f"Masukkan Fungsi: ")
        fungsi = sym.simplify(fungsi)
        batas_bawah = float(input(f"Masukkan batas bawah: "))
        batas_atas = float(input(f"Masukkan batas atas: "))
        iterasi = int(input(f"Masukkan batas iterasi: "))
        delta_x = (abs(batas_atas - batas_bawah))/iterasi

        kanan(fungsi, batas_atas, iterasi, delta_x)

        plot_riemann(fungsi, batas_bawah, batas_atas, iterasi, 'right')

        Main()


    elif user == '3':
        fungsi = input(f"Masukkan Fungsi: ")
        fungsi = sym.simplify(fungsi)
        batas_bawah = float(input(f"Masukkan batas bawah: "))
        batas_atas = float(input(f"Masukkan batas atas: "))
        iterasi = int(input(f"Masukkan batas iterasi: "))
        delta_x = (abs(batas_atas - batas_bawah))/iterasi

        tengah(fungsi, batas_bawah, iterasi, delta_x)

        plot_riemann_center(fungsi, batas_bawah, batas_atas, iterasi)

        Main()

    elif user == '4':
        exit()
        return None
    
    else:
        print("Input Error")
        Main()

Main()
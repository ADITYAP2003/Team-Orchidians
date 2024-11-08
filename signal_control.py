a, b, c, d = 1, 0, 0, 0
r11, r21, r31, r41 = 0, 0, 0, 0
g11, g21, g31, g41 = 0, 0, 0, 0
y11, y21, y31, y41 = 0, 0, 0, 0

if a == 1:
    sig1 = True
    r11 = 0
    g11 = 1
    y11 = 0

    sig2 = True
    r21 = 1
    g21 = 0
    y21 = 0

    sig3 = True
    r31 = 1
    g31 = 0
    y31 = 0

    sig4 = True
    r41 = 1
    g41 = 0
    y41 = 0

elif b == 1:
    sig1 = True
    r11 = 1
    g11 = 0
    y11 = 0

    sig2 = True
    r21 = 0
    g21 = 1
    y21 = 0

    sig3 = True
    r31 = 1
    g31 = 0
    y31 = 0

    sig4 = True
    r41 = 1
    g41 = 0
    y41 = 0

elif c == 1:
    sig1 = True
    r11 = 1
    g11 = 0
    y11 = 0

    sig2 = True
    r21 = 1
    g21 = 0
    y21 = 0

    sig3 = True
    r31 = 0
    g31 = 1
    y31 = 0

    sig4 = True
    r41 = 1
    g41 = 0
    y41 = 0

elif d == 1:
    sig1 = True
    r11 = 1
    g11 = 0
    y11 = 0

    sig2 = True
    r21 = 1
    g21 = 0
    y21 = 0

    sig3 = True
    r31 = 1
    g31 = 0
    y31 = 0

    sig4 = True
    r41 = 0
    g41 = 1
    y41 = 0

print("sig1:", sig1)
print("sig2:", sig2)
print("sig3:", sig3)
print("sig4:", sig4)

print("r11:", r11)
print("g11:", g11)
print("y11:", y11)

print("r21:", r21)
print("g21:", g21)
print("y21:", y21)

print("r31:", r31)
print("g31:", g31)
print("y31:", y31)

print("r41:", r41)
print("g41:", g41)
print("y41:", y41)

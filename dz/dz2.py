# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат

print("x y z w")
for w in range(2):
    for y in range(2):
        for z in range(2):
            for x in range(2):
                if ((w and z) or (y !=0) or (x !=0) and (w !=0)):
                    print(x, y, z, w)

import torch

b = torch.tensor(32)
w1 = torch.tensor(1.8)

x1 = int(input("Enter the Celcius in Degress:"))
y_pred = 1*b + x1*w1
print("Celcius to Faranheit is :", y_pred)



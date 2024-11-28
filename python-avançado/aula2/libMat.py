import matplotlib.pyplot as plt


"""
meses = ['Jan', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTI =[60, 52, 76, 89, 105, 95]
qtdRH =[40, 35, 17, 28, 35, 65]

# plt.plot(meses, qtdTI, label="TI", color="blue", linestyle="-.", marker=".")
# plt.plot(meses, qtdRH, label="RH", color="red", linestyle="--", marker="o")
plt.bar(meses, qtdTI, label="TI", color="blue", linestyle="-.")
plt.bar(meses, qtdRH, label="RH", color="red", linestyle="--")
plt.title("Chamados abertos")
plt.xlabel("Meses")
plt.ylabel("Quantidade")
plt.legend()
"""





navegadores = ["Chrome", "Firefox", "Edge"]
qtde = [1200, 600, 200]
cores = ["red", "green", "blue"]


plt.pie(qtde, labels=navegadores, colors=cores)

plt.show()

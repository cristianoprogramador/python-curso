import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Define o nível de log para ERROR ou superior
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Desativa as operações customizadas do oneDNN

import tensorflow as tf  # Importar o TensorFlow após definir as variáveis de ambiente


class Produto:
  def __init__(self, nome, preco, categoria):
    self.nome = nome
    self.preco = preco
    self.categoria = categoria

produtos = [
    Produto("Camiseta", 29.99, "Roupas"),
    Produto("Calça Jeans", 79.99, "Roupas"),
    Produto("Tenis", 99.99, "Calçados"),
    Produto("SmartPhone", 1429.99, "Eletronico"),
    Produto("Notebook", 3000.99, "Eletronico"),
    Produto("Livro - Como Viver", 15.99, "Livros"),
]

nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])

media = tf.reduce_mean(precos)
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, "Eletronico"))

print(media)
print(eletronicos)

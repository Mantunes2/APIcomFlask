from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Olá bem-vindo a API</h1>'

@app.route('/vendas')
def vendas():
  tabela = pd.read_excel('Vendas.xlsx')
  valor = tabela['Valor Final'] * tabela['Quantidade']
  values = valor.sum()
  total_prds = tabela['Quantidade'].sum()
  valor_json = {
    'Total de produtos vendidos': int(total_prds),
    'Total de Vendas': int(values)
  }
  return jsonify(valor_json)

@app.route('/produtos')
def produtos():
  tabela = pd.read_excel('Vendas.xlsx')
  total_pr = tabela.groupby('Produto').sum()
  produto = total_pr.index.to_list()
  produto_json = {'Produtos': produto}
  return jsonify(produto_json)

@app.route('/lojas')
def lojas():
  tabela = pd.read_excel('Vendas.xlsx')
  tabela = tabela.apply(lambda x: x.replace("Center Shopping Uberlândia", "Center Shopping Uberlandia"))
  soma = tabela.groupby('ID Loja').sum()
  loja = soma.index.to_list()
  loja_json = {'Lojas': loja}
  return jsonify(loja_json)

if __name__ == '__main__':
  app.run(debug=True)

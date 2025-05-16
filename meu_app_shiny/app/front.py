from shiny import App, ui, render #importação do shiny
from datetime import datetime #para lidar com as datas
import pandas as pd #analisar e manipular os dados no formato tabular
import matplotlib.pyplot as plt #só conseguimos criar e personalizar gráficos com esse import


app_ui = ui.page_fluid( #o primeiro é o nome técnico, o segundo o nome que aparece para o usuário 

    ui.input_date("data", "Data que foi realizada a transação"), #selecionar a data de transação
    ui.input_text("produto", "Descrição da transação"), #descrever gastos/receita
    ui.input_numeric("valor", "Valor R$", value=0, step=0.01), #Para inserir o valor (positivo para receita, negativo para gasto).
    ui.input_select(
        "categoria",
        "Categoria", 
        ["Alimentação", "Transporte", "Lazer","Estudo", "Salário", "Renda Extra"]),
    ui.input_action_button("salvar", "Registrar"), #botão de salvar, depois decidir no shiny qual o melhor botão ui


# ui.row(
#     ui.column(6, ui.output_plot("grafico_categoria")),
#     ui.column(6, ui.output_plot("grafico"))

) #)
app = App(app_ui, None)  # None indica que não há server
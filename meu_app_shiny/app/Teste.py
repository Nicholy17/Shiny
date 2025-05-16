from shiny import App, ui, render
import pandas as pd
import matplotlib.pyplot as plt

from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("Olá, Shiny!"),
    ui.input_slider("n", "Número de pontos:", 1, 100, 50),
    ui.output_plot("grafico")
)

def server(input, output, session):
    @output
    @render.plot
    def grafico():
        
        plt.scatter(range(input.n()), range(input.n()), color="purple")
        return plt.gcf()

app = App(app_ui, server)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.button import Button
import pandas as pd
import servicos

class Formulario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FileChooserListView(
            on_selection=self.file_selected
        ))
        botao_processar = Button(text="Processar arquivo")
        botao_processar.bind(on_press=self.processar_arquivo)
        self.add_widget(botao_processar)

    def file_selected(self, filechooser, selection):
        self.arquivo = selection[0]

    def processar_arquivo(self, instance):
        try:
            dataframe = pd.read_csv(self.arquivo)
            resultado = servicos.processar_arquivo(dataframe)
            popup = Popup(title='Resultado', content=Button(text=resultado), size_hint=(0.5, 0.5))
            popup.open()
        except Exception as e:
            popup = Popup(title='Erro', content=Button(text=str(e)), size_hint=(0.5, 0.5))
            popup.open()

class Aplicativo(App):
    def build(self):
        return Formulario()

if __name__ == '__main__':
    Aplicativo().run()
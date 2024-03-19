from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image


class BarberShopApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical')

        # Imagem de fundo
        background = Image(source='IMAGEM-BLOG-DPG-14.jpg', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        # Título
        title = Label(text='Bem-vindo ao Agendamento de Barbearias', size_hint=(1, None), height=50)
        layout.add_widget(title)

        # Botão para explorar as barbearias
        explore_button = Button(text='Explorar Barbearias', size_hint=(1, None), height=50)
        layout.add_widget(explore_button)

        # Botão para ver agendamentos
        appointments_button = Button(text='Meus Agendamentos', size_hint=(1, None), height=50)
        layout.add_widget(appointments_button)

        # Botão para sair do aplicativo
        exit_button = Button(text='Sair', size_hint=(1, None), height=50)
        layout.add_widget(exit_button)

        return layout


if __name__ == '__main__':
    BarberShopApp().run()

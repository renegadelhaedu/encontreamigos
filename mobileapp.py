#pip install kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
from kivy.core.window import Window
import json
from kivy.utils import get_color_from_hex
from kivy.uix.scrollview import ScrollView

class MainApp(App):

    def send_request(self, *args):
        url = 'http://127.0.0.1:5000/listarpessoas/externo'
        headers = {'Content-Type': 'application/json'}
        body = {'usuário': 'rene', 'senha':'123'}
        UrlRequest(url, req_headers=headers, req_body=json.dumps(body), method='POST',
                   on_success=self.on_success, on_error=self.on_error)

    def on_success(self, request, response):
        print(response)
        self.list_layout.clear_widgets()
        self.list_layout.add_widget(Label(text=f""))
        for item in response:

            self.list_layout.add_widget(
                Label(text=f"Nome: {item['nome']}", font_size=20, color=get_color_from_hex('#FFFFFF')))
            self.list_layout.add_widget(
                Label(text=f"E-mail: {item['email']}", font_size=20, color=get_color_from_hex('#FFFFFF')))
            self.list_layout.add_widget(Label(text=f""))


    def on_error(self, req, error):
        self.list_layout.clear_widgets()
        self.list_layout.add_widget(Label(text="ERRO"))

    def build(self):
        Window.size = (400, 600)

        main_layout = BoxLayout(orientation='vertical', padding=20)
        scrollview = ScrollView()

        request_button = Button(text="Enviar", size_hint=(0.3, 0.1), size=(50, 50),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        request_button.bind(on_press=self.send_request)

        self.list_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=30)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))

        scrollview.add_widget(self.list_layout)

        main_layout.add_widget(request_button)
        main_layout.add_widget(scrollview)

        return main_layout

if __name__ == '__main__':
    MainApp().run()

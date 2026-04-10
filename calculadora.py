# arquivo: calculator.py

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4  # 4 colunas como na imagem
        self.spacing = [5, 5]
        self.padding = [10, 10, 10, 10]

        # Display
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=40
        )
        self.add_widget(self.display)
        # Espaço para cobrir 4 colunas
        self.add_widget(Button(disabled=True, background_color=(0,0,0,0)))
        self.add_widget(Button(disabled=True, background_color=(0,0,0,0)))
        self.add_widget(Button(disabled=True, background_color=(0,0,0,0)))

        # Lista de botões
        buttons = [
            "C", "%", "⌫", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ",", "=", ""
        ]

        for b in buttons:
            if b == "":
                self.add_widget(Button(disabled=True, background_color=(0,0,0,0)))
            else:
                btn = Button(text=b, font_size=32)
                btn.bind(on_press=self.on_button_press)
                self.add_widget(btn)

        self.last_operator = None
        self.first_number = None

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "⌫":
            self.display.text = self.display.text[:-1]
        elif text in ("+", "-", "×", "÷", "%"):
            if self.display.text:
                self.first_number = self.display.text
                self.last_operator = text
                self.display.text = ""
        elif text == "=":
            if self.first_number and self.last_operator:
                second_number = self.display.text
                try:
                    expr = f"{self.first_number}{self.last_operator}{second_number}"
                    # Substituir símbolos para Python
                    expr = expr.replace("×", "*").replace("÷", "/").replace("%", "/100*")
                    result = str(eval(expr))
                except:
                    result = "Erro"
                self.display.text = result
                self.first_number = None
                self.last_operator = None
        else:
            # número ou vírgula
            self.display.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
    
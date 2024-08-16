import reflex as r  

class MyApp(r.App):  
    def build(self):  
        return r.Column(  
            [  
                r.Text("¡Hola, Reflex!"),  
                r.Input(placeholder="Escribe algo..."),  
                r.Button("Enviar", on_click=self.handle_click),  
            ]  
        )  

    def handle_click(self, _):  
        r.alert("¡Botón presionado!")  

if __name__ == "__main__":  
    r.run(MyApp)
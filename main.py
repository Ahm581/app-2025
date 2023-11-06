from kivymd.app import MDApp
class MainApp(MDApp):
    def build(self):
        self.title = "Principles of Agriculture"
        self.theme_cls.primary_palette = 'Green'

MainApp().run()
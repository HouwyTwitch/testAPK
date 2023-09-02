from kivy import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'minimum_width', '350')
Config.set('graphics', 'minimum_height', '600')

from kivymd.app import MDApp
from kivy.lang import Builder

colors = {
    "Teal": {
        "200": "#080808",
        "500": "#080808",
        "700": "#080808",
    },
    "Red": {
        "200": "#080808",
        "500": "#080808",
        "700": "#080808",
    },
    "Light": {
        "StatusBar": "#E0E0E0",
        "AppBar": "#FFFFFF",
        "Background": "#F8F8F8",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
}

class Blender(MDApp):

    def build(self):
        self.title = 'Blender - multiplatform SDA'
        self.theme_cls.colors = colors
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_string(
            '''
#:import toast kivymd.toast.toast
BoxLayout:
    orientation:'vertical'

    MDBottomNavigation:
        selected_color_background: '#90ee02'

        MDBottomNavigationItem:
            name: 'GuardScreen'
            icon: 'key-outline'
            text: 'Guard'
            MDLabel:
                id: "guard_code"
                text: "STEAM"
                font_size: dp(60)
                font_name: "./res/Garnett Semibold Regular.ttf"
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": 0.9}
                padding: "4dp", "4dp"
                allow_copy: True
            MDProgressBar:
                pos_hint: {"center_x": .5, "center_y": 0.82}
                size_hint: (0.8, None)
                value: 50
                color: 1, 1, 1, 1
                radius: [self.height/2]
                height: dp(12)
                canvas:
                    Color:
                        rgba: 224/255, 224/255, 224/255, 1 
                    RoundedRectangle:
                        pos: self.x, self.center_y - self.height/2
                        size: self.width, self.height
                        radius: [self.height/2]
                    Color:
                        rgba: 8/255, 8/255, 8/255, 1                       
                    RoundedRectangle:
                        pos: self.x, self.center_y - self.height/2
                        size: self.width * (self.value / float(self.max)) if self.max else 0, self.height
                        radius: [self.height/2]

        MDBottomNavigationItem:
            name: 'ConfirmationsScreen'
            icon: 'list-status'
            text: 'Confimations'

            MDLabel:
                text: 'Here will be list of confirmations'
                font_name: "./res/Garnett Semibold Regular.ttf"
                halign: 'center'
        
        MDBottomNavigationItem:
            name: 'AccountManagmentScreen'
            icon: 'account-outline'
            text: 'Accounts'

            MDLabel:
                text: 'Here will be list of accounts'
                font_name: "./res/Garnett Semibold Regular.ttf"
                halign: 'center'

        MDBottomNavigationItem:
            name: 'SettingsScreen'
            icon: 'cog-outline'
            text: 'Settings'

            MDLabel:
                text: 'Here will be settings'
                font_name: "./res/Garnett Semibold Regular.ttf"
                halign: 'center'

<Toast>:
    size_hint: (0.2, 0.04)
    pos_hint: {"center_x": .5, "center_y": 0.2}
'''
        )

Blender().run()

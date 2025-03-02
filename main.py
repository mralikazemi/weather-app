from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
    MDListItemLeadingAvatar,
)
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import AsyncImage
import arabic_reshaper
from bidi.algorithm import get_display
import webbrowser
import requests
import time
from datetime import datetime
from kivy.metrics import dp




class DrawerLabel(MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()

class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()
    trailing_text_color = ColorProperty()

    _trailing_text_obj = None

    def on_trailing_text(self, instance, value):
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)

    def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value


class MYAPLICATION(MDApp):
    style = ""
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.style = Builder.load_file("main.kv")
        
        return self.style
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
    def on_start(self):
        text = "اسم شهر را وارد کنید"
        arabic_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(arabic_text)
        self.style.hint_button.text = bidi_text
        text = "داشبورد"
        arabic_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(arabic_text)
        self.style.dasboard.text = bidi_text

    def open_link(self, url):
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Error opening link: {e}")
    def show_alert_dialog(self):
        self.dialog=MDDialog(
            MDDialogIcon(
                icon="window-close",
            ),
            MDDialogHeadlineText(
                text="Are you Sure?",
            ),
            
            MDDialogSupportingText(
                text="You Will Close The Application With This Action.",
            ),
            MDDialogContentContainer(
                MDDivider(),
                MDDivider(),
                orientation="vertical",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    style="text",
                    on_release=self.close,
                ),
                MDButton(
                    MDButtonText(text="Close"),
                    style="text",
                    on_release=self.Stop,
                ),
                spacing="8dp",
            ),
        )
        self.dialog.open()
    def contact_us(self):
        MDDialog(
            MDDialogHeadlineText(
                text="Contact us in SocialMedia.",
                halign="center",
            ),
            MDDialogSupportingText(
                text="You Can Report Problems & Issues!",
            ),
            MDDialogContentContainer(
                MDListItem(
                    MDListItemLeadingAvatar(
                        source="asset/logo/tel.png",
                    ),
                    MDListItemSupportingText(
                        text="@Mr_Ali_Kazemi",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                    on_release=self.on_tel_click,
                ),
                MDListItem(
                    MDListItemLeadingAvatar(
                        source="asset/logo/insta.png",
                    ),
                    MDListItemSupportingText(
                        text="@Mr_Ali_Kazemi",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                    on_release=self.on_insta_click,
                ),
                MDListItem(
                    MDListItemLeadingAvatar(
                        source="asset/logo/gmail.png",
                    ),
                    MDListItemSupportingText(
                        text="KhodeAnonymous@gmail.com",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                    on_release=self.on_gmail_click,
                ),
                orientation="vertical",
            ),
        ).open()

    def on_tel_click(self, instance):
        print("Telegram clicked!")
        self.open_link("https://telegram.me/Mr_Ali_Kazemi")

    def on_insta_click(self, instance):
        print("Instagram clicked!")
        self.open_link("https://instagram.com/Mr_Ali_Kazemi")
    def on_gmail_click(self, instance):
        print("Gmail clicked!")
    def close(self,object):
        self.dialog.dismiss()
    def Stop(self,object):
        self.stop()
    def result(self,show: bool= None,error: int= 0):
        city = self.root.ids.weather_hint
        city_country = self.root.ids.city_country
        weather = self.root.ids.weather
        image_pic = self.root.ids.image_pic
        temp_f = self.root.ids.temp_f
        temp_c = self.root.ids.temp_c
        speed = self.root.ids.speed
        humidity = self.root.ids.humidity
        scroll_view = self.root.ids.scroll_view
        error_code_1 = self.root.ids.error_code_1
        error_code_2 = self.root.ids.error_code_2
        error_code_3 = self.root.ids.error_code_3
        pishbini = self.root.ids.pishbini
        if show:
            if error_code_1.opacity ==1:
                error_code_1.opacity = 0
            if error_code_2.opacity ==1:
                error_code_2.opacity = 0
            if error_code_3.opacity ==1:
                error_code_3.opacity = 0
            
            if city.opacity == 0:
                city.opacity = 1
                city_country.opacity= 1
                weather.opacity= 1
                image_pic.opacity= 1
                temp_f.opacity= 1
                temp_c.opacity=1
                humidity.opacity= 1
                speed.opacity= 1
                scroll_view.opacity= 1
                pishbini.opacity= 1

        else:
            if city.opacity == 1:
                city.opacity = 0
                city_country.opacity = 0
                weather.opacity= 0
                image_pic.opacity= 0
                temp_f.opacity= 0
                temp_c.opacity= 0
                humidity.opacity= 0
                speed.opacity= 0
                scroll_view.opacity= 0
                pishbini.opacity= 0
            if error==1:
                if error_code_1.opacity ==0:
                    error_code_1.opacity = 1
                if error_code_2.opacity ==1:
                    error_code_2.opacity = 0
                if error_code_3.opacity ==1:
                    error_code_3.opacity = 0

                text = arabic_reshaper.reshape("هنوز چیزی وارد نکردی که\nلطفا اول اسم شهر یا منطقه رو وارد کن\nبعد سرچ کن")
                text = get_display(text)
                self.style.error_code_1.text = text
            if error==2:
                if error_code_1.opacity ==1:
                    error_code_1.opacity = 0
                if error_code_2.opacity ==0:
                    error_code_2.opacity = 1
                if error_code_3.opacity ==1:
                    error_code_3.opacity = 0
                text = arabic_reshaper.reshape("داداش ناموسن این شهر وجود نداره")
                text = get_display(text)
                self.style.error_code_2.text = text
            if error==3:
                if error_code_1.opacity ==1:
                    error_code_1.opacity = 0
                if error_code_2.opacity ==1:
                    error_code_2.opacity = 0
                if error_code_3.opacity ==0:
                    error_code_3.opacity = 1
                text = arabic_reshaper.reshape("متاسفانه نتت وصل نیست\nاول نتتو اوکی کن بعدا تلاش کن")
                text = get_display(text)
                self.style.error_code_3.text = text                    

    def search(self):
        city_name = self.style.city_name.text
        try:
            if len(city_name)!=0:
                key = "5e16bdf676b7079f37c0928cbf65fd48"
                response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
                response = response.json()
                weather = response["weather"][0]["main"]
                description = response["weather"][0]["description"]
                icon = response["weather"][0]["icon"]
                temp = response["main"]["temp"]
                humidity = response["main"]["humidity"]
                wind = response["wind"]["speed"]
                country = response["sys"]["country"]
                name = response["name"]
                cod = response["cod"]
                if cod == 200:
                    self.result(show=True)
                    self.style.weather_hint.text = description
                    self.style.city_country.text = str(f"{city_name}, {country}")
                    self.style.weather.text = weather
                    self.style.image_pic.source = f"asset/icon/{icon}@2x.png"
                    self.style.temp_f.text = f"{round(temp)}°F"
                    self.style.temp_c.text = f"{int(temp)-273}°C"
                    self.style.humidity.text = f"Humidity : {humidity}"
                    self.style.speed.text = f"Speed : {wind}"
                    self.style.pishbini.text = get_display(arabic_reshaper.reshape("پیش بینی هوا در روزهای آتی:"))
                    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id={response["id"]}&appid={key}")
                    response = response.json()
                    times = response["list"]
                    forecast_container = self.root.ids.forecast_container
                    forecast_container.clear_widgets()
                    for item in times:
                        day = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
                        feels_like = item["main"]["feels_like"]
                        temp_max = item["main"]["temp_max"]
                        weather = item["weather"][0]["main"]
                        card = MDCard(
                                        size_hint=(None, None),
                                        size=("130dp", "160dp"),
                                        radius=[15],
                                        padding="8dp",
                                        elevation=3,
                                    )
                        layout = MDBoxLayout(orientation="vertical", spacing="5dp", padding="5dp")
                        icon = AsyncImage(
                            source=f"asset/icon/{item["weather"][0]["icon"]}@2x.png",
                            size_hint=(None, None),
                            size=("60dp", "60dp"),
                            pos_hint={"center_x": 0.5},
                        )
                        day_label = MDLabel(
                                                text=f"{item["dt_txt"].split(' ')[0].split('2025-')[1]} {item["dt_txt"].split(' ')[1].split(':')[0]} {day.strftime("%a")} ",  # نام کامل روز
                                                theme_text_color="Primary",
                                                font_size="14sp",
                                                bold=True,
                                                halign="center",
                                                valign="center",
                                                size_hint_y=None,
                                                height=dp(20)
                                            )
                        temp_label = MDLabel(
                                                text=f'feel: {int(round(feels_like))-273}°C\nMax: {int(round(temp_max)-273)}°C',
                                                theme_text_color="Secondary",
                                                font_size="13sp",
                                                halign="center",
                                                valign="center",
                                                size_hint_y=None,
                                                height=dp(40),
                                            )
                        desc_label = MDLabel(
                                                text=f"{weather}",
                                                theme_text_color="Hint",
                                                font_size="12sp",
                                                halign="center",
                                                valign="center",
                                                size_hint_y=None,
                                                height=dp(10)
                                            )

                        layout.add_widget(icon)
                        layout.add_widget(day_label)
                        layout.add_widget(temp_label)
                        layout.add_widget(desc_label)
                        card.add_widget(layout)
                        forecast_container.add_widget(card)
                    
            else:
                self.result(show=False,error=1)
        except Exception as e:
            if "HTTPSConnectionPool"in str(e):
                self.result(show=False,error=3)
            else:
                self.result(show=False,error=2)

if __name__ == "__main__":
    MYAPLICATION().run()

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from pytube import YouTube


class demoapp(MDApp):
    def build(self):
        screen = Screen()
        d_but = MDFillRoundFlatButton(text='Downlaod', pos_hint ={'center_x':0.5, 'center_y':0.7}, on_release=self.download_video)
        screen.add_widget(d_but)
        self.link = MDTextField(pos_hint ={'center_x':0.5, 'center_y':0.8}, hint_text='Insert your video url', size_hint_x=None, width=300)
        screen.add_widget(self.link)
        self.title_lable = MDLabel(text='YouTube Video Downloader', width=10, pos_hint ={'center_x':0.888, 'center_y':0.96})
        screen.add_widget(self.title_lable)
        self.info_lable = MDLabel(text='', width=10, pos_hint ={'center_x':0.93, 'center_y':0.6})
        screen.add_widget(self.info_lable)
        self.pro = MDProgressBar(orientation='vertical')
        screen.add_widget(self.pro)
        return screen
    
    def download_video(self, obj):
        try:
             link_ = self.link._get_text()
             object = YouTube(url=link_)
             video = object.streams.get_highest_resolution()
             video.download(output_path="Downloads")
             self.info_lable.text = 'Download Finished...'
        except:
            self.info_lable.text = 'Download Faild'
if __name__ == '__main__':
    demoapp().run()
          
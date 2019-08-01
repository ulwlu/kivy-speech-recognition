


# -*- coding:utf-8 -*-



#SpeechRecognition Library
import speech_recognition
#speech_recognition.Recognizer().energy_threshold = 4000
speech_recognition.Recognizer().dynamic_energy_threshold = True
speech_recognition.Recognizer().pause_threshold = 0.8
from googleapiclient import discovery
import re
from pykakasi import kakasi
kakasi = kakasi()
kakasi.setMode("H", "a")
kakasi.setMode("K", "a")
kakasi.setMode("J", "a")

#Kivy Library
from kivy.app import App
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, 
    "NotoSansJP-Regular.otf")



class FuncLabel(BoxLayout):
  hnum = NumericProperty(0)
  tnum = NumericProperty(0)
  unum = NumericProperty(0)
  total = NumericProperty(0)
  boxtext = StringProperty("音声認識開始")
  boxcol  = StringProperty("3196E6")



  # Input Voice
  def speech_input(self):

    # Record Audio
    with speech_recognition.Microphone() as source:
      audio = speech_recognition.Recognizer().listen(source)
     
    # OutPut
    try:
      input_voice = speech_recognition.Recognizer().recognize_google(audio, language="ja-JP")
      print("\n\t===== デバッグ 入力音声="+input_voice)
      self.conv_text(input_voice)
    except speech_recognition.UnknownValueError:
      pass
    except speech_recognition.RequestError as e:
      pass



  # Custom Input Voice
  def conv_text(self, input_voice):

    #Japanese Convert into Alphabet
    alphabet_voice = kakasi.getConverter().do(input_voice)
    print("\t===== デバッグ アルファベット="+alphabet_voice)

    #Kunyomi Convert into Number
    trans_num = {
        "reiko":"0", "zeroko":"0", 
        "hitotsu":"1", "ikko":"1", "itsuko":"1", 
        "futatsu":"2", "niko":"2", "nico":"2",
        "mitsu":"3", "sanko":"3", 
        "yotsu":"4", "shiko":"4", "yonko":"4", 
        "itsutsu":"5", "goko":"5", 
        "mutsu":"6", "rokko":"6", "rokuko":"6", "rotsuko":"6",
        "nanatsu":"7", "nanako":"7", 
        "yatsu":"8", "hakko":"8", "hachiko":"8", "hatsuko":"8",
        "kokonotsu":"9", "kyuuko":"9",
        "juu":"10", "jukko":"10", "jutsuko":"10"
    }
    for kunyomi in trans_num.keys():
      if re.search(kunyomi, alphabet_voice):
        alphabet_voice = re.sub(kunyomi, trans_num[kunyomi], alphabet_voice)
    print("\t===== デバッグ 訓読み変換="+alphabet_voice+"\n")
  
    # Regular Expression Search
    self.hnum = 0
    self.tnum = 0
    self.unum = 0
    self.total = 0
    # All
    htu = re.search(r"""
        (zenbu|sankotomo|3tomo|
        hana[^0-9]*teitou[^0-9]*usagi|
        hana[^0-9]*usagi[^0-9]*teitou|
        teitou[^0-9]*hana[^0-9]*usagi|
        teitou[^0-9]*usagi[^0-9]*hana|
        usagi[^0-9]*hana[^0-9]*teitou|
        usagi[^0-9]*teitou[^0-9]*hana|
    )[^0-9]*(\d+)""", alphabet_voice)
    if htu:
      self.hnum = int(htu.group(2))
      self.tnum = int(htu.group(2))
      self.unum = int(htu.group(2))

    else:
      # two combination
      ht = re.search(r"(hana[^0-9]*teitou|teitou[^0-9]*hana)[^0-9]*(\d+)", alphabet_voice)
      tu = re.search(r"(teitou[^0-9]*usagi|usagi[^0-9]*teitou)[^0-9]*(\d+)", alphabet_voice)
      uh = re.search(r"(usagi[^0-9]*hana|hana[^0-9]*usagi)[^0-9]*(\d+)", alphabet_voice)

      if ht:
        self.hnum = int(ht.group(2))
        self.tnum = int(ht.group(2))
        u = re.search(r"(usagi)[^0-9]*(\d)", alphabet_voice)
        if u:
          self.unum = int(u.group(2))

      elif tu:
        self.tnum = int(tu.group(2))
        self.unum = int(tu.group(2))
        h = re.search(r"(hana)[^0-9]*(\d)", alphabet_voice)
        if h:
          self.hnum = int(h.group(2))

      elif uh:
        self.hnum = int(uh.group(2))
        self.unum = int(uh.group(2))
        t = re.search(r"(teitou)[^0-9]*(\d)", alphabet_voice)
        if t:
          self.tnum = int(t.group(2))

      else:
        h = re.search(r"(hana)[^0-9]*(\d)", alphabet_voice)
        if h:
          self.hnum = int(h.group(2))

        t = re.search(r"(teitou)[^0-9]*(\d)", alphabet_voice)
        if t:
          self.tnum = int(t.group(2))

        u = re.search(r"(usagi)[^0-9]*(\d)", alphabet_voice)
        if u:
          self.unum = int(u.group(2))

    self.total = (self.hnum+self.tnum+self.unum)*200


  
class Pres(App):

  def build(self):
    self.title = "xxx自動生成"
    Window.bind(on_key_down = self.handle_key)
    return super(Pres, self).build()



  def handle_key(self, window, code, code2, char, modifier):
    sm = self.root.ids.sm
    if code == 8:
      sm.transition.direction = 'left'
      sm.current = sm.previous()
    if code == 13:
      if (sm.current == 'ご注文受付開始(2/4ステップ目)'):
        self.root.boxtext = "音声認識実行中"
        self.root.boxcol = 'DC4A39'
        self.root.speech_input()
      sm.transition.direction = 'right'
      sm.current = sm.next()



if __name__ == '__main__':
  Pres().run()
  print("{0}{1}{2}".format(Pres.hnum, Pres.tnum, Pres.unum))

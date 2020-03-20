<h3 align="center">kivy-speech-recognition</h3>
<p align="center">ᓚᘏᗢ Python GUI App to reply speech.</p>


## Notes

**This repository is very old and made rough. Not maintained anymore.**

**このリポジトリはかなり前に、雑に制作されたものです。あらかじめご了承ください。**


## Content
Kivy + Google Speech to Textを使ったGUIのクロスプラットフォーム音声認識アプリ。

作ったのは2014年頃。私が人生で初めてプログラムに触れた作品です。屋台を営んでいる友人の希望を実現するため、個人受託で開発しました。

「提灯、花、ウサギは〜個」という注文形式に対応した音声認識です。

## Installation
1: Pythonをインストール( 参考:　https://www.sejuku.net/blog/33294 )

2: コマンドプロンプトかターミナルで pip install pipenv を実行

3: portaudioをインストール
        windowsなら
            http://www.portaudio.com/ からインストール
        macなら
            brew install portaudio
            brew link portaudio
			
4: sdlをインストール
        windowsなら
            http://www.libsdl.org からインストール
        macなら
            brew install sdl

5: main.pyがあるフォルダで pipenv install　を実行

6: python main.py で音声認識を実行します。
        ３秒以内に声をかけてください。

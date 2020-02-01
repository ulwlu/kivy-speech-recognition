# CONTENT
Kivyを使ったGUIの音声認識アプリ。
作ったのは2014年頃。初めてプログラムに触れたものです。
GoogleCloudPlatformを用いた音声認識アプリです。
「提灯、花、ウサギは〜個」という注文形式に対応した音声認識です。

# HowTo
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

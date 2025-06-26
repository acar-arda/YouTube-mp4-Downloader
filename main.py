import FreeSimpleGUI as sg
import threading
from functions import download_video

sg.theme('Black')

label1 = sg.Text("URL Giriniz:")
url = sg.Input(key='url')

label2 = sg.Text("Hedef Yol Seçiniz:")
directory = sg.Input(readonly=True, key='directory'), sg.FolderBrowse()

button = sg.Button("İndir")
result = sg.Text(key='result')

progress_bar = sg.ProgressBar(100, orientation='h', size=(30, 20), key='progressbar')

producer = sg.Text("Made by Arda Acar")

left_column = sg.Column([[label1], [label2]])
right_column = sg.Column([[url], [directory[0], directory[1]]])

layout = [[left_column, right_column], [button, progress_bar], [result, sg.Push(), producer]]

window = sg.Window("YouTube mp4 Downloader", layout=layout, font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=100)
    match event:
        case 'İndir':
            window['progressbar'].update_bar(0)
            if not values['directory'] or not values['url']:
                window['result'].update("Lütfen URL ve hedef klasör alanını boş bırakmayın!")
                continue
            threading.Thread(target=download_video, args=(values['url'], values['directory'], window), daemon=True).start()
        case '-PROGRESS-':
            window['progressbar'].update_bar(values['-PROGRESS-'])
        case '-RESULT-':
            window['result'].update(values['-RESULT-'])
        case sg.WIN_CLOSED:
            break

window.close()
# Librerie richieste: imageio, imageio-ffmpeg

import os
import imageio

videoSrc = os.path.abspath("Video.mp4")                      # Assegnerà ala variabile 'videoSrc' il percorso completo del file 'Video.mp4'.

def Vid2Gif(PathSrc, Formato):                               # La funzione prenderà come parametri 'VideoSrc' e il formato di conversione Es: (videoSrc, '.gif')
    outputSrc = os.path.splitext(PathSrc)[0] + Formato       # Verrò tolto '.mp4' a 'Video' e verrà aggiunta al nome del file l'estensione finale: Video.gif
    print(f"Converto: {PathSrc} in {outputSrc}")             # Lo script avviserà l'utente che inizierà la conversione

    try:                                                     # Ciclo Try per gestire le eccezioni
        lettura = imageio.get_reader(PathSrc)                   # 'lettura' si occuperà di ottenere il contenuto del file tramite la funzione get_reader(pathsrc)
        fps = lettura.get_meta_data()['fps']                    # Otterà gli FPS del file input per usarli nel file output
        convert = imageio.get_writer(outputSrc, fps=fps)        # 'convert' sfrutterà la funzione get_writer(videoSrc, fps) per eseguire la conversione.

        for frames in lettura:                                  # Loop che si occuperà di prendere tutti i frame del video
            convert.append_data(frames)                         # e di convertirli nel formato finale, .gif in questo caso.
            print(f"Frame: {frames}")                           # Stamperà a schermo i frame totali elaborati.

        print("Conversione completata!")                        # Avviserà che l'operazione è stata completata
        convert.close()                                         # Verrà chiusa quindi la conversione.
    except Exception as errore:                               # Nel caso in cui qualcosa andasse storto:
        print(errore)                                         # stamperà a schermo l'errore.


Vid2Gif(videoSrc, '.gif')                                      # Chiamata alla funzione, passando come argomenti il video e il formato da convertire.
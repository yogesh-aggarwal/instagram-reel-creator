# import interface
import editor


def main():
    media = editor.prepare_media(
        "Content/video.mp4",
        "Content/audio.mp3",
        "Content/content.txt",
    )
    reel = editor.create_reel(media)
    editor.export_reel(reel, "Output/Reel.mp4")
    # interface.start_gui()


main()

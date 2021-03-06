import os
import readtime
import moviepy.editor as mp

MIN_TEXT_TIME = 3


class Media:
    video: mp.VideoClip = None
    audio: mp.AudioClip = None
    content: tuple[str] = None


def export_reel(clip: mp.VideoClip, output_file_name: str = "reel.mp4"):
    clip.write_videofile(output_file_name)


def create_reel(
    media: Media,
    extend_clip_to_text: bool = False,
    font_size: int = 70,
    font_name: str = "Obrazec-Bold",
    color: str = "white",
    stroke_color: str = "black",
) -> None:
    if media.audio:
        media.video.audio = media.audio
    media.video.resize((1080, 1920))
    media.video = media.video.fx(mp.vfx.colorx, 0.8)

    content_len = len(media.content)

    clips = []
    last_time_point = 0
    for index, text in enumerate(media.content):
        duration = max(readtime.of_text(text, 120).seconds, MIN_TEXT_TIME)
        print(duration)
        text_duration = duration
        subclip_timing = (last_time_point, last_time_point + duration)

        if extend_clip_to_text and (index == content_len - 1):
            subclip_timing = (last_time_point, media.video.duration)
            text_duration = media.video.duration - last_time_point

        last_time_point += duration
        subclip = media.video.subclip(*subclip_timing)
        content_clip = mp.TextClip(
            text,
            color=color,
            fontsize=font_size,
            font=font_name,
            stroke_color=stroke_color,
            stroke_width=1.3,
        )
        content_clip = content_clip.set_position(
            ("center", "center"
             )).set_duration(text_duration).crossfadein(1).crossfadeout(1)

        clip = mp.CompositeVideoClip([subclip, content_clip])
        clips.append(clip)

    final_clip = mp.concatenate_videoclips(clips)
    return final_clip


def prepare_media(
    video_file_name: str,
    audio_file_name: str,
    content_file_name: str,
) -> Media:
    media = Media()
    do_include_audio = not os.path.exists(audio_file_name)
    media.video = mp.VideoFileClip(video_file_name,
                                   target_resolution=(1920, 1080),
                                   audio=do_include_audio)
    if not do_include_audio:
        media.audio = mp.AudioFileClip(audio_file_name)
    with open(content_file_name) as f:
        media.content = tuple(map(lambda x: x.replace("\n", ""),
                                  f.readlines()))
    return media

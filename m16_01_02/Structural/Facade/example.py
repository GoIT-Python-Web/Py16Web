class VideoFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print(f"Decoding video file: {self.filename}")


class AudioFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print(f"Decoding audio file: {self.filename}")


class SubtitleFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print(f"Adding subtitle file: {self.filename}")


class VideoPlayer:
    def __init__(self, video: VideoFile, audio: AudioFile, subtitle: SubtitleFile):
        self.video = video
        self.audio = audio
        self.subtitle = subtitle

    def play(self):
        self.video.decode()
        self.audio.decode()
        self.subtitle.decode()


if __name__ == '__main__':
    player = VideoPlayer(
        VideoFile("movie.mp4"),
        AudioFile("sound.wav"),
        SubtitleFile("text.srt")
    )

    player.play()


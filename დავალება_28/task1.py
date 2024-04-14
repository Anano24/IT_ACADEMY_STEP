# დავალება 1.

# შექმენით მედია ფლეიერის აპლიკაცია. განსაზღვრეთ ინტერფეისები დაკვრის, პაუზის, გაჩერების, გადახვევის და სწრაფი წინსვლის
# ფუნქციებისთვის. განახორციელეთ კლასები აუდიო პლეერისთვის, ვიდეო პლეერისთვის და სტრიმინგის პლეერისთვის. დარწმუნდით,
# რომ თითოეული მოთამაშე ახორციელებს მხოლოდ მის ფუნქციონალურ ინტერფეისებს. მაქსიმალურად გამოიყენეთ SOLID პრინციპები!!!


from abc import ABC, abstractmethod


# Define an abstract base class for media player interfaces
class MediaPlayerInterface(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Define an abstract base class for recorded media player interfaces
class RecordedMediaPlayerInterface(MediaPlayerInterface):
    @abstractmethod
    def rewind(self):
        pass

    @abstractmethod
    def fast_forward(self):
        pass


# Define a concrete class for playing audio files
class AudioPlayer(RecordedMediaPlayerInterface):
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def play(self):
        print(f"Start playing {self.audio_file}")

    def pause(self):
        print(f"{self.audio_file} paused")
    
    def stop(self):
        print(f"{self.audio_file} stopped")
    
    def rewind(self, seconds):
        if seconds < 0:
            raise ValueError("Second must be a positive number!")
        print(f"{self.audio_file} rewind by {seconds} seconds")

    def fast_forward(self, seconds):
        if seconds < 0:
            raise ValueError("Second must be a positive number!")
        print(f"{self.audio_file} fast forwarded by {seconds} seconds")

       
# Define a concrete class for playing video files
class VideoPlayer(RecordedMediaPlayerInterface):
    def __init__(self, video_file):
        self.video_file = video_file

    def play(self):
        print(f"Start playing {self.video_file}")

    def pause(self):
        print(f"{self.video_file} paused")
    
    def stop(self):
        print(f"{self.video_file} stopped")
    
    def rewind(self, seconds):
        if seconds < 0:
            raise ValueError("Second must be a positive number!")
        print(f"{self.video_file} rewind by {seconds} seconds")

    def fast_forward(self, seconds):
        if seconds < 0:
            raise ValueError("Second must be a positive number!")
        print(f"{self.video_file} fast forwarded by {seconds} seconds")


# Define a concrete class for live streaming media playback
class LiveStreamingPlayer(MediaPlayerInterface):
    def __init__(self, streaming_file):
        self.streaming_file = streaming_file

    def play(self):
        print(f"Start streaming {self.streaming_file}")

    def pause(self):
        print(f"{self.streaming_file} paused")
    
    def stop(self):
        print(f"{self.streaming_file} stopped")



# Instantiate an audio player and demonstrate its usage
audio = AudioPlayer("Audio file")
audio.play()
audio.fast_forward(15)
print()

# Instantiate a video player and demonstrate its usage
video = VideoPlayer("video file")
video.play()
video.pause()
video.rewind(20)
print()

# Instantiate a live streaming player and demonstrate its usage
stream = LiveStreamingPlayer("Stream file")
stream.play()
stream.stop()


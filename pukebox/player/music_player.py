from queue import Queue
from enum import Enum
import vlc

from pukebox.player.track import Track

class PlayState(Enum):
    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"

class MusicPlayer:
    def __init__(self) -> None:
        self.playing: PlayState = PlayState.STOPPED
        self.queue: Queue[Track] = Queue()
        self.__instance = vlc.Instance()
        self.__player = self.__instance.media_player_new()

    def play(self, track: Track) -> None:
        media = self.__instance.media_new(str(track.full_path))
        self.__player.set_media(media)
        self.__player.play()
        self.playing = PlayState.PLAYING

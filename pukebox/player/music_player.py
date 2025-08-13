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
        self.__player = vlc.Instance().media_player_new()

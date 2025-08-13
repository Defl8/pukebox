from queue import Queue

class MusicPlayer:
    def __init__(self) -> None:
        self.playing: bool = False
        self.queue: Queue[str] = Queue()

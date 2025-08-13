from tinytag import TinyTag
from pukebox.player.music_player import MusicPlayer
from pukebox.player.track import Track


def main() -> None:
    player = MusicPlayer()
    print(f"Initial play state: {player.playing}")
    tag = TinyTag.get("/home/wjames/music/fuckboy.mp3")
    player.play(Track(
        id=0,
        title=tag.title,
        artist=tag.artist,
        album=tag.album,
        duration=tag.duration,
        full_path="/home/wjames/music/fuckboy.mp3",
    ))

if __name__ == "__main__":
    main()

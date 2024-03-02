from typing import List
from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            searched_album = next(filter(lambda a:a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if searched_album.published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(searched_album)
        return f"Album {album_name} has been removed."

    def details(self):
        albums = "\n".join(a.details() for a in self.albums)

        return f"Band {self.name}\n" \
               f"{albums}\n"



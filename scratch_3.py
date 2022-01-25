import json
import xml.etree.ElementTree as et


class Song: #
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    """
    Used to serialize classes
    """
    def serialize(self, song, format):
        # if format == 'JSON':
        #     song_info = {
        #         'id': song.song_id,
        #         'title': song.title,
        #         'artist': song.artist
        #     }
        #     return json.dumps(song_info)
        if format == 'JSON': # first improvement
            return self._serialize_to_json(song)
        # elif format == 'XML':
        #     song_info = et.Element('song', attrib={'id': song.song_id})
        #     title = et.SubElement(song_info, 'title')
        #     title.text = song.title
        #     artist = et.SubElement(song_info, 'artist')
        #     artist.text = song.artist
        #     return et.tostring(song_info, encoding='unicode')
        elif format == 'XML': # first improvement
            return self._serialize_to_xml(song)
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')

    def _get_serializer(self, format): # second improvement
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)


class SongSerializer1:
    # code that depends on an interface to complete its task
    # client component
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    # interface, creator component
    # returns the string representation of
    # the class
    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    # concrete implementations of the product
    # interface defined is referred to as the product component
    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    # concrete implementations of the product
    # interface defined is referred to as the product component
    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


# implementation
song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()

print(serializer.serialize(song, 'JSON'))
class Room:
    def __init__(self, name, fee, capacity):
        self.name = name
        self.fee = fee
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def song_count(self):
        return len(self.songs)    

    def checkin_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return "no entry"

    def checkout_guest(self, guest):
        self.guests.remove(guest)

    def guest_count(self):
        return len(self.guests)

    
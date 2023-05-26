import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1", 100, 1)
        self.room_2 = Room("Room 2", 50, 2)
        self.song_1 = Song("close to you", "carpenters")
        self.song_2 = Song("goldfinger", "shirley bassey")
        self.guest_1 = Guest("Alan Partridge", 100)
        self.guest_2 = Guest("Lynn Benfield", 9500)

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room_1.name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.money)

    def test_room_has_fee(self):
        self.assertEqual(100, self.room_1.fee)

    def test_room_has_capacity(self):
        self.assertEqual(1, self.room_1.capacity)

    def test_can_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, self.room_1.song_count())

    def test_can_remove_song(self):
        self.room_2.add_song(self.song_2)
        self.room_2.remove_song(self.song_2)
        self.assertEqual(0, self.room_2.song_count())

    def test_can_checkin_guest(self):
        self.room_1.checkin_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())

    def test_can_checkout_guest(self):
        self.room_2.checkin_guest(self.guest_2)
        self.room_2.checkout_guest(self.guest_2)
        self.assertEqual(0, self.room_2.guest_count())

    def test_full_service_MVP(self):
        self.room_1.checkin_guest(self.guest_1)
        self.room_1.add_song(self.song_1)
        self.room_1.remove_song(self.song_1)
        self.room_1.checkout_guest(self.guest_1)

    def test_sufficient_funds__true_if_enough(self):
          self.assertEqual(True, self.guest_1.sufficient_funds(self.room_1))

    # def test_full_service_EXT_enough_funds_and_enough_capacity(self):
    #     self.room_1.checkin_guest(self.guest_1)
    #     self.room_1.add_song(self.song_1)
    #     self.room_1.remove_song(self.song_1)
    #     self.room_1.checkout_guest(self.guest_1)


    

    # def test_can_remove_song(self):
    #     self.room.remove_song(self.song_1)
    #     self.assertEqual(0, self.room.song_count())


    # def test_room_has_songs(self):
        # self.assertEqual(["close to you by carpenters"], self.room.songs)

    # def test_room_has_guests(self):
    #     self.assertEqual(["Alan Partridge"], self.room.guests)

    # def test_add_song(self):
    #     self.room.add_song(self.room)
    #     self.assertEqual((["close to you by carpenters"]), self.room.songs)


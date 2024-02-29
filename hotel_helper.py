package hotelbooking;

import java.util.ArrayList;
import java.util.List;

/**
 * The Hotel class represents a hotel with rooms and provides methods for adding rooms, booking rooms, and canceling bookings.
 */
public class Hotel {
    private List<Room> rooms;

    /**
     * Constructs a new Hotel object with an empty list of rooms.
     */
    public Hotel() {
        rooms = new ArrayList<>();
    }

    /**
     * Adds a room to the hotel.
     *
     * @param room The room to be added.
     */
    public void addRoom(Room room) {
        rooms.add(room);
    }

    /**
     * Books a room in the hotel.
     *
     * @param roomNumber The room number to be booked.
     * @return Returns true if the room is successfully booked, false otherwise.
     * @throws IllegalArgumentException if the room number is invalid.
     */
    public boolean bookRoom(int roomNumber) {
        // Find the room with the given room number
        Room room = findRoom(roomNumber);

        // If the room is found and is available, book the room
        if (room != null && room.isAvailable()) {
            room.book();
            return true;
        }

        return false;
    }

    /**
     * Cancels a booking for a room in the hotel.
     *
     * @param roomNumber The room number to be canceled.
     * @return Returns true if the booking is successfully canceled, false otherwise.
     * @throws IllegalArgumentException if the room number is invalid.
     */
    public boolean cancelBooking(int roomNumber) {
        // Find the room with the given room number
        Room room = findRoom(roomNumber);

        // If the room is found and is booked, cancel the booking
        if (room != null && !room.isAvailable()) {
            room.cancelBooking();
            return true;
        }

        return false;
    }

    /**
     * Finds a room in the hotel based on the room number.
     *
     * @param roomNumber The room number to search for.
     * @return Returns the Room object if found, null otherwise.
     * @throws IllegalArgumentException if the room number is invalid.
     */
    private Room findRoom(int roomNumber) {
        // Check if the room number is valid
        if (roomNumber <= 0) {
            throw new IllegalArgumentException("Invalid room number.");
        }

        // Search for the room with the given room number
        for (Room room : rooms) {
            if (room.getRoomNumber() == roomNumber) {
                return room;
            }
        }

        return null; // Room not found
    }
}

/**
 * The Room class represents a hotel room.
 */
class Room {
    private int roomNumber;
    private boolean available;

    /**
     * Constructs a new Room object with the given room number.
     *
     * @param roomNumber The room number.
     */
    public Room(int roomNumber) {
        this.roomNumber = roomNumber;
        this.available = true;
    }

    /**
     * Gets the room number.
     *
     * @return Returns the room number.
     */
    public int getRoomNumber() {
        return roomNumber;
    }

    /**
     * Checks if the room is available.
     *
     * @return Returns true if the room is available, false otherwise.
     */
    public boolean isAvailable() {
        return available;
    }

    /**
     * Books the room.
     *
     * @throws IllegalStateException if the room is already booked.
     */
    public void book() {
        if (!available) {
            throw new IllegalStateException("Room is already booked.");
        }
        available = false;
    }

    /**
     * Cancels the booking for the room.
     *
     * @throws IllegalStateException if the room is not booked.
     */
    public void cancelBooking() {
        if (available) {
            throw new IllegalStateException("Room is not booked.");
        }
        available = true;
    }
}

/**
 * The HotelBookingApp class demonstrates the usage of the Hotel class.
 */
public class HotelBookingApp {
    public static void main(String[] args) {
        // Create a new hotel
        Hotel hotel = new Hotel();

        // Add rooms to the hotel
        hotel.addRoom(new Room(101));
        hotel.addRoom(new Room(102));
        hotel.addRoom(new Room(103));

        // Book a room
        int roomNumber = 102;
        boolean isBooked = hotel.bookRoom(roomNumber);
        if (isBooked) {
            System.out.println("Room " + roomNumber + " is booked.");
        } else {
            System.out.println("Room " + roomNumber + " is not available.");
        }

        // Cancel a booking
        boolean isCanceled = hotel.cancelBooking(roomNumber);
        if (isCanceled) {
            System.out.println("Booking for room " + roomNumber + " is canceled.");
        } else {
            System.out.println("Room " + roomNumber + " is not booked.");
        }
    }
}

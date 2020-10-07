//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

public class Concert {
    private double ticketPrice;
    private int capacity;
    private int ticketsSold;
    private String location;
    private String date;


    public Concert(double ticketPrice, int capacity, String location, String date) {
        this.ticketPrice = ticketPrice;
        this.capacity = capacity;
        this.location = location;
        this.date = date;
        ticketsSold = 0;
    }

    public Concert(int capacity, String location, String date) {
        this(30, capacity, location, date);
    }

    public boolean isSoldOut() {
        return (capacity <= ticketsSold);
    }

    public void sellTicket() {
        if (!isSoldOut()) {
            ticketsSold++;
        }
    }

    public String toString() {
        return "A concert on " + date + " at " + location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public void setTicketPrice(double ticketPrice) {
        this.ticketPrice = ticketPrice;
    }

    public double getTicketPrice() {
        return ticketPrice;
    }

    public int getCapacity() {
        return capacity;
    }

    public int getTicketsSold() {
        return ticketsSold;
    }

    public String getLocation() {
        return location;
    }

    public String getDate() {
        return date;
    }
}
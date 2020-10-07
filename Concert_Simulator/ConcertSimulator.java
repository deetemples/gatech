public class ConcertSimulator {
    public static void main(String[] args) {
        Musician chris = new Musician("Christopher W. Klaus", "Violin", 30);
        System.out.println(chris);
        System.out.println("exp: " + chris.getSkillLevel());
        Musician uga = new Musician("UGA", "students", 234);
        System.out.println(uga);

        Fan gerald = new Fan(14, 8, 52, true, chris);
        gerald.announceFavoriteMusician();

        Concert show = new Concert(500, 60, "Mercedes-Benz Stadium", "02/03/2019");
        Concert show2 = new Concert(12, "Tabernacle", "one day");
        show2.setLocation("here");
        show2.setTicketPrice(16);

        chris.rehearse();
        System.out.println(chris);
        System.out.println("exp: " + chris.getSkillLevel());
        chris.perform();
        System.out.println("exp: " + chris.getSkillLevel());

        while (show.getTicketsSold() < 60) {
            show.sellTicket();
        }

        for (int i=0; i<15; i++) {
            show2.sellTicket();
        }

        if (show2.isSoldOut()) {
            System.out.println("Sorry! " + show2 + " is fully booked!" + show2.getTicketsSold());
        }

        if (show.isSoldOut()) {
            System.out.println("Sorry! " + show + " is fully booked!");
        }

        System.out.println(gerald.liveTweet(show));
        System.out.println(gerald.liveTweet(show2));
    }
}
//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

public class Fan {
    private int yearsAsFan;
    private int albumsBought;
    private int concertsAttended;
    private boolean buzzcard;
    private Musician favoriteMusician;


    public Fan(int yearsAsFan, int albumsBought, int concertsAttended, boolean buzzcard, Musician favoriteMusician) {
        this.yearsAsFan = yearsAsFan;
        this.albumsBought = albumsBought;
        this.concertsAttended = concertsAttended;
        this.buzzcard = buzzcard;
        this.favoriteMusician = favoriteMusician;
    }

    public boolean winGiveaway() {
        return true;
    }

    public String liveTweet(Concert concert) {
        String tweet = "";
        if (yearsAsFan > 5) {
            tweet = tweet.concat("Best band ever!\n");
        }

        if (concert.getTicketPrice() > 100) {
            tweet = tweet.concat("Totally worth my entire bank account!\n");
        }

        if (albumsBought >= 1) {
            tweet = tweet.concat("Even better in person!\n");
        }

        concertsAttended++;
        tweet = tweet.concat("I've been to " + concertsAttended
            + ((concertsAttended == 1) ? " concert!" : " concerts!"));
        return tweet;
    }

    public void lostBuzzcard() {
        if (yearsAsFan > 3) {
            buzzcard = false;
        }
    }

    public void announceFavoriteMusician() {
        System.out.println("My favorite musician is " + favoriteMusician.getName() + "!");
    }

    public int getYearsAsFan() {
        return yearsAsFan;
    }

    public int getAlbumsBought() {
        return albumsBought;
    }

    public int getConcertAttended() {
        return concertsAttended;
    }

    public boolean getBuzzcard() {
        return buzzcard;
    }

    public Musician getFavoriteMusician() {
        return favoriteMusician;
    }
}
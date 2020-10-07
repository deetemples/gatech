//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

public class Musician {
    private String name;
    private String instrument;
    private int yearsPlaying;
    private double skillLevel;


    public Musician(String name, String instrument, int yearsPlaying) {
        this.name = name;
        this.instrument = instrument;
        this.yearsPlaying = yearsPlaying;
        skillLevel = 1.0;
        for (int i = 0; i < yearsPlaying; i++) {
            skillLevel = skillLevel + 0.5;
        }
    }

    public Musician(String name, String instrument) {
        this(name, instrument, 0);
    }

    public void rehearse() {
        yearsPlaying++;
        skillLevel = skillLevel + 0.5;
    }

    public void perform() {
        skillLevel++;
    }

    public String toString() {
        return "My name is " + name + ". I have been playing " + instrument + " for " + yearsPlaying + " years.";
    }

    public String getName() {
        return name;
    }

    public String getInstrument() {
        return instrument;
    }

    public int getYearsPlaying() {
        return yearsPlaying;
    }

    public double getSkillLevel() {
        return skillLevel;
    }
}
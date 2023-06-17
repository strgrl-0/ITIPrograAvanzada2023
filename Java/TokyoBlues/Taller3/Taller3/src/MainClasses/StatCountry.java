package MainClasses;

public class StatCountry {
    private String countryName;
    private int inhabitantsBeforeWar;
    private int inhabitantsAfterWar;
    private int attacksPerformedInCountry;
    private int totalRecruits;

    public StatCountry(
        String countryName,
        int inhabitantsBeforeWar,
        int inhabitantsAfterWar,
        int attacksPerformedInCountry,
        int totalRecruits){

        this.countryName = countryName;
        this.inhabitantsBeforeWar = inhabitantsBeforeWar;
        this.inhabitantsAfterWar = inhabitantsAfterWar;
        this.attacksPerformedInCountry = attacksPerformedInCountry;
        this.totalRecruits = totalRecruits;
    }

    public static StatCountry create(
    String countryName,
    int inhabitantsBeforeWar, 
    int inhabitantsAfterWar,
    int attacksPerformedInCountry,
    int totalRecruits){

        StatCountry current = new StatCountry(
            countryName,
            inhabitantsBeforeWar,
            inhabitantsAfterWar,
            attacksPerformedInCountry,
            totalRecruits
        );

        return current;
    }

    @Override
    public String toString() {
        String toPrintStatCountry;
        toPrintStatCountry =   countryName + " " +
                            inhabitantsBeforeWar + " " +
                            inhabitantsAfterWar + " " +
                            attacksPerformedInCountry + " " +
                            totalRecruits;

        return toPrintStatCountry;
    }
}

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

    public static StatCountry create(String[] fileLineParts){

        String countryName = fileLineParts[0];
        int inhabitantsBeforeWar = Integer.parseInt(fileLineParts[1]);
        int inhabitantsAfterWar = Integer.parseInt(fileLineParts[2]);
        int attacksPerformedInCountry = Integer.parseInt(fileLineParts[3]);
        int totalRecruits = Integer.parseInt(fileLineParts[4]);
        
        StatCountry current = new StatCountry(
            countryName,
            inhabitantsBeforeWar,
            inhabitantsAfterWar,
            attacksPerformedInCountry,
            totalRecruits
        );
        
        return current;
    }

    //get

    public String getCountryName(){
        return countryName;
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

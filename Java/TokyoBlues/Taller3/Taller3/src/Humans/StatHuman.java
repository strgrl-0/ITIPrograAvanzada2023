package Humans;
import Humans.Programmers.*;

public abstract class StatHuman{

    private int uniqueId;
    private String uniqueName;
    private String uniqueSurname;
    private String uniqueSpecialization;

    //builder
    public StatHuman(
    int id, 
    String name, 
    String surname, 
    String specialization
    ){
        this.uniqueId = id; 
        this.uniqueName = name;
        this.uniqueSurname = surname; 
        this.uniqueSpecialization = specialization;
    }

    //Programmers
    public static IaEngineer createIaEngineer(String[] partsIaEngineer){
        IaEngineer currentIaengineer = IaEngineer.create(
            Integer.parseInt(partsIaEngineer[0]),
            partsIaEngineer[1],
            partsIaEngineer[2],
            partsIaEngineer[3],
            Integer.parseInt(partsIaEngineer[4]),
            partsIaEngineer[5],
            Integer.parseInt(partsIaEngineer[6])
        );

        return currentIaengineer;

    }

    public static ThreatAnalyst createThreatAnalyst(String[] partsThreatAnalyst){
        ThreatAnalyst currentThreatAnalyst = ThreatAnalyst.create(
            Integer.parseInt(partsThreatAnalyst[0]),
            partsThreatAnalyst[1],
            partsThreatAnalyst[2],
            partsThreatAnalyst[3],
            Integer.parseInt(partsThreatAnalyst[4]),
            partsThreatAnalyst[5],
            Integer.parseInt(partsThreatAnalyst[6])
        );

        return currentThreatAnalyst;

    }

    public static CriptographyXpert createCriptographyXpert(String[] partsCriptographyXpert){
        CriptographyXpert currentCriptographyXpert = CriptographyXpert.create(
            Integer.parseInt(partsCriptographyXpert[0]),
            partsCriptographyXpert[1],
            partsCriptographyXpert[2],
            partsCriptographyXpert[3],
            Integer.parseInt(partsCriptographyXpert[4]),
            partsCriptographyXpert[5],
            partsCriptographyXpert[6],
            Integer.parseInt(partsCriptographyXpert[7]),
            partsCriptographyXpert[8]
        );

        return currentCriptographyXpert;

        

    }

    
    //Generalized caller
    
    public static StatHuman createHumanFromString(String[] parts) {
        
        switch(parts[3]){ 
            case "IaEngineer": 
                return createIaEngineer(parts);
            case "ThreatAnalyst":
                return createThreatAnalyst(parts); 
            case "CriptographyXpert":
                return createCriptographyXpert(parts);
            default:
                return null;

        }
    }
    

    //calls



    //set get
    public int getUniqueId(){
        return uniqueId;
    }

    public String getUniqueName(){
        return uniqueName;
    }

    public String getUniqueSurname(){
        return uniqueSurname;
    }

    public String getUniqueSpecialization(){
        return uniqueSpecialization;
    }

}

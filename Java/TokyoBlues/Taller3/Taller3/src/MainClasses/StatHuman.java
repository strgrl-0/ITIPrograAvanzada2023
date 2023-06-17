package MainClasses;

import Humans.Programmers.*;
import Humans.Soldiers.*;

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

    //Soldiers

    public static Artillery createArtillery(String[] parts){

        float strToFloat;
        strToFloat = Float.parseFloat(parts[7]);

        Artillery current = Artillery.create(
            Integer.parseInt(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            Integer.parseInt(parts[5]),
            Integer.parseInt(parts[6]),
            strToFloat
        );

        return current;
    }


    public static Infantry createInfantry(String[] parts){
        Infantry current = Infantry.create(
            Integer.parseInt(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            Integer.parseInt(parts[5]),
            Integer.parseInt(parts[6]),
            parts[7]
        );
        return current;
    }


    public static Intelligence createIntelligence(String[] parts){
        Intelligence current = Intelligence.create(
            Integer.parseInt(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            Integer.parseInt(parts[5]),
            Integer.parseInt(parts[6]),
            Integer.parseInt(parts[7])
            
        );
        return current;
    }


    public static SpecOps createSpecOps(String[] parts){
        SpecOps current = SpecOps.create(
            Integer.parseInt(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            Integer.parseInt(parts[5]),
            Integer.parseInt(parts[6]),
            Integer.parseInt(parts[7]),
            Integer.parseInt(parts[8])
        );
        return current;
    }
    


    public static Logistics createLogistics(String[] parts){
        Logistics current = Logistics.create(
            Integer.parseInt(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            Integer.parseInt(parts[5]),
            Integer.parseInt(parts[6]),
            Integer.parseInt(parts[7])
        );
        return current;
    }

    //Generalized caller
    
    public static StatHuman createHumanFromString(String[] parts) {
        String specializationProgrammer = parts[3];
        String specializationSoldier = parts[4];
        
        for(int i = 0; i<1; i++){
            switch(specializationProgrammer){ 
                case "IaEngineer": 
                    return createIaEngineer(parts);
                case "ThreatAnalyst":
                    return createThreatAnalyst(parts); 
                case "CriptographyXpert":
                    return createCriptographyXpert(parts);

            }
        }

        switch(specializationSoldier){
            case "Artillery":
                return createArtillery(parts);
            case "Infantry":
                return createInfantry(parts);
            case "Intelligence":
                return createIntelligence(parts);
            case "SpecOps":
                return createSpecOps(parts);
            case "Logistics":
                return createLogistics(parts);

        }
        
        return null;
    
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



    
    @Override
    public String toString() {
        String toPrintStatHuman =   uniqueId + " " + 
                                    uniqueName + " " + 
                                    uniqueSurname;
        return toPrintStatHuman;
    }


}

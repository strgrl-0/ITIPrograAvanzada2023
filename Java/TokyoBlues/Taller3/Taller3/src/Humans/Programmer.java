package Humans;

import MainClasses.StatHuman;

public class Programmer extends StatHuman{

    private int programmer_value;
    //Builder
    public Programmer(                   
    int id, 
    String name, 
    String surname, 
    String specialization,
    int programmerValue
    ){
        super(id, name, surname, specialization);

        this.programmer_value = programmerValue;

        
    }

    public int getProgrammerValue(){
        return programmer_value;
    }

    
    @Override
    public String toString() {                                  //programmerValue is NOT shown
        String toPrintProgrammer;
        toPrintProgrammer = super.toString() + " " +
                            getUniqueSpecialization() + " ";
        return toPrintProgrammer;
    }
}


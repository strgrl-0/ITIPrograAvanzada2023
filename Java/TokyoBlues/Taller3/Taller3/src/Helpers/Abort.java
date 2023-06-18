package Helpers;

import MainClasses.*;

public abstract class Abort {

    public static Object delete(
        Object currentObject, 
        boolean delete){

            if(delete==true){
                currentObject = null;
                System.gc();
                return currentObject;
            }else{
                return currentObject;
            }
    }

    public static boolean valuesLimiter(int value){
        int maxValue = 999;
        boolean isValueOffRange = false;
        
        if(value>maxValue){
            isValueOffRange = true;
            System.out.println("The value " + value + 
            " is out of the 999 limit");
            return isValueOffRange;
        }else{
            isValueOffRange = false;
            return isValueOffRange;
        }
    }

    public static boolean isCountryRepeated(
        String country, 
        StatCountry countryObject){
            String countryObjCountryNameToStr = countryObject.getCountryName();
            if(country == countryObjCountryNameToStr){
                return true;
            }else{
                return false;
            }
        }
    
    public static boolean isProgrammerLevelValid(String level){
        String[] validLevels = new String[]{"Low", "Intermediate", "Advanced"};
        
        for(int i = 0; i<validLevels.length; i++){
            if(validLevels[i].equals(level)){
                return !true;
            }
        }
        return !false;
    }
}

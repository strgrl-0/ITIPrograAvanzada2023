package Helpers;

public abstract class Abort {

    public static Object delete(
        Object currentObject, 
        boolean isValid){
            if(isValid==false){
                currentObject = null;
                System.gc();
                return currentObject;
            }else{
                return currentObject;
            }
    }

}
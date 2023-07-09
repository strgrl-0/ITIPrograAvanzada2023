package Login;

import java.util.*;

import MainClasses.User;

public abstract class MainLogin {

    public static boolean Login(Object[] usrArr){
        String username = getUsernameFromInput();
        String[] usrStringArr = getUsrStringArr(usrArr);
        //problem with getUsrIndex

        if(isUserRegisteredAlready(username, usrStringArr)==true){
            String password = getPasswordFromInput();
            User currentUser = (User) usrArr[getUserIndexFromUsrArr(usrArr, username)];
            boolean isPasswordValid = passwordCheck(password, currentUser);

            boolean IsClearanceValid = false;
            
            if(isPasswordValid == true){
                IsClearanceValid = checkClearance(currentUser);
                System.out.println("pasVal");
            }else{
                System.exit(0);
            }

            if(IsClearanceValid == true){

                System.out.println("a");
                
                switch(currentUser.getClearance()){
                    case "Admin":
                        return true;

                    case "User":
                        return false;
                }
                
            }

        }else{
            System.out.println("not registered already");
        }
        return false;
    }


    public static String[] getUsrStringArr(Object[] usrArr){
        int usrArrLength = usrArr.length;

        String[] usrStringArr = new String[usrArrLength];
        User[] usrClassArr = new User[usrArrLength];
        
        
        for (int i = 0; i<usrArrLength; i++){
            usrClassArr[i] = (User) usrArr[i];
            usrStringArr[i] = usrClassArr[i].getUsername();
        }

        return usrStringArr;

    }

    public static boolean isUserRegisteredAlready(
        String username, 
        String[] usrStringArr){
        int usrArrLength = usrStringArr.length;

        for(int i = 0; i<usrArrLength; i++){

            if(username.equals(usrStringArr[i])){
                System.out.println("found");
                return true;
            }
        }
        System.out.println("not found");
        return false;
    }

    public static int getUserIndexFromUsrArr(
        Object[] usrArr, 
        String username){

        int usrArrLength = usrArr.length;

        for(int i = 0; i<usrArrLength; i++){
            if(username == usrArr[i]){
                return i;
            }
        }
        return 0;
    }

    public static String getPasswordFromInput(){
        Scanner passIn = new Scanner(System.in);
        System.out.println("Password: ");

        String password = passIn.nextLine();

        return password;
    }

    public static String getUsernameFromInput(){
        Scanner usernameIn = new Scanner(System.in);
        System.out.println("Username: ");

        String username = usernameIn.nextLine();

        return username;
    }

    public static boolean passwordCheck(String password, User current){
        int tryCount = 0;
        while(tryCount<2){
            if(password.equals(current.getPassword())){
                return true;
            }else{
                System.out.println("Wrong Password");
                tryCount++;
                password = getPasswordFromInput();
            }
        }
        System.out.println("TOO MUCH TRIES, ABORTING");
        System.exit(0);
        return false;
    }

    public static boolean checkClearance(User current){
        String clearance = current.getClearance();
        switch(clearance){
            case "Admin":
                return true;
            case "User":
                return true;
            default:
                System.out.println("Clearance NOT valid");
                System.exit(0);
                return false;
        }
    }
    
}

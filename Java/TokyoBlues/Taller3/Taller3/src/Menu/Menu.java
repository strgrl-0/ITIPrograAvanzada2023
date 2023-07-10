package Menu;

import Menu.Procedures.menuUsrProcedures;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import Helpers.Node.NodeSystem;
import Humans.*;
import MainClasses.StatCountry; //
import MainClasses.User; //          TODO: TAKE IMPORT AWAY IF NOT NEEDED
import MainClasses.Ia; //
import Humans.Soldier;
import Humans.Soldiers.Artillery;
import Menu.History;
import Menu.Player;

public class Menu implements menuUsrProcedures {
    private Object[] usrArr;
    private Object[] programmersArr;
    private Object[] soldiersArr;
    private Object[] countriesArr;
    private Object[] iasArr;

    // subfunctions flags/arrs
    private boolean teamCreated = false;
    private History[] battleHistory;
    private User currentProfile;

        //Top arrays    
    private Player[] topGlobals;

    public Menu(Object[] usrArr, Object[] programmersArr, Object[] soldiersArr, Object[] countriesArr,
                Object[] iasArr, User currentProfile) {
        this.usrArr = usrArr;
        this.programmersArr = programmersArr;
        this.soldiersArr = soldiersArr;
        this.countriesArr = countriesArr;
        this.iasArr = iasArr;
        this.currentProfile = currentProfile;    
    }

    // Main Usr menu/interaction
    public void menuUsr() {

        Scanner scannerUsr = new Scanner(System.in);
        int option = -1;

        while (option == -1) {
            System.out.println("0.Ver galería de soldados");
            System.out.println("1.Ver galeria de programadores");
            System.out.println("2.Crear equipo");
            System.out.println("3.Registro de batallas");
            System.out.println("4.Cambiar Perfil");
            System.out.println("5.Ver Top");
            System.out.println("6.Pelear contra una IA");
            System.out.println("7.Volver al Login"); // Funcion agregada
            System.out.println("8.Salir");
        }

        try {
            option = Integer.parseInt(scannerUsr.nextLine());

            switch (option) {
                case 0:

                    break;

                case 1:

                    break;

                case 2:

                    break;

                case 3:

                    break;

                case 4:

                    break;

                case 5:

                    break;

                case 6:

                    break;

                case 7:

                    break;

                case 8:
                    System.exit(0);
                    break;

            }
        } catch (Exception e) {
            System.out.println("No se pueden ingresar opciones que no sean números");
        }

    }
    // SubFunctions

    public void showSoldierGallery(Object[] soldiersArr) {
        String toPrint;

        for (int i = 0; i < soldiersArr.length; i++) {
            Soldier currentObjectToSoldier = (Soldier) soldiersArr[i];
            toPrint = currentObjectToSoldier.toString();
            System.out.println(toPrint);
        }
    }

    public void showProgrammerGallery(Object[] programmersArr) {
        String toPrint;

        for (int i = 0; i < programmersArr.length; i++) {
            Programmer currentObjectToProgrammer = (Programmer) programmersArr[i];
            toPrint = currentObjectToProgrammer.toString();
            System.out.println(toPrint);
        }
    }

    public NodeSystem createTeam(Object[] programmersArr, Object[] soldiersArr) {
        if (teamCreated == true) {
            System.out.println("El equipo ya ha sido creado");
            return null;
        }

        System.out.println("Crea tu equipo");
        System.out.println("Ingresa tus soldados");
        Scanner scanData = new Scanner(System.in);

        // NodeSys creation

        NodeSystem nodeSys = new NodeSystem();
        teamCreated = true;

        for (int i = 0; i < 3; i++) {
            switch (i) {
                case 0:
                    System.out.println("Soldado 1"); // Dialogo
                    break;

                case 1:
                    System.out.println("Soldado 2");
                    break;

                case 2:
                    System.out.println("Soldado 3");
                    break;
            }
            String scannedString = scanData.nextLine();
            int soldierId = Integer.parseInt(scannedString);    //Adds soldier by id to linkedlist
            nodeSys.add(searchSoldier(soldierId));
        }

        for (int i = 0; i < 2; i++) {
            switch (i) {
                case 0:
                    System.out.println("Programador 1");
                    break;

                case 1:
                    System.out.println("Programador 2");
                    break;
            }
            String scannedString = scanData.nextLine();
            int programmerId = Integer.parseInt(scannedString);
            nodeSys.add(searchProgrammer(programmerId));
        }

        scanData.close();

        return nodeSys;

    }

    // createTeam subFunctions
    private Soldier searchSoldier(int id) {
        for (int i = 0; i < soldiersArr.length; i++) {
            Soldier current = (Soldier) soldiersArr[i];
            if (current.getUniqueId() == id) {
                return current;
            }
        }

        return null;
    }

    private Programmer searchProgrammer(int id) {
        for (int i = 0; i < programmersArr.length; i++) {
            Programmer current = (Programmer) programmersArr[i];
            if (current.getUniqueId() == id) {
                return current;
            }
        }

        return null;
    }

    // resume interface implementation
    public void showHistory() {
        try {
            battleHistory = preCharge();     //tries precharge

        } catch (FileNotFoundException e) {
            for(int i = 0; i<battleHistory.length; i++){        //sens to Menu after showing up         
                if(battleHistory[i].getPlayer()==currentProfile.getUsername()){
                    System.out.println(battleHistory[i]);
                }
            }
            menuUsr();
        }
    }

    // showHistory subfunctions

    private History[] preCharge() throws FileNotFoundException {
        File HistoryFile = new File("src/File/history.txt");
        // History File structure: String ai, String battleResult, float winrate, String player
        if (HistoryFile.exists() == true) {
            Scanner scanHistory = new Scanner(HistoryFile);
            History[] historyArr = new History[fileArrSize(HistoryFile)];
            int i = 0;

            while (scanHistory.hasNextLine()) {
                String[] parts = scanHistory.nextLine().split(",");
                String ai = parts[0];
                String battleResult = parts[1];
                float winrate = Float.parseFloat(parts[2]);
                String player = parts[3];

                History current = new History(ai, battleResult, winrate, player);

                historyArr[i] = current;
                i = i + 1;
            }

            scanHistory.close();
            return historyArr;
        }
        return null;
    }

    private int fileArrSize(File HistoryFile) throws FileNotFoundException {
        Scanner scan = new Scanner(HistoryFile);
        int fileSize = 0;

        while (scan.hasNextLine()) {
            fileSize++;
            scan.nextLine();
        }
        scan.close();
        return fileSize;
    }

    // resume interface impl

    public void changeProfile(User currentProfile){
        System.out.println("1.Cambiar Contraseña");
        System.out.println("2.Cambiar Nombre");
        System.out.println("3.Cambiar país");
        System.out.println("0.Volver al menu");

        Scanner lineIn = new Scanner(System.in);
        int choosenOption = Integer.parseInt(lineIn.nextLine());

        switch(choosenOption){
            case 0:
            menuUsr();
            break;
            case 1:
            System.out.println("Ingresa el nuevo Usuario");
            String newName = lineIn.nextLine();
            currentProfile.setUsername(newName);
            menuUsr();
            break;
            case 2:
            System.out.println("Ingresa la nueva contraseña");
            String newPassword = lineIn.nextLine();
            currentProfile.setPassword(newPassword);
            menuUsr();
            break;
            case 3:
            System.out.println("Ingresa el nuevo país");
            String newCountry = lineIn.nextLine();
            currentProfile.setCountry(newCountry);
            menuUsr();
            break;
            default:
            System.out.println("Debes elegir una opcion valida");
            break;

        }

        lineIn.close();

    }

    public void showTop(){
        System.out.println("1.Ver top global");
        System.out.println("2.Ver top nacional");
        System.out.println("0.Volver al menu");

        //global top impl

    }

    private Player[] createGlobalTop(History[] battleHistory){      //TODO: battlehistory must include a player attribute in order to know who battled what
        if(battleHistory[0] == null){
            System.out.println("El top está vacio");
        }
        Player[] scoreChart = createScoreChart();

        int maxValue = 0;
        int aux = maxValue;

        for(int i = 0; i<scoreChart.length; i++){
            if(maxValue < scoreChart[i].getScore()){
                aux = maxValue;
                maxValue = scoreChart[i].getScore();
            }
        }

        for(int i = 0; i<scoreChart.length; i++){

        }

        return null;
    }

    private Player[] createScoreChart(){
        Player[] scoreChart = new Player[battleHistory.length];
        int iterations = battleHistory.length;

        for(int i = 0; i<iterations; i++){
            int totalCurrentScore = 0;
            String currentPlayer = battleHistory[i].getPlayer();

            for(int j = 0; j<iterations; j++){
                if(currentPlayer == battleHistory[j].getPlayer()){
                    totalCurrentScore = addOrTake(totalCurrentScore, battleHistory[j].getBattleResult());
                }
            }
            Player current = new Player(currentPlayer, totalCurrentScore);
            scoreChart[i] = current;
        }

        return scoreChart;
    }            //TODO: Use a Player type array to store all the players and their times, then use that info to create the tops

    private int addOrTake(int currentValue, String flag){
        if(flag == "Win"){
            currentValue = currentValue + 3;
        } else if(flag == "Lose"){
            currentValue = currentValue - 3;
        }

        return currentValue;
    }

    public int fightAgainstAi(Object[] programmersArr, Object[] soldiersArr, Object[] aiArr){
        return 0;
    }

    public void menuAdmin() {

    }

}

package Menu;

public class History {
    private String ai;
    private String battleResult;
    private float winrate;
    private String player;

    public History(String ai, String battleResult, float winrate, String player){
        this.ai = ai;
        this.battleResult = battleResult;
        this.winrate = winrate;
        this.player = player;
    }

    //set get
    public String getAi(){
        return ai;
    }
    public String getBattleResult(){
        return battleResult;
    }
    public float getWinrate(){
        return winrate;
    }
    public String getPlayer(){
        return player;
    }

    public void setAi(String ai){
        this.ai = ai;
    }
    public void setBattleResult(String battleResult){
        this.battleResult = battleResult;
    }
    public void setWinrate(float winrate){
        this.winrate = winrate;
    }
    public void setPlayer(String player){
        this.player = player;
    }

    @Override
    public String toString(){
        String toPrint;
        toPrint = ai + " " + battleResult + " " + winrate;
        return toPrint;
    }
}

package Menu;

public class History {
    private String ai;
    private String battleResult;
    private float winrate;

    public History(String ai, String battleResult, float winrate){
        this.ai = ai;
        this.battleResult = battleResult;
        this.winrate = winrate;
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

    public void setAi(String ai){
        this.ai = ai;
    }
    public void setBattleResult(String battleResult){
        this.battleResult = battleResult;
    }
    public void setWinrate(float winrate){
        this.winrate = winrate;
    }
    
    @Override
    public String toString(){
        String toPrint;
        toPrint = ai + " " + battleResult + " " + winrate;
        return toPrint;
    }
}

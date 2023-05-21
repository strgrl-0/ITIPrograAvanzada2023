import java.util.Arrays;

public class Pais {
	private String pais;
	private String[] regiones;
	
	//Constructor
	public Pais(String pais,int cantRegiones,String[] regiones) {
		this.pais = pais;
		this.regiones = new String[cantRegiones];
		for(int i=0;i<cantRegiones;i++){
			this.regiones[i] = regiones[i];
		}
	}

	//---GETTERS AND SETTERS---
	public String getPais() {
		return pais;
	}
	
	public void setPais(String pais) {
		this.pais = pais;
	}
	
	public String[] getRegiones() {
		return regiones;
	}
	
	public void setRegiones(String[] regiones) {
		this.regiones = regiones;
	}

	@Override
	public String toString() {
		return "Pais [pais=" + pais + ", regiones=" + Arrays.toString(regiones) + "]";
	}
	
	
	
}

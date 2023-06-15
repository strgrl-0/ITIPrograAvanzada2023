
public class Debilidad {
	private String debilidad;
	private int nivelAmenaza;
	
	//Constructor
	public Debilidad(String debilidad, int nivelAmenaza) {
		this.debilidad = debilidad;
		this.nivelAmenaza = nivelAmenaza;
	}

	//Getters and Setters
	public String getDebilidad() {
		return debilidad;
	}

	public void setDebilidad(String debilidad) {
		this.debilidad = debilidad;
	}

	public int getNivelAmenaza() {
		return nivelAmenaza;
	}

	public void setNivelAmenaza(int nivelAmenaza) {
		this.nivelAmenaza = nivelAmenaza;
	}

	//ToString
	@Override
	public String toString() {
		return "Debilidad [debilidad=" + debilidad + ", nivelAmenaza=" + nivelAmenaza + "]";
	}
	
	
}

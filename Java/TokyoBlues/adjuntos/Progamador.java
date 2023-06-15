import java.util.Arrays;

public class Progamador {
	private int id;
	private String nombre;
	private String apellido;
	private int aniosExperiencia; //Años de experiencia
	private String[] lenguajes;
	private String pais;
	private String ciudad;
	
	//Constructor
	public Progamador(int id, String nombre, String apellido, int aniosExperiencia,String[] lenguajes,int cantLenguajes,String pais,String ciudad) {
		this.id = id;
		this.nombre = nombre;
		this.apellido = apellido;
		this.aniosExperiencia = aniosExperiencia;
		this.lenguajes = new String[cantLenguajes];
		for(int i=0;i<cantLenguajes;i++){
			this.lenguajes[i] = lenguajes[i];
		}
		this.pais = pais;
		this.ciudad = ciudad;
	}

	//---GETTERS AND SETTERS---
	
	public int getId() {
		return id;
	}



	public void setId(int id) {
		this.id = id;
	}



	public String getNombre() {
		return nombre;
	}



	public void setNombre(String nombre) {
		this.nombre = nombre;
	}



	public String getApellido() {
		return apellido;
	}



	public void setApellido(String apellido) {
		this.apellido = apellido;
	}



	public int getAniosExperiencia() {
		return aniosExperiencia;
	}



	public void setAniosExperiencia(int aniosExperiencia) {
		this.aniosExperiencia = aniosExperiencia;
	}



	public String[] getLenguajes() {
		return lenguajes;
	}



	public void setLenguajes(String[] lenguajes) {
		this.lenguajes = lenguajes;
	}



	public String getPais() {
		return pais;
	}



	public void setPais(String pais) {
		this.pais = pais;
	}



	public String getCiudad() {
		return ciudad;
	}



	public void setCiudad(String ciudad) {
		this.ciudad = ciudad;
	}



	@Override
	public String toString() {
		return "Progamador [id=" + id + ", nombre=" + nombre + ", apellido=" + apellido + ", aniosExperiencia="
				+ aniosExperiencia + ", lenguajes=" + Arrays.toString(lenguajes) + ", pais=" + pais + ", ciudad="
				+ ciudad + "]";
	}

	
	


	
	
	
}

public class Persona {
    private int edad;
    private String nombre;
    private String telefono;

    

    public int getEdad() {
        return edad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public static void main(String[] args) {
        Persona persona = new Persona(); 

    persona.setEdad(20);
    persona.setNombre("Juan");
    persona.setTelefono("1234567890");

    System.out.println("Edad: " + persona.getEdad());
    System.out.println("Nombre: " + persona.getNombre());
    System.out.println("Telefono: " + persona.getTelefono());
    
    }

    

}


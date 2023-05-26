public class main {
    
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setEdad(27);
        cliente.setNombre("Juan");
        cliente.setTelefono("123456789");
        cliente.setCredito("1000");

        System.out.println("Nombre: " + cliente.getNombre()
                + "\nEdad: " + cliente.getEdad()
                + "\nTelefono: " + cliente.getTelefono()
                + "\nCredito: " + cliente.getCredito());
    }
}

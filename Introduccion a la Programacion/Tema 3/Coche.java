public class Coche {
    int numPuerta;

    public  void aumentarPuertas(int num) {
        this.numPuerta = this.numPuerta + num;
        
    }
    
    public static void main(String[] args) {
        Coche coche = new Coche();
        coche.numPuerta = 5;
        coche.aumentarPuertas(2);
        System.out.println("El coche tiene " + coche.numPuerta + " puertas");
    }

}
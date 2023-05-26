public class SumaNumeros {
    public static void sumarTresNumeros(int num1, int num2, int num3) {
        int suma = num1 + num2 + num3;
        System.out.println("La suma de los tres números es: " + suma);
    }
    
    public static void main(String[] args) {
        int numero1 = 5;
        int numero2 = 10;
        int numero3 = 15;
        
        sumarTresNumeros(numero1, numero2, numero3);
    }
}

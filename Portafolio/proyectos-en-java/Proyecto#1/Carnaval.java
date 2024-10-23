/*Omamr polanco
 Alanis Zamora
 Karin Sarmiento
 Valentina Orozco*/

 import java.io.*;
 public class Carnaval{
     
     public static void main (String[] args) throws IOException{ 
         BufferedReader reader = new BufferedReader (new InputStreamReader(System.in));
         int opcion = 0;
         //Llamada a los metodos externos
         XOJuego juego = new XOJuego(); 
         XOGanador ganador = new XOGanador();
         Ruleta ruleta = new Ruleta();
         do{
          //Menu de opciones
         System.out.println("Escoja el juego:");
         System.out.println("1. X y O");
         System.out.println("2. Ruleta");   
         System.out.println("3. Salir");
         System.out.print(">");
         try{
         opcion = Integer.parseInt(reader.readLine());
         } catch (Exception e){
             System.out.println("Error. El valor debe ser del 1-3)");
             continue;
         }
             
         switch (opcion){
             case 1:
             System.out.println("¡Bienvenido! Ha elegido X y O");
         char winner = ' ';
 
         while (winner == ' ' && !juego.Boardlleno()) {
             System.out.println("Turno del jugador " + juego.getplayeract());
             juego.printBoard();
             /*Opcion 1. Debes ingresar primero la fila y luego la columna hasta que alguno jugador gane o empate*/
             System.out.print("Ingrese la fila (1-3): ");            
             int row = Integer.parseInt(reader.readLine()) - 1;        
             System.out.print("Ingrese la columna (1-3): ");
             int col = Integer.parseInt(reader.readLine()) - 1;
 
             //Error si se ingresa una coordenada no valida
             if (juego.makeMove(row, col)) {         
                 winner = cal.calganador(juego.board);
                 juego.switchPlayer();
             } else {
                 System.out.println("Movimiento inválido. Inténtalo de nuevo.");
             }
         }
 
          //Impresion de resultados de la partida
         juego.printBoard();
         if (winner == 'X') {
             System.out.println("¡Jugador X ES EL GANADOR!");     
             System.out.println("¡Gracias por jugar!");
         } else if (winner == 'O') {
             System.out.println("¡Jugador O ES EL GANADOR!");
             System.out.println("¡Gracias por jugar!");
         } else {
             System.out.println("EMPATE");
             System.out.println("¡Gracias por jugar!");
         }
         break;
 
         //Opcion 2. El metodo inicia preguntandote un numero del 1-10 y la cantidad de dinero que quiere apostar
         case 2:
         System.out.println("¡Bienvenido! Ha elegido La Ruleta"); 
         System.out.println("Su saldo inicial es de $100.00");
         ruleta.Ruletajuego();
         break;
 
         //Opcion 3. Salir del menú
         case 3:                    
         System.out.println("¡Vuelva pronto!");
         break;
 
         //Error si se escoje un numero que no este dentro del rango 1-3
         default:           
         System.out.println("Error. Por favor ingrese un numero del 1-3");
     }
     //La eleccion del menu continua hasta que se ingrese 3
 } while (opcion != 3); 
 }
 }


   
        

import java.io.*;
import java.util.Set;
import java.util.HashSet;

public class BattleshipMain {
    public static void main(String[] args) throws IOException   {
        
        BufferedReader shinxlector = new BufferedReader(new InputStreamReader(System.in));
        Boardload dratini = new Boardload();
        Barcos vaporeon = new Barcos();
        Attackboard pancham = new Attackboard();

        String usu1 = "";
        String usu2 = "";
        int tam = 0;
        int selec = 0;
        int ship2 = 0;
        int ship3 = 0;
        int ship4 = 0;
        int turno = 0;
        int atinar1 = 0;
        int atinar2 = 0;
        int lost = 0;
        String ori = "";
        String fila = "";
        String columna = "";
        String prueba = "";
        String ataque = "";
        String [] vec1;
        String [] vec2;
        String [] resul1 = new String [4];
        String [] resul2 = new String [4];
        Set<String> santa1 = new HashSet<>();
        Set<String> santa2 = new HashSet<>();
        Set<String> gift1 = new HashSet<>();
        Set<String> gift2 = new HashSet<>();

        System.out.println("Bienvenido a nuestro increible juego de BattleShip!!!");
        System.out.println();
        System.out.print("Jugador 1. Ingrese su nombre de usuario: ");
        usu1 = shinxlector.readLine();
        System.out.println();
        System.out.print("Jugador 2. Ingrese su nombre de usuario: ");
        usu2 = shinxlector.readLine();
        System.out.println();
        System.out.println("Aqui están tus 2 tableros " + usu1 + " con los que jugarás. El tablero de la izquierda será para tus ataques y el de la derecha será para colocar los barcos.");
        System.out.println();
        String [][] mat1 = dratini.bload();
        String [][] mat2 = dratini.bload();
        String [][] mat4 = dratini.bload();

        for (int f = 0; f < 10; f++)    {
            for (int c = 0; c < 10; c++)    {
                System.out.print(mat1 [f][c]);
            }
            System.out.print("   ");
            for (int c = 0; c < 10; c++)    {
                System.out.print(mat2 [f][c]);
            }
            System.out.println();
        }
        System.out.println();
        while (selec < 4)    {
        System.out.println(usu1 +"! Empecemos a ubicar tus barcos. ¿Qué barco deseas poner primero? (4, 3, 2)");
        do{
            try{
            tam = Integer.parseInt(shinxlector.readLine());
            if (tam < 2 || tam > 4){
                System.out.println("Error. Ingrese solo los numeros 4, 3 y 2");

             }
            }catch (Exception e){
                System.out.println("Error. Ingrese solo los numeros 4, 3 y 2");

            }

       } while (tam < 2 || tam > 4);//fin do while
        
        /*Hacerlo a tu manera*/while (tam == 2 && ship2 > 1 || tam == 3 && ship3 > 0 || tam == 4 && ship4 > 0)    {
            System.out.print("Este barco ya alcanzo la cantidad maxima de unidades a colocar. Por favor ingrese un nuevo tamaño de barco: ");
            tam = Integer.parseInt(shinxlector.readLine());
        }
        
        if (tam == 2)   {
            ship2 = ship2 + 1;
        }   else if (tam == 3)  {
            ship3 = ship3 + 1;
        }   else    {
            ship4 = ship4 + 1;
        }

        vec1 = new String[tam];
        vec2 = new String[tam];

        System.out.println("Ahora, escoge en qué dirección deseas colocar tu nave, ya sea horizontal (H) o vertical (V): ");
        ori = shinxlector.readLine();
        /*Hacerlo a tu maanera*/while (!ori.equalsIgnoreCase("H") && !ori.equalsIgnoreCase("V"))  {
           System.out.println("Error. Solo puede ser 'V' o 'H'");
           ori=shinxlector.readLine();
        }

        if (ori.equalsIgnoreCase("H"))   {
        System.out.println("Muy bien, ahora escoge las coordenadas");
        System.out.println("Primero escoge la fila: ");
        fila = shinxlector.readLine();
        /*Hacerlo a tu manera*/while (fila.compareTo("I") > 0 || fila.compareTo("A") < 0)  {
            System.out.println("Error. La letra debe estar dentro del rango de las filas, intenta otra vez: ");
            fila = shinxlector.readLine();
        }
        for (int a = 0; a < tam; a++)    {
            System.out.println("Ahora, escoge las coordenadas de las columnas: ");
            vec1 [a] = shinxlector.readLine();
            /*Hacerlo a tu manera*/while (Integer.parseInt(vec1[a]) > 9 || Integer.parseInt(vec1[a]) < 1)  {
                System.out.println("Error. La cifra ingresada no concuerda con los valores de las columnas. Por favo ingresa de nuevo un valor: ");
                vec1 [a] = shinxlector.readLine();
            }
            prueba = fila + vec1 [a];
            

            while (santa1.contains(prueba) || Integer.parseInt(vec1[a]) > 9 || Integer.parseInt(vec1[a]) < 1)    {
                System.out.println("Error. Coordenada repetida, ingresa una nueva");
                vec1 [a] = shinxlector.readLine();
                prueba = fila + vec1 [a];
            }
            santa1.add(prueba);
            resul1 [selec] = "Barco de tamaño " + tam + ", coordenada inicial es " + fila + vec1 [a] + " en " + ori;
        }
        
        }   else if (ori.equalsIgnoreCase("V"))  {
            System.out.println("Muy bien, ahora escoge las coordenadas");
        System.out.println("Primero escoge la columna: ");
        columna = shinxlector.readLine()
    ;
        /*Hacerlo a tu manera*/while (Integer.parseInt(columna) > 9 || Integer.parseInt(columna) < 1)  {
            System.out.println("Error. El numero debe estar dentro del rango de las columnas, intenta otra vez: ");
            columna = shinxlector.readLine();
        }
        for (int a = 0; a < tam; a++)    {
            System.out.println("Ahora, escoge las coordenadas de las filas: ");
            vec2 [a] = shinxlector.readLine();
            /*Hacerlo a tu manera*/while (vec2 [a].compareTo("I") > 0 || vec2 [a].compareTo("A") < 0)  {
                System.out.println("Error. La letra ingresada no concuerda con los valores de las filas. Por favo ingresa de nuevo un valor: ");
                vec2 [a] = shinxlector.readLine();
            }
            prueba = vec2 [a] + columna;
            

            while (santa1.contains(prueba) || vec2 [a].compareTo("I") > 0 || vec2 [a].compareTo("A") < 0)    {
                System.out.println("Error. Coordenada repetida, ingresa una nueva");
                vec1 [a] = shinxlector.readLine();
                prueba = vec2 [a] + columna;
            }
            santa1.add(prueba);
            resul1 [selec] = "Barco de tamaño " + tam + ", coordenada inicial es " + vec2 [a] + columna + " en " + ori;
        }
        
        }
    String [][] matbarcos1 =  vaporeon.barcos(tam, ori, fila, columna, vec1, vec2, mat2, mat4);

    for (int f = 0; f < 10; f++)  {
        for (int c = 0; c < 10; c++)  {
            if (matbarcos1[f][c].equals(" O "))     {
                mat2[f][c] = " O ";
            }
        }
    }
    for (int f = 0; f < 10; f++)  {
        for (int c = 0; c < 10; c++)    {
            System.out.print(mat1 [f][c]);
        }
        System.out.print("   ");
        for (int c = 0; c < 10; c++)    {
            System.out.print(mat2 [f][c]);
        }
        System.out.println();
    }
    selec = selec + 1;
        }//Fin while principal
    selec = selec * 0;
    tam = tam * 0;
    ship2 = ship2 * 0;
    ship3 = ship3 * 0;
    ship4 = ship4 * 0;

    System.out.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");

        System.out.println();
        System.out.println("Aqui están tus 2 tableros " + usu2 + " con los que jugarás. El tablero de la izquierda será para tus ataques y el de la derecha será para colocar los barcos.");
        System.out.println();
        String [][] mat3 = dratini.bload();
        /*String [][]*/ mat4 = dratini.bload();

        for (int f = 0; f < 10; f++)    {
            for (int c = 0; c < 10; c++)    {
                System.out.print(mat3 [f][c]);
            }
            System.out.print("   ");
            for (int c = 0; c < 10; c++)    {
                System.out.print(mat4 [f][c]);
            }
            System.out.println();
        }
        System.out.println();
    while (selec < 4)    {
        System.out.println(usu2 +"! Empecemos a ubicar tus barcos. ¿Qué barco deseas poner primero? (4, 3, 2)");
        do{
            try{
            tam = Integer.parseInt(shinxlector.readLine());
            if (tam < 2 || tam > 4){
                System.out.println("Error. Ingrese solo los numeros 4, 3 y 2");

             }
            }catch (Exception e){
                System.out.println("Error. Ingrese solo los numeros 4, 3 y 2");

            }

       } while (tam < 2 || tam > 4);//fin do while
        
        /*Hacerlo a tu manera*/while (tam == 2 && ship2 > 1 || tam == 3 && ship3 > 0 || tam == 4 && ship4 > 0)    {
            System.out.print("Este barco ya alcanzo la cantidad maxima de unidades a colocar. Por fvor ingrese un nuevo tamaño de barco: ");
            tam = Integer.parseInt(shinxlector.readLine());
        }
        
        if (tam == 2)   {
            ship2 = ship2 + 1;
        }   else if (tam == 3)  {
            ship3 = ship3 + 1;
        }   else    {
            ship4 = ship4 + 1;
        }

        vec1 = new String[tam];
        vec2 = new String[tam];

        System.out.println("Ahora, escoge en qué dirección deseas colocar tu nave, ya sea horizontal (H) o vertical (V): ");
        ori = shinxlector.readLine();
        /*Hacerlo a tu maanera*/while (!ori.equalsIgnoreCase("H") && !ori.equalsIgnoreCase("V"))  {
           System.out.println("Error. Solo puede ser 'V' o 'H'");
           ori=shinxlector.readLine();
        }

        if (ori.equalsIgnoreCase("H"))   {
        System.out.println("Muy bien, ahora escoge las coordenadas");
        System.out.println("Primero escoge la fila: ");
        fila = shinxlector.readLine();
        /*Hacerlo a tu manera*/while (fila.compareTo("I") > 0 || fila.compareTo("A") < 0)  {
            System.out.println("Error. La letra debe estar dentro del rango de las filas, intenta otra vez: ");
            fila = shinxlector.readLine();
        }
        for (int a = 0; a < tam; a++)    {
            System.out.println("Ahora, escoge las coordenadas de las columnas: ");
            vec1 [a] = shinxlector.readLine();
            /*Hacerlo a tu manera*/while (Integer.parseInt(vec1[a]) > 9 || Integer.parseInt(vec1[a]) < 1)  {
                System.out.println("Error. La cifra ingresada no concuerda con los valores de las columnas. Por favo ingresa de nuevo un valor: ");
                vec1 [a] = shinxlector.readLine();
            }
            prueba = fila + vec1 [a];
            

            while (santa2.contains(prueba) || Integer.parseInt(vec1[a]) > 9 || Integer.parseInt(vec1[a]) < 1)    {
                System.out.println("Error. Coordenada repetida, ingresa una nueva");
                vec1 [a] = shinxlector.readLine();
                prueba = fila + vec1 [a];
            }
            santa2.add(prueba);
            resul2 [selec] = "Barco de tamaño " + tam + ", coordenada inicial es " + fila + vec1 [a] + " en " + ori;
        }

        }   else if (ori.equalsIgnoreCase("V"))  {
            System.out.println("Muy bien, ahora escoge las coordenadas");
        System.out.println("Primero escoge la columna: ");
        columna = shinxlector.readLine();
        /*Hacerlo a tu manera*/while (Integer.parseInt(columna) > 9 || Integer.parseInt(columna) < 1)  {
            System.out.println("Error. El numero debe estar dentro del rango de las columnas, intenta otra vez: ");
            columna = shinxlector.readLine();
        }
        for (int a = 0; a < tam; a++)    {
            System.out.println("Ahora, escoge las coordenadas de las filas: ");
            vec2 [a] = shinxlector.readLine();
            /*Hacerlo a tu manera*/while (vec2 [a].compareTo("I") > 0 || vec2 [a].compareTo("A") < 0)  {
                System.out.println("Error. La letra ingresada no concuerda con los valores de las filas. Por favo ingresa de nuevo un valor: ");
                vec2 [a] = shinxlector.readLine();
            }
            prueba = vec2 [a] + columna;
            

            while (santa2.contains(prueba) || vec2 [a].compareTo("I") > 0 || vec2 [a].compareTo("A") < 0)    {
                System.out.println("Error. Coordenada repetida, ingresa una nueva");
                vec2 [a] = shinxlector.readLine();
                prueba = vec2 [a] + columna;
            }
            santa2.add(prueba);
            resul2 [selec] = "Barco de tamaño " + tam + ", coordenada inicial es " + vec2 [a] + columna + " en " + ori;
        }
        }
    String [][] matbarcos2 =  vaporeon.barcos(tam, ori, fila, columna, vec1, vec2, mat2, mat4);

    for (int f = 0; f < 10; f++)  {
        for (int c = 0; c < 10; c++)  {
            if (matbarcos2[f][c].equals(" O "))     {
                mat4[f][c] = " O ";
            }
        }
    }
    for (int f = 0; f < 10; f++)  {
        for (int c = 0; c < 10; c++)    {
            System.out.print(mat3 [f][c]);
        }
        System.out.print("   ");
        for (int c = 0; c < 10; c++)    {
            System.out.print(mat4 [f][c]);
        }
        System.out.println();
    }
    selec = selec + 1;
        }//Fin while principal

        selec = selec * 0;
    tam = tam * 0;
    ship2 = ship2 * 0;
    ship3 = ship3 * 0;
    ship4 = ship4 * 0;

    System.out.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");

    System.out.println("Bien! Que comience la batalla!!!");

    while ((atinar1 != 11) && (atinar2 != 11))      {
        if (turno % 2 == 0)     {
    System.out.println("Es el turno de " + usu1 + ". Elije dónde vas a atacar: ");
    System.out.print("Escoge primero el valor de la fila: ");
        fila = shinxlector.readLine();

        if (turno % 2 == 0 && fila.equalsIgnoreCase("Exit"))   {
                    System.out.println("Parece que " + usu1 + " a decidido rendirce.");
                    System.out.println("El ganador ese caso es " + usu2 + "!!!");
                    lost = lost + 1;
                    break;
                }

        System.out.println();
        /*Hacerlo a tu manera*/while (fila.compareTo("I") > 0 || fila.compareTo("A") < 0)  {
            System.out.print("Error. La letra debe estar dentro del rango de las filas, intenta otra vez: ");
            fila = shinxlector.readLine();
            if (turno % 2 == 0 && fila.equalsIgnoreCase("Exit"))   {
                    System.out.println("Parece que " + usu1 + " a decidido rendirse.");
                    System.out.println("El ganador en ese caso es " + usu2 + "!!!");
                    lost = lost + 1;
                    break;
                }
        }
            System.out.println("Ahora, escoge el valor de la columna: ");
            columna = shinxlector.readLine();
            if (turno % 2 == 0 && columna.equalsIgnoreCase("Exit"))   {
                    System.out.println("Parece que " + usu1 + " a decidido rendirse.");
                    System.out.println("El ganador ese caso es " + usu2 + "!!!");
                    lost = lost + 1;
                    break;
                }

            /*Hacerlo a tu manera*/while (Integer.parseInt(columna) > 9 || Integer.parseInt(columna) < 1)  {
                System.out.println("Error. La cifra ingresada no concuerda con los valores de las columnas. Por favo ingresa de nuevo un valor: ");
                columna = shinxlector.readLine();
                if (turno % 2 == 0 && columna.equalsIgnoreCase("Exit"))   {
                    System.out.println("Parece que " + usu1 + " a decidido rendirse.");
                    System.out.println("El ganador ese caso es " + usu2 + "!!!");
                    lost = lost + 1;
                    break;
                }
            }
            ataque = fila + columna;
            
            while (gift1.contains(ataque) || Integer.parseInt(columna) > 9 || Integer.parseInt(columna) < 1 || fila.compareTo("I") > 0 || fila.compareTo("A") < 0)    {
                System.out.println("Coordenada repetida. Ingresa una nueva");
                System.out.println("Ingrese un nuevo valor para la fila: ");
                fila = shinxlector.readLine();
                System.out.println("Ingrese un nuevo valor para la columna: ");
                columna = shinxlector.readLine();
                ataque = fila + columna;
            }
            gift1.add(ataque);
            
        }   else if (turno % 2 == 1)  {
            System.out.println("Es el turno de " + usu2 + ". Elije dónde vas a atacar: ");
            System.out.print("Escoge primero el valor de la fila: ");
                fila = shinxlector.readLine();

                if (turno % 2 == 1 && fila.equalsIgnoreCase("Exit"))   {
                            System.out.println("Parece que " + usu2 + " a decidido rendirse.");
                            System.out.println("El ganador ese caso es " + usu1 + "!!!");
                            lost = lost + 2;
                            break;
                        }

                System.out.println();
                /*Hacerlo a tu manera*/while (fila.compareTo("I") > 0 || fila.compareTo("A") < 0)  {
                    System.out.print("Error. La letra debe estar dentro del rango de las filas, intenta otra vez: ");
                    fila = shinxlector.readLine();
                    if (turno % 2 == 1 && fila.equalsIgnoreCase("Exit"))   {
                            System.out.println("Parece que " + usu2 + " a decidido rendirse.");
                            System.out.println("El ganador en ese caso es " + usu1 + "!!!");
                            lost = lost + 2;
                            break;
                        }
                }
                    System.out.println("Ahora, escoge el valor de la columna: ");
                    columna = shinxlector.readLine();
                    if (turno % 2 == 1 && columna.equalsIgnoreCase("Exit"))   {
                            System.out.println("Parece que " + usu2 + " a decidido rendirse.");
                            System.out.println("El ganador ese caso es " + usu1 + "!!!");
                            lost = lost + 2;
                            break;
                        }

                    /*Hacerlo a tu manera*/while (Integer.parseInt(columna) > 9 || Integer.parseInt(columna) < 1)  {
                        System.out.println("Error. La cifra ingresada no concuerda con los valores de las columnas. Por favo ingresa de nuevo un valor: ");
                        columna = shinxlector.readLine();
                        if (turno % 2 == 1 && columna.equalsIgnoreCase("Exit"))   {
                            System.out.println("Parece que " + usu2 + " a decidido rendirse.");
                            System.out.println("El ganador ese caso es " + usu1 + "!!!");
                            lost = lost + 2;
                            break;
                        }
                    }
                    ataque = fila + columna;
                    
                    while (gift2.contains(ataque) || Integer.parseInt(columna) > 9 || Integer.parseInt(columna) < 1 || fila.compareTo("I") > 0 || fila.compareTo("A") < 0)    {
                        System.out.println("Error. Coordenada repetida, ingresa una nueva.");
                        System.out.println("Ingrese un nuevo valor para la fila: ");
                        fila = shinxlector.readLine();
                        System.out.println("Ingrese un nuevo valor para la columna: ");
                        columna = shinxlector.readLine();
                        ataque = fila + columna;
                    }
                    gift2.add(ataque);
            }
            String [][] attackmat = pancham.battack (turno, fila, columna, mat2, mat4);

            if (turno % 2 == 0)     {
                for (int f = 0; f < 10; f++)    {
                    for (int c = 0; c < 10; c++)    {
                        if (attackmat [f][c].equals(" X "))     {
                            mat1 [f][c] = " X ";
                            atinar1++;
                        }   else if (attackmat [f][c].equals(" 0 "))    {
                            mat1 [f][c] = " 0 ";
                        }
                    }
                }
                for (int f = 0; f < 10; f++)    {
                    for (int c = 0; c < 10; c++)    {
                        System.out.print(mat1[f][c]);
                    }
                    System.out.print("   ");
                    for (int c = 0; c < 10; c++)    {
                        System.out.print(mat2[f][c]);
                    }
                    System.out.println();
                }   
            }   else if (turno % 2 == 1) {
                for (int f = 0; f < 10; f++)    {
                    for (int c = 0; c < 10; c++)    {
                        if (attackmat [f][c].equals(" X "))     {
                            mat3 [f][c] = " X ";
                            atinar2++;
                        }   else if (attackmat [f][c].equals(" 0 "))    {
                            mat3 [f][c] = " 0 ";
                        }
                    }
                }

                for (int f = 0; f < 10; f++)    {
                    for (int c = 0; c < 10; c++)    {
                        System.out.print(mat3[f][c]);
                }
                System.out.print("   ");
                for (int c = 0; c < 10; c++)    {
                    System.out.print(mat4[f][c]);
                }
                System.out.println();
            }   
        }
            System.out.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
            turno = turno + 1;
            }

        System.out.println("Partida terminada. Es momento de ver un pequeño resumen de la partida: ");

        if (atinar1 == 11 || lost == 2)   {
            System.out.println(usu1 + " a sido el ganador de esta partida. GG EZ!!!");
            System.out.println("La partida duró un total de " + turno + " turnos.");
            System.out.println("Este es el resumen de " + usu1 + ": ");
            System.out.println(resul1[0] + "\n" + resul1[1] + "\n" + resul1[2] + "\n" + resul1[3]);
            System.out.println("Este es el resumen de " + usu2 + ": ");
            System.out.println(resul2[0] + "\n" + resul2[1] + "\n" + resul2[2] + "\n" + resul2[3]);
        }   else if (atinar2 == 11 || lost == 1)     {
            System.out.println(usu2 + " a sido el ganador de esta partida. GG EZ!!!");
            System.out.println("La partida duró un total de " + turno + " turnos.");
            System.out.println("Este es el resumen de " + usu2 + ": ");
            System.out.println(resul2[0] + "\n" + resul2[1] + "\n" + resul2[2] + "\n" + resul2[3]);
            System.out.println("Este es el resumen de " + usu1 + ": ");
            System.out.println(resul1[0] + "\n" + resul1[1] + "\n" + resul1[2] + "\n" + resul1[3]);
        }

    }//Fin Public
}//Fin Main
public class Barcos     {

    public String [][] barcos (int tam, String ori, String fila, String columna, String [] vec1, String [] vec2, String [][] mat2, String [][] mat4)    {

        String [][] ship = new String [10][10];
        int [] filas = new int [vec1.length];
        int [] columnas = new int [vec2.length];
        int fi = 0;
        int num = 0;

       if (ori.equalsIgnoreCase("V"))   {
        for (int x = 0; x < vec2.length; x++)  {
            char letra = vec2 [x].charAt(0);
            int caracter = letra - 'A' + 1;
            columnas [x] = caracter;

            num = Integer.parseInt(columna);
        }
       }    else if (ori.equalsIgnoreCase("H"))   {

            char let = fila.charAt(0);
            fi = let - 'A' + 1;

        for (int y = 0; y < vec1.length; y++)   {
            filas [y] = Integer.parseInt(vec1 [y]);
            }
        }

        for (int f = 0; f < 10; f++)  {
                    for (int c = 0; c < 10; c++)  {
                        ship [f][c] = mat2 [f][c];
                        ship [f][c] = mat4 [f][c];
                    }
                }
        for (int f = 0; f < 10; f++)  {
                    for (int c = 0; c < 10; c++)  {
                        boolean coincide = false;

        if (ori.equalsIgnoreCase("H"))   {

                for (int i = 0; i < filas.length; i++) {
                    if (f == fi && c == filas [i]) {
                        coincide = true;
                            break; 
                    }
                }
                if (coincide) {
                    ship[f][c] = " O ";
                    } /*else {
                    ship[f][c] = " ~ ";*/
            }   else if (ori.equalsIgnoreCase("V"))  {

                for (int i = 0; i < columnas.length; i++) {
                    if (f == columnas [i] && c == num ) {
                        coincide = true;
                            break; 
                    }
                }
                if (coincide) {
                ship[f][c] = " O ";
                } /*else {
                ship[f][c] = " ~ ";*/
            }
            
        }
        }
        return ship;
    }//Fin barcos
}//Fin Public
public class Attackboard {
    public String [][] battack (int turno, String fila, String columna, String [][] mat2, String [][] mat4)     {

        String [][] att = new String [10][10];
        int contN = 1;  // cont = contador, N = Numero
        char contL = 'A';   // cont = contador, L = Letra
        int filas = 0;
        int columnas = 0;

       
        for (int x = 0; x < 1; x++)   {
            char letra = fila.charAt(0);
            int caracter = letra - 'A' + 1;
            filas = caracter;
        }

        for (int y = 0; y < 1; y++){
            columnas = Integer.parseInt(columna);
        }

        // Inicializar todas las posiciones con espacios en blanco
            for (int f = 0; f < 10; f++) {
                for (int c = 0; c < 10; c++) {

                    if (f == 0 && c == 0) {
                        att[f][c] = " / ";

                    }   else if (f == 0 && c >= 0 && c < 10)  {
                        att[f][c] = " " + Integer.toString(contN) + " ";
                        contN = contN + 1;

                    }   else if (f >= 0 && f < 10 && c == 0)  {
                        att[f][c] = " " + Character.toString(contL) + " ";
                        contL++;
                    
                    }   else {
                        if (turno % 2 == 0) {
                            if (f == filas && c == columnas) {
                                if (mat4[f][c].equals(" O ")) {
                                    att[f][c] = " X ";
                                } else {
                                    att[f][c] = " 0 ";
                                }
                            } else {
                                att[f][c] = " ~ ";
                            }
                        } else if (turno % 2 == 1) {
                            if (f == filas && c == columnas) {
                                if (mat2[f][c].equals(" O ")) {
                                    att[f][c] = " X "; // Acierto
                                } else {
                                    att[f][c] = " 0 "; // Fallo
                                }
                            } else {
                                att[f][c] = " ~ ";
                            }
                        }
                    }
                }
            }
        return att;
    }
}
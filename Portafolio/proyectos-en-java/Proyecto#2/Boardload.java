public class Boardload  {

    public String [][] bload () {

        int contN = 1;  // cont = contador, N = Numero
        char contL = 'A';   // cont = contador, L = Letra
        String [][] mat = new String [10][10];  //mat = Matriz

            for (int f = 0; f < 10; f++)    {
                for (int c = 0; c < 10; c++)    {
                    if (f == 0 && c == 0)   {
                        mat [f][c] = "  ";
                    }   else if (f == 0 && c > 0 && c < 10)  {
                        mat [f][c] = " " + Integer.toString(contN) + " ";
                        contN++;
                    }   else if (f > 0 && f < 10 && c == 0) {
                        mat [f][c] = " " + Character.toString(contL);
                        contL++;
                    }   else {
                        mat [f][c] = " ~ ";
                    }
                }//Fin Columna
            }//Fin Fila

            contN = (contN * 0) + 1;
            contL = 'A';

        return mat;

    }//Fin bload
}//Fin Public
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class Main {

    public static ArrayList<ArrayList<Integer>> leerArchivo(String path) {
        
        ArrayList<ArrayList<Integer>> ret = new ArrayList<>();
        
        try {
            File archivo = new File(path);
            Scanner scanner = new Scanner(archivo);
            while (scanner.hasNextLine()) {
                String linea = scanner.nextLine();
                String[] inputs = linea.split(" ");
                ArrayList<Integer> intInputs = new ArrayList<>();
                for(String string: inputs) {
                    intInputs.add( Integer.parseInt(string) );
                }
                ret.add(intInputs);
            } scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("No se encontró el archivo, por favor revisa el path asignado.");
            e.printStackTrace();
        }
        return ret;
    }

    public static void darSolucion(ArrayList<ArrayList<Integer>> casos) {
        int numCasos = casos.get(0).get(0);
        System.out.println(numCasos);

        for(int i = 1; i < casos.size(); i++) {
            
            if (i >= casos.size()) {
                break;
            }

            ArrayList<ArrayList<Integer>> caso = new ArrayList<>();
            int N = casos.get(i).get(0);
            int M = casos.get(i).get(1);
            
            System.out.println(casos.get(i));
            i += 1;

            while (casos.get(i).size() == 3) {
                caso.add(casos.get(i));
                if (i+1 < casos.size() && casos.get(i+1).size() != 2) {
                    i += 1;
                } else {
                    break;
                }
            }

            Solution solve = new Solution(N, M, caso);
            
        }
    }

    public static void main(String[] args) {
        System.out.println("=== CASO 2 - j.torres16 / Jaime Torres ===");
        try {
            ArrayList<ArrayList<Integer>> casos = leerArchivo(args[0]);
            darSolucion(casos);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Parece no haberse indicado un archivo en el comando, ingresar manualmente? (y/n)");
            Scanner scan = new Scanner(System.in);
            String input = scan.nextLine();
            
            if (input.equals("y")) {
                System.out.println("Por favor, digita la dirección del archivo de prueba.");
                input = scan.nextLine();
                ArrayList<ArrayList<Integer>> casos = leerArchivo(input);
                darSolucion(casos);
                scan.close();
            } else {
                scan.close();
            }
        }
    }
}
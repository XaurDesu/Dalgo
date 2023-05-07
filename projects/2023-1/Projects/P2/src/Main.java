import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.HashMap;
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
            
            i += 1;

            while (casos.get(i).size() == 3) {
                caso.add(casos.get(i));
                if (i+1 < casos.size() && casos.get(i+1).size() != 2) {
                    i += 1;
                } else {
                    break;
                }
            }

            HashMap<Integer, ArrayList<ArrayList<Integer>>> input = darAdjList(caso);
            System.out.println(input);
        }
    }

    public static HashMap<Integer, ArrayList<ArrayList<Integer>>> darAdjList(ArrayList<ArrayList<Integer>> caso) {
        //hacer lista de adyacencia
        HashMap<Integer, ArrayList<ArrayList<Integer>>> adjList = new HashMap<Integer, ArrayList<ArrayList<Integer>>>(); 

        for (ArrayList<Integer> conexion: caso) {
            if (!adjList.containsKey(conexion.get(0))) {
                ArrayList<ArrayList<Integer>> connect = new ArrayList<>(); 
                connect.add(new ArrayList<>());
                connect.get(0).add(conexion.get(1));
                connect.get(0).add(conexion.get(2));
                adjList.put(conexion.get(0),connect);
            } else {
                ArrayList<Integer> connect = new ArrayList<>(); 
                connect.add(conexion.get(1));
                connect.add(conexion.get(2));

                adjList.get(conexion.get(0)).add(connect);
            }
        }

        return adjList;
    }

    public static void main(String[] args) {
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
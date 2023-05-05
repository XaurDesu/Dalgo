import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class Main {

    public static ArrayList<Object> leerArchivo(String path) {
        
        ArrayList<Object> ret = new ArrayList<>(null);
        
        try {
            File archivo = new File(path);
            Scanner scanner = new Scanner(archivo);
            while (scanner.hasNextLine()) {
                String linea = scanner.nextLine();
                Object[] inputs = linea.split(" ");
                for(Object string: inputs) {
                    string = (int)string;
                }
                ret.add(inputs);
            } scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("No se encontró el archivo, por favor revisa el path asignado.");
            e.printStackTrace();
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
        try {
            ArrayList<Object> casos = leerArchivo(args[0]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Parece no haberse indicado un archivo en el comando, ingresar manualmente? (y/n)");
            
        }
    }
}
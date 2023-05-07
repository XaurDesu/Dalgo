import java.util.ArrayList;

public class Solution {

    int N;
    int M;
    ArrayList<ArrayList<Integer>> caso;
    
    public void problemSolution() {
        int N = this.N;
        int M = this.M;
        ArrayList<ArrayList<Integer>> caso = this.caso;

        for (ArrayList<Integer> conexion: caso) {
            int origin = conexion.get(0);
            int destination = conexion.get(1);
            int type = conexion.get(2);
        }
    }

    public Solution(int N, int M, ArrayList<ArrayList<Integer>> caso) {
        this.N = N;
        this.M = M;
        this.caso = caso;
    }
}

import java.net.*;
import java.io.*;
import java.util.*;


public class serverJ {

    public static void main(String[] args) {
        int PORT = 1234;
        System.out.println("Waiting for a player");
        try {
            ServerSocket server = new ServerSocket(PORT); // create the server once
            while (true) {
                Socket s = server.accept(); // wait for a connection
                s.setReuseAddress(true);
                System.out.println("Established connection: NEW GAME");
                BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
                PrintWriter pw = new PrintWriter(s.getOutputStream());
                String level = in.readLine();
                int dif = Integer.parseInt(level);
                String palabra = getPalabra(dif);
                
                System.out.println("Dificultad seleccionada: "+ level);
                pw.println(palabra);
                pw.flush();
                
                BufferedReader fin = new BufferedReader(new InputStreamReader(s.getInputStream()));
                String ffin = fin.readLine();
                if (ffin.equals("VICTORIA"))
                    System.out.println("EL JUGADOR HA GANADO!!");
                else if(ffin.equals("DERROTA"))
                    System.out.println("EL JUGADOR HA PERDIDO!!");
                
                String sscore = fin.readLine();
                int score = Integer.parseInt(sscore);
                System.out.println("La puntuación es:" + sscore);
                
                pw.close();
                in.close();
                fin.close();
                //scr.close();
                s.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String getPalabra(int level){
        String palabra;
        Random r = new Random();
        int random = r.nextInt(8)+1;
        ArrayList<String> easy = new ArrayList<String>();
        ArrayList<String> medium = new ArrayList<String>();
        ArrayList<String> hard = new ArrayList<String>();
        easy.add("caballo");
        easy.add("gallina");
        easy.add("celular");
        easy.add("tablero");
        easy.add("libreta");
        easy.add("mochila");
        easy.add("sombrilla");
        easy.add("lapicero");
        easy.add("colores");
        easy.add("bolillo");
        medium.add("calculadora");
        medium.add("computadora");
        medium.add("xochimilco");
        medium.add("estructura");
        medium.add("aplicaciones");
        medium.add("videollamada");
        medium.add("sacapuntas");
        medium.add("entrenamiento");
        medium.add("popularidad");
        medium.add("tendencia");
        hard.add("unapalabradificil");
        hard.add("esdificilponerpalabras");
        hard.add("givemesomething");
        hard.add("itisnotmuch");
        hard.add("thisisalmostready");
        hard.add("yamatenmeplos");
        hard.add("pepepecaspicapapas");
        hard.add("odioprogramarenjava");
        hard.add("cuantocuestas");
        hard.add("estaesunapalabradeprueba");

        if(level == 1)
            palabra = easy.get(random);
        else if( level == 2)
            palabra = medium.get(random);
        else
            palabra = hard.get(random);

        return palabra;
    }
}
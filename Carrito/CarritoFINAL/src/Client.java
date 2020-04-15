import java.util.*;
import java.net.*;
import java.io.*;
import javax.swing.JOptionPane;

public class Client {
    static ProductList p;
    String nombre =  JOptionPane.showInputDialog(null, "Escribe tu nombre");
    static int actualizar = 0;
    static DatagramSocket cl;
    static DatagramPacket peticion;
    public void rcvList(){
        try{
            //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Escribe tu nombre: ");
            
            byte[] b = nombre.getBytes();
            String host = "127.0.0.1";
            int pto = 1234;
            cl = new DatagramSocket();
            InetAddress dst = null;
            try{
                    dst = InetAddress.getByName(host);
            }catch(UnknownHostException u){
                    System.err.println("La direccion no es valida...");
                    System.exit(1);
            }
            peticion = new DatagramPacket(b, b.length, dst, pto);
            cl.send(peticion);
            System.out.println("\n Esperando respuesta del servidor...");
            byte[] recvBuf = new byte[65500];
            DatagramPacket pkt = new DatagramPacket(recvBuf, recvBuf.length);
            cl.receive(pkt);
            ByteArrayInputStream bais = new ByteArrayInputStream(recvBuf);
            ObjectInputStream ois = new ObjectInputStream(new BufferedInputStream(bais));
            p = (ProductList)ois.readObject(); 
            System.out.println("Conexion con el servidor establecida...\n");
            System.out.println("-----BIENVENIDO: " + nombre + "-----\n");
            System.out.println("\nLISTA DE PRODUCTOS:   ");
            for (Producto prod : p.ListaProductos) {
                prod.verDatos(prod);
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public void updateList(){
        try{
            ByteArrayOutputStream baos = new ByteArrayOutputStream(65500);
            ObjectOutputStream oos = new ObjectOutputStream(new BufferedOutputStream(baos));
            oos.flush();
            oos.writeObject(p);
            oos.flush();
            byte[] sendBuf = baos.toByteArray();
            DatagramPacket respuesta = new DatagramPacket(sendBuf, sendBuf.length, peticion.getAddress(), peticion.getPort());
            cl.send(respuesta);
        }
       catch(Exception e){
           e.printStackTrace();
       }
    }
        
   
}
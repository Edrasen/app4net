import java.net.*;
import java.util.*;
import java.io.*;

public class Server {
    public static void main(String[] args) {
        try
        {   
            ProductList p = new ProductList();
            Producto p1 = new Producto(1234, "Sabritas", "Frituras", 12, 50, "D:\\ESCOM\\REDES_2\\CarritoFinal\\src\\test\\sabritas.png");
            Producto p2 = new Producto(5648, "Danonino", "Danone", 4.50, 25, "D:\\ESCOM\\REDES_2\\CarritoFinal\\src\\test\\danonino.png");
            Producto p3 = new Producto(245, "Chetos", "Frituras", 10, 33, "D:\\ESCOM\\REDES_2\\CarritoFinal\\src\\test\\chetos.png");
            p.ListaProductos.add(p1);
            p.ListaProductos.add(p2);
            p.ListaProductos.add(p3);
            int pto = 1234;
            DatagramSocket s = new DatagramSocket(pto);
            InetAddress dst = null;
            s.setReuseAddress(true);
            System.out.println("Servidor iniciado, esperando mensaje...");
            for(;;){
                byte[] recvBuf = new byte[65500];
                DatagramPacket peticion = new DatagramPacket(recvBuf, recvBuf.length);
                s.receive(peticion);
                String nombre = new String(peticion.getData(),0,peticion.getLength());
                System.out.println("Nuevo cliente de nombre:  " + nombre + "  desde   " + peticion.getAddress() + ":" + peticion.getPort());
                ByteArrayOutputStream baos = new ByteArrayOutputStream(65500);
                ObjectOutputStream oos = new ObjectOutputStream(new BufferedOutputStream(baos));
                oos.flush();
                oos.writeObject(p);
                oos.flush();
                byte[] sendBuf = baos.toByteArray();
                DatagramPacket respuesta = new DatagramPacket(sendBuf, sendBuf.length, peticion.getAddress(), peticion.getPort());
                s.send(respuesta);
                System.out.println("Lista de productos enviada");
                
            DatagramPacket pkt = new DatagramPacket(recvBuf, recvBuf.length);
            s.receive(pkt);
            ByteArrayInputStream bais2 = new ByteArrayInputStream(recvBuf);
            ObjectInputStream ois2 = new ObjectInputStream(new BufferedInputStream(bais2));
            p = (ProductList)ois2.readObject();             
            System.out.println("\n\n----------LISTA DE PRODUCTOS ACTUALIZADA:----------\n\n");
            for (Producto prod : p.ListaProductos) {
                prod.verDatos(prod);
            }
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}
import java.util.*;
import java.io.Serializable;

public class ProductList implements Serializable{

    ArrayList<Producto> ListaProductos = new ArrayList<Producto>();

    public void addProduct(Producto p){
        ListaProductos.add(p);
    }

    public void removeProduct(Producto p){
        for (Producto producto : ListaProductos) {
            if(p.id == producto.id)
                producto.existencias = producto.existencias - 1;
        }
        
    }
}

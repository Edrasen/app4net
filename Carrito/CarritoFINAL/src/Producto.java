import java.io.Serializable;


public class Producto implements Serializable{
    int id;
    String nombre;
    String categoria;
    Double precio;
    int promocion;
    int existencias;
    String img_src;
    
    public Producto(){
    
    }
    
    public String getNombre() {
        return nombre;
    }

    public String getCategoria() {
        return categoria;
    }

    public Double getPrecio() {
        return precio;
    }

    public int getExistencias() {
        return existencias;
    }

    public int getId() {
        return id;
    }

    public int getPromocion() {
        return promocion;
    }

    public String getImg_src() {
        return img_src;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public void setPrecio(Double precio) {
        this.precio = precio;
    }

    public void setPromocion(int promocion) {
        this.promocion = promocion;
    }

    public void setExistencias(int existencias) {
        this.existencias = existencias;
    }

    public void setImg_src(String img_src) {
        this.img_src = img_src;
    }
    
    
    
    public Producto(int id, String nombre, String categoria, double precio, int existencias, String imgsrc){
        this.id = id;
        this.nombre = nombre;
        this.categoria = categoria;
        this.precio = precio;
        this.existencias = existencias;
        this.img_src  = imgsrc;
    }
    public void verDatos(Producto p){
        System.out.println("\nINFORMACION DEL PRODUCTO");
        System.out.println("Id: " + getId());
        System.out.println("Nombre: " + getNombre());
        System.out.println("Categoria: " + getCategoria());
        System.out.println("Precio: " + getPrecio());
        System.out.println("Existencias: " + getExistencias());
        System.out.println("Descuento: " + getPromocion());
    }
}

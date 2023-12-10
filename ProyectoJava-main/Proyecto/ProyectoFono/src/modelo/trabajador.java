/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

/**
 *
 * @author miguel pereira
 */
public class trabajador extends persona {
    
    private String usuario,password,correo,rol;

    public trabajador() {
    }

    public trabajador(String usuario, String password, String correo, String rol, int rut, String dv, String pnombre, String snombre, String apaterno, String amaterno) {
        super(rut, dv, pnombre, snombre, apaterno, amaterno);
        this.usuario = usuario;
        this.password = password;
        this.correo = correo;
        this.rol = rol;
    }

    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getRol() {
        return rol;
    }

    public void setRol(String rol) {
        this.rol = rol;
    }
    
    
   
}

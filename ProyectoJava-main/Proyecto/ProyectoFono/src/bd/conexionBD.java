/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author miguel pereira
 */
public class conexionBD {
    public Connection obtenerConexion(){
        Connection conexion=null;
        String url,user,password;        
        //hago la inicialización de mis variables
        url="jdbc:mysql://localhost:3306/fono";//mi base de datos
        user="root";
        password="";        
        try
        {            
            conexion= DriverManager.getConnection(url,user,password);
            System.out.println("Conexión Exitosa");
        }catch(SQLException e){
            System.out.println("Error de conexion BD: "+e.getMessage());
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }
        return conexion;
    }
}

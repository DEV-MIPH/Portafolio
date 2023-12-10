/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controlador;
import bd.conexionBD;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import modelo.paciente;
import modelo.trabajador;
/**
 *
 * @author miguel pereira
 */

public class conexionUsuario {
    PreparedStatement ps = null;
    String query;
    ResultSet rs = null;
    public boolean inicioSesion(String user ,String pass){
        boolean resultado = false;
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="select * from trabajador where usuario = ? ";
            ps = cnx.prepareStatement(query);
            ps.setString(1, user);
            rs = ps.executeQuery();
        
        try {
            if(rs.next()){
                if(pass.equals(rs.getString(8))){
                    resultado = true;
                    
                }
            
            }
            
        
        ps.close();
        rs.close();
        cnx.close();
        
        }catch (SQLException ex) {
            System.out.println("Error de datos: "+ ex.getMessage());
            
        }
        
        } catch (SQLException ex) {
            System.out.println("Error de datos: "+ ex.getMessage());
        }
        return resultado;
    }
    public boolean registrarTrabajador(trabajador newTrabajador){
        
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="INSERT INTO trabajador (rut, dv_persona, pnombre, snombre, apaterno, amaterno, usuario, password, correo, rol) "
                    + "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
            ps = cnx.prepareStatement(query);
            ps.setInt(1,newTrabajador.getRut());
            ps.setString(2, newTrabajador.getDv());
            ps.setString(3, newTrabajador.getPnombre());
            ps.setString(4, newTrabajador.getSnombre());
            ps.setString(5,newTrabajador.getApaterno());
            ps.setString(6, newTrabajador.getAmaterno());
            ps.setString(7, newTrabajador.getUsuario());
            ps.setString(8, newTrabajador.getPassword());
            ps.setString(9, newTrabajador.getCorreo());
            ps.setString(10,newTrabajador.getRol());
            ps.executeUpdate();
            
            ps.close();
            
            cnx.close();
            
            return true;
            
        }catch(SQLException ex){
            System.out.println("Error SQL al agregar trabajador: "+ex.getMessage());
            return false;
        }catch(Exception ex){
            System.out.println("Error al agregar trabajador: "+ex.getMessage());
            return false;
        }
    }
    public boolean registrarPaciente(paciente newPaciente){
        boolean resultado = false;
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="INSERT INTO paciente (rut, dv_persona, pnombre, snombre, apaterno, amaterno) "
                    + "VALUES (?, ?, ?, ?, ?, ?)";
            ps = cnx.prepareStatement(query);
            ps.setInt(1,newPaciente.getRut());
            ps.setString(2, newPaciente.getDv());
            ps.setString(3, newPaciente.getPnombre());
            ps.setString(4, newPaciente.getSnombre());
            ps.setString(5,newPaciente.getApaterno());
            ps.setString(6, newPaciente.getAmaterno());
            
            ps.executeUpdate();
            
            ps.close();
            cnx.close();
            
            return true;
            
        }catch(SQLException ex){
            System.out.println("Error SQL al agregar trabajador: "+ex.getMessage());
            return false;
        }catch(Exception ex){
            System.out.println("Error al agregar trabajador: "+ex.getMessage());
            return false;
        }
    }

    public List<trabajador> TodosLosTrabajadores(){
        List<trabajador> listaTrabajadores = new ArrayList<>();
        String query;
        ResultSet rs = null;
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="select rut, dv_persona, pnombre, snombre, apaterno, amaterno, usuario, password, correo, rol"
                    + " from trabajador order by rol,apaterno ";
            ps = cnx.prepareStatement(query);
            rs = ps.executeQuery();
            while(rs.next()){
                trabajador trabajador = new trabajador();
                trabajador.setRut(rs.getInt("rut"));
                trabajador.setDv(rs.getString("dv_persona"));      
                trabajador.setPnombre(rs.getString("pnombre"));
                trabajador.setSnombre(rs.getString("snombre"));
                trabajador.setApaterno(rs.getString("apaterno"));
                trabajador.setAmaterno(rs.getString("amaterno"));
                trabajador.setUsuario(rs.getString("usuario"));
                trabajador.setPassword(rs.getString("password"));
                trabajador.setCorreo(rs.getString("correo"));
                trabajador.setRol(rs.getString("rol"));
                listaTrabajadores.add(trabajador);
                
            }
            cnx.close();
            ps.close();
            rs.close();
            
        }catch(SQLException ex){
            System.out.println("Error SQL al buscar trabajadores: "+ex.getMessage());
            
        }catch(Exception ex){
            System.out.println("Error al buscar trabajadores: "+ex.getMessage());
            
        }
        return listaTrabajadores;
    }
        public List<trabajador> buscarXtrabajador(int rut){
        List<trabajador> listaTrabajadores = new ArrayList<>();
        String query;
        ResultSet rs = null;
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="select *"
                    + "from trabajador where rut=?";
            ps = cnx.prepareStatement(query);
            ps.setInt(1, rut);
            rs = ps.executeQuery();
            if(rs.next()){
                trabajador trabajador = new trabajador();
                trabajador.setRut(rs.getInt("rut"));
                trabajador.setDv(rs.getString("dv_persona"));      
                trabajador.setPnombre(rs.getString("pnombre"));
                trabajador.setSnombre(rs.getString("snombre"));
                trabajador.setApaterno(rs.getString("apaterno"));
                trabajador.setAmaterno(rs.getString("amaterno"));
                trabajador.setUsuario(rs.getString("usuario"));
                trabajador.setPassword(rs.getString("password"));
                trabajador.setCorreo(rs.getString("correo"));
                trabajador.setRol(rs.getString("rol"));
                listaTrabajadores.add(trabajador);
                
            }
            cnx.close();
            ps.close();
            rs.close();
            
        }catch(SQLException ex){
            System.out.println("Error SQL al buscar trabajador: "+ex.getMessage());
            
        }catch(Exception ex){
            System.out.println("Error al buscar trabajador: "+ex.getMessage());
            
        }
        return listaTrabajadores;
    }
        
    
    public String buscarNombre(String user){
        String nombre = "";
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="select * from trabajador where usuario = ? ";
            ps = cnx.prepareStatement(query);
            ps.setString(1, user);
            rs = ps.executeQuery();
        try {
            if(rs.next()){
                nombre = rs.getString("pnombre");
                }   
        cnx.close();
        ps.close();
        rs.close();
        
        }catch (SQLException ex) {
            System.out.println("Error de datos: "+ ex.getMessage());
            
        }
        } catch (SQLException ex) {
            System.out.println("Error de datos: "+ ex.getMessage());
        }
        return nombre;
        
    }
    public List<paciente> buscarTodosLosPaciente(){
        List<paciente> listaPaciente = new ArrayList<>();
        String query;
        ResultSet rs = null;
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="SELECT *"
                    + "FROM paciente order by apaterno ";
            ps = cnx.prepareStatement(query);
            
            rs = ps.executeQuery();
            while(rs.next()){
                paciente paciente = new paciente();
                paciente.setRut(rs.getInt("rut"));
                paciente.setDv(rs.getString("dv_persona"));
                
                paciente.setPnombre(rs.getString("pnombre"));
                paciente.setSnombre(rs.getString("snombre"));
                paciente.setApaterno(rs.getString("apaterno"));
                paciente.setAmaterno(rs.getString("amaterno"));
                listaPaciente.add(paciente);
                
            }
            cnx.close();
            ps.close();
            rs.close();
            
        }catch(SQLException ex){
            System.out.println("Error SQL al buscar pacientes: "+ex.getMessage());
            
        }catch(Exception ex){
            System.out.println("Error al buscar pacientes: "+ex.getMessage());
            
        }
        return listaPaciente;
    }
    public List<paciente> buscarPorRutPaciente(int rut){
        List<paciente> listaPaciente = new ArrayList<>();
        String query;
        ResultSet rs = null;
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="select *"
                    + "from paciente where rut = ? order by apaterno ";
            ps = cnx.prepareStatement(query);
            ps.setInt(1, rut);
            rs = ps.executeQuery();
            if(rs.next()){
                paciente paciente = new paciente();
                paciente.setRut(rs.getInt("rut"));
                paciente.setDv(rs.getString("dv_persona"));
                paciente.setPnombre(rs.getString("pnombre"));
                paciente.setSnombre(rs.getString("snombre"));
                paciente.setApaterno(rs.getString("apaterno"));
                paciente.setAmaterno(rs.getString("amaterno"));
                listaPaciente.add(paciente);
                
            }
            cnx.close();
            ps.close();
            rs.close();
            
        }catch(SQLException ex){
            System.out.println("Error SQL al buscar paciente: "+ex.getMessage());
            
        }catch(Exception ex){
            System.out.println("Error al buscar paciente: "+ex.getMessage());
            
        }
        return listaPaciente;
    }
    public Boolean eliminarUsuario(int rut){
        
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="DELETE FROM trabajador WHERE rut= ? ";
            ps = cnx.prepareStatement(query);
            ps.setInt(1, rut);
            ps.executeUpdate();
            
            
            cnx.close();
            ps.close();
            return true;
        
        }catch(SQLException ex){
            System.out.println("Error SQL al borrar trabajadores: "+ex.getMessage());
            return false;
        }catch(Exception ex){
            System.out.println("Error al borrar trabajadores: "+ex.getMessage());
            return false;
        }
        
        
    }
    public Boolean eliminarPaciente(int rut){
        
        try{
            conexionBD conn=new conexionBD();
            Connection cnx=conn.obtenerConexion();
            query="DELETE FROM paciente WHERE rut= ? ";
            ps = cnx.prepareStatement(query);
            ps.setInt(1, rut);
            ps.executeUpdate();
            
            
            cnx.close();
            ps.close();
            return true;
        
        }catch(SQLException ex){
            System.out.println("Error SQL al borrar paciente: "+ex.getMessage());
            return false;
        }catch(Exception ex){
            System.out.println("Error al borrar paciente: "+ex.getMessage());
            return false;
        }
        
        
    }
    
   
    
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

/**
 *
 * @author miguel pereira
 */
public class paciente extends persona{
    private String id_paciente;

    public paciente() {
    }


    public paciente(String id_paciente, int rut, String dv, String pnombre, String snombre, String apaterno, String amaterno) {
        super(rut, dv, pnombre, snombre, apaterno, amaterno);
        this.id_paciente = id_paciente;
    }

    public String getId_paciente() {
        return id_paciente;
    }

    public void setId_paciente(String id_paciente) {
        this.id_paciente = id_paciente;
    }
   
}

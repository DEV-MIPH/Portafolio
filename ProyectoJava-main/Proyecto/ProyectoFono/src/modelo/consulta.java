/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

import java.util.Date;

/**
 *
 * @author miguel pereira
 */
public class consulta {
    private String observacion;
    private int rut_trabajador,rut_paciente;
    private Date fecha_consulta;

    public consulta() {
    }

    public consulta(String observacion, int rut_trabajador, int rut_paciente, Date fecha_consulta) {
        this.observacion = observacion;
        this.rut_trabajador = rut_trabajador;
        this.rut_paciente = rut_paciente;
        this.fecha_consulta = fecha_consulta;
    }

    public String getObservacion() {
        return observacion;
    }

    public void setObservacion(String observacion) {
        this.observacion = observacion;
    }

    public int getRut_trabajador() {
        return rut_trabajador;
    }

    public void setRut_trabajador(int rut_trabajador) {
        this.rut_trabajador = rut_trabajador;
    }

    public int getRut_paciente() {
        return rut_paciente;
    }

    public void setRut_paciente(int rut_paciente) {
        this.rut_paciente = rut_paciente;
    }

    public Date getFecha_consulta() {
        return fecha_consulta;
    }

    public void setFecha_consulta(Date fecha_consulta) {
        this.fecha_consulta = fecha_consulta;
    }
          
    
}

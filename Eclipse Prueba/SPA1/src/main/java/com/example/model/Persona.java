package com.example.model;

import java.util.Date;
import java.io.Serializable;
import javax.persistence.*;

@Entity
public class Persona {
	@Id
    @Column
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column
    private String nombre;
    @Column
    private String apellidos;
    @Column
    private int TipoDoc;
    @Column
    private String Documento;
    @Column
    @Temporal(javax.persistence.TemporalType.DATE)
    private Date FechaNac;
    @Column
    private String Correo;
    @Column
    private int LugarRes;
    @Column
    private int telefono;
    @Column
    private String Usuario;
    @Column
    private String password;
    
    
	public Persona(Long id, String nombre, String apellidos, int tipoDoc, String documento, Date fechaNac, String correo,
			int lugarRes, int telefono, String usuario, String password) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.apellidos = apellidos;
		TipoDoc = tipoDoc;
		Documento = documento;
		FechaNac = fechaNac;
		Correo = correo;
		LugarRes = lugarRes;
		this.telefono = telefono;
		Usuario = usuario;
		this.password = password;
	}
	
	public Persona()
	{
		super();
	}
	
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellidos() {
		return apellidos;
	}
	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}
	public int getTipoDoc() {
		return TipoDoc;
	}
	public void setTipoDoc(int tipoDoc) {
		TipoDoc = tipoDoc;
	}
	public String getDocumento() {
		return Documento;
	}
	public void setDocumento(String documento) {
		Documento = documento;
	}
	public Date getFechaNac() {
		return FechaNac;
	}
	public void setFechaNac(Date fechaNac) {
		FechaNac = fechaNac;
	}
	public String getCorreo() {
		return Correo;
	}
	public void setCorreo(String correo) {
		Correo = correo;
	}
	public int getLugarRes() {
		return LugarRes;
	}
	public void setLugarRes(int lugarRes) {
		LugarRes = lugarRes;
	}
	public int getTelefono() {
		return telefono;
	}
	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}
	public String getUsuario() {
		return Usuario;
	}
	public void setUsuario(String usuario) {
		Usuario = usuario;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
    
}

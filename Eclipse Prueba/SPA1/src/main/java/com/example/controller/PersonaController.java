package com.example.controller;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;

import com.example.repository.PersonaRepository;
import com.example.model.Persona;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;

@CrossOrigin(origins ="http://localhost:4200",maxAge=3600)
@RestController
@RequestMapping({"/personas"})
public class PersonaController {
	@Autowired
    private PersonaRepository personaRepository;

    @GetMapping("/employees")
    public List<Persona> getAllEmployees() {
        return personaRepository.findAll();
    }
}

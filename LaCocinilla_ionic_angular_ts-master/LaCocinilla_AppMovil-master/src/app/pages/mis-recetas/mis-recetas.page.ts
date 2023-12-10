import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DbrecetaService } from 'src/app/services/dbreceta.service';



@Component({
  selector: 'app-mis-recetas',
  templateUrl: './mis-recetas.page.html',
  styleUrls: ['./mis-recetas.page.scss'],
})
export class MisRecetasPage implements OnInit {

  nombreReceta = "";
  categoriaReceta = "";
  descripcionReceta = "";
  ingredientesReceta = "";
  preparacionReceta = "";
  favoritoReceta = 0;

  categorias:any[]=[
    {id:1, categoria:"Pastas"},
    {id:2, categoria:"Pizza"},
    {id:3, categoria:"Panaderia"},
    {id:4, categoria:"Ensaladas"},
    {id:5, categoria:"Postres"},
  ] 

  constructor(private dbservice: DbrecetaService, private router: Router) { }
  
  guardar(){
    this.dbservice.addReceta(this.nombreReceta,this.categoriaReceta,this.descripcionReceta,this.ingredientesReceta,this.preparacionReceta, this.favoritoReceta);
    this.dbservice.presentToast("Receta agregada");
    this.router.navigate(['/lobby']);
  }

  limpiar(){
    this.nombreReceta = "";
    this.categoriaReceta = "";
    this.descripcionReceta = "";
    this.ingredientesReceta = "";
    this.preparacionReceta = "";
  }

  customCounterFormatter(inputLength: number, maxLength: number) {
    return `${maxLength - inputLength} maximo de caracteres`;
  }

  ngOnInit(){

  } 

}

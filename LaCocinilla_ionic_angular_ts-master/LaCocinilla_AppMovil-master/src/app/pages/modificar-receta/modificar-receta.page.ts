import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DbrecetaService } from 'src/app/services/dbreceta.service';

@Component({
  selector: 'app-modificar-receta',
  templateUrl: './modificar-receta.page.html',
  styleUrls: ['./modificar-receta.page.scss'],
})
export class ModificarRecetaPage implements OnInit {

  idReceta = "";
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

  constructor( private router: Router, private activatedroute: ActivatedRoute, private dbsevice: DbrecetaService) { 
    this.activatedroute.queryParams.subscribe(param => {
      if (this.router.getCurrentNavigation()?.extras.state) {
        this.idReceta = this.router.getCurrentNavigation()?.extras.state?.["idEnviado"];
        this.nombreReceta = this.router.getCurrentNavigation()?.extras.state?.["nombreEnviado"];
        this.categoriaReceta = this.router.getCurrentNavigation()?.extras.state?.["categoriaEnviado"];
        this.descripcionReceta = this.router.getCurrentNavigation()?.extras.state?.["descripcionEnviado"];
        this.ingredientesReceta = this.router.getCurrentNavigation()?.extras.state?.["ingredientesEnviado"];
        this.preparacionReceta = this.router.getCurrentNavigation()?.extras.state?.["preparacionEnviado"];
        this.favoritoReceta = this.router.getCurrentNavigation()?.extras.state?.["favoritoEnviado"];       
      }
    })
  }

  editar(){
    this.dbsevice.updateReceta(this.idReceta, this.nombreReceta,this.categoriaReceta, this.descripcionReceta, this.ingredientesReceta, this.preparacionReceta, this.favoritoReceta);
    this.dbsevice.presentToast("Receta Actualizada");
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

  ngOnInit() {
  }

}

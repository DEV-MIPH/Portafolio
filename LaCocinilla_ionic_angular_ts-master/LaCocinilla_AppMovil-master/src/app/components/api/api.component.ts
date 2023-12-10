import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ConnectApiService } from '../../services/connect-api.service';

@Component({
  selector: 'app-api',
  templateUrl: './api.component.html',
  styleUrls: ['./api.component.scss'],
})
export class ApiComponent  implements OnInit {

  ///este es el controlador del modal, solo trae una unica receta
  isModalOpen = false;


  ///

nombreReceta: string = '';
recetas: any[] = [];
recetaBuscada: any[]=[] 

setOpen(isOpen: boolean,receta:any) {    
  this.isModalOpen = isOpen;
  this.recetas =  this.connectApiService.recetario(receta.nombre)
  if (isOpen == false && this.recetas.length == 1){
    this.recetas = this.connectApiService.verRecetas();
  }
  
}

  constructor( private activateRoute: ActivatedRoute, private router: Router, private connectApiService: ConnectApiService) { 
   
  }

  async ionViewWillEnter(){
    this.connectApiService.buscarReceta(this.nombreReceta);
    this.recetas = this.connectApiService.verRecetas();
    
  }
  ngOnInit() {
  }
  buscarReceta(){
    this.connectApiService.buscarReceta(this.nombreReceta);
    this.recetas = this.connectApiService.verRecetas();
    console.log(this.recetas)
  }
  
  
}

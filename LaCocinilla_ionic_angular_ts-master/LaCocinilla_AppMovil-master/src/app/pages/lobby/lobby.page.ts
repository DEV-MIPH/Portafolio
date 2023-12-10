import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MisRecetasService } from 'src/app/services/mis-recetas.service';
import { Receta } from 'src/app/class/receta';
import { NavigationExtras } from '@angular/router';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.page.html',
  styleUrls: ['./lobby.page.scss'],
})

export class LobbyPage {

  recetas : Receta[] = [];
  constructor( private router: Router, private activatedRoute: ActivatedRoute, private misRecetasService: MisRecetasService) { 
    this.init();
    this.router.navigate(['/lobby/api']);       
  }

  segmentChanged($event: any){    
    console.log($event);
    let direccion = $event.detail.value;
    
    if (direccion === 'misrecetas'){
      let navigationExtras: NavigationExtras = {
        state: {
          Misrecetas: this.recetas
        }
      };
      this.router.navigate(['/lobby/misrecetas'], navigationExtras);
      console.log("pase por recetas")
    }else{
      this.router.navigate(['/lobby/'+direccion]);
    }
  }

  cerrarSesion(){
    localStorage.removeItem('ingresado')
    this.router.navigate(['/login'])
  }

  async init(){
    this.recetas = this.misRecetasService.retornarRecetas();
    console.log("cargue recetas");
  }
  
}

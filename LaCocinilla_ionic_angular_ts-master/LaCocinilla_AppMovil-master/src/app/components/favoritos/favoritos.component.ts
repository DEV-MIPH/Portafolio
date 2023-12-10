import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { DbrecetaService } from 'src/app/services/dbreceta.service';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';
import { ToastController } from '@ionic/angular';
import { ElasticMailService } from 'src/app/services/elastic-mail.service';

@Component({
  selector: 'app-favoritos',
  templateUrl: './favoritos.component.html',
  styleUrls: ['./favoritos.component.scss'],
})
export class FavoritosComponent  implements OnInit {

  ///este es el controlador del modal, solo trae una unica receta
  isModalOpen = false;  

  RecetaElegida: any 

  recetas: any = [
    {
      nombre: "Nombre de la receta",
      categoria: "Categoria de la receta",
      descripcion: "Descripcion de la receta",
      ingredientes: "Ingredientes de la receta",
      preparacion: "Preparacion de la receta",
      favorito: 0
    }
  ]

  
  
  constructor(private router: Router, private servicioDB: DbrecetaService, private socialSharing: SocialSharing, public toastController: ToastController, private elasticMailService: ElasticMailService) { }

  ngOnInit(){
    this.servicioDB.dbState().subscribe((res: any) => {
      if (res){
        this.servicioDB.fetchRecetas().subscribe((item: any) => {
          this.recetas = item;
        });
      }
    });
  }

  

  
  getItem($event: any){
    const valor = $event.target.value;
    console.log('valor del control' + valor);
  }

  editar(item: any) {
    let navigationextras: NavigationExtras = {
      state : {
        idEnviado : item.id,
        nombreEnviado : item.nombre,
        categoriaEnviado : item.categoria,
        descripcionEnviado : item.descripcion,
        ingredientesEnviado : item.ingredientes,
        preparacionEnviado : item.preparacion,
        favoritoEnviado : item.favorito
      }
    }
    this.router.navigate(['/modificar-receta'],navigationextras);
  }

  eliminar(item: any){
    this.servicioDB.deleteReceta(item.id);
    this.servicioDB.presentToast("Receta eliminada");
  }

  
  setOpen(isOpen: boolean) {    
    this.isModalOpen = isOpen; 
  }

  async recetaSeleccionada(receta:any){
    this.RecetaElegida = receta;
  }
  
  //comados que se tienen que instalar para correr el social-sharing
  //npm i cordova-plugin-x-socialsharing
  //npm i @awesome-cordova-plugins/social-sharing@5.41.0 --legacy-peer-deps
  //npm i @awesome-cordova-plugins/core --legacy-peer-deps
  compartir(item:any){
    let correo = localStorage.getItem('correo');
    this.socialSharing.share("Te han compartido una receta desde 'La Cocinilla'. Una nueva manera para organizar tus recetas. "+ "\n" + "Nombre: " + item.nombre + "\n" + "Categoría: " + item.categoria + "\n" + "Ingredientes: " + item.ingredientes+ "\n" + "Preparación: " + item.preparacion)
      .then((res) => { 
        this.elasticMailService.sendEmail(correo)
        this.presentToast("Receta Compartida de manera exitosa"+ "\n" + "Correo enviado a: " + correo)
        }).catch(() => {          
          this.presentToast("Error al compartir")
          //alert(JSON.stringify(error));
        }) 
      
             
  }
  agregarFavorito(item:any){
    let id = item.id
    let favorito = item.favorito
    this.servicioDB.agregarFavorito(id,favorito)
    this.setOpen(false);
  }

  async presentToast(mensaje: string) {
    const toast = await this.toastController.create({ 
      message: mensaje,
      duration: 3000 
    }); 
    toast.present(); 
  }
}

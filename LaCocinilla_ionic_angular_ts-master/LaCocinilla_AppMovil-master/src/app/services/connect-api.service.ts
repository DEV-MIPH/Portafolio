import { Injectable } from '@angular/core';
import { ToastController } from '@ionic/angular';


@Injectable({
  providedIn: 'root'
})
export class ConnectApiService {

  recetas: any[] = [];
  

  constructor(public toastController:ToastController) { }

  buscarReceta(nombreReceta?: string ){
    let apiUrl = 'https://apirecetas-b014f-default-rtdb.firebaseio.com/recetas/-Nh9T1pYNws5yfg9Okxc.json';
    this.recetas = [];

  
    fetch(apiUrl)
    .then((response) => {
      if (!response.ok){
        throw new Error(`la solicitud no se pudo completar con fallo: ${response.status})`);
      }
      return response.json();
    })
    .then((data) => {
      
      if (data && data.meals){
        
        for (const receta of data.meals) {
          if (!nombreReceta || receta.strMeal.toLowerCase().includes(nombreReceta.toLowerCase())) {
          const ingredientes = [];
          for (let i = 1; i <= 20; i++) {
            const ingrediente = receta[`strIngredient${i}`];
            const medida = receta[`strMeasure${i}`];
            if (ingrediente && ingrediente.trim() !== '') {
              ingredientes.push(`${medida ? medida + ' ' : ''}${ingrediente}`);
            }
          }

          const recetaInfo = {
            id: receta.idMeal,
            nombre: receta.strMeal,
            ingredientes: ingredientes.join(', '),
            preparacion: receta.strInstructions,
            imagen: receta.strMealThumb + '/preview',
            categoria: receta.strCategory,
            procedencia: receta.strArea,
            algo: receta.strIngredient6
          };
      
          this.recetas.push(recetaInfo);
          
          
        }
      }
        if (this.recetas.length > 0){
          console.log('recetas encontradas');
          
        }else{
          
          console.log('no se encontraron recetas');
          this.presentToast('No se encontraron recetas');
        }
      }else{
        console.log('no se encontraron recetas');
        this.presentToast('No se encontraron recetas');
      }
    })
            
    
}
  recetario(nombreReceta: string){
    const receta = this.recetas.filter(receta => receta.nombre === nombreReceta)
    return receta
   
  }
  verRecetas(){
    console.log(this.recetas)
    return this.recetas
    
  }
  async presentToast(msg: string) {
    const toast = await this.toastController.create({
      message: msg,
      duration: 2500,
      position: 'bottom',
    });

    await toast.present();
  }

  

}

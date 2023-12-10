import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Receta } from '../class/receta';
import { ToastController } from '@ionic/angular';

@Injectable({
  providedIn: 'root'
})
export class MisRecetasService {

  recetas: Receta[] = [];
  private _storage: Storage | null = null;

  constructor(private storage : Storage, public toastController: ToastController) {
    this.init();
    
   }

  async init() {
    const storage = await this.storage.create();
    this._storage = storage;
    this.cargarRecetas();
  }
  guardarReceta(receta: Receta){
    
    const existe = this.recetas.find(recetaGuardada => recetaGuardada.nombre === receta.nombre);
    if (existe) {
      this.presentToast('Ya existe una receta con ese nombre');
      return;
    }else{
      this.recetas.unshift(receta);
      
      this._storage?.set('recetas', this.recetas);
      this.presentToast('Receta guardada');
    }
  }
  async cargarRecetas(){
    const misRecetas = await this._storage?.get('recetas') ;
    if (misRecetas){
      this.recetas = misRecetas;
    }
  }
  retornarRecetas(){
    return this.recetas;
  }
  verRecetas(){
    this.cargarRecetas();
    console.log(this.recetas);
    return this.recetas;
  }
  borrarReceta(id: number){
    this.recetas = this.recetas.filter(receta => receta.id !== id);
    this._storage?.set('recetas', this.recetas);
    this.presentToast('Receta eliminada');
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

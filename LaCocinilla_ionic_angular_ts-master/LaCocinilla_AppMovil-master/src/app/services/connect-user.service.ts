import { Injectable } from '@angular/core';
import { ToastController } from '@ionic/angular';
import { Usuario } from '../class/usuario';


@Injectable({
  providedIn: 'root'
})
export class ConnectUserService {

  usuarios: Usuario[] = [];
  id: number=-2;
  constructor(public toastController: ToastController) {}

   async iniciarSesion(email: string, password: string ):Promise<boolean>{
    let api = 'https://apirecetas-b014f-default-rtdb.firebaseio.com/usuarios/-NkBfwhcvF5nVg_-N4H8.json';

    try{
      const response = await fetch(api);
      if (!response.ok){
        throw new Error(`la solicitud no se pudo completar con fallo: ${response.status})`);
      }
      const data = await response.json();
      if (data && Array.isArray(data)){
        for (const usuario of data) {
          if (usuario.username === email.toLowerCase() && usuario.password === password) {
            this.presentToast('top','Bienvenido ' + usuario.nombre);
            return true;
          }
        }
        console.log("Usuario no encontrado");
        this.presentToast('bottom','Usuario no encontrado');
      }
      return false;
    }catch (error){
      console.log(error);
      this.presentToast('bottom','Error al conectar con la BD');
      return false;
    }
   }

  async presentToast(position: 'top' | 'middle' | 'bottom',
                     message: string,
                     duration?:number) {
    const toast = await this.toastController.create({
      message: message,
      duration: duration?duration:2000,
      position: position,
    });
    await toast.present();
  }  
  async modificarPassword(id: number, newPassword:string): Promise<boolean>{
    
    try{
      console.log(id);
      let idBuscada = id-1;
      console.log(idBuscada);
      const api = `https://apirecetas-b014f-default-rtdb.firebaseio.com/usuarios/-NkBfwhcvF5nVg_-N4H8/${idBuscada}.json`;
      console.log(api);
      const response = await fetch(api, {

        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({password:newPassword})
      });

      if (!response.ok){
        console.log("Error en la api: "+response.status);
        throw new Error(`la solicitud no se pudo completar con fallo: ${response.status})`);
      }
      return true;
      

      
    }catch(error){
      console.log(error);
      this.presentToast('bottom','Error al conectar con la BD');
      return false;
    }
  }

  async buscarId(email: string){
    let api = 'https://apirecetas-b014f-default-rtdb.firebaseio.com/usuarios/-NkBfwhcvF5nVg_-N4H8.json';
    this.usuarios = [];
    
    const response = await fetch(api);
    if (!response.ok){
      throw new Error(`la solicitud no se pudo completar con fallo: ${response.status})`);
    }
    const data = await response.json();

    if (data){
      const usuarios:Usuario[] = Object.values(data);
      const usuarioEncontrado = usuarios.find((usuario) => usuario.username === email);
      
      if (usuarioEncontrado){
        console.log(usuarioEncontrado);
        return usuarioEncontrado
      }else{
        console.log("Usuario no encontrado");
        return ;
      }
    }else{
      console.log("Usuario no encontrado");
      return ;
    }
    
          
  }

  async verId(correo: string){
    const usuario = await this.buscarId(correo);
    console.log(usuario);
    return usuario;
  
  }

  
}

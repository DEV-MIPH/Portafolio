import { Component, OnInit } from '@angular/core';
import { ToastController } from '@ionic/angular';
import { ActivatedRoute, Router, NavigationExtras } from '@angular/router';
import { ConnectUserService } from 'src/app/services/connect-user.service';
import { Usuario } from 'src/app/class/usuario';





@Component({
  selector: 'app-forget',
  templateUrl: './forget.page.html',
  styleUrls: ['./forget.page.scss'],
})



export class ForgetPage implements OnInit {
  
  constructor(public toastController: ToastController,private activateRoute: ActivatedRoute, private router: Router, private connectUser: ConnectUserService) {}
  

  ngOnInit() {
  }
  usuario = {
    correo:"",
  }
  usuarioBuscado:any;
  campo:string="";

  async ionViewWillEnter(){
    this.connectUser.verId(this.usuario.correo);
    console.log(this.connectUser.id);
  }
  
  async enviar(){
    console.log(this.usuario.correo);
    if (this.validateModel(this.usuario)==false){
      this.presentToast('bottom','El campo '+this.campo+' no puede estar vacio');
    }
    else{
      this.usuarioBuscado = await this.connectUser.verId(this.usuario.correo);
      console.log(this.usuarioBuscado);
  
      if (this.usuarioBuscado){
      let navigationExtras: NavigationExtras = {
        state: {
          usuario : this.usuarioBuscado
        }
      };
      console.log(this.usuarioBuscado)
      this.router.navigate(["/forget2"],navigationExtras);
      }
      else{
        this.presentToast('bottom','El correo no existe');
      }
    }

    
  }


  
  
  
  validateModel(model:any){
    //se recorre todas las entradas del modelo y le digo que me entregue el Object entries para obtener su nombre de variable (clave=key) y su valor(value)
    for(var[key,value] of Object.entries(model)){
      //hacemos un condicional que si su valor es vacio retorna un false
      if(value==""){//preguntar a la profe si podemos cambiarlo a un minimo de caracteres con la funcion lenght
        this.campo=key;
        return false;
      }
    }
    return true;
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
}

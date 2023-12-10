import {  OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { NavController, ToastController } from '@ionic/angular';
import { ActivatedRoute } from '@angular/router';
import { Component } from '@angular/core';
import { AnimationController } from '@ionic/angular';
import { Animation } from '@ionic/angular';
import { ViewChild } from '@angular/core';
import { IonCard } from '@ionic/angular';
import { ElementRef } from '@angular/core';
import { ConnectUserService } from 'src/app/services/connect-user.service';
import { ElasticMailService } from 'src/app/services/elastic-mail.service';



@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  
  

  /**modelo para el inicio de sesion 
   * tiene 2 variable ambas iniciadas en blanco
   * cada variable es una clave y se le asigna un valor inicial en vacio
  */
  usuario = {
    usuario:"",
    contrasena:""
  }

  ListaDeUsuarios = [
    { usuario: "usuario1", contrasena: "contrasena1" },
    { usuario: "usuario2", contrasena: "contrasena2" },
    { usuario: "usuario3", contrasena: "contrasena3" },
    { usuario: "usuario4", contrasena: "contrasena4" },
    { usuario: "usuario5", contrasena: "contrasena5" },
    { usuario: "usuario6", contrasena: "contrasena6" },
    { usuario: "usuario7", contrasena: "contrasena7" },
    { usuario: "usuario8", contrasena: "contrasena8" },
    { usuario: "usuario9", contrasena: "contrasena9" },
    { usuario: "usuario10", contrasena: "contrasena10" }
  ];

  // variable local donde se almacena el campo faltante
  campo:string="";
  
  //le pasamos al constructor una variable privada con la clase Router y una variable publica con la clase ToastController
  constructor(private activateRoute: ActivatedRoute, private router: Router,public toastController: ToastController,public connectUserService:ConnectUserService,public elasticMailService:ElasticMailService) { 

    localStorage.removeItem('ingresado');

    //hacemos la llamada a los datos recibidos en la ventana de login
    this.activateRoute.queryParams.subscribe(params =>{//aca es donde estamos haciendo la llamada en una funcion de tipo flecha
      if (this.router.getCurrentNavigation()?.extras.state){
        this.ListaDeUsuarios = this.router.getCurrentNavigation()?.extras.state?.["listaUsuarios"];
      
      }else{
        this.router.navigate(['/login']);
      }

    })
  }
  
  
  

  ngOnInit() {
    
  
    }
    

  olvidar(){
    localStorage.removeItem('ingresado');
    let navigationExtras: NavigationExtras = {
      state: {
        listaUsuarios:this.ListaDeUsuarios
      }
    };
    this.router.navigate(['/forget'],navigationExtras);  
  }
  async ingresar() { 

    if (!this.validateModel(this.usuario)) {
      this.presentToast('bottom', 'El campo ' + this.campo + ' es obligatorio');
    } else {
      let validacion = await this.connectUserService.iniciarSesion(this.usuario.usuario,this.usuario.contrasena);
      console.log(validacion);
      if (validacion) {
        localStorage.setItem('ingresado', 'true');
        localStorage.setItem('correo', this.usuario.usuario);
        let navigationExtras: NavigationExtras = {
          state: {
            user: this.usuario.usuario
          }
        };
        

        
      
          
        
        this.router.navigate(['/lobby'], navigationExtras);
      } 
    }
  }
  

  /**
   * validateModel sirve para validar que se ingrese algo en los
   * campos del html mediante su modelo
   */
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




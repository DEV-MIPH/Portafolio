import { Component, OnInit } from '@angular/core';
import { ToastController } from '@ionic/angular';
import { ActivatedRoute, Router, NavigationExtras } from '@angular/router';
import { ConnectUserService } from 'src/app/services/connect-user.service';

interface Usuario{
  usuario:string;
  contrasena:string;
}

@Component({
  selector: 'app-forget2',
  templateUrl: './forget2.page.html',
  styleUrls: ['./forget2.page.scss'],
})
export class Forget2Page implements OnInit {
  data:any;
  usuario:any;
  id:any;
  constructor(private activateRoute: ActivatedRoute, private router: Router,public toastController: ToastController,private connectUser: ConnectUserService ) { 
    //hacemos la llamada a los datos recibidos en la ventana de login
    this.activateRoute.queryParams.subscribe(params =>{//aca es donde estamos haciendo la llamada en una funcion de tipo flecha
      if (this.router.getCurrentNavigation()?.extras.state){
        this.usuario = this.router.getCurrentNavigation()?.extras.state?.["usuario"];
        console.log(this.usuario)
      }else{
        this.router.navigate(['/login']);
      }

    })
  }
  
  ngOnInit() {
  }
  campo:string="";
  nuevaContrasena:string="";
  confirmarContrasena:string="";
  
  restaurarContrasena(){
    if (this.nuevaContrasena == this.confirmarContrasena){
      this.connectUser.modificarPassword(this.usuario.id,this.nuevaContrasena);
      this.presentToast('bottom','Contraseña actualizada');
      this.router.navigate(['/login']);
    }
    else{
      this.presentToast('bottom','Las contraseñas no coinciden');
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
  
}


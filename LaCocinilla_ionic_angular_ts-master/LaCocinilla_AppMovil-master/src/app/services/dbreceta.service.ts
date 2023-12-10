import { Injectable } from '@angular/core';
import { SQLite, SQLiteObject } from '@awesome-cordova-plugins/sqlite/ngx';
import { Platform, ToastController } from '@ionic/angular';
import { BehaviorSubject, Observable } from 'rxjs';
import { Receta } from '../class/receta';


@Injectable({
  providedIn: 'root'
})
export class DbrecetaService {

  public database!: SQLiteObject;
  tblRecetas: string = "CREATE TABLE IF NOT EXISTS receta(id INTEGER PRIMARY KEY autoincrement, nombre VARCHAR(30) NOT NULL, categoria VARCHAR(30) NOT NULL, descripcion TEXT NOT NULL, ingredientes TEXT NOT NULL, preparacion TEXT NOT NULL, favorito INTEGER NOT NULL);";
  listaRecetas = new BehaviorSubject<Receta[]>([]);
  listaRecetasFav = new BehaviorSubject<Receta[]>([]);
  
  private isDbReady:
    BehaviorSubject<boolean> = new BehaviorSubject(false); 

  constructor( private sqlite: SQLite, private platform: Platform, public toastController: ToastController) { 
    this.crearDB();
  }

//Método que crea la base de datos si no Existe o carga la existente
crearDB(){
  this.platform.ready().then(() => {
    this.sqlite.create({
      name: 'recetas.db',
      location: 'default'
    }).then((db: SQLiteObject) => {
      this.database = db;
      this.presentToast("BD Creada");
      this.crearTablas();
    }).catch(e => this.presentToast(e));
  })
}

//Método que crea la tabla Receta Usuario si no Existe o carga la existente
async crearTablas(){
  try {
    await this.database.executeSql(this.tblRecetas, []);
    this.presentToast("Tabla Creada");
    this.cargarRecetas();
    this.isDbReady.next(true);
  } catch (error) {
    this.presentToast("Error en Crear Tabla: " + error);
  }
}

//Método que carga en la ListaRecetas TODO el contenido de la tabla Receta
cargarRecetas(){
  let items: Receta[] = [];
  this.database.executeSql('SELECT * FROM receta', [])
    .then(res => {
      if (res.rows.length > 0) {
        for (let i = 0; i < res.rows.length; i++){
          items.push({
            id: res.rows.item(i).id,
            nombre: res.rows.item(i).nombre,
            categoria: res.rows.item(i).categoria,
            descripcion: res.rows.item(i).descripcion,
            ingredientes: res.rows.item(i).ingredientes,
            preparacion: res.rows.item(i).preparacion,
            favorito: res.rows.item(i).favorito                            
          });
        }
      }
    });
  this.listaRecetas.next(items);  
}



//Método que inserta un nuevo registro en la tabla Receta
async addReceta(nombre: any, categoria: any, descripcion: any, ingredientes: any, preparacion:any, favorito:any){
  let data = [nombre, categoria, descripcion, ingredientes, preparacion, favorito]
  await this.database.executeSql('INSERT INTO receta(nombre,categoria,descripcion,ingredientes,preparacion,favorito) VALUES(?,?,?,?,?,?)', data);
  this.cargarRecetas();
}

//Método que actualiza los campos de la receta filtrando por el id
async updateReceta(id: any, nombre: any, categoria: any, descripcion: any, ingredientes: any, preparacion:any, favorito:any){
  let data = [nombre, categoria, descripcion, ingredientes, preparacion, favorito, id]
  await this.database.executeSql('UPDATE Receta SET nombre=?, categoria=?, descripcion=?, ingredientes=?, preparacion=?, favorito=? WHERE id=?', data);
  this.cargarRecetas();
}

//Método que elimina un registro por id de la tabla Receta
async deleteReceta(id: any){
  await this.database.executeSql('DELETE FROM receta WHERE id=?', [id]);
  this.cargarRecetas();
}

//Método que verifica la suscripción del Observable
dbState(){
  return this.isDbReady.asObservable();
}

//Método que se ejecuta cada vez que se hace un cambio en la tabla de la BD
fetchRecetas(): Observable<Receta[]> {
  return this.listaRecetas.asObservable();
}

fetchRecetasFav(): Observable<Receta[]> {
  return this.listaRecetasFav.asObservable();
}

mostrarFavorito(){
  let items: Receta[] = [];
  let favoritoSet=1
  this.database.executeSql('SELECT * FROM receta WHERE favorito = ?', [favoritoSet])
    .then(res => {
      if (res.rows.length > 0) {
        for (let i = 0; i < res.rows.length; i++){
          items.push({
            id: res.rows.item(i).id,
            nombre: res.rows.item(i).nombre,
            categoria: res.rows.item(i).categoria,
            descripcion: res.rows.item(i).descripcion,
            ingredientes: res.rows.item(i).ingredientes,
            preparacion: res.rows.item(i).preparacion,
            favorito: res.rows.item(i).favorito                            
          });
        }
      }
    });
  this.listaRecetasFav.next(items);  
}
async agregarFavorito(id:any,favorito:any){
  
  if(favorito == 1){
    let recetaFavorito = 0
    let data = [recetaFavorito,id]
    await this.database.executeSql('UPDATE Receta SET favorito=? WHERE id=?', data);
    this.cargarRecetas();
    this.presentToast("Se quito esta receta de favoritos")
  }
  else{
    let recetaFavorito = 1
    let data = [recetaFavorito,id]
    await this.database.executeSql('UPDATE Receta SET favorito=? WHERE id=?', data);
    this.cargarRecetas();
    this.presentToast("Se agrego esta receta a favoritos")
  }
  
}


//

//
async presentToast(mensaje: string) {
  const toast = await this.toastController.create({ 
    message: mensaje,
    duration: 3000 
  }); 
  toast.present(); 
}

}

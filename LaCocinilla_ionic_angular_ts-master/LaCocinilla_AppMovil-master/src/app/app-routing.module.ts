import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { IngresadoGuard } from './ingresado.guard';
import { NoIngresadoGuard } from './no-ingresado.guard';

const routes: Routes = [  
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'login',
    loadChildren: () => import('./pages/login/login.module').then( m => m.LoginPageModule),
    canActivate:[NoIngresadoGuard]
  },
  {
    path: 'lobby',
    loadChildren: () => import('./pages/lobby/lobby.module').then( m => m.LobbyPageModule),
    canActivate:[IngresadoGuard]
  },
  
  {
    path: 'forget',
    loadChildren: () => import('./pages/forget/forget.module').then( m => m.ForgetPageModule),
    canActivate:[NoIngresadoGuard]
  },
  {
    path: 'mis-recetas',
    loadChildren: () => import('./pages/mis-recetas/mis-recetas.module').then( m => m.MisRecetasPageModule),
    canActivate:[IngresadoGuard]
  },
  {
    path: 'forget2',
    loadChildren: () => import('./pages/forget2/forget2.module').then( m => m.Forget2PageModule),
    canActivate:[NoIngresadoGuard]
  },
  {
    path: 'modificar-receta',
    loadChildren: () => import('./pages/modificar-receta/modificar-receta.module').then( m => m.ModificarRecetaPageModule),
    canActivate:[IngresadoGuard]
  },
  {
    path: '**',
    loadChildren: () => import('./pages/not-found/not-found.module').then( m => m.NotFoundPageModule)
  },  
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }

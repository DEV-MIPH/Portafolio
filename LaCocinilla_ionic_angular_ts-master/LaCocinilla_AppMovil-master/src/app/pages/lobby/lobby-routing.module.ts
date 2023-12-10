import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LobbyPage } from './lobby.page';
import { ApiComponent } from 'src/app/components/api/api.component';
import { MisrecetasComponent } from 'src/app/components/misrecetas/misrecetas.component';
import { FavoritosComponent } from 'src/app/components/favoritos/favoritos.component';

const routes: Routes = [
  {
    path: '',
    component: LobbyPage,
    children: [
      {
        path: 'api',
        component: ApiComponent
      },
      {
        path: 'misrecetas',
        component: MisrecetasComponent 
      },
      {
        path: 'favoritos',
        component: FavoritosComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class LobbyPageRoutingModule {}

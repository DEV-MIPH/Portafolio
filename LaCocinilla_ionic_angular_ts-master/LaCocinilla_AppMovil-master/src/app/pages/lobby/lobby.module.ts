import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { LobbyPageRoutingModule } from './lobby-routing.module';

import { LobbyPage } from './lobby.page';

import { ApiComponent } from 'src/app/components/api/api.component';
import { MisrecetasComponent } from 'src/app/components/misrecetas/misrecetas.component';
import { FavoritosComponent } from 'src/app/components/favoritos/favoritos.component';
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    LobbyPageRoutingModule
  ],
  declarations: [LobbyPage, ApiComponent, MisrecetasComponent, FavoritosComponent]
})
export class LobbyPageModule {}
